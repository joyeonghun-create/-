import streamlit as st
import openai
import os

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "key"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit 앱
st.title(" 🎶음악 추천 서비스 🎶")
st.subheader("🎤당신의 현재 기분에 맞는 음악을 추천해 드립니다.")

# 사용자 입력
mood_description = st.text_area("현재 기분을 간단히 설명해주세요:")

# 버튼 클릭 시 추천 음악 생성
if st.button("음악 추천 받기💿"):
    if mood_description.strip():
        with st.spinner("음악을 추천하는 중입니다..."):
            try:
                # OpenAI ChatCompletion 요청
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "user",
                            "content": f"나는 지금 다음과 같은 기분이야: {mood_description}. "
                                       f"이 기분에 어울리는 음악 10곡을 k-pop,pop,j-pop,rock등 다양한 장르로 간단한 이유와 함께 추천해줘. ",
                        }
                    ],
                )

                # OpenAI 응답 처리
                music_recommendations = response['choices'][0]['message']['content']
                st.success("📜추천 음악 리스트📜")
                st.write(music_recommendations)

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("기분을 입력해주세요!")
