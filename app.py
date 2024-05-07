import streamlit as st
from eda import run_eda
from home import run_home
from predict import run_predict

# 차트에 한글 나오게 설정
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')



def main():


    #sidebar
    selectbox_list = ['🏠홈', '📊EDA', '👨‍💻심장마비 예측']

    st.sidebar.header('💪당신의 심장은 건강한가요?', divider='red')
    st.sidebar.image('https://cdn.icon-icons.com/icons2/2134/PNG/512/heart_cute_emoji_emo_icon_131637.png')
    st.sidebar.subheader('', divider='red')
    choice_selectbox = st.sidebar.selectbox('메뉴 선택', selectbox_list)
    st.sidebar.title('')
    st.sidebar.title('')
    st.sidebar.title('')
    st.sidebar.title('')
    st.sidebar.page_link('https://www.kaggle.com/datasets/m1relly/heart-attack-prediction', label='데이터 출처', icon='💾')

    


    if choice_selectbox == selectbox_list[0]:
        st.title('💘 :red[심장마비] 발병 예측')
        st.image('https://cdn.pixabay.com/animation/2023/06/26/14/52/14-52-08-199_512.gif', width=500)
        if st.button("도움말"):
            st.write_stream(run_home)
    

    elif choice_selectbox == selectbox_list[1]:
        st.title('📊 EDA 분석')
        run_eda()

    elif choice_selectbox == selectbox_list[2]:
        st.title('👨‍💻 심장 마비 예측')
        run_predict()
    

    


if __name__ == "__main__":
    main()