import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import joblib
import time
import numpy as np

def cook_breakfast():
    msg = st.toast('잠시만 기다려주세요...')
    time.sleep(1)
    msg.toast('BMI 계산중...')
    time.sleep(1)
    msg.toast('BMI 정보가 저장되었습니다!', icon = "🎉")


def run_predict():
    
    st.subheader('심장 마비 발병 여부 예측하기')
    st.title('')

    # 1. 예측하기 위해서 유저에게 데이터 입력받기
    # Age(나이) , Cholestrol(콜레스트롤 수치) , Heart Rate(심박수) , Exercise Hours Per Week(주에 운동 몇시간) , systolic blood pressure(수축기 혈압) , diastolic blood pressure(이완기 혈압)
    # Sedentary Hours Per Day (하루에 얼마나 앉아있냐) , BMI
    # Trglycerides(중성지방 수치) , Stress Level(스트레스 수준) , Physical Activity Days Per Week(주에 몇번 신체활동) , Sleep Hours Per Day(하루 수면시간) , Diabetes(당뇨병), 
    #  Family History(가족력) , Smoking(흡연 유무) , Obesity(비만이신가요) , Alcohol Consumption(음주 여부)
    # Previous Heart Problems(이전에 심장 문제) , Medication Use(약물 사용) , Sex(성별)

    st.subheader('나이', divider='gray')
    age = st.number_input('나이를 입력해주세요!' , 1)
    st.subheader('')


    st.subheader('심박수', divider='gray')
    heart_rate = st.number_input('현재 심박수를 입력해주세요!', step=20, value=60)
    st.subheader('')


    st.subheader('주 운동 시간', divider='gray')
    exercise_hours_per_week = st.number_input('일주일에 운동을 몇 시간 하시나요?' , 0)
    st.subheader('')


    st.subheader('수축기 혈압', divider='gray')
    systolic_blood_pressure = st.number_input('수축기 혈압을 알려주세요! (최고 혈압)', 0, step=20, value=120)
    st.subheader('')


    st.subheader('이완기 혈압', divider='gray')
    diastolic_blood_pressure = st.number_input('이완기 혈압을 알려주세요! (최저 혈압)', 0, step=20, value=80)
    st.subheader('')


    st.subheader('하루 앉아있는 시간', divider='gray')
    sedentary_hours_per_day = st.slider('하루에 얼마나 앉아 계신가요?', 0, 24)
    st.subheader('')

    
    st.subheader('BMI', divider='gray')
    weight = st.number_input('체중을 알려주세요!', value=60)
    height = st.number_input('키를 알려주세요!', value=170)
    bmi = round(weight / (height/100)**2, 2)
    if st.button('BMI 계산하기', help='입력하신 키와 체중으로 BMI를 계산합니다!'):
        cook_breakfast()
        st.info(f'당신의 BMI는 {bmi}입니다!', icon='👉')
    st.subheader('')

    
    
    st.subheader('중성 지방 수치', divider='gray')
    trglycerides = st.number_input('중성 지방 수치를 알려주세요!', min_value=0, value=140, step=10)
    if st.button('모르겠어요😥', help='버튼을 클릭하시면 BMI를 바탕으로 중성지방 수치를 입력합니다!'):
        st.toast('사용자님의 BMI를 바탕으로 중성지방 수치를 입력할게요!')
        time.sleep(.5)
        if bmi < 18.5:
            trglycerides = 130
        elif 18.5 <= bmi < 23:
            trglycerides = 140
        elif 23<= bmi < 25:
            trglycerides = 170
        elif 25<= bmi <30:
            trglycerides = 250
        else:
            trglycerides = 400
        st.toast('잠시만 기다려주세요...')
        time.sleep(.5)
        st.toast('중성 지방 수치를 저장하였습니다!', icon='🎉')
    st.subheader('')


    st.subheader('콜레스트롤', divider='gray')
    cholestrol = st.number_input('콜레스트롤 수치를 입력해주세요!', step=20, value=120)
    if st.button('모르겠어요😢', help='버튼을 클릭하시면 BMI를 바탕으로 콜레스트롤 수치를 입력합니다!'):
        st.toast('사용자님의 BMI를 바탕으로 콜레스트롤 수치를 입력할게요!')
        if bmi < 18.5:
            cholestrol = 100
        elif 18.5 <= bmi < 23:
            cholestrol = 120
        elif 23<= bmi < 25:
            cholestrol = 150
        elif 25<= bmi <30:
            cholestrol = 160
        else:
            cholestrol = 180
        st.toast('잠시만 기다려주세요...')
        time.sleep(.5)
        st.toast('콜레스트롤 수치를 저장하였습니다!', icon='🎉')
    st.subheader('')


    st.subheader('스트레스 수준', divider='gray')
    stress_level = st.slider('스트레스 수준을 입력해주세요!', 1, 10, help='(좋음 1  ~  10 나쁨)')
    st.subheader('')
    


    st.subheader('주 신체 활동 횟수', divider='gray')
    physical_activity_days_per_week = st.slider('일주일에 신체 활동을 몇번 하시나요?', 0, 7)
    st.subheader('')


    st.subheader('하루 수면 시간', divider='gray')
    sleep_hours_per_day = st.slider('하루에 몇 시간 주무시나요?', 0, 24, value=7)
    st.subheader('')


    st.subheader('당뇨병', divider='gray')
    diabetes = st.radio('당뇨가 있으신가요?', options=['예', '아니오'], horizontal=True)
    if diabetes == '아니오':
        diabetes = 0
    else:
        diabetes = 1
    st.subheader('')


    st.subheader('가족력', divider='gray')
    family_history = st.radio('가족중에 심장마비를 경험한 인원이 있나요?', options=['예', '아니오'], horizontal=True)
    if family_history == '아니오':
        family_history = 0
    else:
        family_history = 1
    st.subheader('')

    
    st.subheader('흡연', divider='gray')
    smoking = st.radio('흡연을 하시나요?', options=['예', '아니오'], horizontal=True)
    if smoking == '아니오':
        smoking = 0
    else:
        smoking = 1
    st.subheader('')


    if bmi < 18.5:
        Obesity = 0
    elif 18.5 <= bmi < 23:
        Obesity = 0
    elif 23<= bmi < 25:
        Obesity = 1
    elif 25<= bmi <30:
        Obesity = 1
    else:
        Obesity = 1


    st.subheader('음주', divider='gray')
    alcohol_consumption = st.radio('음주를 하시나요?', options=['예', '아니오'], horizontal=True)
    if alcohol_consumption == '아니오':
        alcohol_consumption = 0
    else:
        alcohol_consumption = 1
    st.subheader('')

    
    st.subheader('과거 심장마비 경험', divider='gray')
    previous_heart_problems = st.radio('과거에 심장마비를 경험한 적이 있나요?', options=['예', '아니오'], horizontal=True)
    if previous_heart_problems == '아니오':
        previous_heart_problems = 0
    else:
        previous_heart_problems = 1
    st.subheader('')


    medication_use = 0


    st.subheader('성별', divider='gray')
    sex = st.radio('성별을 알려주세요!', options=['남자', '여자'], horizontal=True)
    if sex == '남자':
        sex = 0
    else:
        sex = 1
    st.subheader('')


    #2 예측
    
    # 2-1. 모델 불러오기
    regressor = joblib.load('./model/heart_attack_prediction.pkl')

    # 2-2. 유저가 입력한 데이터를 모델에 예측할 수 있도록 가공
    new_data = [age, cholestrol, heart_rate, exercise_hours_per_week, systolic_blood_pressure, diastolic_blood_pressure, sedentary_hours_per_day, bmi, trglycerides, stress_level, 
                physical_activity_days_per_week, sleep_hours_per_day, diabetes, family_history, smoking, Obesity, alcohol_consumption, previous_heart_problems, medication_use, sex]
    
    new_data = np.array(new_data).reshape(1,-1)

    # 2-3. 예측하기
    y_pred = regressor.predict(new_data)
    print(y_pred)
    
    # 2-4. 유저에게 보여주기
    if st.button('예측하기'):
        progress_text = "예측중입니다.. 잠시만 기다려주세요.."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        if y_pred == 1:
            st.error('당신은 심장 마비를 경험할 것으로 예측됩니다.. 건강 관리에 신경써주세요!')
        else:
            st.balloons()
            st.image('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWcwZXRyNWZ5czNuMTd4cXZmbjN6dGJ6ODZma2N6czRqZnVtbjJmdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YrfHgORAzpJKtXINnQ/giphy.gif', use_column_width=True)
            st.info('당신은 심잠 마비를 경험하지 않을 것으로 예측됩니다! 지금처럼 건강에 신경써주세요!')

