import streamlit as st
import pandas as pd
import seaborn as sb

# 차트에 한글 나오게 설정
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    plt.rc('font', family='NanumGothic')
    sb.set(font='NanumGothic')

def run_eda():
    
    df = pd.read_csv('data.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.drop('Medication Use', axis=1, inplace=True)
    col = ['심장마비 경험', '나이', '콜레스트롤 수치', '심박수', '주 운동 시간', '수축기 혈압', '이완기 혈압',
                '하루에 앉아있는 시간', 'BMI', '중성지방 수치', '스트레스 수준', '주 신체활동 일수', '수면 시간', '당뇨병',
                '가족력', '흡연', '비만', '음주', '과거 심장 질환', '성별']
    
    col_rate = ['심장마비 경험 비율', '나이 비율', '콜레스트롤 수치 비율', '심박수 비율', '주 운동 시간 비율', '수축기 혈압 비율', '이완기 혈압 비율',
                '하루에 앉아있는 시간 비율', 'BMI 비율', '중성지방 수치 비율', '스트레스 수준 비율', '주 신체활동 일수 비율', '수면 시간 비율', '당뇨병 비율',
                '가족력 비율', '흡연 비율', '비만 비율', '음주 비율', '과거 심장 질환 비율', '성별 비율']

    df.columns = col

    df['성별'].loc[df['성별'] == 1, ] = '남자'
    df['성별'].loc[df['성별'] == 0, ] = '여자'

    df['심장마비 경험'].loc[df['심장마비 경험'] == 1, ] = '예'
    df['심장마비 경험'].loc[df['심장마비 경험'] == 0, ] = '아니오'

    df['주 운동 시간'] = round(df['주 운동 시간'], 0)
    df['하루에 앉아있는 시간'] = round(df['하루에 앉아있는 시간'], 0)

    df['당뇨병'].loc[df['당뇨병'] == 1, ] = '예'
    df['당뇨병'].loc[df['당뇨병'] == 0, ] = '아니오'

    df['가족력'].loc[df['가족력'] == 1, ] = '예'
    df['가족력'].loc[df['가족력'] == 0, ] = '아니오'

    df['흡연'].loc[df['흡연'] == 1, ] = '예'
    df['흡연'].loc[df['흡연'] == 0, ] = '아니오'

    df['비만'].loc[df['비만'] == 1, ] = '예'
    df['비만'].loc[df['비만'] == 0, ] = '아니오'

    df['음주'].loc[df['음주'] == 1, ] = '예'
    df['음주'].loc[df['음주'] == 0, ] = '아니오'

    df['과거 심장 질환'].loc[df['과거 심장 질환'] == 1, ] = '예'
    df['과거 심장 질환'].loc[df['과거 심장 질환'] == 0, ] = '아니오'



    st.subheader('')
    st.subheader('데이터', divider='gray')
    st.dataframe(df)

    st.subheader('')
    st.subheader('그래프 보기', divider='gray')
    col_choice = st.selectbox('그래프 보기', options=col)

    if col_choice == col[0]: # 심장마비 경험 비율
        fig = plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[0]].value_counts().index, y=df[col[0]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[0]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[0]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[0], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(fig)

    elif col_choice == col[1]: # 나이 비율(미완)
        pass

    elif col_choice == col[2]: # 콜레스트롤 수치 비율(미완)
        pass

    elif col_choice == col[3]: # 심박수 비율(미완)
        pass

    elif col_choice == col[4]: # 주 운동시간 비율(미완)
        pass

    elif col_choice == col[5]: # 수축기 혈압 비율(미완)
        pass

    elif col_choice == col[6]: # 이완기 혈압 비율(미완)
        pass

    elif col_choice == col[7]: # 하루에 앉아있는 시간 비율
        feature = df.groupby(col[7])[col[7]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=feature.index, y=feature.values)
        plt.subplot(1, 2, 2)
        plt.pie(x=feature.values, autopct="%.1f%%", pctdistance=0.8,
                labels= feature.index)
        plt.suptitle(col_rate[7], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[8]: # BMI 비율 (미완)
        pass

    elif col_choice == col[9]: # 중성지방 수치 비율(미완)
        pass

    elif col_choice == col[10]: # 스트레스 수준 비율
        feature = df.groupby(col[10])[col[10]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=feature.index, y=feature.values)
        plt.subplot(1, 2, 2)
        plt.pie(x=feature.values, autopct="%.1f%%", pctdistance=0.8,
                labels= feature.index)
        plt.suptitle(col_rate[10], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[11]: # 주 신체활동 일수 비율
        feature = df.groupby(col[11])[col[11]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=feature.index, y=feature.values)
        plt.subplot(1, 2, 2)
        plt.pie(x=feature.values, autopct="%.1f%%", pctdistance=0.8,
                labels= feature.index)
        plt.suptitle(col_rate[11], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[12]: # 수면시간 비율
        feature = df.groupby(col[12])[col[12]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=feature.index, y=feature.values)
        plt.subplot(1, 2, 2)
        plt.pie(x=feature.values, autopct="%.1f%%", pctdistance=0.8,
                labels= feature.index)
        plt.suptitle(col_rate[12], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[13]: # 당뇨병 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[13]].value_counts().index, y=df[col[13]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[13]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[13]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[13], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[14]: # 가족력 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[14]].value_counts().index, y=df[col[14]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[14]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[14]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[14], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[15]: # 흡연 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[15]].value_counts().index, y=df[col[15]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[15]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[15]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[15], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[16]: # 비만 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[16]].value_counts().index, y=df[col[16]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[16]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[16]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[16], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[17]: # 음주 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[17]].value_counts().index, y=df[col[17]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[17]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[17]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[17], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[18]: # 과거 심장질활 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[18]].value_counts().index, y=df[col[18]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[18]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[18]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[18], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[19]: # 성별 비율
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'})
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[19]].value_counts().index, y=df[col[19]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[19]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[19]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[19], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    

