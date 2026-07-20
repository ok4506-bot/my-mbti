# -*- coding: utf-8 -*-
# 서브 페이지: MBTI 워크 스타일 분석
# 이 파일은 반드시 pages/ 폴더 안에 있어야 합니다.
 
import streamlit as st
from pokemon_data import MBTI_POKEMON, MBTI_WORK, poke_img
 
st.set_page_config(page_title="MBTI 워크 스타일 분석", page_icon="💼", layout="centered")
 
st.title("💼 MBTI 워크 스타일 분석")
st.markdown("#### 본인의 MBTI를 알면 나와 가장 잘 맞는 최적의 일터 환경과 근무 위치, 업무 스타일을 파악할 수 있어요!")
st.divider()
 
mbti_list = list(MBTI_WORK.keys())
selected_mbti = st.selectbox("🧭 당신의 MBTI를 선택하세요", ["선택해주세요"] + mbti_list)
 
if selected_mbti != "선택해주세요":
    work = MBTI_WORK[selected_mbti]
    poke = MBTI_POKEMON[selected_mbti]
 
    st.divider()
 
    head_l, head_r = st.columns([1, 2])
    with head_l:
        st.image(poke_img(poke["번호"]), use_container_width=True)
    with head_r:
        st.markdown(f"## {poke['이모지']} {selected_mbti}")
        st.markdown(f"**{poke['별명']}** · 파트너 포켓몬 **{poke['포켓몬']}** 와 함께 알아보는 워크 스타일!")
 
    st.write("")
 
    st.markdown("### 🏞️ 최적의 일터 환경")
    st.info(work["환경"])
 
    st.markdown("### 📍 추천 근무 위치")
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #e0f7fa, #e8f5e9);
            border-radius: 16px; padding: 24px; text-align: center;
            border: 2px solid #4db6ac;">
            <p style="font-size: 30px; font-weight: bold; margin: 0; color: #00695c;">
                {work['위치']}
            </p>
            <p style="font-size: 16px; margin: 10px 0 0 0; color: #333;">
                {work['위치설명']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
 
    st.markdown("### 🛠️ 나의 업무 스타일")
    st.success(work["스타일"])
 
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### 🎯 잘 맞는 분야")
        st.warning(work["잘맞는일"])
    with col_b:
        st.markdown("#### 🤝 동료를 위한 협업 팁")
        st.warning(work["협업팁"])
 
    st.divider()
    st.caption("⚠️ MBTI 기반 분석은 재미와 참고용이에요. 실제 커리어 결정은 다양한 요소를 함께 고려해주세요!")
 
else:
    st.markdown(
        """
        <div style="text-align: center; padding: 40px; color: #888;">
            <p style="font-size: 60px; margin: 0;">💼</p>
            <p style="font-size: 18px;">위에서 MBTI를 선택하면<br>나에게 딱 맞는 워크 스타일이 나타나요!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
st.divider()
st.caption("Made with ⚡ Streamlit | 이미지: PokeAPI 공식 아트워크 | 재미로 봐주세요 😊")
 
