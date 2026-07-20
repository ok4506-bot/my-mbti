# -*- coding: utf-8 -*-
# 서브 페이지: MBTI 포켓몬 배틀 (독립 실행 - 다른 파일 import 없음)
# 별도 라이브러리 없이 streamlit 내장 components.html 로 애니메이션 연출
import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="MBTI 포켓몬 배틀", page_icon="⚔️", layout="centered")

def poke_img(dex_num: int) -> str:
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_num}.png"

# ---------------- MBTI별 포켓몬 ----------------
MBTI_POKEMON = {
    "INTJ": {"별명": "용의주도한 전략가", "포켓몬": "뮤츠", "번호": 150, "이모지": "🧬"},
    "INTP": {"별명": "논리적인 사색가", "포켓몬": "로토무", "번호": 479, "이모지": "🔌"},
    "ENTJ": {"별명": "대담한 통솔자", "포켓몬": "리자몽", "번호": 6, "이모지": "🔥"},
    "ENTP": {"별명": "뜨거운 논쟁을 즐기는 변론가", "포켓몬": "개굴닌자", "번호": 658, "이모지": "🥷"},
    "INFJ": {"별명": "선의의 옹호자", "포켓몬": "가디안", "번호": 282, "이모지": "💫"},
    "INFP": {"별명": "열정적인 중재자", "포켓몬": "이브이", "번호": 133, "이모지": "🌸"},
    "ENFJ": {"별명": "정의로운 사회운동가", "포켓몬": "루카리오", "번호": 448, "이모지": "🌊"},
    "ENFP": {"별명": "재기발랄한 활동가", "포켓몬": "피카츄", "번호": 25, "이모지": "⚡"},
    "ISTJ": {"별명": "청렴결백한 논리주의자", "포켓몬": "괴력몬", "번호": 68, "이모지": "💪"},
    "ISFJ": {"별명": "용감한 수호자", "포켓몬": "라프라스", "번호": 131, "이모지": "🌊"},
    "ESTJ": {"별명": "엄격한 관리자", "포켓몬": "한카리아스", "번호": 445, "이모지": "🦈"},
    "ESFJ": {"별명": "사교적인 외교관", "포켓몬": "해피너스", "번호": 242, "이모지": "🥚"},
    "ISTP": {"별명": "만능 재주꾼", "포켓몬": "스라크", "번호": 123, "이모지": "🗡️"},
    "ISFP": {"별명": "호기심 많은 예술가", "포켓몬": "포챠마", "번호": 393, "이모지": "🐧"},
    "ESTP": {"별명": "모험을 즐기는 사업가", "포켓몬": "마기라스", "번호": 248, "이모지": "🏔️"},
    "ESFP": {"별명": "자유로운 영혼의 연예인", "포켓몬": "푸린", "번호": 39, "이모지": "🎤"},
}

# ---------------- MBTI별 전용 무기 3종 (이름, 이모지, 위력, 한 줄 설명) ----------------
MBTI_WEAPONS = {
    "INTJ": [("전략 지도", "🗺️", 22, "모든 수를 미리 계산한다"), ("냉기 레이저", "🧊", 26, "감정 없이 정확하게 명중"), ("심리 포박구", "🔗", 20, "상대의 다음 수를 봉쇄")],
    "INTP": [("지식의 서", "📖", 21, "이론으로 허점을 찌른다"), ("호기심 렌즈", "🔍", 19, "약점을 정밀 분석"), ("실험 폭탄", "🧪", 27, "예측불가 반응 유발")],
    "ENTJ": [("지휘봉", "🎖️", 24, "팀 전체를 지휘하는 일격"), ("화염 검", "🔥", 28, "거침없이 밀어붙인다"), ("강철 방패", "🛡️", 18, "허점을 만들지 않는다")],
    "ENTP": [("언변의 채찍", "🗣️", 20, "말로 먼저 흔들어놓는다"), ("혼돈의 구슬", "🌀", 26, "예측 불가능한 궤적"), ("순간이동 부츠", "👢", 22, "빈틈을 파고든다")],
    "INFJ": [("직관의 지팡이", "🔮", 23, "상대의 수를 꿰뚫어본다"), ("치유의 빛", "✨", 17, "동료를 지키며 싸운다"), ("수호의 오라", "🕊️", 21, "조용하지만 확실한 한 방")],
    "INFP": [("감성의 붓", "🖌️", 20, "마음이 담긴 일격"), ("몽환의 실", "🧵", 19, "상대를 혼란에 빠뜨림"), ("공감의 물결", "🌊", 23, "깊은 울림으로 흔든다")],
    "ENFJ": [("격려의 깃발", "🚩", 22, "모두를 하나로 모은다"), ("결속의 사슬", "⛓️", 20, "함께라면 무너지지 않는다"), ("영감의 빛줄기", "🌟", 25, "순간의 확신이 만든 일격")],
    "ENFP": [("열정의 폭죽", "🎆", 25, "터지는 에너지 그 자체"), ("즉흥의 부메랑", "🪃", 21, "예상 못한 각도로 명중"), ("반짝임 가루", "✨", 18, "분위기를 단숨에 바꾼다")],
    "ISTJ": [("강철 망치", "🔨", 27, "원칙대로, 확실하게"), ("규율의 사슬", "⛓️", 19, "흐트러짐 없는 일격"), ("방패진", "🛡️", 20, "빈틈을 허용하지 않는다")],
    "ISFJ": [("수호의 방패", "🛡️", 18, "누군가를 지키기 위한 힘"), ("치유의 물약", "🧪", 16, "회복하며 버텨낸다"), ("보호의 결계", "🔵", 22, "조용히, 그러나 견고하게")],
    "ESTJ": [("지휘의 검", "🗡️", 26, "명령과 동시에 실행된다"), ("질서의 사슬", "⛓️", 21, "체계적으로 몰아붙인다"), ("통솔의 깃발", "🚩", 23, "흔들림 없는 진격")],
    "ESFJ": [("화합의 리본", "🎀", 19, "모두의 마음을 하나로"), ("축복의 종", "🔔", 20, "울림이 퍼져나간다"), ("배려의 방패", "🛡️", 21, "따뜻하지만 단단하게")],
    "ISTP": [("만능 렌치", "🔧", 22, "필요한 순간 정확히 사용"), ("기습 단검", "🗡️", 25, "군더더기 없는 일격"), ("정밀 사격", "🎯", 24, "감이 아니라 계산으로")],
    "ISFP": [("감각의 붓", "🎨", 20, "예술적인 한 수"), ("은신 망토", "🧥", 18, "존재감 없이 접근"), ("자유의 활", "🏹", 23, "얽매이지 않는 궤도")],
    "ESTP": [("스릴 부스터", "🏍️", 26, "속도로 승부를 본다"), ("근접 격투 글러브", "🥊", 25, "몸으로 부딪히는 힘"), ("승부수 주사위", "🎲", 21, "판을 뒤집는 배짱")],
    "ESFP": [("무대의 스포트라이트", "🎤", 22, "시선을 압도한다"), ("매혹의 리본", "🎀", 20, "분위기로 제압"), ("열광 유도기", "📣", 24, "관중을 내 편으로")],
}

# ---------------- 랜덤 상대 포켓몬 풀 (야생 포켓몬 느낌으로 다양하게) ----------------
WILD_POOL = [
    ("고라파덕", 54), ("잠만보", 143), ("두트리오", 46), ("팬텀", 94), ("망나뇽", 149),
    ("갸라도스", 130), ("나시", 103), ("딱구리", 76), ("피죤투", 18), ("독침붕", 15),
    ("치렁이", 24), ("또가스", 110), ("헤라크로스", 214), ("깜까미", 198), ("리자드", 5),
    ("이상해꽃", 3), ("거북왕", 9), ("케이시", 63), ("잉어킹", 129), ("코일", 81),
    ("모래두지", 27), ("니드킹", 34), ("갈가리", 461), ("한카리아스", 445),
]

# ---------------- 헤더 ----------------
st.title("⚔️ MBTI 포켓몬 배틀")
st.markdown("#### 내 MBTI 포켓몬이 전용 무기 3개를 들고, 랜덤 야생 포켓몬과 맞붙어요!")
st.divider()

mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("🧭 당신의 MBTI를 선택하세요", ["선택해주세요"] + mbti_list, key="battle_mbti")

if selected_mbti != "선택해주세요":
    player = MBTI_POKEMON[selected_mbti]
    weapons = MBTI_WEAPONS[selected_mbti]

    st.divider()

    # ---- 내 포켓몬 & 무기 소개 ----
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        st.image(poke_img(player["번호"]), use_container_width=True)
    with p_col2:
        st.markdown(f"## {player['이모지']} {player['포켓몬']}")
        st.caption(f"{selected_mbti} · {player['별명']}")

    st.markdown("### 🗡️ 장착한 전용 무기 3종")
    w1, w2, w3 = st.columns(3)
    for col, (name, emoji, power, desc) in zip([w1, w2, w3], weapons):
        with col:
            st.markdown(
                f"""
                <div style="text-align:center; background:#fff3e0; border:2px solid #ffb74d;
                            border-radius:14px; padding:14px;">
                    <p style="font-size:34px; margin:0;">{emoji}</p>
                    <p style="font-weight:bold; margin:4px 0;">{name}</p>
                    <p style="font-size:12px; color:#777; margin:0;">{desc}</p>
                    <p style="font-size:12px; color:#e65100; margin:4px 0 0 0;">위력 {power}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    # ---- 전투 시작 버튼 ----
    start = st.button("⚔️ 전투 시작!", use_container_width=True, type="primary")

    if start:
        # 상대 포켓몬 랜덤 선정 (내 포켓몬과 이름 겹치지 않게)
        candidates = [w for w in WILD_POOL if w[0] != player["포켓몬"]]
        opp_name, opp_num = random.choice(candidates)

        # ---- 배틀 시뮬레이션 (파이썬에서 미리 계산) ----
        player_hp, opp_hp = 100, 100
        log_lines = []
        hp_track = []  # (turn, actor, dmg, crit, player_hp, opp_hp)

        turn = 0
        max_turns = 12
        while player_hp > 0 and opp_hp > 0 and turn < max_turns:
            turn += 1
            # 플레이어 턴: 무기를 순환하며 사용
            w_name, w_emoji, w_power, _ = weapons[(turn - 1) % 3]
            crit = random.random() < 0.2
            dmg = w_power + random.randint(5, 15)
            if crit:
                dmg = int(dmg * 1.5)
            opp_hp = max(0, opp_hp - dmg)
            log_lines.append(
                f"{turn}턴 · {player['포켓몬']}의 {w_emoji} {w_name}! "
                f"{'💥 급소 히트! ' if crit else ''}{dmg}의 데미지!"
            )
            hp_track.append((turn, "opponent", dmg, crit, player_hp, opp_hp))

            if opp_hp <= 0:
                break

            # 상대 턴: 야생의 반격
            o_crit = random.random() < 0.15
            o_dmg = random.randint(10, 22)
            if o_crit:
                o_dmg = int(o_dmg * 1.5)
            player_hp = max(0, player_hp - o_dmg)
            log_lines.append(
                f"{turn}턴 · 야생의 {opp_name}이(가) 반격! "
                f"{'💥 급소 히트! ' if o_crit else ''}{o_dmg}의 데미지!"
            )
            hp_track.append((turn, "player", o_dmg, o_crit, player_hp, opp_hp))

        if player_hp <= 0 and opp_hp <= 0:
            winner = "무승부"
        elif opp_hp <= 0:
            winner = "player"
        else:
            winner = "opponent"

        st.session_state["battle_data"] = {
            "player_name": player["포켓몬"],
            "player_emoji": player["이모지"],
            "player_img": poke_img(player["번호"]),
            "opp_name": opp_name,
            "opp_img": poke_img(opp_num),
            "log_lines": log_lines,
            "hp_track": hp_track,
            "winner": winner,
        }

    # ---- 배틀 애니메이션 렌더링 ----
    if "battle_data" in st.session_state:
        bd = st.session_state["battle_data"]

        log_js_array = "[" + ",".join(
            "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\"" for line in bd["log_lines"]
        ) + "]"
        hp_js_array = "[" + ",".join(
            "{turn:%d,actor:\"%s\",dmg:%d,crit:%s,playerHp:%d,oppHp:%d}" % (
                t, actor, dmg, "true" if crit else "false", php, ohp
            ) for (t, actor, dmg, crit, php, ohp) in bd["hp_track"]
        ) + "]"

        if bd["winner"] == "player":
            result_text = f"🏆 {bd['player_name']} 승리!"
            result_color = "#2e7d32"
        elif bd["winner"] == "opponent":
            result_text = f"💀 야생의 {bd['opp_name']}에게 패배..."
            result_color = "#c62828"
        else:
            result_text = "🤝 무승부!"
            result_color = "#616161"

        html_code = """
        <div style="font-family: -apple-system, sans-serif;">
        <style>
            .arena { display:flex; justify-content:space-between; align-items:flex-start; padding:10px; }
            .fighter { width:44%; text-align:center; }
            .fighter img { width:100%; max-width:150px; transition: transform 0.15s; }
            .hpbar-bg { background:#e0e0e0; border-radius:10px; height:16px; width:100%; overflow:hidden; margin-top:6px; border:1px solid #bbb;}
            .hpbar-fill { height:100%; border-radius:10px; transition: width 0.5s ease-out; }
            .hp-player { background:linear-gradient(90deg,#66bb6a,#43a047); }
            .hp-opp { background:linear-gradient(90deg,#ef5350,#e53935); }
            .name-tag { font-weight:bold; margin-top:6px; }
            .vs-text { font-size:28px; font-weight:bold; color:#555; padding-top:50px; }
            .shake { animation: shake 0.3s; }
            @keyframes shake { 0%{transform:translateX(0)} 25%{transform:translateX(-8px)} 50%{transform:translateX(8px)} 75%{transform:translateX(-6px)} 100%{transform:translateX(0)} }
            .flash { animation: flash 0.3s; }
            @keyframes flash { 0%{filter:brightness(1)} 50%{filter:brightness(2) saturate(2)} 100%{filter:brightness(1)} }
            .dmg-float { position:absolute; font-size:22px; font-weight:bold; color:#ff1744; animation: floatUp 0.9s ease-out forwards; pointer-events:none; }
            .dmg-float.crit { color:#ff6d00; font-size:28px; }
            @keyframes floatUp { 0%{opacity:1; transform:translateY(0);} 100%{opacity:0; transform:translateY(-40px);} }
            .fighter-wrap { position:relative; display:inline-block; width:100%; }
            .log-box { background:#1e1e1e; color:#7CFC00; font-family:monospace; font-size:13px; padding:12px;
                       border-radius:10px; height:150px; overflow-y:auto; margin-top:16px; line-height:1.6; }
            .result-banner { text-align:center; font-size:26px; font-weight:bold; margin-top:16px; padding:16px;
                              border-radius:14px; opacity:0; transition: opacity 0.6s; }
            .result-show { opacity:1; }
            .confetti { position:fixed; top:-20px; font-size:22px; animation: fall linear forwards; z-index:9999; }
            @keyframes fall { to { transform: translateY(500px) rotate(360deg); opacity:0; } }
        </style>

        <div class="arena">
            <div class="fighter">
                <div class="fighter-wrap" id="playerWrap">
                    <img src="__PLAYER_IMG__" id="playerImg">
                </div>
                <div class="name-tag">__PLAYER_EMOJI__ __PLAYER_NAME__ (나)</div>
                <div class="hpbar-bg"><div class="hpbar-fill hp-player" id="playerHpBar" style="width:100%"></div></div>
            </div>
            <div class="vs-text">VS</div>
            <div class="fighter">
                <div class="fighter-wrap" id="oppWrap">
                    <img src="__OPP_IMG__" id="oppImg">
                </div>
                <div class="name-tag">🐾 야생의 __OPP_NAME__</div>
                <div class="hpbar-bg"><div class="hpbar-fill hp-opp" id="oppHpBar" style="width:100%"></div></div>
            </div>
        </div>

        <div class="log-box" id="logBox">전투 준비 중...</div>
        <div class="result-banner" id="resultBanner" style="color:__RESULT_COLOR__;">__RESULT_TEXT__</div>
        </div>

        <script>
        const logLines = __LOG_ARRAY__;
        const hpTrack = __HP_ARRAY__;
        const logBox = document.getElementById('logBox');
        const playerBar = document.getElementById('playerHpBar');
        const oppBar = document.getElementById('oppHpBar');
        const playerWrap = document.getElementById('playerWrap');
        const oppWrap = document.getElementById('oppWrap');
        const resultBanner = document.getElementById('resultBanner');

        logBox.innerHTML = "";

        function spawnDamage(target, dmg, crit) {
            const el = document.createElement('div');
            el.className = 'dmg-float' + (crit ? ' crit' : '');
            el.style.left = (40 + Math.random()*20) + '%';
            el.style.top = '20%';
            el.innerText = (crit ? '💥-' : '-') + dmg;
            target.appendChild(el);
            setTimeout(() => el.remove(), 900);
        }

        function playStep(i) {
            if (i >= hpTrack.length) {
                setTimeout(() => {
                    resultBanner.classList.add('result-show');
                    for (let c = 0; c < 16; c++) {
                        const conf = document.createElement('div');
                        conf.className = 'confetti';
                        conf.style.left = Math.random()*100 + '%';
                        conf.style.animationDuration = (1.5 + Math.random()*1.5) + 's';
                        conf.innerText = ['🎉','⭐','🎊','✨'][Math.floor(Math.random()*4)];
                        document.body.appendChild(conf);
                        setTimeout(() => conf.remove(), 3500);
                    }
                }, 300);
                return;
            }
            const step = hpTrack[i];
            const targetWrap = step.actor === 'player' ? playerWrap : oppWrap;
            targetWrap.classList.add('shake', 'flash');
            spawnDamage(targetWrap, step.dmg, step.crit);
            setTimeout(() => targetWrap.classList.remove('shake', 'flash'), 300);

            playerBar.style.width = step.playerHp + '%';
            oppBar.style.width = step.oppHp + '%';

            const p = document.createElement('div');
            p.innerText = '▶ ' + logLines[i];
            logBox.appendChild(p);
            logBox.scrollTop = logBox.scrollHeight;

            setTimeout(() => playStep(i + 1), 1100);
        }

        setTimeout(() => playStep(0), 600);
        </script>
        """

        html_code = html_code.replace("__PLAYER_IMG__", bd["player_img"])
        html_code = html_code.replace("__PLAYER_EMOJI__", bd["player_emoji"])
        html_code = html_code.replace("__PLAYER_NAME__", bd["player_name"])
        html_code = html_code.replace("__OPP_IMG__", bd["opp_img"])
        html_code = html_code.replace("__OPP_NAME__", bd["opp_name"])
        html_code = html_code.replace("__LOG_ARRAY__", log_js_array)
        html_code = html_code.replace("__HP_ARRAY__", hp_js_array)
        html_code = html_code.replace("__RESULT_TEXT__", result_text)
        html_code = html_code.replace("__RESULT_COLOR__", result_color)

        components.html(html_code, height=560, scrolling=False)

        st.button("🔄 다시 다른 상대와 대결하기", key="rebattle_btn")

else:
    st.markdown(
        """
        <div style="text-align: center; padding: 40px; color: #888;">
            <p style="font-size: 60px; margin: 0;">⚔️</p>
            <p style="font-size: 18px;">위에서 MBTI를 선택하면<br>전용 무기를 든 내 포켓몬이 나타나요!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()
st.caption("Made with ⚡ Streamlit | 이미지: PokeAPI 공식 아트워크 | 재미로 봐주세요 😊")
