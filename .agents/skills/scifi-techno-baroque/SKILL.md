---
name: scifi-techno-baroque
description: 1970년대 아날로그 사이언스 판타지 시네마, 고대 의식용 바이오메카닉, 유물 기술(Relic-like Technology), 수제 프랙티컬 세트 및 35mm 필름 질감을 구현하기 위한 AI 비디오 및 이미지 프롬프트 스타일 가이드입니다.
version: 1.0.0
author: Antigravity
license: MIT
metadata:
  tags: [scifi-techno-baroque, techno-baroque, ancient-tech, 70s-sci-fantasy, practical-effects, analog-film, seedance, kling, wan, minimax]
---

# 🐅⚙️ SF 테크노 바로크 스타일 가이드 (Sci-Fi Techno-Baroque Prompting Guide)

본 가이드는 **1970년대 아날로그 사이언스 판타지 시네마(테리 길리엄, 짐 헨슨 스타일의 실물 세트 미학)**와 **고대 의식용 바이오메카닉(Ancient Ceremonial Biomechanical)**이 융합된 독보적인 세계관을 구현하기 위한 공식 스킬북입니다.

---

## 🧭 1. 핵심 철학 및 6대 비주얼 언어 (The 6 Visual Languages)

이 스타일의 핵심은 **"현대식 디지털/사이버펑크 요소를 100% 배제하고, 온몸을 기계 갑옷으로 덮는 대신 마치 정교한 고대 왕실 보석 장신구처럼 보이지만 알고 보면 인공지능 기계인 절제의 미학"**을 구현하는 것입니다.

### 💎 안면 장신구 위장형 사이버네틱스 수칙 (Subtle Facial Jewelry Cybernetics Rule)
* **전신 중갑옷 지양**: 몸통 전체를 투박한 로봇 갑옷으로 덮지 말고, 생체 본연의 자연스러운 질감(생물의 털, 인간의 피부 톤)을 70~80% 그대로 유지합니다.
* **눈가/이마/관자놀이 집중**: 한쪽 눈, 관자놀이, 귀 뒤, 이마 옆 라인을 따라 **"왕실 앤틱 귀걸이나 브로치처럼 생겼지만, 극도로 미세한 황동 톱니와 광학 조리개 렌즈가 맞물려 돌아가는 지능형 유물 인터페이스"**를 배치합니다.
* **디자인 키워드**: `delicate gilded brass filigree eyepiece, disguised antique jewel-encrusted cybernetics, miniature clockwork aperture, understated sacred AI relic`.

---

| 항목 | 핵심 키워드 및 미학 규격 | 실전 프롬프트 영문 프리셋 |
| :--- | :--- | :--- |
| **① Shape (형태)** | 곡선형 기계 구조 + 극도로 화려한 고대 의식용 장식 | `curved mechanical structures, ornate ceremonial ornaments, circular brass gears, filigree mechanical joints` |
| **② Material (재질)** | 손때 묻은 금속, 천연 보석, 낡은 섬유 | `gilded brass, darkened bronze, oxidized copper, aged silver, gemstones, weathered leather, antique embroidered silk` |
| **③ Technology (기술 철학)** | 유물형 기계, 잊혀진 고대 사이버네틱스 | `relic-like technology, sacred machinery, ceremonial cybernetics, forgotten futuristic machinery, mechanical clockwork pistons` |
| **④ Lighting (조명)** | 백열전구 및 촛불, 깊은 브라운 섀도우 | `warm tungsten candlelight, amber practical incandescent bulbs, deep brown shadows, high contrast chiaroscuro` |
| **⑤ Camera (구도/렌즈)** | 24~28mm 빈티지 광각 구면 렌즈, 깊은 전경 | `24mm vintage spherical lens, deep foreground staging, low-angle heroic framing, practical set staging` |
| **⑥ Film (필름 질감)** | 1970s 35mm 컬러 네거티브 질감, 광학 결함 | `1970s 35mm color negative film, organic film grain, soft reddish halation, gentle optical bloom, slightly faded warm colors` |

---

## 🔒 2. [Style] 고정 앵커 프리셋 (Permanent Style Anchor)

모든 이미지 생성기(Midjourney, FLUX) 및 비디오 프롬프트의 `[Style]` 필드에는 아래 블록을 **단 한 단어도 수정하지 않고 그대로 고정 삽입**합니다.

```text
1970s analog science-fantasy cinema, ancient ceremonial technology, ornate biomechanical design, gilded brass, darkened bronze, aged silver, raw gemstones, ritual ornaments, forgotten futuristic machinery, hand-built practical sets, warm tungsten candlelight, amber practical lights, deep brown shadows, 35mm color negative film, organic film grain, soft reddish halation, gentle optical bloom, slightly faded warm colors, vintage spherical lens, physical mechanical construction.
```

### 🚫 네거티브 필수 제외 요소 (Strict Exclusions)
```text
modern cyberpunk neon, sleek digital futurism, clean chrome, plastic surfaces, modern CGI gloss, blue laser glows, holograms, anime style, flat 2D, modern sharp digital video, cold clinical 4K sharpness, harsh digital contrast, clean digital sensor look.
```

---

## ⚠️ 2-1. [영구 철칙] 고화질·선명함과 빈티지의 상호 배제 원칙 (Incompatibility of Digital Sharpness & Vintage Aesthetics)

> **💡 핵심 물리 법칙**: 현대 디지털의 "고화질·선명함(Sharpness)"과 1970~90년대 "빈티지 아날로그 필름"은 광학적·물리적으로 **절대 공존할 수 없습니다.**

* **충돌 원인과 AI 왜곡 메커니즘**:
  - `crisp`, `sharp`, `laser-sharp`, `pristine`, `ultra-clear`, `4K/8K clarity` 같은 단어가 1개라도 프롬프트에 들어가는 순간, 비디오 AI는 빈티지의 핵심인 **"부드러운 빛 번짐(Bloom), 붉은빛 할레이션(Halation), 부드럽게 들뜬 암부(Lifted milky shadows)"**를 렌더링 결함/불량으로 판단하여 모조리 지워버리고, 쨍하고 번들거리는 현대식 디지털 스마트폰/CGI 질감으로 강제 변환합니다.
* **프롬프트 내 영구 금기 단어 (Zero Tolerance Prohibited Keywords)**:
  - `crisp`, `sharp`, `laser-sharp`, `razor-sharp`, `pristine`, `ultra-sharp`, `4K clarity`, `8K resolution`, `pristine telecine transfer`.
* **Negative 필수 수칙**:
  - `Negative`에 **`blurry`를 적는 행위를 100% 영구 금지**합니다 (소프트한 빈티지 광학 블룸을 AI가 삭제하는 주범).
  - 대신 **`modern sharp digital video, cold clinical 4K sharpness, harsh digital contrast, clean digital sensor look`**을 Negative에 반드시 명시하여 차갑고 쨍한 디지털 질감을 원천 차단합니다.
* **빈티지 광학 질감 표준 표현 (Optical Softness & Patina First)**:
  - 선명함 대신 **`Subtle soft optical diffusion`**, **`gentle reddish halation`**, **`soft film contrast with gently lifted shadows`**, **`natural organic film grain patina with delicate analog softness`** 등 광학적 부드러움과 유기적 질감으로만 묘사합니다.

---

## 🎬 3. 프로덕션 파이프라인 (3-Step Pipeline)

### Step 1 — 프롬프트 앵커 분리 (키프레임 생성)
`STYLE`은 영구 고정하고, `SUBJECT`만 교체하여 원하는 대상을 생성합니다.
- **예시 (호랑이 수호자)**:
  - `SUBJECT: A majestic Korean tiger transformed into an ancient ceremonial biomechanical guardian, filigree brass exoskeleton, sacred embroidered silk saddle.`
- **예시 (실험실과 여성)**:
  - `SUBJECT: A retro female scholar in vintage round glasses operating an ornate cast-iron energy projector inside an attic cluttered with practical machinery and giant cobwebs.`

### Step 2 — Image-to-Video (I2V) 비디오 엔진 연동 (Seedance 2.5 / Wan 3.0 / Kling 3.0)
1. 완성된 앵커 이미지를 비디오 생성기에 레퍼런스로 업로드합니다.
2. `[Roles]`에는 외형 묘사를 일체 배제하고 **`@[태그명]: Exactly as in reference photo.`**만 기재합니다.
3. 본문에는 오직 **카메라 무빙, 인물의 연기, 기계의 유압 가동, 환경음**에만 집중합니다.

### Step 3 — LoRA 학습 데이터셋 규격 (P_ANCIENT_TECH)
세계관을 단일 LoRA 모델로 영구 박제할 경우 아래 비율을 권장합니다.
- **트리거 워드**: `P_ANCIENT_TECH`
- **권장 데이터셋 수량**: 40~60장
  - 인간/인물 (왕, 사제, 학자, 기계 장인): 25%
  - 동물/환수 바이오메카닉 (호랑이, 독수리, 코끼리): 25%
  - 실내 프랙티컬 세트장 (다락방 실험실, 황동 천문대): 20%
  - 대형 건축/도시 전경: 15%
  - 세부 소품/유물 기계 컷: 15%

---

## 📋 4. 비디오 생성기 단일 표준 프롬프트 템플릿

```markdown
Part-1 [Aspect Ratio: 16:9]

[Tags]
@tiger_guardian

[Roles]
@tiger_guardian: Exactly as in reference photo.

[Style]
1970s analog science-fantasy cinema, ancient ceremonial technology, ornate biomechanical design, gilded brass, darkened bronze, aged silver, gemstones, ritual ornaments, forgotten futuristic machinery, hand-built practical sets, warm tungsten candlelight, amber practical lights, deep brown shadows, 35mm color negative film, organic film grain, soft reddish halation, gentle optical bloom, slightly faded warm colors, vintage spherical lens, physical mechanical construction.

[Start State]
Low-angle 24mm vintage spherical lens shot. @tiger_guardian stands motionless in an ancient stone temple, heavy mechanical forelegs planted firmly on the worn carpet.

[Timeline]
00-04s [Shot 1: Slow creeping push-in from ground level]:
@tiger_guardian slowly raises its mechanical paw, internal brass gears rotating with heavy friction. Its amber feline eyes narrow with supreme authority.
<Heavy metallic clank, deep hydraulic hiss, low rumbling tiger breath>

04-08s [Shot 2: Low-angle tracking tilt-up]:
Camera tracks slowly along the ornate filigree spine armor as ceremonial red tassels sway slightly under warm flickering candlelight.
<Soft cloth rustle, subtle brass gear ticking, ambient temple echo>

[End State]
Camera locks into a frontal low-angle close-up as the tiger lets out a deep silent breath, golden eyes glinting in the tungsten glow.

[Audio]
<Heavy metallic gear clanks, hydraulic piston hisses, low animal growls, crackling candle fire, hollow stone hall resonance>

[Negative]
modern cyberpunk neon, sleek digital futurism, clean chrome, LED lights, CGI gloss, modern transitions, watermark, logo, text, subtitles, BGM, music.
```
