import streamlit as st
import pandas as pd
import seaborn as sb
import time

# 차트에 한글 나오게 설정
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    plt.rc('font', family='NanumGothic')

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


    up_col = ['심장마비 경험', '나이', '하루에 앉아있는 시간', '스트레스 수준', '주 신체활동 일수', '수면 시간', '당뇨병',
                '가족력', '흡연', '비만', '음주', '과거 심장 질환', '성별']

    st.subheader('')
    st.subheader('데이터', divider='gray')
    st.dataframe(df)


    st.subheader('')
    st.subheader('컬럼별 비율 그래프 보기', divider='gray')
    #col_choice = st.selectbox('어떤 ', options=up_col, )
    col_choice = st.selectbox( "어떤 컬럼의 비율 그래프를 확인하시겠습니까?",
                        up_col,
                        index=None,
                        placeholder="컬럼을 선택해주세요...",)
    st.write("선택한 컬럼 👉 ", col_choice)

    if col_choice == col[0]: # 심장마비 경험 비율
        fig = plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[0]].value_counts().index, y=df[col[0]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[0]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[0]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[0], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(fig)

    elif col_choice == col[1]: # 나이 비율
        fig = plt.figure(figsize=(12,8))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
        sb.countplot(x=df[col[1]], color='#2EFEF7')
        plt.title(col_rate[1]+'\n', fontsize=14)
        plt.xticks(rotation=90)
        plt.xlabel('\n나이')
        st.pyplot(fig)

    elif col_choice == col[7]: # 하루에 앉아있는 시간 비율
        feature = df.groupby(col[7])[col[7]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
        plt.subplot(1, 2, 1)
        sb.barplot(x=feature.index, y=feature.values)
        plt.subplot(1, 2, 2)
        plt.pie(x=feature.values, autopct="%.1f%%", pctdistance=0.8,
                labels= feature.index)
        plt.suptitle(col_rate[7], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif col_choice == col[10]: # 스트레스 수준 비율
        feature = df.groupby(col[10])[col[10]].count()
        plt.figure(figsize=(12,5))
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
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
        sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic')
        plt.subplot(1, 2, 1)
        sb.barplot(x=df[col[19]].value_counts().index, y=df[col[19]].value_counts())
        plt.subplot(1, 2, 2)
        plt.pie(x=df[col[19]].value_counts(), autopct="%.1f%%", pctdistance=0.8,
                labels= df[col[19]].value_counts().index, shadow=True, explode=[0.05,0.05])
        plt.suptitle(col_rate[19], fontsize=16)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()




# 컬럼별 그래프 보기
#-------------------------------------------------------------------------------------------------------------------------

    df_corr = pd.read_csv('data.csv')
    df_corr.drop('Unnamed: 0', axis=1, inplace=True)
    df_corr.drop('Medication Use', axis=1, inplace=True)
    col = ['심장마비 경험', '나이', '콜레스트롤 수치', '심박수', '주 운동 시간', '수축기 혈압', '이완기 혈압',
                '하루에 앉아있는 시간', 'BMI', '중성지방 수치', '스트레스 수준', '주 신체활동 일수', '수면 시간', '당뇨병',
                '가족력', '흡연', '비만', '음주', '과거 심장 질환', '성별']
    
    df_corr.columns = col
    
    heart_attack_corr = df_corr.corr()["심장마비 경험"]
    heart_attack_corr = heart_attack_corr.drop("심장마비 경험", axis=0).sort_values(ascending=False)



    st.subheader('')
    st.subheader('')
    st.subheader('상관관계 확인하기', divider='gray')

    fig_barplot = plt.figure(figsize=(10,5))
    sb.set(rc={'axes.facecolor':'c0c0c0', 'figure.facecolor':'lightblue'}, font='NanumGothic', font_scale=0.8)
    sb.barplot(x=heart_attack_corr.index, y=heart_attack_corr, color="#4a804d")
    plt.xticks(rotation=60)
    plt.ylim(-0.03, 0.03)
    plt.title("심장마비와 변수들의 상관관계 ", fontsize=15)
    st.pyplot(fig_barplot)

# 버튼을 토글처럼 만들기
#--------------------------------------------------------------------------
    def word():
        opening_words = """
        \n**상관계수란**?
        \n👉 두 변수 사이의 통계적 관계를 표현하기 위해 특정한 상관 관계의 정도를 수치적으로 나타낸 계수입니다!

        \n- 상관 계수가 **1에 가까울수록 강력한 비례 관계**입니다.
        \n- 상관 계수가 **0에 가까울수록 약한 비례/반비례 관계**입니다
        \n- 상관 계수가 **-1에 가까울수록 강력한 반비례 관계**입니다

        \n\n 상관 계수를 확인하고 위 상관관계 그래프를 해석해보세요!
        """

        for word in opening_words.split(" "):
            yield word + " "
            time.sleep(0.027)
    
    if 'button' not in st.session_state:
        st.session_state.button = False

    def click_button():
        st.session_state.button = not st.session_state.button

    st.button('상관계수란?', on_click=click_button, help='상관계수를 확인하려면 버튼을 클릭하세요!', disabled=False)

    if st.session_state.button:
        st.write_stream(word)
        st.image('https://t1.daumcdn.net/cfile/tistory/99C148495C6AA1AA16')
        

    else:
        pass
#--------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

    

