import streamlit as st


def run_home():
        opening_words = """
        \n이 앱은 **심장 마비를 경험한 사람들과 경험하지 않은 사람들의 건강 상태 데이터**를 분석하여 **차트를 제공**하고, **심장마비 발병 여부를 예측**할 수 있습니다. 

        \n**심장 마비와 신체 정보의 상관관계를 분석하여 차트로 제공합니다.**
        차트를 확인하여 심장 마비를 유발하는 요인들을 파악할 수 있습니다.

        \n또한 **심장 마비 발병 예측 서비스를 제공합니다.**
        사용자님이 입력하신 정보를 가지고 심장 마비 발병 여부를 예측합니다. 

        
        \n좌측 메뉴에서 **EDA**를 선택하시면 상관관계를 분석한 차트를 제공합니다.
        사용자님이 선택하여 원하는 정보를 확인할 수 있습니다.

        \n좌측 메뉴에서 **심장마비 예측**을 선택하시면 사용자님이 입력하신 정보로 심장병 발병 여부를 예측합니다.
        
        \n이제 앱을 시작해보세요!😊
        """

        
        st.image('https://cdn.pixabay.com/animation/2023/06/26/14/52/14-52-08-199_512.gif', width=500)
        st.write(opening_words)

        st.subheader('', divider='gray')
        st.page_link('https://www.kaggle.com/datasets/m1relly/heart-attack-prediction', label='**데이터는 Kaggle에 있는 Heart Attack Prediction Data를 이용하였습니다.**', 
                     icon='💾', help='출처로 이동')