# -*- coding: utf-8 -*-
# 메인 페이지: MBTI 포켓몬 추천 (독립 실행 - 다른 파일 import 없음)
import streamlit as st
import random

st.set_page_config(page_title="MBTI 포켓몬 추천소", page_icon="⚡", layout="centered")

def poke_img(dex_num: int) -> str:
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_num}.png"

MBTI_POKEMON = {
    "INTJ": {"별명": "용의주도한 전략가", "포켓몬": "뮤츠", "번호": 150, "이모지": "🧬", "타입": "에스퍼",
        "이유": "냉철한 지능과 완벽한 전략으로 모든 상황을 계산하는 뮤츠는 INTJ의 상징 그 자체예요. 혼자만의 시간 속에서 세상을 꿰뚫어 보는 통찰력이 닮았습니다.",
        "궁합포켓몬": [("프테라", 142), ("메타그로스", 376)]},
    "INTP": {"별명": "논리적인 사색가", "포켓몬": "로토무", "번호": 479, "이모지": "🔌", "타입": "전기/고스트",
        "이유": "다양한 형태로 변신하며 기계 속을 탐구하는 로토무처럼, INTP는 끝없는 호기심으로 세상의 원리를 파고드는 탐구자예요.",
        "궁합포켓몬": [("폴리곤Z", 474), ("야도란", 80)]},
    "ENTJ": {"별명": "대담한 통솔자", "포켓몬": "리자몽", "번호": 6, "이모지": "🔥", "타입": "불꽃/비행",
        "이유": "강력한 카리스마로 하늘을 지배하는 리자몽은 목표를 향해 거침없이 나아가는 ENTJ의 리더십을 그대로 보여줘요.",
        "궁합포켓몬": [("갸라도스", 130), ("보만다", 373)]},
    "ENTP": {"별명": "뜨거운 논쟁을 즐기는 변론가", "포켓몬": "개굴닌자", "번호": 658, "이모지": "🥷", "타입": "물/악",
        "이유": "예측 불가능한 움직임과 재치 있는 전술로 상대를 압도하는 개굴닌자처럼, ENTP는 번뜩이는 아이디어로 판을 뒤집는 천재예요.",
        "궁합포켓몬": [("조로아크", 571), ("팬텀", 94)]},
    "INFJ": {"별명": "선의의 옹호자", "포켓몬": "가디안", "번호": 282, "이모지": "💫", "타입": "에스퍼/페어리",
        "이유": "트레이너의 마음을 읽고 목숨 걸고 지켜주는 가디안은 깊은 공감 능력과 헌신을 가진 INFJ와 완벽하게 닮았어요.",
        "궁합포켓몬": [("루기아", 249), ("세레비", 251)]},
    "INFP": {"별명": "열정적인 중재자", "포켓몬": "이브이", "번호": 133, "이모지": "🌸", "타입": "노말",
        "이유": "무한한 가능성을 품고 자신만의 길을 찾아가는 이브이는 이상을 향해 조용히 성장하는 INFP의 여정과 같아요.",
        "궁합포켓몬": [("님피아", 700), ("치코리타", 152)]},
    "ENFJ": {"별명": "정의로운 사회운동가", "포켓몬": "루카리오", "번호": 448, "이모지": "🌊", "타입": "격투/강철",
        "이유": "파동으로 모두의 마음을 느끼고 정의를 위해 싸우는 루카리오는 사람들을 이끌고 성장시키는 ENFJ의 모습 그 자체예요.",
        "궁합포켓몬": [("윈디", 59), ("칠색조", 250)]},
    "ENFP": {"별명": "재기발랄한 활동가", "포켓몬": "피카츄", "번호": 25, "이모지": "⚡", "타입": "전기",
        "이유": "에너지 넘치는 매력으로 모두에게 사랑받는 피카츄! 어디서든 분위기를 밝히는 ENFP의 긍정 에너지와 찰떡이에요.",
        "궁합포켓몬": [("파치리스", 417), ("토게키스", 468)]},
    "ISTJ": {"별명": "청렴결백한 논리주의자", "포켓몬": "괴력몬", "번호": 68, "이모지": "💪", "타입": "격투",
        "이유": "맡은 일은 묵묵히, 그리고 확실하게 해내는 괴력몬은 책임감과 성실함의 대명사인 ISTJ와 닮은꼴이에요.",
        "궁합포켓몬": [("딱구리", 76), ("보스로라", 306)]},
    "ISFJ": {"별명": "용감한 수호자", "포켓몬": "라프라스", "번호": 131, "이모지": "🌊", "타입": "물/얼음",
        "이유": "넓은 등으로 사람들을 태우고 바다를 건너주는 라프라스는 조용히 타인을 돌보는 ISFJ의 따뜻함을 담고 있어요.",
        "궁합포켓몬": [("해피너스", 242), ("밀탱크", 241)]},
    "ESTJ": {"별명": "엄격한 관리자", "포켓몬": "한카리아스", "번호": 445, "이모지": "🦈", "타입": "드래곤/땅",
        "이유": "압도적인 실행력으로 목표를 향해 돌진하는 한카리아스는 체계적이고 결단력 있는 ESTJ의 추진력을 보여줘요.",
        "궁합포켓몬": [("대짱이", 260), ("토대부기", 389)]},
    "ESFJ": {"별명": "사교적인 외교관", "포켓몬": "해피너스", "번호": 242, "이모지": "🥚", "타입": "노말",
        "이유": "행복의 알을 나눠주며 모두를 치유하는 해피너스처럼, ESFJ는 주변 사람들을 챙기고 화목을 만드는 분위기 메이커예요.",
        "궁합포켓몬": [("픽시", 36), ("라란티스", 754)]},
    "ISTP": {"별명": "만능 재주꾼", "포켓몬": "스라크", "번호": 123, "이모지": "🗡️", "타입": "벌레/비행",
        "이유": "군더더기 없는 움직임과 실전 감각의 달인 스라크는 필요한 순간에만 나서서 완벽하게 해결하는 ISTP와 닮았어요.",
        "궁합포켓몬": [("앱솔", 359), ("핫삼", 212)]},
    "ISFP": {"별명": "호기심 많은 예술가", "포켓몬": "포챠마", "번호": 393, "이모지": "🐧", "타입": "물",
        "이유": "자존심은 세지만 사실은 감성 충만한 포챠마! 자기만의 미학을 지키며 살아가는 ISFP의 귀여운 고집과 똑 닮았어요.",
        "궁합포켓몬": [("파이리", 4), ("누오", 195)]},
    "ESTP": {"별명": "모험을 즐기는 사업가", "포켓몬": "마기라스", "번호": 248, "이모지": "🏔️", "타입": "바위/악",
        "이유": "산을 무너뜨릴 기세로 화끈하게 밀어붙이는 마기라스는 스릴을 즐기고 행동으로 보여주는 ESTP의 에너지와 딱이에요.",
        "궁합포켓몬": [("에레키블", 466), ("헬가", 229)]},
    "ESFP": {"별명": "자유로운 영혼의 연예인", "포켓몬": "푸린", "번호": 39, "이모지": "🎤", "타입": "노말/페어리",
        "이유": "무대 위에서 노래하는 걸 사랑하는 푸린은 주목받을 때 가장 빛나는 ESFP의 흥과 끼를 그대로 보여줘요.",
        "궁합포켓몬": [("라이츄", 26), ("마임맨", 122)]},
}

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
    st.markdown("<p style='text-align:center; font-size:20px; color:#555; margin-bottom:0;'>당신의 파트너 포켓몬은...</p>", unsafe_allow_html=True)

    img_l, img_c, img_r = st.columns([1, 2, 1])
    with img_c:
        st.image(poke_img(data["번호"]), use_container_width=True)

    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffe4e1, #fff8dc); border-radius: 20px; padding: 20px; text-align: center; border: 3px solid #ff6b6b;">
            <p style="font-size: 44px; font-weight: bold; margin: 0; color: #e63946;">{data['이모지']} {data['포켓몬']} {data['이모지']}</p>
            <p style="font-size: 18px; margin: 5px 0 0 0; color: #457b9d;">타입: {data['타입']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown("### 💡 왜 이 포켓몬일까요?")
    st.success(data["이유"])

    st.markdown("### 🤝 함께하면 좋은 궁합 포켓몬")
    c1, c2 = st.columns(2)
    for col, (p_name, p_num) in zip([c1, c2], data["궁합포켓몬"]):
        with col:
            st.image(poke_img(p_num), use_container_width=True)
            st.markdown(f"<p style='text-align:center; font-size:20px; font-weight:bold; margin-top:-10px;'>{p_name}</p>", unsafe_allow_html=True)

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
    st.markdown("""
        <div style="text-align: center; padding: 40px; color: #888;">
            <p style="font-size: 60px; margin: 0;">🔴</p>
            <p style="font-size: 18px;">위에서 MBTI를 선택하면<br>당신의 파트너 포켓몬이 나타나요!</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Made with ⚡ Streamlit | 이미지: PokeAPI 공식 아트워크 | 재미로 봐주세요 😊")
