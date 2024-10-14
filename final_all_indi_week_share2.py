import pandas as pd

apt_tx_indi_26_weeks = pd.read_csv('recent26_tx_indi.csv')
apt_res_indi_26_weeks = pd.read_csv('recent26_res_indi.csv')

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# 데이터 전처리
goyang_monthly_tx = apt_tx_indi_26_weeks.copy()
goyang_monthly_res = apt_res_indi_26_weeks.copy()

# 'CLS_NM' 열에서 특정 값이 있는 행들만 필터링
'''앞 8개 그래프 : 매매가격지수 그래프'''
filtered_data1 = goyang_monthly_tx[goyang_monthly_tx['CLS_NM'].isin(['전국', '고양시'])]
filtered_data2 = goyang_monthly_tx[goyang_monthly_tx['CLS_NM'].isin(['6대광역시', '고양시'])]
filtered_data3 = goyang_monthly_tx[goyang_monthly_tx['CLS_NM'].isin(['전국', '덕양구', '일산동구', '일산서구'])]
filtered_data4 = goyang_monthly_tx[goyang_monthly_tx['CLS_NM'].isin(['6대광역시', '덕양구', '일산동구', '일산서구'])]
'''뒤 8개 그래프 : 전세가격지수 그래프'''
filtered_data5 = goyang_monthly_res[goyang_monthly_res['CLS_NM'].isin(['전국', '고양시'])]
filtered_data6 = goyang_monthly_res[goyang_monthly_res['CLS_NM'].isin(['6대광역시', '고양시'])]
filtered_data7 = goyang_monthly_res[goyang_monthly_res['CLS_NM'].isin(['전국', '덕양구', '일산동구', '일산서구'])]
filtered_data8 = goyang_monthly_res[goyang_monthly_res['CLS_NM'].isin(['6대광역시', '덕양구', '일산동구', '일산서구'])]

'''1번그래프 : 매매가격지수 고양시 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min1 = filtered_data1['DTA_VAL'].min()
y_min_with_margin1 = y_min1 - (y_min1 * 0.01)
y_max1 = filtered_data1['DTA_VAL'].max()
y_max_with_margin1 = y_max1 + (y_max1 * 0.01)

# Plotly 그래프 생성
fig1 = px.line(filtered_data1,
               x='WRTTIME_IDTFR_ID',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '고양시': '#0047AB',
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
        'text': '매매가격지수 최근 26주 고양시 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
    ),
    yaxis=dict(
        showline=True,
        showticklabels=True,
        title=None,
        tickfont=dict(size=25, family='Verdana', color='gray'),
        tickmode='array',  # 수동으로 tick 설정
        tickvals=tickvals1,  # y축 눈금 위치
        showgrid=True,  # 가로선 표시
        gridcolor='rgba(211, 211, 211, 0.5)',  # 연한 회색 점선
        gridwidth=1,
        range=[y_min_with_margin1, y_max_with_margin1]  # y축의 최솟값과 최댓값에 마진 추가
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''2번그래프 : 매매가격지수 고양시 6대광역시 비교'''
# y축 최솟값과 최댓값 계산
y_min2 = filtered_data2['DTA_VAL'].min()
y_min_with_margin2 = y_min2 - (y_min2 * 0.008)
y_max2 = filtered_data2['DTA_VAL'].max()
y_max_with_margin2 = y_max2 + (y_max2 * 0.008)

# Plotly 그래프 생성
fig2 = px.line(filtered_data2,
               x='WRTTIME_IDTFR_ID',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '고양시': '#0047AB',
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
        'text': '매매가격지수 최근 26주 고양시 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''3번그래프 : 매매가격지수 등락률 고양시 전국 비교'''
# 전월 대비 등락률 계산
filtered_data1_change = filtered_data1.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data1_change['prev_valAmount'] = filtered_data1_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data1_change['change_rate'] = (filtered_data1_change['DTA_VAL'] - filtered_data1_change['prev_valAmount']) / \
                                       filtered_data1_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min1_change = filtered_data1_change['change_rate'].min()
y_min_with_margin1_change = y_min1_change - (abs(y_min1_change) * 2)
y_max1_change = filtered_data1_change['change_rate'].max()
y_max_with_margin1_change = y_max1_change + (abs(y_max1_change) * 1)

# Plotly 그래프 생성
fig3 = px.line(filtered_data1_change,
               x='WRTTIME_IDTFR_ID',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '고양시': '#0047AB',
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
        'text': '매매가격지수 등락률 최근 26주 고양시 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2r%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''4번그래프 : 아파트 매매가격지수 등락률 고양시 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data2_change = filtered_data2.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data2_change['prev_valAmount'] = filtered_data2_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data2_change['change_rate'] = (filtered_data2_change['DTA_VAL'] - filtered_data2_change['prev_valAmount']) / \
                                       filtered_data2_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min2_change = filtered_data2_change['change_rate'].min()
y_min_with_margin2_change = y_min2_change - (abs(y_min2_change) * 2)
y_max2_change = filtered_data2_change['change_rate'].max()
y_max_with_margin2_change = y_max2_change + (abs(y_max2_change) * 1)

# Plotly 그래프 생성
fig4 = px.line(filtered_data2_change,
               x='WRTTIME_IDTFR_ID',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '고양시': '#0047AB',
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
        'text': '매매가격지수 등락률 최근 26주 고양시 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2r%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''5번그래프 : 매매가격지수 고양시 지역구별 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min5 = filtered_data3['DTA_VAL'].min()
y_min_with_margin5 = y_min5 - (y_min5 * 0.01)
y_max5 = filtered_data3['DTA_VAL'].max()
y_max_with_margin5 = y_max5 + (y_max5 * 0.01)

# Plotly 그래프 생성
fig5 = px.line(filtered_data3,
               x='WRTTIME_IDTFR_ID',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '덕양구': '#0047AB',
                   '일산동구': '#008080',
                   '일산서구': '#A95FBA',
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
        'text': '매매가격지수 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''6번그래프 : 매매가격지수 고양시 지역구별 6대광역시 비교'''

# y축 최솟값과 최댓값 계산
y_min6 = filtered_data4['DTA_VAL'].min()
y_min_with_margin6 = y_min6 - (y_min6 * 0.01)
y_max6 = filtered_data4['DTA_VAL'].max()
y_max_with_margin6 = y_max6 + (y_max6 * 0.01)

# Plotly 그래프 생성
fig6 = px.line(filtered_data4,
               x='WRTTIME_IDTFR_ID',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '덕양구': '#0047AB',
                   '일산동구': '#008080',
                   '일산서구': '#A95FBA',
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
        'text': '매매가격지수 최근 26주 고양시 지역구별 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''7번그래프 : 매매가격지수 등락률 고양시 지역구별 전국 비교'''
# 전월 대비 등락률 계산
filtered_data3_change = filtered_data3.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data3_change['prev_valAmount'] = filtered_data3_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data3_change['change_rate'] = (filtered_data3_change['DTA_VAL'] - filtered_data3_change['prev_valAmount']) / \
                                       filtered_data3_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min3_change = filtered_data3_change['change_rate'].min()
y_min_with_margin3_change = y_min3_change - (abs(y_min3_change) * 1)
y_max3_change = filtered_data3_change['change_rate'].max()
y_max_with_margin3_change = y_max3_change + (abs(y_max3_change) * 1)

# Plotly 그래프 생성
fig7 = px.line(filtered_data3_change,
               x='WRTTIME_IDTFR_ID',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '덕양구': '#0047AB',
                   '일산동구': '#008080',
                   '일산서구': '#A95FBA',
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
        'text': '매매가격지수 등락률 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''8번그래프 : 매매가격지수 등락률 고양시 지역구별 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data4_change = filtered_data4.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data4_change['prev_valAmount'] = filtered_data4_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data4_change['change_rate'] = (filtered_data4_change['DTA_VAL'] - filtered_data4_change['prev_valAmount']) / \
                                       filtered_data4_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min4_change = filtered_data4_change['change_rate'].min()
y_min_with_margin4_change = y_min4_change - (abs(y_min4_change) * 1)
y_max4_change = filtered_data4_change['change_rate'].max()
y_max_with_margin4_change = y_max4_change + (abs(y_max4_change) * 1)

# Plotly 그래프 생성
fig8 = px.line(filtered_data4_change,
               x='WRTTIME_IDTFR_ID',
               y='change_rate',
               color='CLS_NM',
               color_discrete_map={
                   '덕양구': '#0047AB',
                   '일산동구': '#008080',
                   '일산서구': '#A95FBA',
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
        'text': '매매가격지수 등락률 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''9번그래프 : 전세가격지수 고양시 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min9 = filtered_data5['DTA_VAL'].min()
y_min_with_margin9 = y_min9 - (y_min9 * 0.01)
y_max9 = filtered_data5['DTA_VAL'].max()
y_max_with_margin9 = y_max9 + (y_max9 * 0.01)

# Plotly 그래프 생성
fig9 = px.line(filtered_data5,
               x='WRTTIME_IDTFR_ID',
               y='DTA_VAL',
               color='CLS_NM',
               color_discrete_map={
                   '고양시': '#0047AB',
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
        'text': '전세가격지수 최근 26주 고양시 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''10번그래프 : 전세가격지수 고양시 6대광역시 비교'''
# y축 최솟값과 최댓값 계산
y_min10 = filtered_data6['DTA_VAL'].min()
y_min_with_margin10 = y_min10 - (y_min10 * 0.008)
y_max10 = filtered_data6['DTA_VAL'].max()
y_max_with_margin10 = y_max10 + (y_max10 * 0.008)

# Plotly 그래프 생성
fig10 = px.line(filtered_data6,
                x='WRTTIME_IDTFR_ID',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '고양시': '#0047AB',
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
        'text': '전세가격지수 최근 26주 고양시 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''11번그래프 : 전세가격지수 등락률 고양시 전국 비교'''
# 전월 대비 등락률 계산
filtered_data5_change = filtered_data5.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data5_change['prev_valAmount'] = filtered_data5_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data5_change['change_rate'] = (filtered_data5_change['DTA_VAL'] - filtered_data5_change['prev_valAmount']) / \
                                       filtered_data5_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min5_change = filtered_data5_change['change_rate'].min()
y_min_with_margin5_change = y_min5_change - 0.2
y_max5_change = filtered_data5_change['change_rate'].max()
y_max_with_margin5_change = y_max5_change + 0.1

# Plotly 그래프 생성
fig11 = px.line(filtered_data5_change,
                x='WRTTIME_IDTFR_ID',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '고양시': '#0047AB',
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
        'text': '전세가격지수 등락률 최근 26주 고양시 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''12번그래프 : 전세가격지수 등락률 고양시 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data6_change = filtered_data6.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data6_change['prev_valAmount'] = filtered_data6_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data6_change['change_rate'] = (filtered_data6_change['DTA_VAL'] - filtered_data6_change['prev_valAmount']) / \
                                       filtered_data6_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min6_change = filtered_data6_change['change_rate'].min()
y_min_with_margin6_change = y_min6_change - 0.1
y_max6_change = filtered_data6_change['change_rate'].max()
y_max_with_margin6_change = y_max6_change + 0.1

# Plotly 그래프 생성
fig12 = px.line(filtered_data6_change,
                x='WRTTIME_IDTFR_ID',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '고양시': '#0047AB',
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
        'text': '전세가격지수 등락률 최근 26주 고양시 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''13번그래프 : 전세가격지수 고양시 지역구별 전국 비교'''

# y축 최솟값과 최댓값 계산
y_min13 = filtered_data7['DTA_VAL'].min()
y_min_with_margin13 = y_min13 - (y_min13 * 0.01)
y_max13 = filtered_data7['DTA_VAL'].max()
y_max_with_margin13 = y_max13 + (y_max13 * 0.01)

# Plotly 그래프 생성
fig13 = px.line(filtered_data7,
                x='WRTTIME_IDTFR_ID',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '덕양구': '#0047AB',
                    '일산동구': '#008080',
                    '일산서구': '#A95FBA',
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
        'text': '전세가격지수 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''14번그래프 : 전세가격지수 고양시 지역구별 6대광역시 비교'''

# y축 최솟값과 최댓값 계산
y_min14 = filtered_data8['DTA_VAL'].min()
y_min_with_margin14 = y_min14 - (y_min14 * 0.01)
y_max14 = filtered_data8['DTA_VAL'].max()
y_max_with_margin14 = y_max14 + (y_max14 * 0.01)

# Plotly 그래프 생성
fig14 = px.line(filtered_data8,
                x='WRTTIME_IDTFR_ID',
                y='DTA_VAL',
                color='CLS_NM',
                color_discrete_map={
                    '덕양구': '#0047AB',
                    '일산동구': '#008080',
                    '일산서구': '#A95FBA',
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
        'text': '전세가격지수 최근 26주 고양시 지역구별 6대광역시 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''15번그래프 : 전세가격지수 등락률 고양시 지역구별 전국 비교'''
# 전월 대비 등락률 계산
filtered_data7_change = filtered_data7.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data7_change['prev_valAmount'] = filtered_data7_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data7_change['change_rate'] = (filtered_data7_change['DTA_VAL'] - filtered_data7_change['prev_valAmount']) / \
                                       filtered_data7_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min7_change = filtered_data7_change['change_rate'].min()
y_min_with_margin7_change = y_min7_change - 0.3
y_max7_change = filtered_data7_change['change_rate'].max()
y_max_with_margin7_change = y_max7_change + 0.15

# Plotly 그래프 생성
fig15 = px.line(filtered_data7_change,
                x='WRTTIME_IDTFR_ID',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '덕양구': '#0047AB',
                    '일산동구': '#008080',
                    '일산서구': '#A95FBA',
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
        'text': '전세가격지수 등락률 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

'''16번그래프 : 전세가격지수 등락률 고양시 지역구별 6대광역시 비교'''
# 전월 대비 등락률 계산
filtered_data8_change = filtered_data8.sort_values(['CLS_NM', 'WRTTIME_IDTFR_ID'])
filtered_data8_change['prev_valAmount'] = filtered_data8_change.groupby('CLS_NM')['DTA_VAL'].shift(1)
filtered_data8_change['change_rate'] = (filtered_data8_change['DTA_VAL'] - filtered_data8_change['prev_valAmount']) / \
                                       filtered_data8_change['prev_valAmount'] * 100

# y축 최솟값과 최댓값 계산
y_min8_change = filtered_data8_change['change_rate'].min()
y_min_with_margin8_change = y_min8_change - 0.3
y_max8_change = filtered_data8_change['change_rate'].max()
y_max_with_margin8_change = y_max8_change + 0.15

# Plotly 그래프 생성
fig16 = px.line(filtered_data8_change,
                x='WRTTIME_IDTFR_ID',
                y='change_rate',
                color='CLS_NM',
                color_discrete_map={
                    '덕양구': '#0047AB',
                    '일산동구': '#008080',
                    '일산서구': '#A95FBA',
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
        'text': '전세가격지수 등락률 최근 26주 고양시 지역구별 전국 비교',
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
        showticklabels=False,
        title=None,
        showgrid=False,  # 세로선
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
        tickformat=".2%",
    ),
    width=750,  # 그래프 너비
    height=500,  # 그래프 높이
    plot_bgcolor='white',  # 그래프 배경색을 깔끔한 흰색으로
    paper_bgcolor='white',  # 전체 배경색을 가벼운 회색
    margin=dict(l=40, r=40, t=80, b=60),  # 여백 조정
)

# Dash 애플리케이션 초기화
app = dash.Dash(__name__)
server = app.server

# 레이아웃 정의
app.layout = html.Div([
    dcc.Graph(id='line-chart', figure=fig1),
    dcc.Interval(id='graph-interval', interval=3000, n_intervals=0)  # 5초 간격
])

# 콜백 함수 정의
@app.callback(
    Output('line-chart', 'figure'),
    Input('graph-interval', 'n_intervals')
)
def update_graph(n):
    # 3개의 그래프를 순환
    figures = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13, fig14, fig15, fig16]
    return figures[n % len(figures)]

# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)

# '고양시': '#B0E0E6',
# '덕양구': '#B0E0E6',
# '일산동구': '#EAB8E4',
# '일산서구': '#90EE90',
# '6대광역시': '#FFB6C1',
# '전국': '#FFB6C1',

# 등락률 %표기
# 애니메이션 삭제, 그래프별 3초