# -*- coding: utf-8 -*-
# 메인 페이지: MBTI 포켓몬 추천
# 폴더 구조:
#   app.py            <- 이 파일 (메인, 스트림릿 클라우드에서 Main file로 지정)
#   pokemon_data.py   <- 공용 데이터
#   pages/
#     1_💼_워크_스타일_분석.py

import streamlit as st
import random
from pokemon_data import MBTI_POKEMON, poke_img

st.set_page_config(page_title="MBTI 포켓몬 추천소", page_icon="⚡", layout="centered")

st.title("⚡ MBTI 포켓몬 추천소 🔴")
st.markdown("#### 당신의 MBTI에 딱 맞는 파트너 포켓몬을 찾아드려요!")
st.caption("👈 왼쪽 사이드바에서 **워크 스타일 분석** 페이지로 이동할 수 있어요.")
st.divider()

mbti_list = list(MBTI_POKEMON.keys())

col1, col2 = st.columns([2, 1])
with col1:
    selected_mbti = st.selectbox("🧭 당신의 MBTI를 선택하세요", ["선택해주세요"] + mbti_list)
with col2:
    st.write("")
    st.write("")
    random_pick = st.button("🎲 랜덤 뽑기")

if random_pick:
    selected_mbti = random.choice(mbti_list)
    st.info(f"랜덤으로 **{selected_mbti}** 가 선택되었어요!")

if selected_mbti != "선택해주세요":
    data = MBTI_POKEMON[selected_mbti]

    st.balloons()
    st.divider()

    st.markdown(f"## {data['이모지']} {selected_mbti} — {data['별명']}")

    st.markdown(
        "<p style='text-align:center; font-size:20px; color:#555; margin-bottom:0;'>당신의 파트너 포켓몬은...</p>",
        unsafe_allow_html=True,
    )

    img_l, img_c, img_r = st.columns([1, 2, 1])
    with img_c:
        st.image(poke_img(data["번호"]), use_container_width=True)

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ffe4e1, #fff8dc);
            border-radius: 20px; padding: 20px; text-align: center;
            border: 3px solid #ff6b6b;">
            <p style="font-size: 44px; font-weight: bold; margin: 0; color: #e63946;">
                {data['이모지']} {data['포켓몬']} {data['이모지']}
            </p>
            <p style="font-size: 18px; margin: 5px 0 0 0; color: #457b9d;">타입: {data['타입']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### 💡 왜 이 포켓몬일까요?")
    st.success(data["이유"])

    st.markdown("### 🤝 함께하면 좋은 궁합 포켓몬")
    c1, c2 = st.columns(2)
    for col, (p_name, p_num) in zip([c1, c2], data["궁합포켓몬"]):
        with col:
            st.image(poke_img(p_num), use_container_width=True)
            st.markdown(
                f"<p style='text-align:center; font-size:20px; font-weight:bold; margin-top:-10px;'>{p_name}</p>",
                unsafe_allow_html=True,
            )

    st.divider()

    st.markdown("### 🔮 오늘의 트레이너 운세")
    fortunes = [
        "오늘은 전설의 포켓몬을 만날 것 같은 예감! 자신감을 가지세요. ✨",
        "친구와 함께라면 어떤 배틀도 이길 수 있어요. 협력의 날입니다. 🤝",
        "새로운 도전이 행운을 가져다줘요. 낯선 길로 걸어보세요. 🌈",
        "휴식이 필요한 날이에요. 포켓몬센터에서 재충전하세요. 💤",
        "작은 노력이 큰 진화로 이어지는 날! 꾸준함이 답입니다. 📈",
        "생각지 못한 곳에서 희귀 아이템을 발견할지도 몰라요. 🎁",
    ]
    if st.button("🎰 운세 뽑기"):
        st.info(random.choice(fortunes))

else:
    st.markdown(
        """
        <div style="text-align: center; padding: 40px; color: #888;">
            <p style="font-size: 60px; margin: 0;">🔴</p>
            <p style="font-size: 18px;">위에서 MBTI를 선택하면<br>당신의 파트너 포켓몬이 나타나요!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.caption("Made with ⚡ Streamlit | 이미지: PokeAPI 공식 아트워크 | 재미로 봐주세요 😊")
