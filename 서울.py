import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# 데이터 불러오기
apt_tx_indi = pd.read_csv('tx_indi.csv')
apt_res_indi = pd.read_csv('res_indi.csv')

# 데이터를 최근 26주만 남겨주기
apt_tx_indi_sort = apt_tx_indi.sort_values(by='WRTTIME_IDTFR_ID', ascending=False)
recent_26_weeks = apt_tx_indi_sort['WRTTIME_IDTFR_ID'].drop_duplicates().head(26)
apt_tx_indi_26_weeks = apt_tx_indi[apt_tx_indi['WRTTIME_IDTFR_ID'].isin(recent_26_weeks)]
apt_res_indi_sort = apt_res_indi.sort_values(by='WRTTIME_IDTFR_ID', ascending=False)
recent_26_weeks_res = apt_res_indi_sort['WRTTIME_IDTFR_ID'].drop_duplicates().head(26)
apt_res_indi_26_weeks = apt_res_indi[apt_res_indi['WRTTIME_IDTFR_ID'].isin(recent_26_weeks_res)]

# 데이터 복사
seoul_weekly_tx = apt_tx_indi_26_weeks.copy()
seoul_weekly_res = apt_res_indi_26_weeks.copy()

# 'CLS_NM' 열에서 우리가 활용한 지역구들만 필터링
'''앞 8개 그래프 : 매매가격지수 그래프'''
filtered_data1 = seoul_weekly_tx[seoul_weekly_tx['CLS_NM'].isin(['전국', '서울'])]
filtered_data2 = seoul_weekly_tx[seoul_weekly_tx['CLS_NM'].isin(['6대광역시', '서울'])]
filtered_data3 = seoul_weekly_tx[seoul_weekly_tx['CLS_NM'].isin(['전국', '동북권', '서북권', '서남권', '동남권'])]
filtered_data4 = seoul_weekly_tx[seoul_weekly_tx['CLS_NM'].isin(['6대광역시', '동북권', '서북권', '서남권', '남권'])]
'''뒤 8개 그래프 : 전세가격지수 그래프'''
filtered_data5 = seoul_weekly_res[seoul_weekly_res['CLS_NM'].isin(['전국', '서울'])]
filtered_data6 = seoul_weekly_res[seoul_weekly_res['CLS_NM'].isin(['6대광역시', '서울'])]
filtered_data7 = seoul_weekly_res[seoul_weekly_res['CLS_NM'].isin(['전국', '동북권', '서북권', '서남권', '동남권'])]
filtered_data8 = seoul_weekly_res[seoul_weekly_res['CLS_NM'].isin(['6대광역시', '동북권', '서북권', '서남권', '동남권'])]

'''바그래프'''
filtered_data9 = seoul_weekly_tx[seoul_weekly_tx['CLS_NM'].isin(
    ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구',
     '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'])]
filtered_data9 = filtered_data9[~((filtered_data9['CLS_NM'] == '중구') & (filtered_data9['CLS_ID'] != 50044))]
filtered_data9 = filtered_data9[~((filtered_data9['CLS_NM'] == '강서구') & (filtered_data9['CLS_ID'] != 50061))]
filtered_data10 = seoul_weekly_res[seoul_weekly_res['CLS_NM'].isin(
    ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구',
     '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'])]
filtered_data10 = filtered_data10[~((filtered_data10['CLS_NM'] == '중구') & (filtered_data10['CLS_ID'] != 50044))]
filtered_data10 = filtered_data10[~((filtered_data10['CLS_NM'] == '강서구') & (filtered_data10['CLS_ID'] != 50061))]


# x축 표기 위한 기간 단위 변환 함수
def convert_to_year_week(week_code):
    # year = int(week_code[:4])
    week = int(week_code[4:])
    return f'{week}주차'


# x축 표기 위한 기간 단위 변환을 각 데이터들에 적용
filtered_data1['WRTTIME_IDTFR_ID'] = filtered_data1['WRTTIME_IDTFR_ID'].astype(str)
filtered_data1['formatted_week'] = filtered_data1['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data2['WRTTIME_IDTFR_ID'] = filtered_data2['WRTTIME_IDTFR_ID'].astype(str)
filtered_data2['formatted_week'] = filtered_data2['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data3['WRTTIME_IDTFR_ID'] = filtered_data3['WRTTIME_IDTFR_ID'].astype(str)
filtered_data3['formatted_week'] = filtered_data3['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data4['WRTTIME_IDTFR_ID'] = filtered_data4['WRTTIME_IDTFR_ID'].astype(str)
filtered_data4['formatted_week'] = filtered_data4['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data5['WRTTIME_IDTFR_ID'] = filtered_data5['WRTTIME_IDTFR_ID'].astype(str)
filtered_data5['formatted_week'] = filtered_data5['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data6['WRTTIME_IDTFR_ID'] = filtered_data6['WRTTIME_IDTFR_ID'].astype(str)
filtered_data6['formatted_week'] = filtered_data6['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data7['WRTTIME_IDTFR_ID'] = filtered_data7['WRTTIME_IDTFR_ID'].astype(str)
filtered_data7['formatted_week'] = filtered_data7['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data8['WRTTIME_IDTFR_ID'] = filtered_data8['WRTTIME_IDTFR_ID'].astype(str)
filtered_data8['formatted_week'] = filtered_data8['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data9['WRTTIME_IDTFR_ID'] = filtered_data9['WRTTIME_IDTFR_ID'].astype(str)
filtered_data9['formatted_week'] = filtered_data9['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)
filtered_data10['WRTTIME_IDTFR_ID'] = filtered_data10['WRTTIME_IDTFR_ID'].astype(str)
filtered_data10['formatted_week'] = filtered_data10['WRTTIME_IDTFR_ID'].apply(convert_to_year_week)

'''1번그래프 : 매매가격지수 서울 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min1 = filtered_data1['DTA_VAL'].min()
y_min_with_margin1 = y_min1 - (y_min1 * 0.01)
y_max1 = filtered_data1['DTA_VAL'].max()
y_max_with_margin1 = y_max1 + (y_max1 * 0.01)

# Plotly 그래프 생성
fig1 = px.line(filtered_data1,
               x='formatted_week',  # 그래프 x축 기준으로 할 열 지정
               y='DTA_VAL',  # 그래프 y축 기준으로 할 열 지정
               color='CLS_NM',
               color_discrete_map={  # 그래프 색상 지정
                   '서울': '#0047AB',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig1.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals1 = list(range(int(y_min_with_margin1), int(y_max_with_margin1) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig1.update_layout(
    title={
        'text': '매매가격지수 최근 26주 서울 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=27),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,  # x축 값 표시
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,  # y축 값 표시
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals1,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
        gridwidth=1,  # 가로선 굵기
        range=[y_min_with_margin1, y_max_with_margin1]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 흰색
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data1['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data1[filtered_data1['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig1.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig1.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''2번그래프 : 매매가격지수 서울 6대광역시 비교'''
# y축 최솟값과 최댓값 계산
y_min2 = filtered_data2['DTA_VAL'].min()
y_min_with_margin2 = y_min2 - (y_min2 * 0.008)
y_max2 = filtered_data2['DTA_VAL'].max()
y_max_with_margin2 = y_max2 + (y_max2 * 0.008)

# Plotly 그래프 생성
fig2 = px.line(filtered_data2,
               x='formatted_week',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '서울': '#0047AB',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig2.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals2 = list(range(int(y_min_with_margin2), int(y_max_with_margin2) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig2.update_layout(
    title={
        'text': '매매가격지수 최근 26주 서울 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals2,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin2, y_max_with_margin2]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data2['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data2[filtered_data2['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig2.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig2.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''3번그래프 : 매매가격지수 등락률 서울 전국 비교'''
# 전월 대비 등락률 계산
filtered_data1_change = filtered_data1.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data1_change['prev_valAmount'] = filtered_data1_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data1_change['change_rate'] = (filtered_data1_change['DTA_VAL'] - filtered_data1_change['prev_valAmount']) / \
                                       filtered_data1_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min1_change = filtered_data1_change['change_rate'].min()
y_min_with_margin1_change = y_min1_change - 0.2
y_max1_change = filtered_data1_change['change_rate'].max()
y_max_with_margin1_change = y_max1_change + 0.2

# Plotly 그래프 생성
fig3 = px.line(filtered_data1_change,
               x='formatted_week',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '서울': '#0047AB',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig3.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals1_change = list(range(int(y_min_with_margin1_change), int(y_max_with_margin1_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig3.update_layout(
    title={
        'text': '매매가격지수 등락률 최근 26주 서울 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin1_change, y_max_with_margin1_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig3.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data1_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data1_change[filtered_data1_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig3.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig3.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''4번그래프 : 아파트 매매가격지수 등락률 서울 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data2_change = filtered_data2.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data2_change['prev_valAmount'] = filtered_data2_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data2_change['change_rate'] = (filtered_data2_change['DTA_VAL'] - filtered_data2_change['prev_valAmount']) / \
                                       filtered_data2_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min2_change = filtered_data2_change['change_rate'].min()
y_min_with_margin2_change = y_min2_change - 0.2
y_max2_change = filtered_data2_change['change_rate'].max()
y_max_with_margin2_change = y_max2_change + 0.2

# Plotly 그래프 생성
fig4 = px.line(filtered_data2_change,
               x='formatted_week',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '서울': '#0047AB',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig4.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals2_change = list(range(int(y_min_with_margin2_change), int(y_max_with_margin2_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig4.update_layout(
    title={
        'text': '매매가격지수 등락률 최근 26주 서울 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        # tickvals=tickvals2_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin2_change, y_max_with_margin2_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig4.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data2_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data2_change[filtered_data2_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig4.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig4.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''5번그래프 : 매매가격지수 서울 권역별 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min5 = filtered_data3['DTA_VAL'].min()
y_min_with_margin5 = y_min5 - (y_min5 * 0.01)
y_max5 = filtered_data3['DTA_VAL'].max()
y_max_with_margin5 = y_max5 + (y_max5 * 0.01)

# Plotly 그래프 생성
fig5 = px.line(filtered_data3,
               x='formatted_week',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '동북권': '#0047AB',
                   '동남권': '#008080',
                   '서북권': '#A95FBA',
                   '서남권': '#FF8C00',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig5.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals5 = list(range(int(y_min_with_margin5), int(y_max_with_margin5) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig5.update_layout(
    title={
        'text': '매매가격지수 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals5,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin5, y_max_with_margin5]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data3['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data3[filtered_data3['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig5.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig5.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''6번그래프 : 매매가격지수 서울 권역별 6대광역시 비교'''

# y축 최솟값과 최댓값 계산
y_min6 = filtered_data4['DTA_VAL'].min()
y_min_with_margin6 = y_min6 - (y_min6 * 0.01)
y_max6 = filtered_data4['DTA_VAL'].max()
y_max_with_margin6 = y_max6 + (y_max6 * 0.01)

# Plotly 그래프 생성
fig6 = px.line(filtered_data4,
               x='formatted_week',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '동북권': '#0047AB',
                   '동남권': '#008080',
                   '서북권': '#A95FBA',
                   '서남권': '#FF8C00',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig6.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals6 = list(range(int(y_min_with_margin6), int(y_max_with_margin6) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig6.update_layout(
    title={
        'text': '매매가격지수 최근 26주 서울 권역별 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals6,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin6, y_max_with_margin6]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data4['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data4[filtered_data4['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig6.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig6.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''7번그래프 : 매매가격지수 등락률 서울 권역별 전국 비교'''
# 전월 대비 등락률 계산
filtered_data3_change = filtered_data3.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data3_change['prev_valAmount'] = filtered_data3_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data3_change['change_rate'] = (filtered_data3_change['DTA_VAL'] - filtered_data3_change['prev_valAmount']) / \
                                       filtered_data3_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min3_change = filtered_data3_change['change_rate'].min()
y_min_with_margin3_change = y_min3_change - 0.2
y_max3_change = filtered_data3_change['change_rate'].max()
y_max_with_margin3_change = y_max3_change + 0.2

# Plotly 그래프 생성
fig7 = px.line(filtered_data3_change,
               x='formatted_week',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '동북권': '#0047AB',
                   '동남권': '#008080',
                   '서북권': '#A95FBA',
                   '서남권': '#FF8C00',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig7.update_traces(line=dict(width=5))

# y축 라벨 형식 수정
tickvals3_change = list(range(int(y_min_with_margin3_change), int(y_max_with_margin3_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig7.update_layout(
    title={
        'text': '매매가격지수 등락률 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin3_change, y_max_with_margin3_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig7.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data3_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data3_change[filtered_data3_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig7.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig7.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''8번그래프 : 매매가격지수 등락률 서울 권역별 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data4_change = filtered_data4.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data4_change['prev_valAmount'] = filtered_data4_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data4_change['change_rate'] = (filtered_data4_change['DTA_VAL'] - filtered_data4_change['prev_valAmount']) / \
                                       filtered_data4_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min4_change = filtered_data4_change['change_rate'].min()
y_min_with_margin4_change = y_min4_change - 0.2
y_max4_change = filtered_data4_change['change_rate'].max()
y_max_with_margin4_change = y_max4_change + 0.2

# Plotly 그래프 생성
fig8 = px.line(filtered_data4_change,
               x='formatted_week',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '동북권': '#0047AB',
                   '동남권': '#008080',
                   '서북권': '#A95FBA',
                   '서남권': '#FF8C00',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig8.update_traces(line=dict(width=5))

# y축 라벨 형식 수정
tickvals4_change = list(range(int(y_min_with_margin4_change), int(y_max_with_margin4_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig8.update_layout(
    title={
        'text': '매매가격지수 등락률 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin4_change, y_max_with_margin4_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig8.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data4_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data4_change[filtered_data4_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig8.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig8.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''9번그래프 : 전세가격지수 서울 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min9 = filtered_data5['DTA_VAL'].min()
y_min_with_margin9 = y_min9 - (y_min9 * 0.01)
y_max9 = filtered_data5['DTA_VAL'].max()
y_max_with_margin9 = y_max9 + (y_max9 * 0.01)

# Plotly 그래프 생성
fig9 = px.line(filtered_data5,
               x='formatted_week',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '서울': '#0047AB',
                   '6대광역시': '#D50032',
                   '전국': '#D50032',
               },
               markers=False,
               line_shape='spline',
               )

# 선 그래프 색상 및 굵기 설정
fig9.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals9 = list(range(int(y_min_with_margin9), int(y_max_with_margin9) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig9.update_layout(
    title={
        'text': '전세가격지수 최근 26주 서울 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals9,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin9, y_max_with_margin9]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data5['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data5[filtered_data5['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig9.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig9.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''10번그래프 : 전세가격지수 서울 6대광역시 비교'''
# y축 최솟값과 최댓값 계산
y_min10 = filtered_data6['DTA_VAL'].min()
y_min_with_margin10 = y_min10 - (y_min10 * 0.008)
y_max10 = filtered_data6['DTA_VAL'].max()
y_max_with_margin10 = y_max10 + (y_max10 * 0.008)

# Plotly 그래프 생성
fig10 = px.line(filtered_data6,
                x='formatted_week',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '서울': '#0047AB',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig10.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals10 = list(range(int(y_min_with_margin10), int(y_max_with_margin10) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig10.update_layout(
    title={
        'text': '전세가격지수 최근 26주 서울 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals10,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin10, y_max_with_margin10]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data6['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data6[filtered_data6['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig10.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig10.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''11번그래프 : 전세가격지수 등락률 서울 전국 비교'''
# 전월 대비 등락률 계산
filtered_data5_change = filtered_data5.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data5_change['prev_valAmount'] = filtered_data5_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data5_change['change_rate'] = (filtered_data5_change['DTA_VAL'] - filtered_data5_change['prev_valAmount']) / \
                                       filtered_data5_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min5_change = filtered_data5_change['change_rate'].min()
y_min_with_margin5_change = y_min5_change - 0.2
y_max5_change = filtered_data5_change['change_rate'].max()
y_max_with_margin5_change = y_max5_change + 0.2

# Plotly 그래프 생성
fig11 = px.line(filtered_data5_change,
                x='formatted_week',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '서울': '#0047AB',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig11.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals5_change = list(range(int(y_min_with_margin5_change), int(y_max_with_margin5_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig11.update_layout(
    title={
        'text': '전세가격지수 등락률 최근 26주 서울 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin5_change, y_max_with_margin5_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig11.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data5_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data5_change[filtered_data5_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig11.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig11.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''12번그래프 : 전세가격지수 등락률 서울 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data6_change = filtered_data6.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data6_change['prev_valAmount'] = filtered_data6_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data6_change['change_rate'] = (filtered_data6_change['DTA_VAL'] - filtered_data6_change['prev_valAmount']) / \
                                       filtered_data6_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min6_change = filtered_data6_change['change_rate'].min()
y_min_with_margin6_change = y_min6_change - 0.2
y_max6_change = filtered_data6_change['change_rate'].max()
y_max_with_margin6_change = y_max6_change + 0.2

# Plotly 그래프 생성
fig12 = px.line(filtered_data6_change,
                x='formatted_week',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '서울': '#0047AB',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig12.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals6_change = list(range(int(y_min_with_margin6_change), int(y_max_with_margin6_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig12.update_layout(
    title={
        'text': '전세가격지수 등락률 최근 26주 서울 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals2_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin6_change, y_max_with_margin6_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig12.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data6_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data6_change[filtered_data6_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig12.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig12.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''13번그래프 : 전세가격지수 서울 권역별 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min13 = filtered_data7['DTA_VAL'].min()
y_min_with_margin13 = y_min13 - (y_min13 * 0.01)
y_max13 = filtered_data7['DTA_VAL'].max()
y_max_with_margin13 = y_max13 + (y_max13 * 0.01)

# Plotly 그래프 생성
fig13 = px.line(filtered_data7,
                x='formatted_week',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '동북권': '#0047AB',
                    '동남권': '#008080',
                    '서북권': '#A95FBA',
                    '서남권': '#FF8C00',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig13.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals13 = list(range(int(y_min_with_margin13), int(y_max_with_margin13) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig13.update_layout(
    title={
        'text': '전세가격지수 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals13,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin13, y_max_with_margin13]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data7['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data7[filtered_data7['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig13.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig13.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''14번그래프 : 전세가격지수 서울 권역별 6대광역시 비교'''

# y축 최솟값과 최댓값 계산
y_min14 = filtered_data8['DTA_VAL'].min()
y_min_with_margin14 = y_min14 - (y_min14 * 0.01)
y_max14 = filtered_data8['DTA_VAL'].max()
y_max_with_margin14 = y_max14 + (y_max14 * 0.01)

# Plotly 그래프 생성
fig14 = px.line(filtered_data8,
                x='formatted_week',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '동북권': '#0047AB',
                    '동남권': '#008080',
                    '서북권': '#A95FBA',
                    '서남권': '#FF8C00',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig14.update_traces(line=dict(width=6))

# y축 라벨 형식 수정
tickvals14 = list(range(int(y_min_with_margin14), int(y_max_with_margin14) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig14.update_layout(
    title={
        'text': '전세가격지수 최근 26주 서울 권역별 6대광역시 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals14,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin14, y_max_with_margin14]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data8['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data8[filtered_data8['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['DTA_VAL'].idxmax()]
    min_row = cls_data.loc[cls_data['DTA_VAL'].idxmin()]

    # 최대값에 주석 추가
    fig14.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['DTA_VAL'],
        text=f"{max_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig14.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['DTA_VAL'],
        text=f"{min_row['DTA_VAL']:.2f}",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''15번그래프 : 전세가격지수 등락률 서울 권역별 전국 비교'''
# 전월 대비 등락률 계산
filtered_data7_change = filtered_data7.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data7_change['prev_valAmount'] = filtered_data7_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data7_change['change_rate'] = (filtered_data7_change['DTA_VAL'] - filtered_data7_change['prev_valAmount']) / \
                                       filtered_data7_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min7_change = filtered_data7_change['change_rate'].min()
y_min_with_margin7_change = y_min7_change - 0.2
y_max7_change = filtered_data7_change['change_rate'].max()
y_max_with_margin7_change = y_max7_change + 0.2

# Plotly 그래프 생성
fig15 = px.line(filtered_data7_change,
                x='formatted_week',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '동북권': '#0047AB',
                    '동남권': '#008080',
                    '서북권': '#A95FBA',
                    '서남권': '#FF8C00',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig15.update_traces(line=dict(width=5))

# y축 라벨 형식 수정
tickvals7_change = list(range(int(y_min_with_margin7_change), int(y_max_with_margin7_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig15.update_layout(
    title={
        'text': '전세가격지수 등락률 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin7_change, y_max_with_margin7_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig15.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data7_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data7_change[filtered_data7_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig15.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig15.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''16번그래프 : 전세가격지수 등락률 서울 권역별 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data8_change = filtered_data8.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data8_change['prev_valAmount'] = filtered_data8_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data8_change['change_rate'] = (filtered_data8_change['DTA_VAL'] - filtered_data8_change['prev_valAmount']) / \
                                       filtered_data8_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min8_change = filtered_data8_change['change_rate'].min()
y_min_with_margin8_change = y_min8_change - 0.2
y_max8_change = filtered_data8_change['change_rate'].max()
y_max_with_margin8_change = y_max8_change + 0.2

# Plotly 그래프 생성
fig16 = px.line(filtered_data8_change,
                x='formatted_week',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '동북권': '#0047AB',
                    '동남권': '#008080',
                    '서북권': '#A95FBA',
                    '서남권': '#FF8C00',
                    '6대광역시': '#D50032',
                    '전국': '#D50032',
                },
                markers=False,
                line_shape='spline',
                )

# 선 그래프 색상 및 굵기 설정
fig16.update_traces(line=dict(width=5))

# y축 라벨 형식 수정
tickvals8_change = list(range(int(y_min_with_margin8_change), int(y_max_with_margin8_change) + 1))

# 그래프 레이아웃 업데이트 (크기, 제목, 축 스타일, 배경색 등)
fig16.update_layout(
    title={
        'text': '전세가격지수 등락률 최근 26주 서울 권역별 전국 비교',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'}
    },
    legend=dict(
        font=dict(size=30),  # 범례 텍스트 크기 조정
        title=None,  # 범례 제목 숨기기
    ),
    xaxis=dict(
        showline=True,
        showticklabels=True,
        tickfont=dict(size=15, family='Verdana', color='gray'),
        title=None,
        showgrid=True,  # 세로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='auto',  # 수동으로 tick 설정
        # tickvals=tickvals1_change,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin8_change, y_max_with_margin8_change],  # y축의 최솟값과 최댓값에 마진 추가
        zeroline=True,  # 0에서 가로선 표시
        zerolinecolor='rgba(200, 200, 200, 0.5)',  # 0선의 색상
        zerolinewidth=3,  # 0선의 두께
    ),
    width=1120,  # 그래프 너비 (16:9 비율로 설정)
    height=630,  # 그래프 높이 (16:9 비율로 설정)
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    xaxis_tickformat='%Y년%주차',
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="gray")  # 작은 회색 글씨로 표시
        )
    ]
)
fig16.update_yaxes(ticksuffix="%")

# 각 CLS_NM 그룹별 최대값과 최소값을 찾고, 주석 추가
for cls_name in filtered_data8_change['CLS_NM'].unique():
    # 각 CLS_NM별 데이터 필터링
    cls_data = filtered_data8_change[filtered_data8_change['CLS_NM'] == cls_name]

    # 최대값과 최소값 찾기
    max_row = cls_data.loc[cls_data['change_rate'].idxmax()]
    min_row = cls_data.loc[cls_data['change_rate'].idxmin()]

    # 최대값에 주석 추가
    fig16.add_annotation(
        x=max_row['formatted_week'],
        y=max_row['change_rate'],
        text=f"{max_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )
    # 최소값에 주석 추가
    fig16.add_annotation(
        x=min_row['formatted_week'],
        y=min_row['change_rate'],
        text=f"{min_row['change_rate']:.2f}%",
        showarrow=False,
        # textangle=-25,  # 오른쪽으로 기울이기
        xanchor='center',  # 텍스트의 시작점을 왼쪽으로 설정
        yanchor='bottom',  # 텍스트의 시작점을 아래쪽으로 설정
        font=dict(size=15, family='Verdana', color='gray'),  # 폰트 크기와 색상 설정
        # xshift=10  # 오른쪽으로 이동
    )

'''17번그래프 : 서울시 전체 구 최근 주차 매매가격지수'''
# 최신 주차 데이터 필터링
latest_week = filtered_data9['formatted_week'].max()  # 가장 최근 주차 찾기
latest_data = filtered_data9[filtered_data9['formatted_week'] == latest_week]  # 해당 주차 데이터 필터링

# y축 최댓값 계산
y_max9 = filtered_data9['DTA_VAL'].max()

# 색상 목록 정의 (25개 색상)
colors = ['#E74C3C', '#F39C12', '#F1C40F', '#2ECC71', '#1ABC9C', '#3498DB', '#2980B9',
          '#9B59B6', '#E91E63', '#D50032', '#C0392B', '#D4AF37', '#FFA07A', '#8FBC8F', '#00CED1',
          '#4682B4', '#9370DB', '#FFB6C1', '#FFE4C4', '#B0E0E6', '#AFEEEE', '#FF69B4', '#A0522D',
          '#FF6347', '#B22222', '#DAA520', ]

# 서울시 구별 매매가격지수 바 차트 생성
fig17 = px.bar(latest_data,
               x='CLS_NM',  # 구 이름
               y='DTA_VAL',  # 매매가격지수
               color='CLS_NM',  # 구에 따른 색상 구분
               # labels={'CLS_NM': '서울시 구', 'DTA_VAL': '매매가격지수'},  # 라벨 설정
               title=f"서울시 각 구의 최근 주차 매매가격지수 ({latest_week})",  # 그래프 제목
               )

# 강조하고자 하는 구 이름 지정 (예: 중구)
highlight_bar = '동작구'

# 각 바의 색상 및 외곽선 설정
for i, bar in enumerate(fig17.data):
    bar.marker.color = colors[i % len(colors)]  # 색상 지정
    for j, x_value in enumerate(bar.x):
        if x_value == highlight_bar:
            bar.marker.line.width = 5  # 외곽선 두께 설정
            bar.marker.line.color = '#FF4500'  # 외곽선 색상 (주황색)
        else:
            bar.marker.line.width = 0  # 다른 바는 외곽선 없음

# 그래프 레이아웃 업데이트 (스타일 설정)
fig17.update_layout(
    title={
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'},
        'x': 0.5,  # 제목을 중앙에 배치
        'xanchor': 'center',
    },
    xaxis=dict(
        title=None,
        tickfont=dict(size=17, family='Verdana', color='gray'),
        showline=True,
        showgrid=False  # 세로선 제거
    ),
    yaxis=dict(
        title=None,
        showticklabels=True,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        showline=True,
        showgrid=True,  # 가로선 표시
        gridwidth=1,
        range=[70, y_max9 + 5],  # y축의 최솟값과 최댓값에 마진 추가
        gridcolor='rgba(211, 211, 211, 0.5)'  # 연한 회색 가로선
    ),
    bargap=0.3,  # 바 간의 간격 (0~1 사이 값)
    plot_bgcolor='white',  # 그래프 배경색
    paper_bgcolor='white',  # 전체 배경색
    width=1120,  # 그래프 너비
    height=630,  # 그래프 높이
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    showlegend=False,
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="black")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 바 위에 데이터 레이블 추가
for i in range(len(latest_data)):
    fig17.add_annotation(
        x=latest_data['CLS_NM'].iloc[i],  # x축 (구 이름)
        y=latest_data['DTA_VAL'].iloc[i],  # y축 (매매가격지수)
        text=f"{latest_data['DTA_VAL'].iloc[i]:.2f}",  # 값 표시, 소수점 2자리까지
        showarrow=False,
        font=dict(size=13, color='black'),  # 폰트 크기와 색상
        yshift=10  # 바 위에 위치하도록 y축을 약간 위로 이동
    )

'''18번그래프 : 서울시 전체 구 최근 주차 전세가격지수'''
# 최신 주차 데이터 필터링
latest_week2 = filtered_data10['formatted_week'].max()  # 가장 최근 주차 찾기
latest_data2 = filtered_data10[filtered_data10['formatted_week'] == latest_week2]  # 해당 주차 데이터 필터링

# y축 최댓값 계산
y_max10 = filtered_data10['DTA_VAL'].max()

# 색상 목록 정의 (25개 색상)
colors = ['#E74C3C', '#F39C12', '#F1C40F', '#2ECC71', '#1ABC9C', '#3498DB', '#2980B9',
          '#9B59B6', '#E91E63', '#D50032', '#C0392B', '#D4AF37', '#FFA07A', '#8FBC8F', '#00CED1',
          '#4682B4', '#9370DB', '#FFB6C1', '#FFE4C4', '#B0E0E6', '#AFEEEE', '#FF69B4', '#A0522D',
          '#FF6347', '#B22222', '#DAA520', ]

# 서울시 구별 매매가격지수 바 차트 생성
fig18 = px.bar(latest_data2,
               x='CLS_NM',  # 구 이름
               y='DTA_VAL',  # 매매가격지수
               color='CLS_NM',  # 구에 따른 색상 구분
               # labels={'CLS_NM': '서울시 구', 'DTA_VAL': '매매가격지수'},  # 라벨 설정
               title=f"서울시 각 구의 최근 주차 전세가격지수 ({latest_week2})",  # 그래프 제목
               )

# 강조하고자 하는 구 이름 지정 (예: 중구)
highlight_bar = '동작구'

# 각 바의 색상 및 외곽선 설정
for i, bar in enumerate(fig18.data):
    bar.marker.color = colors[i % len(colors)]  # 색상 지정
    for j, x_value in enumerate(bar.x):
        if x_value == highlight_bar:
            bar.marker.line.width = 5  # 외곽선 두께 설정
            bar.marker.line.color = '#FF4500'  # 외곽선 색상 (주황색)
        else:
            bar.marker.line.width = 0  # 다른 바는 외곽선 없음

# 그래프 레이아웃 업데이트 (스타일 설정)
fig18.update_layout(
    title={
        'font': {'size': 25, 'family': 'Montserrat', 'color': '#2B3E50'},
        'x': 0.5,  # 제목을 중앙에 배치
        'xanchor': 'center',
    },
    xaxis=dict(
        title=None,
        tickfont=dict(size=17, family='Verdana', color='gray'),
        showline=True,
        showgrid=False  # 세로선 제거
    ),
    yaxis=dict(
        title=None,
        showticklabels=True,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        showline=True,
        showgrid=True,  # 가로선 표시
        gridwidth=1,
        range=[70, y_max10 + 5],  # y축의 최솟값과 최댓값에 마진 추가
        gridcolor='rgba(211, 211, 211, 0.5)'  # 연한 회색 가로선
    ),
    bargap=0.3,  # 바 간의 간격 (0~1 사이 값)
    plot_bgcolor='white',  # 그래프 배경색
    paper_bgcolor='white',  # 전체 배경색
    width=1120,  # 그래프 너비
    height=630,  # 그래프 높이
    xaxis_tickangle=45,  # x축 눈금 기울기
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
    showlegend=False,
    annotations=[
        dict(
            text="출처:한국부동산원 부동산통계정보",
            x=1,  # 오른쪽 끝으로 배치
            y=0,  # 아래쪽 끝으로 배치
            xref="paper",  # x축 기준으로 paper 사용
            yref="paper",  # y축 기준으로 paper 사용
            xanchor='right',  # 오른쪽 끝에 맞춤
            yanchor='bottom',  # 아래쪽 끝에 맞춤
            showarrow=False,  # 화살표 없이 텍스트만 표시
            font=dict(size=12, color="black")  # 작은 회색 글씨로 표시
        )
    ]
)

# 각 바 위에 데이터 레이블 추가
for i in range(len(latest_data2)):
    fig18.add_annotation(
        x=latest_data2['CLS_NM'].iloc[i],  # x축 (구 이름)
        y=latest_data2['DTA_VAL'].iloc[i],  # y축 (매매가격지수)
        text=f"{latest_data2['DTA_VAL'].iloc[i]:.2f}",  # 값 표시, 소수점 2자리까지
        showarrow=False,
        font=dict(size=13, color='black'),  # 폰트 크기와 색상
        yshift=10  # 바 위에 위치하도록 y축을 약간 위로 이동
    )

# Dash 애플리케이션 초기화
app = dash.Dash(__name__)
server = app.server

# 레이아웃 정의
app.layout = html.Div([
    dcc.Graph(id='line-chart', figure=fig1),
    dcc.Interval(id='graph-interval', interval=10000, n_intervals=0)  # 10초 간격
])


# 콜백 함수 정의
@app.callback(
    Output('line-chart', 'figure'),
    Input('graph-interval', 'n_intervals')
)
def update_graph(n):
    # 그래프를 순환
    figures = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10,
               fig11, fig12, fig13, fig14, fig15, fig16, fig17, fig18]
    # figures=[fig18]
    return figures[n % len(figures)]


# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)