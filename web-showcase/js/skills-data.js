const SKILLS_DATA = [
  // --- 1. MiniMax H3 모션그래픽 & 타이포그래피 (18대 카테고리) ---
  {
    id: "h3-18",
    category: "motion",
    tag: "MiniMax H3",
    tagColor: "badge-purple",
    title: "AAA급 시네마틱 캐릭터 스킬 16초 무한 루프",
    subtitle: "2.39:1 아나모픽 와이드스크린 · 8-샷 연계 · 1초 절대 정적",
    desc: "원신/스타레일 스타일의 게임 스킬 연출. 2초 단위 8-샷 칼박자 연계, 지면 파괴 누적, 1초 무음 후 궁극기 대폭발, 시작 프레임 100% 일치 무한 루프.",
    howItWorks: "AI가 스킬 씬을 뭉개지 않도록 2초 단위로 카메라 화각(40mm ➔ 50mm ➔ 35mm ➔ 28mm)을 바꾸고, 궁극기 폭발 직전 1초간 볼륨을 0dB(무음)으로 떨어뜨려 시청자 몰입도를 극대화합니다.",
    formulaSnippet: `[Camera & Rhythm]: 2s per shot, 8 consecutive cuts, seamless loop to start frame.
[Color LUT]: Rec.709 Teal-Orange, Kodak 5219 grain 12%, Halation 6%.
[Audio Arc]: Action SFX only, 1.0s absolute silence before ultimate burst.`,
    aspectRatio: "2.39:1",
    duration: "16s",
    model: "MiniMax H3",
    bgGradient: "from-indigo-900/60 via-purple-900/40 to-slate-950",
    visualIcon: "⚡",
    keys: ["8-Shot Loop", "1s Silence", "Rec.709 Teal-Orange", "Ground Fracture"],
    timeline: [
      { time: "0-2s", label: "기세 축적", detail: "40mm 레일 트랙 돌진, 부채 끝 백색 발광점 명멸 (0.5s 호흡), 바닥 번개 상승" },
      { time: "2-4s", label: "부채 전개", detail: "50mm 로우앵글 스테디캠 상승, 부채 1/3 전개, 거미줄 번개 방사" },
      { time: "4-6s", label: "횡베기 광인", detail: "35mm 고속 패닝, 3m 초승달 번개 참격, 공기 왜곡 열파, 대사: '散れ'" },
      { time: "6-8s", label: "3단 콤보 연타", detail: "1타: 분수 번개 ➔ 2타: 지면 거미줄 균열 ➔ 3타: 360도 링 충격파" },
      { time: "8-10s", label: "공중 도약 & 풍차", detail: "28mm 광각 지미집 상승, 공중 부채 풍차 회전, 원형 에너지 디스크로 천장 강타" },
      { time: "10-12s", label: "소용돌이 수렴", detail: "40mm 360도 회전 궤도, 바닥 번개 소용돌이, 세로 동공 각성" },
      { time: "12-14s", label: "궁극기 대폭발", detail: "1초 절대 무음(0dB) ➔ 4m 원추형 번개 빔 폭발 ➔ 대사: '雷華閃'" },
      { time: "14-16s", label: "무한 루프 복귀", detail: "완전 정지 카메라, 지면 파괴 흔적 발광, 0초 시작 자세 100% 동일 복귀" }
    ],
    prompt: `[影片总纲] 电影级角色技能展示动画，总时长严格16秒无缝循环loop，画幅比2.39比1变形宽银幕电影规格，无背景音乐，仅角色动作音效与技能音效，8K电影级写实渲染，光线追踪全局光照，体积雾散射，皮肤次表面散射，Kodak 5219胶片颗粒12%，Halation光晕6%，镜头呼吸效应，变形宽银幕镜头椭圆散景与水平拉丝眩光，色彩空间Rec.709带电影级青橙LUT，对比度S型曲线暗部提升12%高光压缩8%，阴影偏青高光偏金，黑位纯净不浮灰。全程聚焦角色主技能「雷华扇舞」，以折扇为核心武器，动作优雅凌厉不重复，每2秒一次平滑镜头转场，禁止任何旋转场景，禁止远景大全景，摄影机最远不得超过角色全身full body，loop终点无缝衔接起点形成永恒循环。`
  },
  {
    id: "h3-07",
    category: "commercial",
    tag: "MiniMax H3",
    tagColor: "badge-pink",
    title: "하이패션 3배속 3D 공간 타이포 에너지 드링크 TVC",
    subtitle: "PINK VOLT · 9개 씬 공간 건축물화 · 스펙 정보 블록 합체",
    desc: "글자를 자막이 아닌 3D 공간의 벽, 터널, 런웨이, 회전 링으로 실체화. 카페인 80mg, 제로슈거, 비타민B, 200엔 가격을 9개 씬으로 쏟아붓는 초고속 커머셜.",
    howItWorks: "자막 오버레이를 쓰면 글자가 깨지므로, 텍스트를 '물리적인 3D 콘크리트 벽/회전 링/빛나는 네온 터널'로 선언하여 AI가 공간 배경의 일부로 렌더링하게 만듭니다.",
    formulaSnippet: `[Typography Architecture]: Words exist as physical 3D structures (tunnels, spinning rings, runway floors), NOT 2D subtitles.
[Speed]: 3x fast-paced hyper kinetic typography.
[Info Hierarchy]: 9 rapid scenes displaying specs (Caffeine, Zero Sugar, B-Vitamins).`,
    aspectRatio: "16:9",
    duration: "15s",
    model: "MiniMax H3",
    bgGradient: "from-pink-950/60 via-purple-950/40 to-slate-950",
    visualIcon: "⚡",
    keys: ["3D Spatial Architecture", "Glossy Neon Reflection", "9-Scene Typography Build", "Spec Merge"],
    timeline: [
      { time: "Scene 1", label: "광고 터널", detail: "벽/천장/바닥의 'NEED ENERGY?'가 카메라 역방향으로 쾌속 질주" },
      { time: "Scene 2", label: "네온 1점 투시", detail: "인물보다 거대한 '¥200'이 수십 개 1점 투시로 연속 돌진" },
      { time: "Scene 3", label: "제품 공중 출현", detail: "손바닥 위 캔 출현 + 360도 회전 + 좌우 충돌 'PINK VOLT' + 번개 방사" },
      { time: "Scene 4", label: "3중 회전 링", detail: "시계/반시계/나선 3겹으로 회전하는 'CAFFEINE 80mg' 링" },
      { time: "Scene 5", label: "패널 폭발 전개", detail: "팔을 휘두르면 중앙에서 좌우로 수십 장의 'ZERO SUGAR' 패널 전개" },
      { time: "Scene 6", label: "런웨이 & 90도 롤", detail: "바닥/벽/천장 타이포 런웨이 'B VITAMINS' 질주 + 카메라 90도 회전" },
      { time: "Scene 7", label: "3대 정보 블록 합체", detail: "좌/우/하단에서 3대 스펙(CAFFEINE / ZERO / B VITAMINS)이 날아와 입체 정렬" },
      { time: "Scene 8-9", label: "레일 질주 & 히어로 샷", detail: "'ALL FOR ¥200' ➔ 3단 락업 ➔ 캔 로고로 초광속 줌인 엔딩" }
    ],
    prompt: `MiniMax H3 Prompt
PINK VOLT・キネティックタイポグラフィ エナジードリンクCM 動画プロンプト

スタイル: 実写映画＋ハイファッション広告＋キネティックタイポグラフィ。3倍速のハイスピードCM。蛍光ピンク、ブラック、ホワイトを中心とした強烈な限定配色。画像1の人物と「PINK VOLT」のピンク色の缶、巨大な英語タイポグラフィを同じ3D空間に配置する。文字を単なる字幕ではなく、壁、床、看板、トンネル、リング、光線、巨大な立体オブジェクトとして使用。

画像1の人物は、参照画像の顔、髪型、衣装、体格、アクセサリー、メイク、配色を全シーンで維持する。PINK VOLTの缶もロゴ、形状、ピンク의 配色、稲妻モチーフを全シーンで統一する。`
  },
  {
    id: "h3-16",
    category: "commercial",
    tag: "MiniMax H3",
    tagColor: "badge-cyan",
    title: "일본 플랫 일러스트 2D 음료 모션 커머셜",
    subtitle: "산토리/포카리스웨트 스타일 · 2D 플랫 벡터 · 128 BPM 마림바 BGM",
    desc: "여름의 열기(옐로우)에서 시원한 청량감(아쿠아)으로 전환되는 15초 6-샷 2D 애니 음료 TVC. 오버슈트 컷아웃 애니메이션과 일본어 의성어 스탬프.",
    howItWorks: "복잡한 3D 렌더링 대신 플랫 2D 벡터와 두꺼운 네이비 외곽선, 컷아웃 오버슈트 모션을 명시하여 산토리 광고 특유의 발랄한 감성을 100% 재현합니다.",
    formulaSnippet: `[Visual Style]: Flat 2D vector illustration, thick navy outlines, springy cutout overshoot animation.
[Color Switch]: Saturated yellow (summer heat) ➔ Aqua water sweep (refreshment).
[Sound & Typography]: Marimba 128 BPM + Kinetic Japanese stamps ('キンッ。', 'ごくっ').`,
    aspectRatio: "16:9",
    duration: "15s",
    model: "MiniMax H3",
    bgGradient: "from-cyan-950/60 via-blue-950/40 to-slate-950",
    visualIcon: "🥤",
    keys: ["Flat 2D Vector", "Overshoot Easing", "Japanese Sound Stamp", "128 BPM Marimba"],
    timeline: [
      { time: "0-2.4s", label: "여름의 열기 & 보틀 솟구침", detail: "채도 높은 옐로우 + 태양 펄스 ➔ 보틀이 솟구치며 오버슈트 착지 ➔ 타이틀: 'この夏、あつい。'" },
      { time: "2.4-5.0s", label: "아쿠아 물결 세척", detail: "아쿠아 물결이 옐로우를 쓸어내며 회전 ➔ 'AOI WATER' 라벨 조립 + 결로 물방울 6개 + 얼음 텀블링" },
      { time: "5.0-7.6s", label: "물 따르기 & 얼음 바운스", detail: "유리잔에 물줄기 낙하 ➔ 얼음 3조각 바운스 ➔ 의성어 스탬프 'キンッ。'" },
      { time: "7.6-10.2s", label: "3모금 음용", detail: "단발머리 여배우 벡터 캐릭터가 3모금 마심 (몸에 청록색 물 차오름) ➔ 의성어 'ごくっ'" },
      { time: "10.2-12.6s", label: "점프 & 승리 카피", detail: "보틀 치켜들고 점프 ➔ 기하학 파티클 링 버스트 ➔ '夏に、' '負けない。'" },
      { time: "12.6-15.0s", label: "화이트 엔드 카드", detail: "보틀 중앙 안착 + 로고타입 + 성우 나레이션: '<d>[Japanese] 夏に、負けない。</d>'" }
    ],
    prompt: `integrated_multimodal_description: Create a complete 15-second Japanese flat-illustration motion-graphics commercial for a bottled mineral water in a clean 16:9 composition. The bottle is the hero of every shot: it appears within the first second, stays large and centred, and its pale blue label reading the exact Latin characters "AOI WATER" is sharp and readable in every frame it occupies. Use friendly 2D vector illustration, thick navy outlines, flat solid colour fills, and springy cutout animation with snappy overshoot easing. Compact palette of warm white, deep navy, bright aqua, deep blue and saturated yellow.

[Shot 1] Begin on a saturated yellow field... "この夏、あつい。"
[Shot 2] Aqua water sweeps across... "AOI WATER" letter by letter...
[Shot 3] Pour into glass... kinetic word "キンッ。" stamps in...
[Shot 4] Actress drinks in 3 gulps... kinetic word "ごくっ" pops in...
[Shot 5] Jump with bottle... "夏に、" then "負けない。"
[Shot 6] Clean white end card... Voiceover: <d>[Japanese] 夏に、負けない。</d>`
  },
  {
    id: "h3-13",
    category: "anime",
    tag: "MiniMax H3",
    tagColor: "badge-purple",
    title: "5인 5초 2D 애니 캐릭터 카드 사선 와이프 몽타주",
    subtitle: "안티 모핑(Anti-Morphing) 100% · 1초당 1인 5비트 · 듀얼 레이어 초상화",
    desc: "서로 다른 5명의 캐릭터가 섞이지 않고 1초마다 사선 그래픽 와이프로 전환되는 애니메이션 오프닝/아이캐치 몽타주.",
    howItWorks: "여러 인물이 한 프레임에 섞여 얼굴이 뭉개지는 현상(Morphing)을 사선 그래픽 와이프와 1초 1인 단독 샷 제한으로 완벽 차단합니다.",
    formulaSnippet: `[Anti-Morphing Rule]: Strictly one character at a time. Diagonal graphic wipe between shots.
[Pacing]: 1.0 second per character, sharp pop cuts.
[Composition]: Medium close-up (face 35-50% height) + Pale monochrome portrait layer in background.`,
    aspectRatio: "16:9",
    duration: "5s",
    model: "MiniMax H3",
    bgGradient: "from-purple-950/60 via-pink-950/40 to-slate-950",
    visualIcon: "🎴",
    keys: ["Anti-Morphing Wipe", "5-Beat Pop Cuts", "Monochrome Portrait Layer", "Medium Close-up Lock"],
    timeline: [
      { time: "0.0-1.0s", label: "Image 1 (다크 바이올렛)", detail: "딥 바이올렛 사선 띠 ➔ 흑발 중2병 소녀 머리 넘기며 미소 + 배경 연보라 초상화" },
      { time: "1.0-2.0s", label: "Image 2 (레드 오렌지)", detail: "레드 오렌지 와이프 ➔ 체육계 소녀 주먹 불끈 미소 + 배경 연오렌지 초상화" },
      { time: "2.0-3.0s", label: "Image 3 (브라이트 골드)", detail: "스파클링 골드 띠 ➔ 트윈테일 여고생 턱 치켜들며 윙크 + 배경 연골드 초상화" },
      { time: "3.0-4.0s", label: "Image 4 (모스 그린)", detail: "모스 그린 슬라이드 ➔ 후드티 남학생 냉소적 반미소 + 배경 연그린 초상화" },
      { time: "4.0-5.0s", label: "Image 5 (더스티 로즈)", detail: "핑크 사선 띠 ➔ 핑크머리 남학생 뒷머리 긁적이며 소심 시선 + 배경 연로즈 초상화" }
    ],
    prompt: `Create a fast-paced 5-second 2D Japanese anime character introduction montage using the five supplied reference images. IMPORTANT: @Image1, @Image2, @Image3, @Image4, and @Image5 are five completely different characters. Preserve each character’s exact face, hairstyle, skin tone, outfit, body type, and accessories. Never merge, morph, blend, or exchange their identities. Show only one character at a time.

FORMAT: 16:9 horizontal video, static graphic-design composition, crisp polished 2D anime linework, clean cel shading. Five consecutive character shots, approximately one second per character. Use sharp rhythmic pop cuts and diagonal graphic wipes. Every character must receive a clearly readable medium close-up or face close-up (35–50% frame height).`
  },
  {
    id: "h3-17",
    category: "motion",
    tag: "MiniMax H3",
    tagColor: "badge-orange",
    title: "핸드메이드 2D 찢어진 종이 콜라주 일본 광고",
    subtitle: "인물 0% 순수 그래픽 · 리소그래프 질감 · 텍스트 화이트리스트",
    desc: "인물 없이 오직 찢어진 종이, 복사기 그레인, 스톱모션 지터만으로 시선을 사로잡는 9:16 세로형 출판/비즈니스 바이럴 광고.",
    howItWorks: "인물을 0% 배제하고 텍스트 화이트리스트와 종이 찢김 마스크를 결합하여 오탈자 없이 완벽한 타이포 모션 그래픽을 유도합니다.",
    formulaSnippet: `[Negative Elements]: Strictly NO people, faces, bodies, photos.
[Texture & Motion]: Torn-paper animation, risograph texture, photocopy grain, stop-motion jitter.
[Text Lock]: Visible-text whitelist ("集客に疲れていませんか？", "そうだ！", "本を書こう！").`,
    aspectRatio: "9:16",
    duration: "15s",
    model: "MiniMax H3",
    bgGradient: "from-amber-950/60 via-orange-950/40 to-slate-950",
    visualIcon: "📄",
    keys: ["Torn-Paper Mask", "Visible-Text Whitelist", "Risograph Texture", "104 BPM Upright Bass"],
    timeline: [
      { time: "Shot 1 (0-3.5s)", label: "문제 제기", detail: "찢어진 마스크 사이로 '集客に疲れていませんか？' + 보이스오버" },
      { time: "Shot 2 (3.5-8.0s)", label: "3중 텍스트 스택", detail: "'SNS集客' ➔ '広告' ➔ '無料セミナー' 3단 스택 뒤집힘 와이프" },
      { time: "Shot 3 (8.0-10.5s)", label: "해결의 섬광", detail: "순간 무음(Hold) ➔ 종이 찢어지며 'そうだ！' 폭발" },
      { time: "Shot 4 (10.5-15.0s)", label: "책 언폴드 & CTA", detail: "책 모양으로 펼쳐지며 '本を書こう！' ➔ 1.5초 완벽 정지" }
    ],
    prompt: `[Shot 1] Premium 2D handmade motion collage designed as a polished 15-second vertical 9:16 Japanese advertising commercial. The visual language combines bold kinetic typography, torn-paper animation, risograph texture, photocopy grain, rough edges, cutout shapes. Absolutely no people, characters, faces, hands, bodies.
Off-screen Voiceover: <d>[Japanese] 集客に疲れていませんか？</d>

[Shot 2] At 00:03.500: Three strips "SNS集客", "広告", "無料セミナー" stack and flip face down into a full-screen torn-paper wipe.
[Shot 3] At 00:08.000: Solid cobalt-blue layer, audio drops out for brief hold, tear opens: "そうだ！" <d>[Japanese] そうだ！</d>
[Shot 4] At 00:10.500: Paper stack unfolds into book pages: "本を書こう！" <d>[Japanese] 本を書こう！</d>`
  },

  // --- 2. 극실사 & 시네마틱 드라마 & 액션 ---
  {
    id: "seedance-combat",
    category: "action",
    tag: "Seedance 2.5",
    tagColor: "badge-blue",
    title: "시댄스 2.5 극실사 맨몸 격투 & 학원 액션물",
    subtitle: "한국 학원물/드라마 · 노-초능력 순수 신체역학 · 폰카 목격자 룩",
    desc: "약한영웅/아저씨 감성의 초현실 맨몸 액션. 체육관 5인 대치, 체중 이동과 관절 레버리지, 5단계 감정 아크, 기물 충돌 및 현장 생음 100% 폴리.",
    howItWorks: "초능력/장풍을 0% 배제하고 '체중 이동, 관절 레버리지, 관성 회전' 등 물리 역학 지시어와 5단계 감정 변화('공포 ➔ 본능 ➔ 집중 ➔ 경악')를 주입해 배우급 실사 연기를 이끌어냅니다.",
    formulaSnippet: `[Physical Mechanics]: Pure kinetic leverage & momentum redirection. Strictly NO magic, NO superpowers.
[Actor Acting Arc]: Fear ("그만해...") ➔ Confusion ➔ Instinct ➔ Concentration ➔ Disbelief ("나... 방금 뭐 한 거야?").
[Camera]: Witness smartphone footage, imperfect framing, focus hunting, natural motion blur.`,
    aspectRatio: "16:9",
    duration: "20s",
    model: "Seedance 2.5",
    bgGradient: "from-amber-950/50 via-slate-900/60 to-slate-950",
    visualIcon: "🥋",
    keys: ["Pure Kinetic Mechanics", "5-Stage Emotional Arc", "Witness Phone-Cam", "Raw Native Foley"],
    timeline: [
      { time: "0-4s", label: "대치 & 공포", detail: "체육관 관람석으로 몰리며 손을 듦. 대사: '그만해...'. 호흡 변화" },
      { time: "4-8s", label: "본능적 회피 & 반격", detail: "주먹 회피 ➔ 손목 캐치 ➔ 체중 역이용 다리 걸기 ➔ 자신의 손을 불신하듯 응시" },
      { time: "8-13s", label: "다수 난투 & 기물 파손", detail: "4인 동시 공격 ➔ 엘보우 & 로우킥 ➔ 배드민턴 카트 전도 및 셔틀콕 비산" },
      { time: "13-17s", label: "후드 탈출 & 장타", detail: "후드 잡힘 ➔ 몸 회전 힐킥 ➔ 오리걸음 회피 후 손바닥 장타로 밀쳐냄" },
      { time: "17-20s", label: "종결 & 혼란 독백", detail: "마지막 돌진 회피 ➔ 매트 벽 충돌 ➔ 정적 속 거친 숨, 독백: '나... 방금 뭐 한 거야?'" }
    ],
    prompt: `Made with seedance 2.5 CONCEPT: Ultra-realistic live-action scene. A young woman is trapped in an empty Korean school gym by five aggressive male students. When they attack simultaneously, instinctive martial-arts reflexes suddenly awaken. She remains completely human—no powers, magic, or supernatural effects. Fast, physical, believable action.

CHARACTER: Use @ref img for identity only. Preserve face, natural skin, messy dark hair, petite athletic build. Black oversized hoodie, loose charcoal sweatpants, worn black sneakers. Expressions: fear → confusion → instinct → concentration → disbelief.

LOCATION: Empty Korean school gym near sunset: polished wooden floor, folded bleachers, basketball hoops, badminton equipment, metal cart, tall windows, warm sunlight, floating dust. Realistic imperfections.

ACTION:
0–4s: She backs toward bleachers as five students surround her. She raises her hands: “그만해…” One rushes. Her breathing changes.
4–8s: He swings. She narrowly evades, catches his wrist, redirects his momentum, and kicks his leg. He drops to one knee. She stares at her hand in disbelief.
8–13s: Four attack together. She continuously dodges, redirects, sweeps, pivots, uses a short elbow and low kick. Attackers collide and stumble naturally. A badminton basket falls and shuttlecocks scatter. Handheld camera struggles to follow.
13–17s: One grabs her hoodie; she twists free, spins into a realistic heel kick, sending him backward. She ducks the second attacker, rises behind him, and uses a short palm strike to make him stumble forward.
17–20s: Final attacker charges. She steps aside; he crashes into the padded wall. Silence. She breathes heavily, looks at her hands, and whispers: “나… 방금 뭐 한 거야?” Camera slowly moves closer. Hair falls across her eyes. CUT TO BLACK.

CAMERA: Handheld smartphone/operator footage, imperfect framing, focus hunting, natural motion blur, brief overshoot, exposure changes, no perfect tracking, minimal slow motion. Feels like a real witness recording an incident.

AUDIO: Native live sound only: breathing, shoe squeaks, fabric movement, impacts, padded-wall hits, bleacher vibration, shuttlecocks, fluorescent hum, Korean dialogue. No music.`
  },
  {
    id: "china-factory",
    category: "action",
    tag: "Seedance 2.5",
    tagColor: "badge-red",
    title: "중국 숏드라마 팩토리 4대 양산 룰 (실사 시대극)",
    subtitle: "지몽 드림이나 시댄스 2.5 · 컷간 100% 자동 연결 · 더빙 상수/변수",
    desc: "80편 시리즈를 리롤 없이 양산하는 공장형 템플릿. 얼굴 그물망 격자 훼손, 재질별 하이라이트 배율 고정, 앞뒤 컷 양방향 인계 박제.",
    howItWorks: "캐릭터 시트 얼굴에 그물망을 씌워 표정이 굳는 복붙 렌더링을 차단하고, 재질 반사광(금속x1.5/피부x0.5/천x0.3)을 수치화해 컷 전환 시 조명이 튀는 문제를 완벽 방어합니다.",
    formulaSnippet: `[Lattice Mesh]: Character sheet face obscured by mesh grid to enforce dynamic facial expressions.
[Material Multipliers]: Metal Highlight x1.5, Skin Highlight x0.5, Fabric Highlight x0.3.
[Clip Handoff]: Start frame anchored to previous shot's motion, End frame text-anchored to next episode's first dialogue.`,
    aspectRatio: "16:9",
    duration: "10s",
    model: "Seedance 2.5 / Kling",
    bgGradient: "from-emerald-950/60 via-slate-900/60 to-slate-950",
    visualIcon: "🏭",
    keys: ["Face-Obscured Mesh", "Material Highlight Multipliers", "Bi-directional Handoff", "Word-by-Word Action Sync"],
    timeline: [
      { time: "0-2s", label: "앞 씬 연결부", detail: "S04 신발 밑창이 화면을 채운 상태에서 착지하며 시작 ➔ 젖은 이끼 석계 착지 및 미끄러짐 ➔ 외침: '와!'" },
      { time: "2-4s", label: "환경 노출 & 인물 등장", detail: "24mm 샷, 청죽 지팡이 따라 카메라 상승 ➔ 운무 걷히며 땀에 젖은 소식(소동파) 등장" },
      { time: "4-7.5s", label: "단어 싱크 대사 1", detail: "'괴상한'에서 웃음주름 ➔ '그 신발'에서 손가락 하강 ➔ '변경'에서 눈 들어 반응 관찰" },
      { time: "7.5-10s", label: "단어 싱크 대사 2", detail: "첫 '당신'에서 정지 ➔ 두번째 '당신'에서 눈썹 올림 ➔ '소동파'에서 눈 응시 ➔ 소식 리액션 컷" }
    ],
    prompt: `【即梦 Dreamina Seedance 2.5 ｜ 《题西林壁：我知道……先等等》S05 ｜ 10秒 ｜ 16:9 ｜ 真人实拍快节奏版】

【输入模式与人物素材绑定】
Omni Reference / 三组真人参考生成。
@女孩=image 1: 作为女孩唯一真人身份参考，锁定同一张脸、双丸子头、白色连帽卫衣、浅灰运动裤和白色运动鞋。
@苏轼=image 2: 作为苏轼唯一真人身份参考，锁定同一张脸、发髻、胡须、灰青色麻布长袍、草编芒鞋和青竹杖。

【10秒连续镜头】
0—2秒：从S04鞋底接近填满画面的状态开始，35mm贴地低机位，一只白色运动鞋沿同一运动方向重重落在湿漉漉的青苔石阶上，鞋底挤出细小水珠并轻微打滑；女孩脱口惊呼：“哇！” 旁边一双黑色草编芒鞋稳稳落地，青竹杖同时点中石缝。
4—7.5秒：切50mm苏轼中近景。说“好怪”时笑纹展开，说“这双鞋”时手指落向鞋面，说“汴京”时抬眼观察女孩反应。完整说：“好怪的小先生！这双鞋，怕是走遍汴京也买不到吧？”
7.5—10秒：切50mm女孩正面中近景。说第一个“你”时短暂停顿，第二个“你”时确认性抬眉，说“苏东坡”时目光牢牢锁定他的眼睛。问：“你……你是苏东坡？”

【尾帧与S06衔接】
50mm苏轼反应近景，青竹杖立在身侧，眼角带笑，目光看着女孩，嘴唇刚要张开。S06从苏轼回答：“东坡在此。不过，我现在还没心情写诗。”开始。`
  },
  {
    id: "phone-cam-realism",
    category: "realistic",
    tag: "General Realism",
    tagColor: "badge-green",
    title: "Old iPhone 1x 렌즈 기반 폰카 극실사 8대 수칙",
    subtitle: "AI 가짜 CG 느낌(Plastic Slop) 100% 제거 · 초현실 생활감",
    desc: "스마트폰으로 직접 찍은 듯한 극강의 현장감. 저화질 압축 노이즈, 핸드헬드 미세 흔들림, 형광등 플리커, 유기적 조명 시프팅.",
    howItWorks: "AI 특유의 미끈거리는 3D CG 룩을 지우기 위해 'Old iPhone 1x 렌즈, 고압축 센서 노이즈, 비대칭 크롭, 무보정 일상광'을 강제 주입합니다.",
    formulaSnippet: `[Optics & Compression]: Old iPhone 1x lens, noticeable sensor noise, heavy video compression artifacts.
[Imperfection Framing]: Unedited phone video aesthetic, crooked framing, accidental edge cut, natural hand tremors.
[Lighting]: Harsh ambient mixed fluorescent light, uncalibrated white balance, lifelike skin pores.`,
    aspectRatio: "16:9 / 9:16",
    duration: "15s",
    model: "Kling / Seedance / H3",
    bgGradient: "from-teal-950/60 via-slate-900/60 to-slate-950",
    visualIcon: "📱",
    keys: ["Old iPhone 1x Lens", "Heavy Compression Noise", "Imperfect Framing", "Organic Light Shift"],
    timeline: [
      { time: "렌즈 규격", label: "Old iPhone 1x", detail: "왜곡 없는 저화질 폰카 1배율 표준 렌즈 명시 (광각/망원 왜곡 차단)" },
      { time: "매체 결함", label: "압축 노이즈", detail: "heavy constant noise, unedited low-quality phone footage 주입" },
      { time: "화면 구도", label: "비대칭 결함", detail: "awkward angle, crooked framing, accidental edge cut 등 실수 연출" },
      { time: "카메라 무빙", label: "미세 떨림", detail: "natural handheld camera shake, unsmooth panning (삼각대/짐벌 배제)" }
    ],
    prompt: `[Camera & Medium]: Authentic handheld smartphone camera footage, captured with an old iPhone 1x standard lens. Noticeable sensor noise, heavy video compression artifacts, unedited low-bitrate phone video aesthetic. Natural hand tremors, subtle micro-jitters, awkward angle with imperfect crooked framing. No cinematic stabilization, strictly no gimbal, no artificial 3D sheen.

[Lighting]: Raw ambient room lighting, uncalibrated white balance, harsh mixed fluorescent and window light, lifelike natural skin textures with pores and slight imperfections.`
  }
];
