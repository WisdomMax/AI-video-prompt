---
name: minimax-h3-prompting
description: MiniMax H3 (Hailuo 3.0) 비디오 생성 모델을 위한 모션그래픽, 타이포그래피, 아날로그 시네마틱, 네이티브 사운드 동기화 및 타임라인 브리프 사용 가이드입니다.
version: 1.2.0
---

# MiniMax H3 (Hailuo 3.0) 비디오 프롬프트 튜닝 & 실전 가이드

MiniMax H3(Hailuo 3.0)는 2K 해상도(24 FPS, 4~15초)의 비디오와 **네이티브 스테레오 오디오(Sound FX, 앰비언트, 음성)**를 동시에 생성하며, 특히 **모션그래픽, 타이포그래피(텍스트 가독성) 및 감성 아날로그 시네마틱 렌더링**에 특화된 차세대 멀티모달 비디오 생성 모델입니다.

---

## 1. MiniMax H3 핵심 기술 스펙 및 독보적 강점

* **해상도 & 프레임레이트**: 2K (최대 3.7 Megapixel 렌더링), 24 FPS
* **생성 시간 제어**: 4초 ~ 15초 (정수 단위 자유 제어 가능)
* **네이티브 오디오 패스 (Native Audio Pass)**: 비디오 렌더링과 동시에 **화면 모션 및 텍스트 팝업 시점에 1:1로 맞춘 사운드 FX, 앰비언트, BGM, 음성**이 자동 반응 합성됨
* **텍스트 가독성 (Legibility)**: 큰 서체, 네온, 3D 타이포그래피 및 UI 렌더링 붕괴가 최소화됨 (큰따옴표 `"TEXT"` 연동)
* **멀티모달 참조 지원**: 이미지(구도/캐릭터), 비디오(모션/카메라 무빙), 오디오(음성/톤) 동시 연동

---

## 2. MiniMax-AI 공식 5대 생성 모드 및 표준 프롬프트 아키텍처 (Official H3 Modes)

MiniMax 공식 저장소(`MiniMax-AI/MiniMax-H3`)에서 정의한 5대 비디오 생성 모드와 공식 3대 코어 필드 구조입니다.

### 💡 공식 5대 모드 규격:
1. **`T2VA` (Text-to-Video & Audio)**: 텍스트만으로 전체 시청각 타임라인을 완전 생성
2. **`I2VA` (Image-to-Video & Audio / First Frame)**: 첫 프레임(`<Picture 1>`)에서 출발하여 앞으로 전개
   - *공식 첫 줄 지시어*: `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`
3. **`FL2VA` (First-and-Last Frame)**: 첫 프레임(`<Picture 1>`)과 마지막 프레임(`<Picture 2>`) 사이의 연속적인 경로 보간(Interpolation)
   - *공식 첫 줄 지시어*: `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.`
4. **`L2VA` (Last Frame Completion)**: 마지막 프레임(`<Picture 1>`)으로 수렴하도록 이전 상태를 역추론하여 착지
   - *공식 첫 줄 지시어*: `How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.`
5. **`Ref2VA` (Full-Reference Mode / 6-Section Architecture)**: 다중 이미지, 비디오, 오디오를 바인딩하는 최상급 6개 섹션 구조 (`subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music`)

### 📋 MiniMax 공식 3대 코어 필드 (Official 3 Core Fields):
```text
integrated_multimodal_description:
[Shot 1] Cinematic, live-action, a medium shot frames...
[Shot 2] At 00:03.500, the camera cuts to...

overall_soundscape:
Ambient wind howling, rhythmic footsteps on stone, sharp metallic sword unsheathe chimes.

non_diegetic_music:
Fast-paced epic cinematic orchestral score with traditional percussion and soaring strings.
```

---

## 2-0. 🛠️ MiniMax-AI 공식 8대 특화 스킬 맵 (8 Official Style Skills)

MiniMax-AI 공식 저장소에서 제공하는 8대 특화 생성기입니다:
1. **`h3-prompt-writing`**: 5대 생성 모드(T2VA, I2VA, FL2VA, L2VA, Ref2VA) 공식 구조화 변환 엔진
2. **`minimalist-product-ad-generator`**: E-커머스 미니멀 제품 광고 숏폼 (비트 동기화 타이포 + 제품 3D 회전)
3. **`3d-animation-short-generator`**: 3D 애니메이션 숏폼 제작기 (스토리보드, 캐릭터/환경 카드, 샷 기획)
4. **`papercraft-stop-motion-explainer`**: 페이퍼크래프트 스톱모션 지식/교육 영상 (다층 디오라마 세트)
5. **`brand-promo-video-generator`**: 브랜드 & 웹사이트 프로모션 숏폼
6. **`music-video-subtitle-generator`**: MV 자막 & 비트 반응형 공간 타이포그래피(Spatial Typography)
7. **`co-op-game-intro-generator`**: 2인 협동 게임 인트로 및 오프닝 메뉴 애니메이션
8. **`paper-collage-explainer-generator`**: 하프톤 페이퍼 콜라주 스톱모션 영상
9. **`handdrawn-live-video-generator`**: 발광 손그림 2D 애니메이션 + 실사 공간 결합 비디오

---

## 2-1. ⚡ 초간결 현상 나열식 기법 (Ultra-Short Phenomenon-Based Method)

수천 자의 복잡한 타임라인 대신, **`멀티모달 레퍼런스([Audio1], [Image1])` + `발생할 현상 5~7줄 불렛포인트`** 조합으로 AI의 자율 보완 능력(AI Interpolation)을 극대화하는 빠른 실험용 프롬프팅 기법입니다.

### 💡 핵심 원리:
* 인물의 외모, 색감, 음악 박자는 레퍼런스 파일(`[Image1]`, `[Audio1]`)에 위임합니다.
* 텍스트 프롬프트는 **화면에서 발동하길 원하는 시각적 기믹/동작 현상**만 직관적으로 나열합니다.

### 📋 초간결 현상 나열 템플릿 (7-Line Template):
```markdown
[Audio1]의 음악과 [Image1]의 인물을 기반으로 제작된 프로모션 비디오.
・음악 보컬에 맞춰 완벽하게 립싱크를 진행한다.
・손으로 그린 2D/3D UI 프레임 안에서 노래를 부른다.
・거대한 마우스 포인터가 등장해 볼을 꼬집듯 잡아당긴다.
・화면이 4분할 그리드로 쪼개지며 각각 다른 앵글을 보여준다.
・에러 팝업 창이 뜨고 ✕ 버튼을 누르면 화면 가득 창이 증식한다.
・비트에 맞춰 빈번하게 화각이 전환되는 다이내믹 멀티 샷.
```

### 🎯 언제 사용하면 좋은가?
1. **빠른 아이디어 스케치 & MV 프로토타입**: 30초 만에 프롬프트를 작성하여 다양한 연출 가능성을 빠르게 탐색할 때.
2. **모션그래픽 & UI 기믹 연출**: 마우스 포인터, 화면 분할, 창 증식 등 After Effects 감성의 그래픽 요소를 직관적으로 테스트할 때.
3. **피드백 루프 실험**: 기본 7줄로 렌더링한 후, 결과물을 보며 `"배경에 리릭 애니메이션 추가"`, `"레드/블루 테마컬러 적용"` 등 필요한 요소만 1줄씩 추가하며 완성해 나갈 때.

---

## 3. Production Brief 5단계 프롬프트 구조

MiniMax H3는 단순 수식어 나열보다 **기획서(Production Brief)** 형태로 작성할 때 가장 뛰어난 퀄리티를 보여줍니다.

$$\text{Prompt} = \text{Subject} \rightarrow \text{Setting} \rightarrow \text{Action} \rightarrow \text{Camera Movement} \rightarrow \text{Audio/Mood}$$

### 작성 공식:
1. **Subject (주제/개체)**: 연출할 인물, 제품, 또는 타이포그래피 요소
2. **Setting (배경/비주얼 시스템)**: 컬러 톤, 백그라운드 재질, 조명 (예: `bold neon style, vibrant green gradient, studio lighting`)
3. **Action (동작/모션)**: 텍스트의 슬라이드, 팝업, 3D 회전 또는 인물의 연기
4. **Camera Movement (카메라 명세)**: `DV 16mm handheld camcorder aesthetic, slow autofocus lag, awkward micro-zoom` 등 정밀 카메라 지시어
5. **Audio / Sound FX (오디오)**: `Audio Pass: energetic beat with a sharp metallic pop when text appears, warm room ambient`

---

## 4. 모션그래픽 & 타이포그래피 렌더링 4대 수칙

1. **정확한 큰따옴표 지시**: 등장시킬 영문/한글 텍스트는 반드시 큰따옴표(`"TEXT"`)로 묶어 명시합니다.
   * *예시*: `Bold kinetic 3D typography reading "iHerb 3-Day Express" sliding into center.`
2. **타이포 모션 스타일 명시**: 텍스트가 어떻게 나타나는지 메커니즘을 적어줍니다.
   * *지시어 예시*: `slide in from left`, `pop with sparkle burst`, `mask reveal`, `3D rotation`
3. **One-Job 원칙 (단일 역할 분담)**:
   * 이미지 레퍼런스 $\rightarrow$ 브랜딩 로고/제품 형태 지정 전용
   * 비디오 레퍼런스 $\rightarrow$ 타이포/카메라 속도감 지정 전용
   * 텍스트 프롬프트 $\rightarrow$ 글자 내용 및 서사 지시 전용
4. **오디오 타격음 싱크 (Native Audio Syncing)**: 텍스트가 팝업되는 시점에 맞는 효과음(`Audio Pass: pop SFX, chime, heavy bass drop`)을 명시하여 화면과 사운드 싱크를 1:1로 결합합니다.

### 4-1. 🎨 [모션그래픽 카테고리 1] 다중 이미지 순차 옴니 레퍼런스 & 그래픽 타이포 모션 (Multi-Image Omni-Reference & Typography Morph)

8장의 일러스트(텍스트/배경/인물 완벽 포함)와 15초 음원([Audio1])을 바인딩하여, After Effects급 2D/3D 키네틱 타이포 뮤직비디오를 초간결하게 구현하는 실전 패턴입니다.

#### 🎨 레퍼런스 이미지의 비주얼 스타일 & 감성 분위기 (Aesthetic Style):
* **`스타일 장르`**: 80~90년대 레트로 시티팝(City Pop) x Y2K 틴에이지 감성 애니메이션 일러스트 (Anime Editorial / Webtoon Aesthetic)
* **`컬러 팔레트 (Color Palette)`**:
  - **빈티지 웜 톤**: 베이지(Beige), 머스타드 옐로우(Mustard Yellow), 레트로 오렌지(Retro Orange)
  - **콘트라스트 쿨 톤**: 딥 네이비(Deep Navy), 빈티지 코발트 블루(Vintage Cobalt Blue), 섀도우 퍼플(Shadow Purple)
  - **캐릭터 포인트**: 파스텔 핑크 트윈테일 헤어(Pastel Pink Hair), 교복 블레이저 & 체크 스커트(School Uniform Blazer)
* **`텍스처 및 그래픽 기법`**:
  - **하프톤/종이 질감(Halftone & Paper Texture)**: 인쇄물 스크린톤 느낌의 자잘한 그레인과 도트 텍스처
  - **볼드 산세리프 & 이탤릭 타이포(Bold Sans-serif & Italic Bold Typography)**: 도로 표지판, 횡단보도, 시계 판, 버스 정류장 광고판 구조물 속에 자연스럽게 박힌 사선/볼드 영문 텍스트 디자인
  - **스토리텔링 공간 구성**: 버스 정류장, 건널목, 지하철/버스 안, 스포트라이트 등 도심 청춘의 하루 일상을 몽타주 형태로 연출

#### 💡 성공의 핵심 비결 (레퍼런스 이미지 분석):
* **`이미지 자체에 타이포그래피 사전 배치`**: 8장의 이미지(`[Image1]`~`[Image8]`)에 이미 영문 가사("Lip gloss, bus stop", "Tick-tock, don't stop", "Two steps, same street" 등)와 도로/시계/버스정류장 그래픽이 완성된 상태로 준비됨.
* **`텍스트 렌더링 붕괴 0% 원천 차단`**: AI에게 글자를 새로 그리라고 시키는 대신, 이미지가 가지고 있는 타이포 레이아웃을 참조하므로 철자 왜곡 없이 100% 완벽한 폰트 모션이 나옴.
* **`15초 / 8장 = 약 1.8초 비트 매칭`**: 15초 음원 보컬 흐름에 맞춰 8장의 일러스트가 비트 드롭마다 자연스럽게 컷 전환 & 모핑됨.

#### 📋 실전 프롬프트 템플릿:
```markdown
Audio1の曲に合うように Image1 Image2 Image3 Image4 Image5 Image6 Image7 Image8を順番にモーフィングさせてください。キャラクターは可愛く動いて、リリックもモーションする。
```
* **한국어 표준형**:
```markdown
[Audio1]의 곡에 맞게 [Image1], [Image2], [Image3], [Image4], [Image5], [Image6], [Image7], [Image8]을 순서대로 모핑/전환시켜 주세요. 캐릭터는 귀엽게 움직이고, 가사(Lyrics)도 타이포 모션 그래픽으로 역동적으로 연출해 주세요.
```

### 4-2. 🏔️ [모션그래픽 카테고리 2] 할리우드 에픽 환경 파괴 & 조립 3D 타이포그래피 (Epic Environmental 3D Typography)

거대한 자연물(절벽, 산, 빙하, 마그마, 고대 유적 등)이 붕괴·폭발하는 물리 연산 속에서 거대한 3D 타이포그래피가 조립되었다가 다시 자연으로 흩어지는 블록버스터급 오프닝 타이틀 기법입니다.

#### 💡 연출 성공 메커니즘:
* **`환경 파괴 $\rightarrow$ 타이포 조립 4단계 물리 법칙`**:
  1. **초기 파괴 (Fracture)**: 산/절벽의 균열과 거대한 먼지 구름 상승 (`collapsing, rock faces fracture, dust clouds rise thousands of feet`)
  2. **공중 회전 & 충돌 (Mid-air Collision)**: 거대한 돌기둥들이 슬로우 모션으로 회전하며 강력하게 격돌 (`monoliths rotate in slow motion, colliding with breathtaking force`)
  3. **물리적 타이포 조립 (Assembly)**: 파편과 먼지가 모여 고대 석재 질감의 거대한 영문 단어 `"DOMINION"`을 형성 (`gradually assemble the monumental word "TEXT", carved from ancient stone`)
  4. **풍화 & 해체 엔딩 (Dissolution)**: 거대한 굉음 후 글자가 다시 모래 먼지로 부서져 바람에 날아가며 사라짐 (`title crumbles into dust carried away by wind`)
* **`텍스처 명세`**: `ancient stone scarred by centuries of erosion` (수 세기의 침식 흉터가 남은 석재 질감)

#### 📋 실전 프롬프트 템플릿:
```markdown
Ultra cinematic title sequence: A gigantic mountain cliff begins collapsing into a deep canyon. Entire rock faces fracture while dust clouds rise thousands of feet into the atmosphere. Giant stone monoliths rotate in slow motion through the air, colliding with breathtaking force. Rock fragments, dust, and debris gradually assemble the monumental word "[TITLE_TEXT]", carved from ancient stone scarred by centuries of erosion. The canyon echoes with a deafening rumble before the title crumbles into dust that is carried away by the wind. Monumental scale, ancient power, Hollywood epic title design.
```

### 4-3. 🎮 [모션그래픽 카테고리 3] AAA 게임 캐릭터 리빌 10-컷 에디토리얼 타이포 트레일러 (AAA Game Character Reveal & Editorial Kinetic Typography)

언리얼 엔진 5(UE5)급 턴어라운드 캐릭터 3D 레퍼런스 시트 1장(`Image1`)을 기반으로, 15초 동안 **정확히 10개의 초고속 시네마틱 하드 컷**과 **하이엔드 에디토리얼 키네틱 타이포그래피**를 결합하는 AAA 게임 캐릭터 공개 트레일러 기법입니다.

#### 💡 연출 성공의 핵심 기법 (10-Cut Micro-Structure):
1. **단일 턴어라운드 레퍼런스 락 (`Single Turnaround Reference Lock`)**:
   - 4면 턴어라운드(정면/측면/후면/3/4뷰) 설정화 1장을 절대적 기준으로 지정하여 10개 컷 전체의 외모, 의상, 무기(카타나), 장신구 붕괴를 0%로 완벽 통제.
2. **10단 시네마틱 컷 분할 공식 (10-Cut Reveal Arc)**:
   - `CUT 01 (0.00–1.20s)`: [무기 매크로] 카타나 칼날 래피드 슬라이드 + 좌측 고속 타이포 진입 `"THE BLADE"`
   - `CUT 02 (1.20–2.50s)`: [손/그립] 붕대 감은 손 조임 + 원형 타겟팅 모션 그래픽 + 수직 타이포 압축 `"DISCIPLINE"`
   - `CUT 03 (2.50–4.00s)`: [상체] 근육/조끼 상승 틸트 + 좌우 충돌 타이포 `"NO MASTER"`
   - `CUT 04 (4.00–5.40s)`: [얼굴/눈빛] 시선 클로즈업 + 수직 분할선 + 그리드 안착 타이포 `"NO FEAR"`
   - `CUT 05 (5.40–6.90s)`: [3/4 히어로 뷰] 90도 오비팅 회전 + 2.5D 캐릭터 등 뒤 가림 텍스트 `"HONOR"`
   - `CUT 06 (6.90–8.40s)`: [전신 실루엣] 피사체 추적 브래킷 UI + 수평 슬라이드 타이포 `"WANDERER"`
   - `CUT 07 (8.40–9.80s)`: [발도 모션] 칼날 궤적이 모션 트레일 타이포로 변형 스냅 `"PRECISION"`
   - `CUT 08 (9.80–11.30s)`: [눈빛 익스트림 익스트림] 찰나의 침묵 + 1프레임 글리치 타이포 `"THE LAST" "RONIN"`
   - `CUT 09 (11.30–13.00s)`: [로우앵글 레전드] 스케일 확대 30% $\rightarrow$ 100% 마스크 통과 `"A LEGEND RISES"`
   - `CUT 10 (13.00–15.00s)`: [최종 타이틀] 4방향 확장 라인 붕괴 $\rightarrow$ 최종 로고 안착 `"THE WANDERER / A LEGEND WITHOUT A MASTER"`
3. **에디토리얼 그래픽 디자인 요소 (Editorial Design System)**:
   - 유치한 사이버펑크 네온이나 잡다한 게임 HUD를 배제하고, **화이트/페일 그레이의 미니멀 지오메트릭 라인, 그리드, 좌표 마크, 브래킷, 2.5D 심도 상호작용**으로 최고급 영화 포스터 감성 연출.

#### 📋 실전 프롬프트 템플릿:
```markdown
Use the uploaded character reference as the absolute visual source of truth. Maintain the exact warrior design, face, hairstyle, muscular anatomy, clothing, and weapon across his shoulders.
Create a 15-second premium AAA game character reveal trailer with exactly 10 cinematic cuts. Combine photorealistic AAA game cinematography with high-end editorial motion graphics and kinetic typography.
Style: AAA game cinematic / Unreal Engine 5 quality / dark historical fantasy / premium editorial campaign
Aspect: 16:9 | Duration: 15s | Cuts: exactly 10
Typography: oversized condensed sans-serif, bold, white/pale-grey
Graphics: minimal geometric lines, grids, brackets, circles, tracking marks

CUT 01 — 0.00–1.20s: MACRO WEAPON OPEN. Blade slide. TEXT: "THE BLADE".
CUT 02 — 1.20–2.50s: HAND / GRIP. Hand tightening. Circular reticle. TEXT: "DISCIPLINE".
CUT 03 — 2.50–4.00s: TORSO REVEAL. Camera travel upward. TEXT: "NO MASTER".
CUT 04 — 4.00–5.40s: FACE REVEAL. Eyes push-in. Vertical line. TEXT: "NO FEAR".
CUT 05 — 5.40–6.90s: THREE-QUARTER HERO. 90-degree orbit. 2.5D depth TEXT: "HONOR".
CUT 06 — 6.90–8.40s: FULL-BODY REVEAL. Silhouette tracking brackets. TEXT: "WANDERER".
CUT 07 — 8.40–9.80s: KATANA MOTION. Blade motion trail turns into TEXT: "PRECISION".
CUT 08 — 9.80–11.30s: EYE CLOSE-UP. Silence. 1-frame glitch TEXT: "THE LAST RONIN".
CUT 09 — 11.30–13.00s: LEGEND SHOT. Low-angle rise. Scaled TEXT: "A LEGEND RISES".
CUT 10 — 13.00–15.00s: FINAL TITLE REVEAL. Full-body hero shot. Rim light. Final Title: "THE WANDERER / A LEGEND WITHOUT A MASTER". CUT TO BLACK.

CINEMATIC QUALITY: Photorealistic AAA game cinematic, Unreal Engine 5, PBR materials, volumetric lighting, anamorphic lens.
CHARACTER LOCK: Maintain identical anatomy, markings, costume, colors, and katana across all 10 cuts.
```

### 4-3-1. 🌸 [모션그래픽 카테고리 3-1] 프리미엄 애니메이션 액션 캐릭터 리빌 13-컷 트레일러 (13-Cut Anime Heroine Kinetic Reveal Trailer)

단일 캐릭터 일러스트/설정화(`@image1`) 1장을 기반으로 15초 동안 **정확히 13개의 초고속 시네마틱 컷(24fps)**, **타이포그래피 카드(Interstitial Cards)**, **발도/액션 슬래시 궤적**, **2.5D 인물-글자 오버랩(Text-Overlap Depth)**을 결합하는 일본 애니메이션/게임 오피셜 캐릭터 공개 트레일러 기법입니다.

#### 💡 13-Cut 인터스티셜 타이포 & 액션 교차 연출 메커니즘:
1. **타이포 사전 선언 및 변수 바인딩 (`Text Variable Binding`)**:
   - `CHARACTER_NAME = "HANA"`
   - `STATUS_TEXT_1 = "BLADE READY"`, `STATUS_TEXT_2 = "MODE: ENGAGE"`
   - `INTERSTITIAL_TEXT_1 = "SYSTEM LINK"`, `INTERSTITIAL_TEXT_2 = "TARGET LOCK"`, `INTERSTITIAL_TEXT_3 = "FULL DRIVE"`
   - `SUBTITLE = "SAKURA STRIKER"`
2. **글자 우선 출력 후 인물 오버랩 규칙 (`Show Text First, Then Overlap`)**:
   - 타이포그래피 컷에서는 항상 **거대한 타이포가 먼저 선명하게 등장하고, 그 위를 캐릭터가 가로지르거나(Overlap), 슬라이드되거나, 뒤에서 튀어나오도록 지시**하여 2.5D 입체감과 가독성을 동시 확보.
3. **13-컷 마이크로 시퀀스 아크 (13-Cut Action Arc)**:
   - `CUT 01 (0.00–1.00s)`: [얼굴 익스트림 클로즈업] 자신감 있는 표정, 흩날리는 머리칼과 꽃잎, 슬로우 푸시인
   - `CUT 02 (1.00–2.00s)`: [발도 매크로] 손잡이 쥐기, 순간 발도, 금속 쇠소리와 화이트/핑크 검광 궤적
   - `CUT 03 (2.00–3.00s)`: [ACTIVE CARD] 화이트 그래픽 스크린 + 거대 `"BLADE READY"` ➔ 캐릭터 발도 준비 포즈 오버랩
   - `CUT 04 (3.00–3.80s)`: [ENGAGE CARD] 블랙 그래픽 스크린 + 거대 `"MODE: ENGAGE"` ➔ 실루엣과 대각선 검광 슬라이스
   - `CUT 05 (3.80–4.90s)`: [배틀 월드 진입] 화이트/다크 아레나 공간 ➔ 초고속 전방 돌진 로우 트래킹
   - `CUT 06 (4.90–5.90s)`: [검격 액션] 회전 참격 ➔ 3색(화이트/핑크/시안) 우아한 검기 트레일 궤적
   - `CUT 07 (5.90–6.60s)`: [INTERSTITIAL 01] 거대 `"SYSTEM LINK"` ➔ 눈동자 크롭 + 전신 실루엣, UI/스캔라인 와이프
   - `CUT 08 (6.60–7.70s)`: [임팩트 격돌] 3개의 지오메트릭 드론 돌진 ➔ 단칼 참격으로 분할 파괴 + 핑크/화이트 임팩트 플래시
   - `CUT 09 (7.70–8.40s)`: [INTERSTITIAL 02] 거대 `"TARGET LOCK"` + 대각선 바 ➔ 대형 인물 클로즈업이 글자 뒤로 슬라이드
   - `CUT 10 (8.40–9.40s)`: [고속 질주 & 소매 와이프] 카메라를 향해 정면 돌진 ➔ 렌즈를 스치며 코트/소매가 전체화면 와이프 전환
   - `CUT 11 (9.40–10.10s)`: [INTERSTITIAL 03] 거대 `"FULL DRIVE"` + 핑크 서클 ➔ 소형 실루엣이 검광과 함께 글자를 가로질러 점프
   - `CUT 12 (10.10–12.20s)`: [히어로 피니시] 공중 강하 후 거대한 마무리 일격 참격 ➔ 거대 핑크/화이트 검기 호선이 공간을 가르고 꽃잎 폭발 ➔ 여유로운 착지 및 카메라 응시 미소
   - `CUT 13 (12.20–15.00s)`: [최종 캐릭터 ID] 아이보리 배경 + 거대 `"HANA"` ➔ 전신 히어로 포즈 오버랩 + 엠블럼 + 서브타이틀 `"SAKURA STRIKER"` / `"BLADE READY"` 안착
4. **편집 및 리듬 규칙 (Editing Rhythm)**:
   - 클로즈업 ➔ 타이포 카드 ➔ 액션 ➔ 타이포 카드 ➔ 액션 ➔ 최종 캐릭터 카드로 이어지는 초고속 교차 리듬.

#### 📋 실전 영문 템플릿 1: Kōda (@aimikoda) 풀 마스터 템플릿 (Universal Master Version)
```text
MiniMax H3 Prompt:
PARAMETERS
CHARACTER_NAME = "[CHARACTER NAME]"
STATUS_TEXT_1 = "[ACTIVE]"
STATUS_TEXT_2 = "[MODE: ENGAGE]"
INTERSTITIAL_TEXT_1 = "[SYSTEM LINK]"
INTERSTITIAL_TEXT_2 = "[TARGET LOCK]"
INTERSTITIAL_TEXT_3 = "[FULL DRIVE]"
SUBTITLE = "[CHARACTER TITLE / CODENAME]"
PROJECT_TEXT = "[OPTIONAL PROJECT NAME]"

Create a 15-second premium cinematic character reveal trailer with exactly 13 distinct cuts, 24fps. Use @image1 as the sole authority for the character's identity, proportions, outfit, materials, colors and visual style. Never redesign the character. Adapt the environment, abilities, VFX and movement naturally to them.

The overall presentation should feel like a premium AAA action-game character introduction. Motion-design sections use a bold editorial language: oversized condensed typography, clean white or pale-grey fields, huge circular color blocks, thin technical diagrams, concentric rings, halftone textures, tiny interface markings, scan lines, geometric accents, sweeping brush or energy strokes and strong foreground/background parallax. The main palette shifts between black and white, icy cyan, electric blue, neon yellow and warm golden amber.

In text-based graphic screens, the typography must appear clearly and be fully readable first, then the character, a cropped close-up or a silhouette may slide in front of it, overlap it or stand beside it. In some graphic-card backgrounds, also use cropped character close-ups or enlarged facial details as integrated design elements. Use the text parameters above exactly.

CUT 01 | 0.00-1.10s | FACE: Extreme cinematic close-up. Calm focused expression, part of the face naturally obscured by hair, hand, mask or accessory. Shallow depth of field and subtle push-in.
CUT 02 | 1.10-2.20s | ACTIVATION: A signature effect ignites around the character's eyes, hands, body or equipment: glowing rings, symbols, particles, energy filaments, holographic nodes or character-specific effects. The gaze lifts as the effect rapidly peaks.
CUT 03 | 2.20-3.20s | ACTIVE CARD: Hard graphic-match into a bright editorial freeze-frame. Large vivid circular field behind the character, oversized black condensed typography, thin technical circles, tiny UI text, halftone detail and sharp diagonal graphic streaks. Show the typography clearly first, then let the character overlap it or enter beside it. A cropped facial close-up or upper-body close-up may be integrated into the background design. Typography: STATUS_TEXT_1
CUT 04 | 3.20-4.10s | ENGAGE CARD: Snap to a high-contrast black character silhouette over a bold horizontal accent-color typography band. The text should read clearly before the silhouette crosses in front of it or locks beside it. A large luminous brushstroke or energy ribbon sweeps diagonally across the foreground with strong motion blur. Typography: STATUS_TEXT_2
CUT 05 | 4.10-5.20s | WORLD: Smash cut into a cinematic environment suited to the character. Wide dramatic perspective as they immediately dash, leap, land or burst forward. Fast whip-pan or reactive tracking camera.
CUT 06 | 5.20-6.20s | DETAIL: Fast close or medium shot of one defining ability, weapon motion, gesture, transformation or acrobatic action. Sharp character, strong foreground streaking.
CUT 07 | 6.20-6.90s | INTERSTITIAL 01: Hard cut to a text-led graphic design screen. Huge condensed typography, layered circles, technical lines, scan lines, halftone textures, tiny data text and aggressive graphic wipes. The typography must be fully readable first, then bring in the character as a smaller integrated figure, cropped close-up or silhouette. Typography: INTERSTITIAL_TEXT_1
CUT 08 | 6.90-7.90s | IMPACT: Return to action from a new aggressive angle. Attack, dodge, ability release or interaction with a simple secondary threat. Low angle, side track, whip-pan or short orbit.
CUT 09 | 7.90-8.60s | INTERSTITIAL 02: Another editorial text card, cleaner and punchier, built from bold typography, diagonal slashes, accent-color bars, fine UI markings and strong parallax. Let the typography dominate first, then place the character beside it or pass a cropped close-up in front for depth. Typography: INTERSTITIAL_TEXT_2
CUT 10 | 8.60-9.60s | VELOCITY: New perspective continues the momentum. Character rushes toward camera, crosses close to lens, launches upward or rapidly changes direction while the environment stretches into controlled speed blur.
CUT 11 | 9.60-10.30s | INTERSTITIAL 03: Final text-based graphic card before the hero beat. Bold oversized typography, sweeping energy stroke, geometric overlays, concentric diagrams and a fast silhouette or cropped character insert. Ensure the text is legible before the character layer overlaps or frames it. Typography: INTERSTITIAL_TEXT_3
CUT 12 | 10.30-12.30s | HERO MOMENT: The character performs their most iconic movement, ability, strike, landing or confident stop. Briefly stabilize at the visual peak, then collapse the shot into a bright smear, silhouette frame or graphic-match transition.
CUT 13 | 12.30-15.00s | CHARACTER ID: Premium final identity card. Clean pale background with enormous translucent concentric circles, fine technical arcs, network nodes, subtle halftone texture, tiny graphic markings and restrained chromatic glints. Place the character in a dynamic full-body hero pose overlapping huge condensed typography. The name should register clearly before the character overlap becomes dominant. A large cropped close-up can also be subtly embedded into the background composition. Behind them, add a large black circular ink-brush or emblem shape containing a ghosted visual motif associated with the character: creature silhouette, symbol, power form, weapon motif or abstract representation of their identity.
Primary typography: CHARACTER_NAME
Secondary: SUBTITLE
Optional: PROJECT_TEXT
Allow the character to overlap the typography for depth.

EDITING: Very aggressive premium game-trailer rhythm. Hard cuts, graphic matches, whip pans, freeze frames, impact flashes, directional smears, foreground wipes, silhouette transitions and short speed ramps. Every cut must introduce a clearly different composition or visual mode. The text-based interstitial cards should break up the action rhythm and keep the sequence from feeling like uninterrupted combat footage. No slow dissolves or long continuous choreography.
BGM DESIGN: Create a fast, character-driven AAA game-trailer score tightly synced to the edit. Adapt genre and instrumentation to the character, building from restrained tension into punchy percussion, bass and rising intensity, with clear hits for cuts, typography, transitions and action beats. Peak at the hero moment and finish with a strong final reveal stinger. Integrate subtle UI ticks, whooshes, energy swells and sub impacts into the music.
```

#### 📋 실전 영문 템플릿 2: HANA 쇼트 버전 (Anime Action Short Version)
```text
MiniMax H3 Prompt — Short Version
Create a 15-second premium anime action character reveal trailer with exactly 13 cuts, 24fps. Use @image1 as the absolute reference. Preserve [CHARACTER_NAME] exactly: [APPEARANCE_AND_OUTFIT_DESCRIPTION]. Do not redesign face, hair, colors, proportions, or costume.

Text:
CHARACTER_NAME = "[NAME]"
STATUS_TEXT_1 = "[STATUS_1]"
STATUS_TEXT_2 = "[STATUS_2]"
INTERSTITIAL_TEXT_1 = "[INT_1]"
INTERSTITIAL_TEXT_2 = "[INT_2]"
INTERSTITIAL_TEXT_3 = "[INT_3]"
SUBTITLE = "[SUBTITLE]"

Style: Premium AAA anime game reveal. Cute but powerful. Fast sword action mixed with bold motion graphics. Use black, white, pale pink, vivid magenta, electric cyan, and tiny gold accents. Use oversized condensed typography, circles, diagonal lines, UI marks, halftone, scan lines, petals, speed streaks, and strong parallax. In text cuts, show the text clearly first, then let character overlap it.

CUT 01 | 0.00–1.00 | FACE: Extreme close-up. Cute confident expression. Soft wind in hair. Petals. Slow push-in.
CUT 02 | 1.00–2.00 | DRAW: Close-up of hand gripping sword. Instant draw. Sharp metallic sound. Bright blade streak. Expression becomes focused.
CUT 03 | 2.00–3.00 | ACTIVE CARD: Bright white graphic screen. Huge text: "[STATUS_TEXT_1]". Show text first, then character enters in a sword-ready pose. Add pink circle, concentric rings, UI details, petals.
CUT 04 | 3.00–3.80 | ENGAGE CARD: Black graphic screen. Bold accent band with text: "[STATUS_TEXT_2]". Show text first, then character silhouette cuts across it. Huge diagonal sword streak.
CUT 05 | 3.80–4.90 | WORLD: Futuristic anime battle arena: white architecture, dark void, glowing rings, floating geometry. Character launches forward at extreme speed. Low tracking shot.
CUT 06 | 4.90–5.90 | SWORD ACTION: Medium close action shot. Character spins and slashes. Sword visible. Three elegant slash trails: white, pink, cyan. Fast short orbit.
CUT 07 | 5.90–6.60 | INTERSTITIAL 01: Text-led screen. Huge text: "[INTERSTITIAL_TEXT_1]". Show text first. Then add cropped close-up of eye and a small full-body silhouette. UI lines, scan lines, circles, wipes.
CUT 08 | 6.60–7.70 | IMPACT: Three simple black geometric enemy drones rush in. Character steps once and performs a single elegant slash. Enemies split into clean fragments. Big pink-white impact flash.
CUT 09 | 7.70–8.40 | INTERSTITIAL 02: Graphic screen. Huge text: "[INTERSTITIAL_TEXT_2]". Show text first. Pink diagonal bar behind it. Large cropped close-up slides behind the letters.
CUT 10 | 8.40–9.40 | VELOCITY: Character rushes straight toward camera. Camera retreats. Passes close to lens. Coat creates a full-frame wipe. Strong speed ramp.
CUT 11 | 9.40–10.10 | INTERSTITIAL 03: Graphic card. Huge text: "[INTERSTITIAL_TEXT_3]". White letters on black. Bright pink circular field and technical rings. Small silhouette jumps across the letters with a sword-light streak.
CUT 12 | 10.10–12.20 | HERO MOMENT: Ultra-wide hero attack. Character descends and performs one powerful finishing slash. Huge glowing sword arc cuts the environment. Petals burst outward. Brief silence after impact. Lands elegantly and looks at camera with a confident smile.
CUT 13 | 12.20–15.00 | CHARACTER ID: Clean pale ivory background. Huge text: "[CHARACTER_NAME]". Show it clearly first. Then character overlaps it in a dynamic full-body hero pose. Behind: black circular emblem, symbol, ghosted sword-slash motif, concentric rings, technical arcs, halftone. Secondary text: "[SUBTITLE]". Final tiny text: "[STATUS_TEXT_1]". Slow push-in. Final sword glint and strong reveal stinger.

Editing: Hard cuts, freeze frames, graphic matches, whip pans, foreground wipes, speed ramps, silhouette transitions, impact flashes. Every cut must look different. Alternate between cute close-up, typography, action, typography, action, final card.
Avoid: Live-action realism, historical samurai style, long hair, gore, unreadable text, duplicate characters.
Music: Fast premium anime game-trailer score. Quiet digital intro, then electronic bass, fast percussion, impacts, sword whooshes, glitch ticks, and strong hit points on every typography cut. Biggest hit on CUT 12. Strong final stinger on CUT 13.
```

#### 📋 실전 영문 템플릿 3: 🌸 화산귀환 청명 전용 13-컷 리빌 트레일러 (Return of the Mount Hua Sect Version)
```text
MiniMax H3 Prompt — Mount Hua Sect Character Reveal
PARAMETERS:
CHARACTER_NAME = "CHUNGMYUNG"
STATUS_TEXT_1 = "PLUM BLOSSOM SWORD"
STATUS_TEXT_2 = "MODE: TAOIST BLADE"
INTERSTITIAL_TEXT_1 = "THE RETURN"
INTERSTITIAL_TEXT_2 = "MOUNT HUA SECT"
INTERSTITIAL_TEXT_3 = "TWENTY-FOUR BLOSSOMS"
SUBTITLE = "DIVINE DRAGON OF MOUNT HUA"
PROJECT_TEXT = "RETURN OF THE MOUNT HUA SECT"

Create a 15-second premium cinematic martial arts anime character reveal trailer with exactly 13 distinct cuts, 24fps. Use @image1 as the absolute authority for the character's identity, proportions, face, dark tied hair, white martial robes with crimson trim, and steel sword. Never redesign the character.

Style: Premium AAA martial arts anime game reveal trailer. Fast lethal swordsmanship mixed with bold oriental editorial motion graphics. Color Palette: Pure ink black, crisp white, fiery vermilion red, soft plum pink, and glowing golden sunset amber. Use oversized condensed typography, ink-wash brushstrokes, traditional plum blossom crests, calligraphic seals, diagonal split slices, swirling petals, and strong 2.5D foreground/background parallax. In text cuts, show the typography clearly first, then let Chungmyung overlap it or cross in front of it.

CUT 01 | 0.00–1.10s | FACE: Extreme cinematic close-up of 15yo Chungmyung. Sharp confident eyes, dark hair whipping in mountain wind, a few glowing pink plum petals drifting past lens. Slow intense push-in.
CUT 02 | 1.10–2.20s | DRAW: Close-up of single right hand gripping the steel sword hilt. Instant razor-fast unsheathe. Crisp metallic chime and a blinding pink-vermilion blade streak. Expression locks into cold focus.
CUT 03 | 2.20–3.20s | ACTIVE CARD: Bright white paper texture screen. Huge bold condensed text: "PLUM BLOSSOM SWORD". Show text clearly first, then Chungmyung enters in a classic Mount Hua sword stance overlapping the letters. Add vermilion circle seal, ink splatters, drifting petals.
CUT 04 | 3.20–4.10s | ENGAGE CARD: Ink-black graphic screen. Bold vermilion horizontal band with text: "MODE: TAOIST BLADE". Show text first, then Chungmyung's dark silhouette dashes across it with a massive diagonal pink blade streak.
CUT 05 | 4.10–5.20s | WORLD: Grand Mount Hua entrance gate and fiery crimson sunset cliffs. Chungmyung sprints forward at blinding speed across the stone courtyard. Low-angle dynamic tracking camera.
CUT 06 | 5.20–6.20s | SWORD ACTION: Medium close action shot. Chungmyung executes a rapid spinning crescent slash. Slender steel sword draws three luminous blade trails: white, pink, and vermilion. Fast short orbital whip.
CUT 07 | 6.20–6.90s | INTERSTITIAL 01: Text-led editorial screen. Huge typography: "THE RETURN". Show text first. Then add cropped macro close-up of his fierce eye and a full-body jumping silhouette with ink-wash brush wipes.
CUT 08 | 6.90–7.90s | IMPACT: Massive rock fragments burst forward. Chungmyung delivers a single clean horizontal strike, bisecting the stone cleanly into sharp fragments. Explosive pink-white plum blossom burst flash.
CUT 09 | 7.90–8.60s | INTERSTITIAL 02: Editorial text card. Huge typography: "MOUNT HUA SECT". Vermilion diagonal bar behind it. Large cropped profile of Chungmyung slides smoothly behind the letters for deep 2.5D parallax.
CUT 10 | 8.60–9.60s | VELOCITY: Chungmyung charges straight toward camera with drawn sword. Camera retreats rapidly. He passes inches from lens as his white robe sleeve creates a full-screen frame wipe. Strong speed ramp.
CUT 11 | 9.60–10.30s | INTERSTITIAL 03: Final graphic card. Huge text: "TWENTY-FOUR BLOSSOMS". White letters on dark ink wash. Large circular plum crest. Small Chungmyung silhouette leaps across the letters with an explosive petal streak.
CUT 12 | 10.30–12.30s | HERO MOMENT: Ultra-wide climax attack. Chungmyung descends from the sky delivering the signature Twenty-Four Plum Blossom finishing slash. Enormous glowing pink sword arc splits the frame, detonating a massive storm of pink plum blossoms. Lands with effortless grace and looks at camera with a triumphant, playful hero smirk.
CUT 13 | 12.30–15.00s | CHARACTER ID: Clean ivory rice-paper background. Huge bold text: "CHUNGMYUNG". Show text clearly first. Then Chungmyung overlaps it in a dynamic full-body martial hero stance. Behind him: large black ink-wash circular emblem, glowing plum blossom crest, and ghosted sword slash motif. Secondary text: "DIVINE DRAGON OF MOUNT HUA". Final text: "RETURN OF THE MOUNT HUA SECT". Slow push-in. Final blade glint and strong reveal stinger.

Editing: Hard cuts, freeze frames, ink-brush wipes, speed ramps, silhouette transitions, impact flashes. Every cut introduces a different dynamic angle. Alternate between sharp close-up, typography, action, typography, action, final ID card.
Avoid: Cyberpunk neon, futuristic sci-fi UI, robots, guns, western armor, gore, unreadable fonts, duplicate characters.
Music: Fast epic martial arts orchestral trailer score with heavy Taiko drums, traditional Korean/Asian strings (gayageum/erhu), explosive brass hits, sword whooshes, crisp metallic rings, and huge musical impacts synced to CUT 03, CUT 07, CUT 11, and CUT 12. Strong final gong/temple bell stinger on CUT 13.
```

### 4-3-2. 🌀 [모션그래픽 카테고리 3-2] Cia0 16초 무한 루프 2.39:1 시네마틱 스킬 쇼케이스 (Cia0 16s Seamless Loop Cinema Skill Showcase)

Cia0(@Cia0_exe)이 정립한 **"2.39:1 아나모픽 와이드스크린 + 16초 8-컷 완벽 무한 루프(Seamless Loop) + 10대 프로덕션 헌법 시스템"** 기법입니다. 단일 무기/스킬(예: 부채, 검, 창 등)을 중심으로 매 2초마다 컷이 전환되며, 종점(16초)의 마지막 정지 포즈와 잔여 광선이 시작점(0초)의 자세와 100% 오차 없이 맞물려 영원히 반복되는 최고급 시네마틱 쇼케이스입니다.

#### 💡 10대 프로덕션 헌법 시스템 (10-Constitution Architecture):
1. **[영상 총강 (Master Overview)]**: 16초 무한 루프, 2.39:1 아나모픽 시네마스코프 규격, 8K 렌더링, 코닥 5219 필름 그레인 12%, 청황(Teal-Orange) LUT, 매 2초 1회 전환, 카메라 최대 거리는 전신(Full Body)으로 제한하여 친밀감 유지.
2. **[색채 성경 (Color Bible)]**: 0~4s 축력(어두운 블루/골드), 4~10s 스킬 해방(화이트 코어 + 바이올렛/시안 그라데이션), 10~16s 수세 순환(실버/다크 그레이).
3. **[카메라 헌법 (Camera Constitution)]**: 8개 컷 전체의 렌즈/조리개/무빙 1:1 고정 (1: 트랙 미세 푸시 40mm T2.8 ➔ 2: 스테디캠 로우 상승 50mm T2.0 ➔ 3: 트랙 급속 패닝 35mm T2.8 ➔ 4: 핸드헬드 어깨 50mm T1.8 ➔ 5: 지미집 상승 28mm T4.0 ➔ 6: 트랙 360 오비팅 40mm T2.0 ➔ 7: 핸드헬드 급속 전진 50mm T1.8 ➔ 8: 절대 정지 50mm T8.0).
4. **[에너지 오라 성경 (Aura Bible)]**: 캐릭터 반경 1.2m 구형 범위 내로 에너지 락온, 0.25초 펄스 주기, 무기와의 1:1 물리 인터랙션(전개 시 방사 ➔ 휘두를 때 잔상 ➔ 접을 때 코어 응축).
5. **[타이포그래피 헌법 (Typography Constitution)]**: 스킬 전개 시 3D 공간에 0.2~0.5초간 한자/영문이 떠오르며 전방/후방으로 입체 비산, 종점에는 거대 메인 타이틀 + 서브타이틀 안착.
6. **[사운드 디자인 헌법 (Sound Constitution)]**: BGM 100% 금지, 4계층 폴리 사운드(환경음 -45dB, 동작/옷자락 -20dB, 스킬/이펙트 -12dB, 음성/기합 -8dB), 스킬 절정 시 1초 절대 침묵(Absolute Silence)으로 긴장감 극대화.
7. **[환경 파괴 누적 시스템 (Environmental Damage Accumulation)]**: 1컷부터 7컷까지 검격/번개가 바닥에 남긴 균열(Crack), 그을음(Scorching), 파편(Debris)이 사라지지 않고 8컷까지 계속 누적되어 사실감 극대화.

#### 📋 Cia0 원본 마스터 프롬프트 (Original Chinese Master):
```text
Prompt MiniMax H3: [影片总纲] 电影级角色技能展示动画，总时长严格16秒无缝循环loop，画幅比2.39比1变形宽银幕电影规格，无背景音乐，仅角色动作音效与技能音效，8K电影级写实渲染，光线追踪全局光照，体积雾散射，皮肤次表面散射，Kodak 5219胶片颗粒12%，Halation光晕6%，镜头呼吸效应，变形宽银幕镜头椭圆散景与水平拉丝眩光，色彩空间Rec.709带电影级青橙LUT，对比度S型曲线暗部提升12%高光压缩8%，阴影偏青高光偏金，黑位纯净不浮灰。全程聚焦角色主技能「[SKILL_NAME]」，以[WEAPON]为核心武器，动作优雅凌厉不重复，每2秒一次平滑镜头转场，禁止任何旋转场景，禁止远景大全景，摄影机最远不得超过角色全身full body，loop终点无缝衔接起点形成永恒循环。

[色彩圣经] 阶段一蓄力起势0至4秒，暗室幽蓝主调(#0A1628)，角色衣白描金(F5F5DC/DAA520)，折扇靛蓝(1E3A5F)，闪电冰蓝(00BFFF)，暗部纯黑(0A0A0A)。阶段二技能释放4至10秒，闪电核心炽白(FFFFFF)，电弧冰蓝渐变紫(#00BFFF至#8A2BE2)，扇面展开虹彩反光，衣袂飘飞金边，Typography金光(#FFD700)。阶段三收势循环10至16秒，余电幽蓝微光(1E3A5F)，扇骨金属冷银(C0C0C0)，暗部青黑(0F1B2E)，终幕Typography金属银灰(C0C0C0)。

[角色档案] @image1
技能主体：[CHARACTER_DESCRIPTION]。手持[WEAPON]，周身环绕[ELEMENT_AURA] aura，脉冲式爆发间隔0.25秒。

[分镜脚本 — 16秒无缝loop]
镜1，0至2秒，中景全身起势蓄力。机位轨道车微推，40毫米，T2.8，高度齐腰，平视微仰8度。
镜2，2至4秒，近景扇面初展。机位斯坦尼康低角度上升，50毫米，T2.0，仰角15度起升至平视。
镜3，4至6秒，中景扇舞横斩。机位轨道车急速横移，35毫米，T2.8，高度齐胸，平视。
镜4，6至8秒，近景扇花连击。机位手持肩扛微晃，50毫米，T1.8，极浅景深，高度齐肩，微俯5度。
镜5，8至10秒，全景跃起扇旋。机位摇臂微升，28毫米广角，T4.0，低角度仰拍30度。
镜6，10至12秒，中景收扇蓄力。机位轨道车环绕，40毫米，T2.0，高度齐腰，环绕速度每秒30度。
镜7，12至14秒，近景终极扇闪。机位手持急速前冲，50毫米，T1.8，极浅景深，高度齐胸。
镜8，14至16秒，终幕循环衔接Typography Art。机位绝对静止，50毫米，T8.0全清晰，无任何运动。Loop终点与镜1起势姿态完全一致形成无缝loop。

[摄影机宪法] 画幅比严格2.39比1变形宽银幕。每镜时长严格2秒，转场使用光学溶解叠化或无缝运动匹配衔接。景深特写T1.8极浅，中景T2.0至T2.8，全景T4.0。Loop终点镜8必须与镜1起势姿态完全一致。
[环境破坏累积系统] 技能释放过程中环境持续受损且不可恢复，破坏痕迹在后续镜头中持续可见，终幕镜8中所有痕迹发出微弱余光与角色呼吸同步明灭。
[声音设计宪法] 绝对禁止背景音乐。仅使用角色动作音效与技能音效，分层混音。
```

### 4-3-3. ⚔️ [모션그래픽 카테고리 3-3] 6-이미지 앙상블 애니메이션 오프닝 타이틀 시퀀스 (6-Image Ensemble Anime Opening Title Sequence)

6장의 이미지 레퍼런스(`Image1`~`Image6`)와 오디오 트랙(`Audio1`)을 바인딩하여 15초 동안 **3명의 캐릭터 솔로 파트(각 3초) ➔ 3인 앙상블 삼각형 구도 ➔ 고속 비트 교차 클로즈업 ➔ 최종 메인 타이틀 안착**으로 이어지는 정통 일본 애니메이션 오프닝 시퀀스 공식입니다.

#### 💡 4대 프로덕션 설계 메커니즘:
1. **6대 이미지 레퍼런스 1:1 역할 분담 바인딩 (`[REFERENCE ROLES]`)**:
   - `Image 1, Image 2, Image 3`: 전체 비주얼, 앙상블 및 컬러 스타일 참조
   - `Image 4`: 제1 캐릭터 (예: 핑크 헤어 검객 여성, 1.5~4.3s 솔로 샷)
   - `Image 5`: 제2 캐릭터 (예: 레드 헤어 검객 여성, 4.3~7.2s 솔로 샷)
   - `Image 6`: 제3 캐릭터 (예: 블랙 헤어 검객 여성, 7.2~10.2s 솔로 샷)
2. **오디오 1:1 비트 동기화 시퀀스 플로우 (Audio-Synced Sequence Flow)**:
   - `0.0–1.5s [비트 오프닝]`: 진홍색 선이 검정을 가르며 꽃잎과 파편 폭발, 그래픽 패널 스냅, 붉은 달 조립
   - `1.5–4.3s [캐릭터 1 솔로]`: 프레임 돌진 ➔ 카타나 발도 ➔ 트래킹 푸시인 ➔ 눈/손/칼날 비트 컷
   - `4.3–7.2s [캐릭터 2 솔로]`: 로우 앵글 트래킹 ➔ 강력한 검 동작 ➔ 휘날리는 머리칼/도포 ➔ 붉은 태양 디스크와 패널 충돌
   - `7.2–10.2s [캐릭터 3 솔로]`: 귀걸이/눈 클로즈업 ➔ 360도 오비팅 회전 ➔ 흐르는 머리칼/소매 ➔ 달 모양 마스크 컷
   - `10.2–12.7s [3인 앙상블 피크]`: 3인 동시 입장 ➔ 강력한 삼각형 구도 형성 ➔ 붉은 달과 사찰 지붕 배경 정렬
   - `12.7–15.0s [피날레 & 타이틀 안착]`: 3인 고속 클로즈업 번갈아 교차 ➔ 최종 히트에 대각선 마스크/검 선 와이프로 메인 타이틀 드러내기 ➔ 3인 앙상블 여운 엔딩
3. **단일 샷 캐릭터 중복 0% 락 (`Strict No Duplicate Rule`)**:
   - 한 샷에 동일 캐릭터의 복제본/레이어드 분신을 절대 금지하고, 오직 단독 샷 또는 3인 자연스러운 앙상블만 허용.
4. **비트 동기화 하드 트랜지션 (Beat Transitions)**:
   - 슬래시 컷, 각진 패널 스냅, 달 마스크 와이프, 꽃잎 줄무늬, 찢어진 종이 셔터, 잉크 임팩트 컷. (부드러운 디졸브/페이드 엄격 금지).

#### 📋 실전 마스터 프롬프트 (Universal English & Korean Version):
```text
Create a fast-paced 15-second, 16:9 anime opening title sequence for an original series titled "[TITLE_NAME]". Use @image1, @image2, @image3 as the overall visual, ensemble, and color style reference. Use @image4 as [CHARACTER_1_DESCRIPTION], @image5 as [CHARACTER_2_DESCRIPTION], and @image6 as [CHARACTER_3_DESCRIPTION]. Preserve each character's face, hairstyle, outfit, proportions, colors, and weapon designs exactly.

Use the provided audio @audio1 as the exact timing reference. Synchronize every cut, character action, camera movement, graphic transition, and title reveal with the beats, accents, fills, build-ups, and final hits. Do not create a separate soundtrack. Only add subtle sword whooshes, cloth movement, and transition impacts beneath the reference audio.

VISUAL STYLE:
Authentic high-energy anime opening combined with premium motion graphics. Use pure black, crimson red, wine red, dusty pink, light ivory, and cool slate blue. Combine angular split screens, diagonal masks, torn paper shapes, manga-style framing, ink textures, petals, crimson moon shapes, torii silhouettes, temple roofs, and razor-sharp graphic lines.
Keep the sequence kinetic and fully animated. Not a slideshow. Characters must run, turn, pivot, slide, draw swords, shift stances, and react to momentum. Hair and clothing must maintain continuous motion. Use tracking shots, whip pans, fast push-ins, low angles, and short camera orbits.
Strictly never show multiple copies of the same character in a single shot. Shots can show one character alone or all three characters together naturally. No clone effects, repeated character pieces, or layered duplicates.

SEQUENCE FLOW:
- [0.0–1.5s]: Open immediately on the first beat. Crimson line slices through black as petals and white fragments burst outward. Pink, red, and black graphic panels snap into place while a crimson moon rapidly assembles in the background.
- [1.5–4.3s]: Spotlight @image4 alone. Runs into frame, plants a foot, turns, and draws sword in one continuous agile motion. Track beside then push into face. Cut between eyes, hand, blade, and full-body movement on audio accents. Use pink petals, red lines, and diagonal panel cuts.
- [4.3–7.2s]: Transition to @image5 on a strong musical hit. Low-angle tracking shot as moving forward, pivoting, and executing powerful controlled sword motions. Long hair and robes billowing in momentum. Large crimson sun disc behind with black-red panels slamming into frame on heavier beats.
- [7.2–10.2s]: Spotlight @image6 alone. Begins with moving close-up of earring and eyes, then orbit as turning, shifting stance, and redirecting blade. Hair and sleeves flowing continuously. Use dark negative space, moon-shaped masks, and precise cuts synchronized to rhythmic details.
- [10.2–12.7s]: Reveal all three characters in one shared scene at major musical peak. Enter through real motion forming a strong triangle composition. Fast camera push or short orbit while crimson moon, torii silhouettes, petals, and graphic debris align behind them. Show each character once.
- [12.7–15.0s]: Rapidly alternate very short moving close-ups of all three characters during final phrase. One character per shot: turning eyes, sword grip, flowing hair, or blade catching light. On final major hit, reveal "[TITLE_NAME]" title through sharp diagonal mask, sword line wipe, and fractured graphic panels.
End on clean ensemble composition of all three characters together with subtle motion on hair, clothes, petals, and light reflections.

TRANSITIONS:
Beat-synchronized slash cuts, angular panel snaps, moon mask wipes, petal streaks, torn paper shutters, ink impact cuts, foreground wipes, and oversized title masks. Strictly no soft dissolves, slow fades, liquid morphing, or random transitions.

TYPOGRAPHY:
Use only title "[TITLE_NAME]". Keep sharp, elegant, premium, and fully readable. No credits, extra text, random symbols, or broken lettering.

FINAL RESULT:
Fast, polished, and rhythmically precise anime opening with expressive character movement, strong graphic editing, strict visual consistency, and zero duplicate characters in the same shot.
```

### 4-3-4. ⚡ [모션그래픽 카테고리 3-4] Cia0 15초 뇌인(雷刃) 무한 루프 & 2.5D 홀로그램 한자 타이포그래피 (Cia0 15s Thunder Blade Seamless Loop & 2.5D Holographic Kanji Typography)

Cia0(@Cia0_exe)이 정립한 **"15초 16:9 2000p 24fps 무한 루프 + 해부학 결함 완벽 락온(Anatomy Lock) + 2.5D 홀로그램 한자 타이포그래피 시스템"** 기법입니다. 단일 캐릭터가 번개 검술(雷刃)을 연속 시전하며, 스킬 절정 순간마다 반투명 크리스털 한자(「斬」「雷」「瞬」「殺」「極」 등)가 3D 공간에 떠오르고, 마지막 프레임이 시작 프레임으로 완벽하게 맞물리는 최상급 액션 PV 공식입니다.

#### 💡 5대 핵심 프로덕션 기술:
1. **[해부학 락온 · 최고 우선순위 (Anatomy Lock)]**:
   - `[解剖锁定 · 最高优先级]`: 전체 영상 단 1명의 인물, 2개 팔, 2개 손, 각 손 5개 손가락 고정. 번개 잔상과 모션블러가 여분의 신체(팔/손가락)로 렌더링되는 AI 다지증/다완증 결함을 100% 원천 차단.
2. **[2.5D 홀로그램 크리스털 타이포그래피 (2.5D Holographic Kanji Typography)]**:
   - 스킬 시전 순간마다 무작위 한자(「斬」「雷」「瞬」「殺」「閃」「破」「極」「滅」 등 1~3자)가 캐릭터 뒤나 참격 궤적 위에 반투명 크리스털 재질 + 프리즘 무지개 굴절로 2.5D 부유 ➔ 유리 깨지는 사운드와 함께 소멸.
   - 마지막 종료 프레임에 중앙 하단 "Cia0 X H3" 스프레이 폰트 안착.
3. **[체적광 번개 렌더링 (Volumetric Ray-Marched Lightning)]**:
   - 단순 2D 이펙트가 아니라 가우스 체적 안개(Gaussian Volumetric Fog) + 레이마칭(Ray-marching)으로 공기 이온화 발광과 주변 환경 그림자를 실시간 연산.
4. **[2초 단위 하드 카메라 시퀀스 (No 360 Spin, 2s Transitions)]**:
   - 360도 회전 금지, 트랙 푸시/슬라이드/단시간 블랙페이드로 매 2초마다 1개 컷씩 전개:
     - `0.0–2.0s`: 100mm 매크로 (손과 칼자루, 번개 지직거림, 눈빛 치켜뜸)
     - `2.0–4.0s`: 24mm 광각 로우앵글 (순보 돌진, 도포 휘날림, 잔상 폭발)
     - `4.0–6.0s`: 50mm 사이드 (대도 횡참, 번개 궤적, 타이포 「斬」 부유)
     - `6.0–8.0s`: 85mm 미디엄 (착지 단슬 착지, 칼끝 지면 삽입, 번개 균열, 타이포 「雷」 부유)
     - `8.0–10.0s`: 35mm 정면 (납도 0.5s 후 발도 거합참, 십자 섬광, 타이포 「瞬」「閃」 교차)
     - `10.0–12.0s`: 24mm 광각 로우 (공중 도약 대기둥 낙뢰, 전신 뇌전 영역, 타이포 「極」 거대화)
     - `12.0–14.0s`: 100mm 매크로 (슬로우모션 납도, 쇳소리 스파크, 살기 수렴)
     - `14.0–15.0s`: 40mm 고정 (동공 전격 잔광 + 타이포 안착 ➔ 0.0s 시작 프레임으로 100% 일치 루프)
5. **[완벽한 무한 루프 (Seamless Loop)]**:
   - 14~15초의 마지막 프레임이 0초의 첫 프레임과 시선, 검 자세, 번개, 불씨 위치까지 100% 동일하게 일치하여 영원히 무한 반복.

#### 📋 Cia0 15초 뇌인 무한루프 원본 마스터 프롬프트 (Chinese Master):
```text
Prompt MiniMax H3: 15秒 | 16:9 | 2000p | 24fps | 无缝循环 | 无配乐仅角色音效
[角色锁定] 完全按照参考图呈现，不重新设计。银白长发与漆黑长发左右对半 split，发丝狂乱飞扬带真实风力物理。冰蓝色双眼锐利如刀，浓重青蓝眼影与深红唇色，眼神充满杀气与专注。面部左侧有深色裂纹状纹身延伸至颈部。头饰为巨大眼球状骨质发饰与金属圆片，悬挂绳结流苏。身着深蓝底日式和服铠甲，肩甲与护腕镶嵌风化骷髅与骨质尖刺，和服上有黄色枫叶与暗红花纹。双手握持一柄武士大刀，黑色缠绳刀柄，圆形锷，刀身修长泛寒光。左手缠绕暴走蓝色闪电，电弧噼啪炸裂照亮半张脸。全片不得改动发型分色、妆容深浅、纹身位置、头饰结构、铠甲骷髅数量与和服花纹。

[解剖锁定 · 最高优先级] 全片仅一名人物：两条手臂两只手每只手五指，手指关节因握刀用力而青筋凸起。严禁多余手臂手掌手指。闪电残影与运动模糊绝不可渲染成额外肢体。

[武器与能力设定 · 雷刃] 她是大刀与雷电的化身。刀身常态泛冷冽银白寒光，每次挥斩时刀刃缠绕高密度蓝色闪电，拖出长达数米的电弧残影。雷电不是贴图，而是真实体积光渲染，具备枝状分叉、核心亮白边缘冰蓝的物理特征，照亮周围环境并产生真实阴影。她能在任意位置瞬身突进，原地留下一道由闪电粒子构成的残像，残像延迟0.3秒后炸裂为放射状电弧。大招时全身爆发球形雷电领域，领域内地面龟裂，碎石悬浮并被电离成发光粒子。

[Typography 系统 · 全息2.5D] 每次释放技能瞬间，画面强制切入一组随机日本汉字或片假名，以全息2.5D形式悬浮于角色身后或斩击轨迹上。字体风格为狂放毛笔书法或锐利哥特体，材质为半透水晶带全光谱虹彩折射，厚度可见，边缘有锯齿状光衍射。文字内容随机变化：「斬」「雷」「瞬」「殺」「閃」「破」「極」「滅」「嵐」「牙」等，每次出现1至3个字，伴随技能节奏同步闪现与消散，绝不固定重复同一组字。文字出现时有玻璃碎裂般的清脆音效对应。最终结束帧画面中央锁定喷漆体白色文字 "Cia0 X H3"，带虹彩描边与轻微overspray颗粒，位置比例固定于画面中心偏下。

[场景] 荒废的日式神社战场，地面龟裂焦黑，散落断裂鸟居与风化石灯笼。背景有燃烧的红色鸟居框架与飘落的灰烬。天空为暴风雨前的铅灰色，云层中隐约滚动闷雷。环境光主要来自她身上的蓝色闪电，形成强烈的冷暖对比——闪电的冷蓝照亮前景，背景的暗红余烬提供微弱补光。整体影调电影级，高对比，胶片颗粒细腻。

[循环核心] 完美闭环，最后一帧必须与第一帧完全一致：她的握刀姿态、闪电缠绕状态、眼神角度、背景火星位置完全相同。故事是她不断重复一套华丽连斩，从起手到收刀入鞘，再瞬间回到起手姿态，永恒循环。首尾帧差异必须小于人眼可辨识阈值。

[色彩] 主色调为闪电的冰蓝#00D4FF与刀光的银白#E0F7FF，辅助色为和服的深蓝#1A237E与暗红#B71C1C。雷电核心纯白，边缘向冰蓝过渡，最外层有极淡的紫晕。全息文字虹彩色散仅作为折射光存在，绝不平涂。整体画面模拟35mm胶片，暗部偏冷蓝，高光带轻微青调，颗粒细腻。

[风格与质感] 2.5D动画电影级，赛璐璐角色线条配合真实雷电体积渲染。和服布料有真实褶皱与飘动物理，铠甲骷髅有风化磨损质感。雷电使用高斯体积雾配合光线步进渲染，产生真实的空气电离发光。刀锋使用各向异性高光，挥斩时有动态模糊拖尾。

[特效 · 持续雷电] 全片闪电效果永不中断：刀身常驻低频电弧缠绕；她呼吸时胸口有微弱的电荷粒子起伏；每次眨眼眼睑边缘闪过极细的电丝。突进时身后拉出由闪电粒子构成的直线轨迹，轨迹持续1.2秒后衰减。格挡时刀身前方生成六边形蜂窝状雷电护盾，护盾表面有能量流动。大招瞬间天空降下数道落雷击中刀尖，落雷照亮整个场景，产生强烈的明暗反差与条状光斑。

[摄影 · 每2秒平滑转场] 严禁360度环绕或旋转镜头。每2秒一次平滑转场，使用快速推轨、甩镜、或极短黑屏切换，保持战斗节奏凌厉。 0.0-2.0秒 100mm微距，刀柄与她紧握的左手，闪电在指缝间游走，眼神从画面下方锐利抬起。 2.0-4.0秒 24mm广角低角度，她瞬身突进，和服下摆飞扬，身后闪电残像炸裂，镜头跟随她的运动方向急速平移。 4.0-6.0秒 50mm侧面，大刀横斩，刀刃闪电拖出弧形光轨，Typography「斬」字在斩击顶点全息浮现。 6.0-8.0秒 85mm中景，她落地瞬间单膝跪地，刀尖插入地面，雷电从刀尖向四周龟裂蔓延，Typography「雷」字从地面裂缝中升起。 8.0-10.0秒 35mm正面，她收刀入鞘0.5秒后又瞬间拔刀，居合斩的刀光与闪电形成十字闪光，Typography「瞬」与「閃」双字交叉浮现。 10.0-12.0秒 24mm广角仰拍，她跃起大招，全身雷电领域爆发，天空落雷汇入刀身，Typography「極」字巨大化笼罩全身。 12.0-14.0秒 100mm微距，收刀归鞘的慢动作，刀锷与鞘口碰撞溅起细小电火花，她嘴角微微上扬，眼神杀气收敛。 14.0-15.0秒 40mm定机位，画面渐暗只剩她眼中电光与中央 "Cia0 X H3" 喷漆文字。
```

### 4-3-5. 🗡️ [모션그래픽 카테고리 3-5] 15초 여성 사무라이 공중 참격 & 히어로 리빌 쇼케이스 (15s Female Samurai Aerial Multi-Slash Hero Reveal)

**"0~2s 칼날 매크로 풀백 ➔ 2~5s 손목 회전 검세 ➔ 5~8s 표적 공중 투척 ➔ 8~12s 공중 도약 3연속 쾌속 절단 ➔ 12~14s 지면 착지 ➔ 14~15s 은은하고 당당한 미소(Satisfying Smirk)"**로 이어지는 15초 단편 애니메이션 액션 쇼케이스의 교과서적인 마스터 템플릿입니다.

#### 💡 6대 핵심 연출 및 샷 흐름:
1. **`0–2s [칼날 매크로 오프닝]`**: 화면 전체를 강철 칼날이 채우며 시작 ➔ 서서히 풀백하며 칼날 뒤 매서운 한쪽 눈 ➔ 얼굴과 상체 공개 (침착, 집중, 위압적인 자신감).
2. **`2–5s [히어로 스탠스 & 손목 회전]`**: 로우 앵글 미디엄 샷 풀백 ➔ 섬세한 손목 스냅 회전으로 방어 검세 ➔ 360도 짧은 오비팅으로 측면에서 정면 히어로 구도로 안착.
3. **`5–8s [타깃 투척 & 슬로우모션 틸트업]`**: 손목 클로즈업 ➔ 목각 표적/나뭇잎을 공중으로 투척 ➔ 슬로우모션으로 허공을 추적하는 눈빛.
4. **`8–12s [공중 도약 연속 절단]`**: 수직 공중 도약 ➔ 로우 앵글 트래킹으로 허공의 표적들을 하나씩 쾌속 참격 분쇄 (스피드 램핑, 극도로 깨끗한 검호, 미세 파편 비산).
5. **`12–14s [전사 착지]`**: 지면 단단한 착지 ➔ 미세한 흙먼지와 꽃잎 버스트 ➔ 머리카락/옷자락의 자연스러운 관성 2차 모션.
6. **`14–15s [최종 히어로 샷]`**: 카메라 슬로우 푸시인 ➔ 정면을 응시하며 은은하고 여유로운 승리의 미소(Quiet Flawless Confidence) ➔ 꽃잎이 렌즈 앞을 스치며 엔딩.

#### 📋 영문 마스터 프롬프트 (Universal English Master Prompt):
```text
Create a 15-second cinematic anime action sequence featuring a beautiful, confident young female samurai warrior.

The visual identity should feel premium, dramatic, elegant, and highly polished, blending modern high-quality anime aesthetics with a traditional Japanese samurai atmosphere.
Her character design is a major visual focus: striking expressive eyes, flowing dark hair, elegant but battle-ready samurai attire, layered fabric, subtle armor elements, a detailed obi belt, traditional Japanese styling, and a refined silhouette.

ENVIRONMENT:
A serene Japanese-inspired courtyard or forest clearing during golden-hour dusk, with warm cinematic light filtering through the trees. Include soft atmospheric haze, small floating flower petals, delicate leaves moving naturally through the air, rich environmental depth, and warm golden light.

SEQUENCE FLOW:
- [0–2s | SWORD-TO-CAMERA OPENING]: Start extremely close to the katana blade, positioned directly in front of the camera so the polished steel dominates and almost entirely covers the frame. The blade catches a sharp glint of light. Keep background heavily blurred. Slowly pull the camera backward from the blade, revealing one of her intense eyes behind the sword, then gradually revealing her face and upper body (calm, focused, intimidatingly confident).
- [2–5s | HERO REVEAL]: Continue the smooth camera pullback into a dynamic low-angle medium shot of the samurai girl standing in a powerful sword stance. She performs a subtle, controlled katana movement: quick wrist rotation, precise defensive pose. Hair, ribbons, and clothing move naturally. Brief orbiting camera movement transitioning from side profile into a frontal hero composition.
- [5–8s | PREPARATION]: Cut to a fast close-up of her hand gripping the katana. She suddenly reaches down, grabs several small lightweight wooden practice pieces and leaves, and throws them upward into the air. Short slow-motion shot as objects rise above her. Camera tilts upward following trajectory as her eyes track objects with absolute precision.
- [8–12s | MID-AIR SWORD SEQUENCE]: Without hesitation, she launches herself vertically into the air. Switch to dramatic low-angle tracking shot looking upward following her jump against sky and drifting petals. While airborne, she performs a rapid sequence of precise katana strikes, cutting through each airborne object one after another. Dynamic camera choreography: quick side-tracking, brief speed ramps during strikes, subtle motion blur, extremely clean sword arcs, tiny scattering fragments.
- [12–14s | WARRIOR LANDING]: As the final object splits apart, she descends. Cut to dramatic ground-level side angle as she lands in a powerful stance. Foot hits ground creating subtle burst of dust, scattering flower petals, and natural secondary movement in flowing clothing and hair. Holds katana confidently beside her.
- [14–15s | FINAL HERO SHOT]: Immediately transition into a slow cinematic push-in toward her face. She slowly raises eyes toward camera and gives a subtle, confident, satisfying smile communicating flawless mastery. A final flower petal gently passes across foreground. End on powerful anime hero frame.

VISUAL & CINEMATIC DIRECTION:
Premium modern anime quality, highly detailed character rendering, expressive eyes, refined facial animation, flowing hair and fabric physics, cinematic depth of field, dramatic golden-hour lighting, polished sword reflections, and smooth transitions between slow motion and real-time movement.
Strictly zero dialogue, zero text, zero subtitles, zero watermark.
```

### 4-4. 🌸 [모션그래픽 카테고리 4] 핑크 머티리얼 키네틱 타이포 MV (Pink Material Kinetic Typography MV)

실사 영화 + 하이패션 광고 + 3배속 키네틱 타이포그래피가 결합된 9개 씬(9-Scene) 형태의 초고속 뮤직비디오 프롬프트입니다. **"글자를 2D 자막이 아닌 9가지 물리 재질(연기, 네온, 크롬, 식물, 전기, 그림자, 종이, 리본, 동공 네온)로 실체화"**하는 최고급 물리학 연출 기법입니다.

#### 💡 9대 물리 재질 타이포그래피 변환 공식 (9 Material Typographic Manifestations):
1. **`Scene 1: 연기 (Smoke)`** $\rightarrow$ 손바닥에서 피어오른 흰 연기가 소용돌이치며 조립: `"FREE YOUR MIND"`
2. **`Scene 2: 네온 라이트 (Neon Line)`** $\rightarrow$ 손가락 궤적을 따라 한붓그리기 점등 + 180도 오비팅: `"LIGHT YOUR OWN WAY"`
3. **`Scene 3: 액체 크롬 (Liquid Chrome)`** $\rightarrow$ 손바닥 위에서 은색/핑크 액체금속이 늘어나고 뒤틀림: `"BECOME WHO YOU CHOOSE"`
4. **`Scene 4: 유기농 식물 덩굴 (Botanical Bloom)`** $\rightarrow$ 바닥에서 싹이 자라나 벽을 타오르며 만개: `"LET YOUR FUTURE BLOOM"`
5. **`Scene 5: 전기 에너지 (Electrical Flare)`** $\rightarrow$ 손끝 사이에서 핑크빛 스파크가 방사형으로 연결: `"POWER YOUR CHOICE"`
6. **`Scene 6: 그림자 분신 (Shadow Anamorphic)`** $\rightarrow$ 인물과 다르게 움직이는 거대한 그림자가 변형: `"STEP INTO YOUR STORY"`
7. **`Scene 7: 페이퍼 아트 (Origami Paper Flip)`** $\rightarrow$ 떠오르는 종이 조각들이 접히고 페이지 넘기듯 반전: `"TURN THE PAGE"`
8. **`Scene 8: 핑크 리본 (Ribbon Spiral Orbit)`** $\rightarrow$ 등 뒤에서 뻗어 나온 리본이 360도 나선형으로 휘감김: `"LIVE BY YOUR RULES"`
9. **`Scene 9: 동공 네온 터널 (Iris Infinite Tunnel)`** $\rightarrow$ 눈동자 홍채 속 네온 발광 $\rightarrow$ 무한 심도 터널로 흡수: `"CHOOSE YOUR LIFE"`

#### 📋 프롬프트 설계 핵심 규칙 (Prompt Construction Rules):
* **`배색 한정 (Color Constraint)`**: 딥 핑크(Deep Pink), 마젠타(Magenta), 블랙(Black), 화이트(White) 중심의 정밀한 하이패션 무드
* **`신체 동기화 (Body-Motion Sync)`**: 인물의 시선, 손바닥, 손가락 궤적에 맞춰 타이포그래피가 물리적으로 발생·변형·이동
* **`정확한 철자 락 (Spelling Legibility Lock)`**: 고속 모션 중에도 각 문구가 최소 1번은 100% 온전하게 읽히도록 강제

### 4-5. ♾️ [모션그래픽 카테고리 5] 스위스 에디토리얼 무한 루프 모션 디자인 (Swiss Editorial Geometric Morph & Infinite Loop)

**"하나의 단어에서 거대한 도시로, 다시 하나의 단어로" (From a Word to a World)** 회귀하는 완벽한 9:16 무한 루프(Seamless Infinite Loop) 최고급 브로드캐스트 모션그래픽 프롬프트입니다.

#### 💡 기하학적 모핑 & 매치 컷 7단계 변환 순환 아크 (7-Stage Morphing Arc):
1. **`0.00–1.40s: TYPE HOOK`** $\rightarrow$ 암흑 속 코발트 커서 깜빡임 $\rightarrow$ 7글자 `"imagine"` 한 자씩 타이핑 + 코발트 펄스
2. **`1.40–3.10s: DOT TO SUN`** $\rightarrow$ 첫 글자 `"i"` 위의 점(dot)으로 급가속 $\rightarrow$ 동심원 확장 $\rightarrow$ 앰버색 태양(Sun Disc)으로 모핑
3. **`3.10–5.20s: SUN TO LENS`** $\rightarrow$ 코로나가 회전 광학 링으로 재배치 $\rightarrow$ 카메라 조리개 렌즈 날개(Aperture Blades) 매치 컷 개폐
4. **`5.20–6.70s: LENS TO IRIS`** $\rightarrow$ 중심축 고정 $\rightarrow$ 조리개 날개가 방사형 코발트 홍채/동공(Stylized Iris)으로 부드럽게 변형
5. **`6.70–10.70s: IRIS TO WORLD`** $\rightarrow$ 동공 관통 급가속 $\rightarrow$ 홍채 라인이 그래픽 터널 $\rightarrow$ 아치 $\rightarrow$ 다리 $\rightarrow$ 타이포그래픽 건축물 도시(Surreal Graphic City)로 확장 비행
6. **`10.70–13.30s: WORLD TO WORD`** $\rightarrow$ 도시 상공으로 상승 $\rightarrow$ 건물들이 글자 획(Stems)으로 납작해지고 다리가 곡선으로 정렬 $\rightarrow$ 다시 7글자 `"imagine"`으로 압축, 앰버 태양은 `"i"`의 점으로 수축
7. **`13.30–15.00s: PERFECT LOOP`** $\rightarrow$ 역순으로 7글자가 지워지며 0.00초의 시작 프레임(코발트 커서)과 100% 동일하게 일치하며 무한 반복 루프 완성

#### 🎨 스위스 에디토리얼 모션 디자인 4대 법칙 (Swiss Motion Rules):
* **`색상 엄격 제한 (Palette Lock)`**: 퓨어 블랙(Black Background), 루미너스 화이트(Luminous White), 일렉트릭 코발트(Electric Cobalt), 레스트레인드 앰버(Restrained Amber) 단 4색만 허용 (보라색 네온/난잡한 파티클 엄격 차단)
* **`중심축 일치 (Center-Axis Alignment)`**: 모든 원형 오브젝트(점 $\rightarrow$ 태양 $\rightarrow$ 렌즈 $\rightarrow$ 조리개 $\rightarrow$ 홍채 $\rightarrow$ 터널)가 단 하나의 중앙 좌표를 공유하여 흔들림 없는 완벽한 형태 매치 컷(Shape-based Match Cut) 구현
* **`스펠링 락 (Spelling Lock)`**: 정확한 소문자 7글자 `"i-m-a-g-i-n-e"` 철자 붕괴 원천 차단

### 4-6. 👟 [모션그래픽 카테고리 6] 핸드페인팅 팝아트 멀티패널 분할 커머셜 (Hand-Painted Pop-Art Multi-Panel Commercial)

미드저니 임파스토/구아슈 스타일(`--sref 1661176918`)의 5장 제품 일러스트와 솔 바스(Saul Bass) 그래픽 모션 디자인을 결합한 15초 16:9 초고속 스니커즈 상업 광고(Commercial) 기법입니다.

#### 💡 성공의 핵심 기법 (Multi-Panel Living Grid System):
1. **5대 레퍼런스 역할 1:1 바인딩 (`[REFERENCE ROLES]`)**:
   - `Image 1`: 메인 히어로 제품 실루엣 (3/4 회전 앵글, 코랄 핑크 배경, 핑크 신발끈)
   - `Image 2`: 4가지 컬러웨이 워킹 앙상블 (메리골드 옐로우 바닥, 보폭 리듬)
   - `Image 3`: 쉘토(슈퍼스타 스타일) 실루엣 (레드 신발끈, 프로필 앵글)
   - `Image 4`: 착용 발목 디테일 (스트라이프 양말, 리본 묶음 클로즈업)
   - `Image 5`: 글로시 페이턴트 매크로 디테일 (두터운 유화 브러시 질감)
2. **다중 분할 화면 격자 시스템 (`Living Grid Split-Screen`)**:
   - 풀프레임 정지컷을 배제하고, **2분할(2-Up), 3분할(3-Up) 멀티 패널이 찰나의 비트마다 쪼개지고, 슬라이드되고, 회전하며 격돌(Split, Slide, Spin, Stutter, Slam)**.
3. **9단계 초고밀도 액트 타임라인 (Dense Action Timeline)**:
   - `0.0–0.6s`: 3패널 분할 플래시 그리드 (Image 5 + Image 1 디테일이 한 방에 등장)
   - `0.6–1.2s`: 패널 푸시 슬라이드 (3개 패널이 중앙으로 쾅 충돌하며 히어로 제품 착지)
   - `1.2–1.8s`: 스트로보스코픽 프리즈 스터터 (2회 연속 깜빡임 정지 잔상)
   - `1.8–3.0s`: 대각선 레이저 슬라이스 와이프 (Image 5 매크로 글로시 하이라이트)
   - `3.0–5.5s`: 2분할 스플릿 스크린 (좌측 걷는 다리 + 우측 회전 신발이 비트마다 스왑)
   - `5.5–8.0s`: 만화경(Kaleidoscope) 패널 회전 와이프 $\rightarrow$ 쉘토 실루엣 레드 레이스
   - `8.0–9.5s`: 프레임 인 프레임 인셋 (작은 패널로 팝업 후 전체화면 확장)
   - `9.5–12.5s`: 쾌속 3패널 플래시 몽타주 3연타 히트
   - `12.5–15.0s`: 코발트 블루 단일 컬러블록으로 패널 슬램 $\rightarrow$ 로고 스탬프 1.0초 완벽 정지
4. **시각 및 오디오 스타일 (Aesthetic & BGM Mapping)**:
   - **스타일**: 솔 바스(Saul Bass)풍의 두터운 구아슈/아크릴 붓 터치, 코발트 블루/메리골드 옐로우/코랄 핑크/크림 화이트의 고대비 프라이머리 팔레트
   - **BGM**: 펑키한 일렉트릭 베이스, 와우 기타, 스네어 롤, 핸드 클랩이 화면 분할 비트와 1:1 타격 동기화

### 4-7. ⚡ [모션그래픽 카테고리 7] 하이패션 3배속 키네틱 타이포 커머셜 (High-Fashion 3x High-Speed Kinetic Typography Commercial)

실사 영화 + 하이패션 광고 + 3배속 키네틱 타이포그래피가 결합된 15초 에너지 드링크(또는 음료/테크 제품) 초고속 상업 광고 기법입니다. **"글자를 2D 자막이 아닌 터널, 바닥, 벽, 네온사인, 회전 링, 런웨이 등 3D 공간 건축물(Spatial Architecture)로 실체화"**하여 제품 스펙(카페인, 제로슈거, 비타민, 가격)을 9단계로 쏟아붓는 기법입니다.

#### 💡 9개 씬(9-Scene) 타이포그래피 공간 건축물 변환 공식:
1. **`Scene 1: 터널 (Ad Tunnel)`** $\rightarrow$ 거대 핑크 터널 벽/천장/바닥에 무수한 `"NEED ENERGY?"`가 카메라 역방향으로 쾌속 질주
2. **`Scene 2: 네온 투시도 (Perspective Neon)`** $\rightarrow$ 거대 네온 `"¥200"`이 인물보다 크게 수십 개 반복되며 극단적 1점 투시 형성
3. **`Scene 3: 제품 공중 출현 (Product Air Reveal)`** $\rightarrow$ 손바닥 앞에 캔 출현 + 360도 회전 + 좌우 슬라이드 충돌 텍스트 `"PINK VOLT"` + 번개 광선 방사
4. **`Scene 4: 회전 타이포 링 (Orbiting Type Rings)`** $\rightarrow$ 인물과 캔 주위를 시계/반시계/나선으로 3중 회전하는 링 타이포 `"CAFFEINE 80mg"`
5. **`Scene 5: 3D 패널 전개 (Panel Expansion)`** $\rightarrow$ 캔을 든 팔을 휘두르면 중앙에서 좌우로 수십 장의 패널이 폭발 전개 `"ZERO SUGAR"`
6. **`Scene 6: 런웨이 & 90도 회전 (Runway & 90-Deg Flip)`** $\rightarrow$ 바닥/벽/천장 타이포 런웨이 `"B VITAMINS"`를 걸으며 카메라 90도 롤 회전(중력 유지)
7. **`Scene 7: 3대 정보 블록 합체 (3-Block Information Merge)`** $\rightarrow$ 좌/우/하단에서 3대 스펙(`CAFFEINE 80mg`, `ZERO SUGAR`, `B VITAMINS`)이 날아와 입체 정렬
8. **`Scene 8: 광속 레일 질주 (Speed Rail & Spiral)`** $\rightarrow$ 빛의 레일을 질주하며 상공 낙하 `"ALL FOR"` + 심도 돌진 `"¥200"` + 나선 회전 `"BIG VALUE"`
9. **`Scene 9: 3단 히어로 샷 (3-Tier Final Hero Lockup)`** $\rightarrow$ 거대 캔 옆으로 3단 텍스트(`PINK VOLT` / `CHARGE SMART` / `¥200`)가 낙하/슬라이드/접근하며 캔 로고로 초광속 줌인 엔딩

#### 🎨 하이패션 커머셜 설계 핵심 규칙 (Commercial Design Rules):
* **`네온 바닥 반사 (Glossy Floor Reflection)`**: 유광 바닥에 핑크/형광 네온이 반사되는 사이버-패션 스튜디오 라이팅
* **`공간 심도 상호작용 (Depth & Occlusion)`**: 글자가 인물과 제품의 앞뒤(Fore/Aft)를 자유롭게 통과하며 같은 3D 공간에 존재함을 증명
* **`스펙 카피 100% 가독성 보장`**: 3배속 초고속 모션 중에도 각 문구와 숫자(용량, 가격, 성분)가 최소 1회는 정면에서 완벽하게 읽히도록 고정

### 4-8. 🎸 [모션그래픽 카테고리 8] 펑크 포스터 & 패션 매거진 키네틱 타이포 MV (Punk Poster & Fashion Editorial Kinetic Typography MV)

실사 영화 + 하이패션 화보 + 펑크 록 포스터(Punk Poster) 감성의 3배속 초고속 키네틱 타이포그래피 뮤직비디오 기법입니다. **극태 산세리프(Extra-Bold Sans-serif)** 영문 텍스트가 인물의 신체와 전후좌우 3D 공간을 휘감고, 분열하고, 테이프처럼 찢어지며(Split & Shred), 동공 속으로 수축되는 9개 씬(9-Scene) 하이퍼 모션 기법입니다.

#### 💡 9개 씬(9-Scene) 펑크 & 에디토리얼 타이포 모션 공식:
1. **`Scene 1: 문자 분할 슬라이드 (Letter-by-Letter Slide)`** $\rightarrow$ 인물 얼굴 앞뒤로 좌우 글자 쪼개져 0.1초 단위 쾌속 슬라이드 `"C-H-O-O-S-E"` + 펄스 박동 줌
2. **`Scene 2: 다단 반복 & 패럴랙스 스크롤 (Multi-Tier Parallax Scroll)`** $\rightarrow$ 상하 수십 단으로 반복되는 `"YOUR"`가 좌측은 위로, 우측은 아래로 반대 스크롤 + 파스 변형
3. **`Scene 3: 패럴랙스 사이드 트래킹 (Side-Tracking Traversal)`** $\rightarrow$ 인물과 완전히 병주하며 등 뒤로 `"L-I-F-E"`가 날아가고 1점 투시 공간으로 진입
4. **`Scene 4: 4중 나선 리본 타워 (4-Tier Ribbon Spiral Tower)`** $\rightarrow$ 발 $\rightarrow$ 허리 $\rightarrow$ 가슴 $\rightarrow$ 머리 4단 텍스트 띠 `"OWN YOUR PATH"`가 360도 역회전하며 나선 타워 구축
5. **`Scene 5: 180도 반전 타이포 터널 (180-Deg Reversal Tunnel)`** $\rightarrow$ 바닥/벽/천장 타이포 터널 `"MAKE YOUR MOVE"` 질주 $\rightarrow$ 카메라가 인물을 추월하며 180도 반전
6. **`Scene 6: 테이프 찢김 & 돌파 (Tape Shredding & Breakthrough)`** $\rightarrow$ 3색(흰/검/핑크) 텍스트 테이프 `"BREAK THE RULES"`가 얼굴 앞을 가로지르다 중앙에서 찢어지며 인물 돌파
7. **`Scene 7: 도리 줌 & 3단 레이어 분리 (Dolly-Zoom & 3-Layer Separation)`** $\rightarrow$ 배경의 `"DECIDE"`, `"YOUR"`, `"OWN"`이 도리 줌과 함께 좌/우/심도로 분리 슬라이드
8. **`Scene 8: 나선 상승 & 원형 타이포 합체 (Spiral Ascent & Circular Fusion)`** $\rightarrow$ 발끝부터 나선 상승하는 `"CREATE YOUR FUTURE"`가 3단어로 분리 회전 후 거대 원형 타이포로 합체
9. **`Scene 9: 동공 수축 & 3단 락업 (Iris Implosion & Final Lockup)`** $\rightarrow$ 3단 텍스트 `"CHOOSE / YOUR / LIFE"`가 동공 속으로 초광속 수축 $\rightarrow$ 눈 깜빡임과 동시에 암전

#### 🎨 펑크 포스터 에디토리얼 설계 핵심 규칙 (Design Rules):
* **`텍스트 테이프 분열 (Text Tape Shredding)`**: 패션 잡지와 펑크 그래픽의 테이프(Tape) 질감을 살려 글자가 찢어지며 인물이 튀어나오는 다이내믹 인터랙션
* **`도리 줌 (Dolly Zoom / Vertigo Effect)`**: 인물 크기는 유지한 채 배경의 거대 타이포그래피만 심도 깊숙이 밀려나는 시네마틱 광학 왜곡
* **`동공 수축 엔딩 (Pupil Implosion)`**: 모든 거대 글자가 한 점(동공)으로 흡수되며 잔상을 남기는 클라이맥스

### 4-9. 📜 [모션그래픽 카테고리 9] 3D 오리가미 오트퀴튀르 페이퍼 스컬프처 & 타이포 MV (3D Origami Haute Couture Paper Sculpture MV)

레퍼런스 이미지/비디오 없이(`No Reference`) 오직 텍스트 프롬프트만으로, 1:1 정방형 15초 동안 **"3D 인형 오리가미 조각(Paper Sculpture) + 모션그래픽(MG) + 키네틱 타이포"** 3요소를 동격의 주역으로 융합하는 최고급 아방가르드 아트 필름 기법입니다.

#### 💡 5단계 완급조절 샷 플로우 (5-Stage Shot & Flow Structure):
1. **`0.00-3.00s | BIRTH (탄생)`**: 거대 아이보리 종이에 검은 접힘선이 달리며 크림슨/골드 노출 $\rightarrow$ 인형 종이 조각 출현 $\rightarrow$ `"FOLD THE LIGHT"` 가사 가독성 우선 100% 온전하게 노출 후 글자가 접히며 MG로 융합
2. **`3.00-6.00s | FORM (형태)`**: 금박 접힘선과 비대칭 어깨 실루엣 $\rightarrow$ `"SHAPE THE SILENCE"` 거대 텍스트 제시 후 원/종이 띠/접힘선으로 분해 재구성
3. **`6.00-9.00s | MOTION (최대 밀도)`**: 비트에 맞춰 종이 원, 그리드, 긴 종이 띠, 대담한 색면이 초고속 재구성 $\rightarrow$ 앞선 2개 구절의 단어 파편을 그래픽 소스로 재활용
4. **`9.00-12.00s | ART (속도 저하 & 예술성)`**: 템포를 늦추고 종이 조각 본연의 미학에 집중 $\rightarrow$ 배후에서 거대한 부채꼴 종이 조각과 반투명 종이/금박 구조물 전개 $\rightarrow$ `"BECOME ART"` 완전 표시
5. **`12.00-15.00s | ICON (재가속 & 수렴)`**: `"FOLD", "SHAPE", "ART"` 파편과 기하학 종이 MG가 고속 재구성 $\rightarrow$ 하나의 상징적인 아트 에디토리얼 판면으로 수렴 엔딩 (완전 정지하지 않고 미세 모션 유지)

#### 🎨 오리가미 오트퀴튀르 설계 핵심 규칙 (Material & Rules):
* **`3대 요소 동격 순환 (Trinity Priority Shift)`**: 종이 인형만 항상 전경에 고정하지 않고, [타이포 $\leftrightarrow$ 오리가미 $\leftrightarrow$ MG]의 시각적 우선순위와 전후 배치를 씬마다 스위칭
* **`머티리얼 팔레트`**: 아이보리(Ivory), 딥 크림슨(Deep Crimson), 매트 블랙(Matte Black), 메탈릭 골드(Metallic Gold), 반투명 종이(Translucent Paper)의 접힘선과 두께감 강조
* **`단 3개 핵심 구절 한정`**: `"FOLD THE LIGHT"`, `"SHAPE THE SILENCE"`, `"BECOME ART"` 단 3개만 사용하여 텍스트 환각/오타 원천 차단

### 4-10. 🔥 [모션그래픽 카테고리 10] 핑크 에너지 9대 인터랙티브 키네틱 타이포 MV (Pink Energy Interactive Kinetic Typography MV)

실사 영화 + 하이패션 광고 + 3배속 키네틱 타이포그래피가 결합된 15초 초고속 에너제틱 뮤직비디오 기법입니다. **"글자를 2D 자막이 아닌 9가지 다이내믹 요소(불꽃, 건반, 블록, 디지털 코드, 스프레이 페인트, 블랙 입자, 네온 시계, 빛의 리본, 동공 네온)"**로 실체화하고, 인물의 신체 동작(걸음, 건반 밟기, 스프레이 분사, 팔 휘두름)과 1:1로 물리 반응시키는 기법입니다.

#### 💡 9개 씬(9-Scene) 인터랙티브 물리 반응 공식:
1. **`Scene 1: 불꽃 텍스트 (Flame Outline)`** $\rightarrow$ 암흑 속 발광 라인 점등 $\rightarrow$ 불꽃처럼 미세하게 흔들리며 맥동 `"IGNITE YOUR WILL"`
2. **`Scene 2: 거대 건반 & 발자국 발광 (Piano Key Step)`** $\rightarrow$ 흑백 핑크 건반 위를 걸을 때마다 음표 폭발 + 나선 회전 `"PLAY YOUR OWN RHYTHM"`
3. **`Scene 3: 3D 큐브 블록 조립 (Cube Block Assembly)`** $\rightarrow$ 부유하던 수천 개 큐브가 180도 회전하며 입체 조립 `"BUILD YOUR FUTURE"`
4. **`Scene 4: 디지털 픽셀 코드 스트림 (Digital Pixel Stream)`** $\rightarrow$ 코드 통로를 걸으며 픽셀 단위로 생성 $\rightarrow$ 바닥 수직 융기 `"CODE YOUR OWN PATH"`
5. **`Scene 5: 스프레이 그래피티 (Spray Paint Graffiti)`** $\rightarrow$ 한 손에 든 스프레이 캔을 휘두르자 페인트 라인이 뻗어나가며 완성 `"MAKE YOUR MARK"`
6. **`Scene 6: 블랙 입자 재구성 (Black Particle Flow)`** $\rightarrow$ 걸어갈 때마다 글자가 입자로 분해되었다가 전방에서 재형성 `"MOVE WITH PURPOSE"`
7. **`Scene 7: 초고속 네온 시계 (Neon Clock Rotation)`** $\rightarrow$ 시계 바늘이 360도 맹렬히 회전하다 순간 정지하며 텍스트 발광 `"NOW IS YOUR TIME"`
8. **`Scene 8: 네온 리본 궤적 (Neon Ribbon Swirl)`** $\rightarrow$ 팔을 휘두르는 궤적에서 발생한 긴 리본이 역회전 나선을 그리며 완성 `"CHASE WHAT MOVES YOU"`
9. **`Scene 9: 동공 네온 터널 (Iris Neon Infinite Tunnel)`** $\rightarrow$ 눈동자 홍채 속 네온 발광 $\rightarrow$ 무한 터널로 광속 돌진 $\rightarrow$ 깜빡임과 함께 암전 `"CHOOSE YOUR LIFE"`

#### 🎨 핑크 에너지 인터랙티브 설계 핵심 규칙 (Interactive Design Rules):
* **`신체-오브젝트 직접 인터랙션`**: 건반을 직접 밟고, 스프레이 캔을 직접 뿌리고, 팔을 휘둘러 리본을 생성하는 **물리적 원인과 결과(Cause & Effect)**를 명확히 제시하여 AI의 모션 설득력을 극대화
* **`입자 & 물리 변환 (Particle & Block Physics)`**: 블록 조립, 입자 흩어짐, 픽셀 스트림 등 다채로운 CG 물리 효과를 적극 활용
* **`정확한 스펠링 락`**: 3배속 초고속 전환 속에서도 9개 주요 카피가 최소 1회는 100% 완전하게 판독되도록 고정

### 4-11. 🩰 [모션그래픽 카테고리 11] 그런지 수묵 발레리나 궤적 타이포 리빌 (Grunge Ink-Wash Ballerina Traveling Typography Reveal)

포스트 아포칼립스 폐허 배경의 단일 1장 잉크 워시 실루엣 원화(`Image 1`)를 기반으로, 15초 동안 **고정 와이드 프레임(Locked-off Static Wide Frame)** 안에서 발레리나가 좌 $\rightarrow$ 우로 춤추며 이동할 때마다 **드레스에서 떨어진 잉크 물방울이 바닥에 차례대로 고체 글자 `"D-A-N-C-E"`로 조립·각인되는** 최고급 시네마틱 아트 필름 기법입니다.

#### 💡 7단계 잉크 형성 및 이동 아크 (Traveling Ink-Formation Cycle):
1. **`0.0–0.5s | OPEN`**: 텅 빈 도시 폐허와 돌다리 고정 앵글 $\rightarrow$ 좌측 구석에서 잉크 덩어리가 모이기 시작
2. **`0.5–1.5s | INK SNAP`**: 잉크가 좌측 끝에서 플리에(Plié) 준비 자세의 잉크 발레리나로 순식간에 응고(Snap)
3. **`1.5–3.2s | 'D' SHED`**: 우측으로 피케(Piqué) & 셰네(Chaîné) 턴 도약 $\rightarrow$ 드레스 자락에서 떨어진 잉크가 바닥에 대문자 `"D"`로 스냅 응고
4. **`3.2–5.0s | 'A' SHED`**: 우측으로 연속 턴 $\rightarrow$ 두 번째 위치에서 잉크가 `"A"`로 스냅 각인
5. **`5.0–8.6s | 'N' & 'C' SHED`**: 세 번째, 네 번째 지점을 우아하게 통과하며 바닥에 `"N"`과 `"C"`가 연이어 생성
6. **`8.6–10.4s | 'E' SHED & FULL TITLE`**: 다섯 번째 지점에서 `"E"`가 완성되며 바닥에 `"DANCE"` 5글자가 완벽히 정렬
7. **`10.4–15.0s | FINAL ARABESQUE & HOLD`**: 우측 끝에서 아라베스크(Arabesque) 피니시 포즈 완성 $\rightarrow$ 폐허 배경 위에서 5글자 `"DANCE"`와 발레리나가 미동 없이 3.8초간 정지 홀드(Hold)

#### 🎨 그런지 수묵 발레리나 설계 핵심 규칙 (Aesthetic Rules):
* **`고정 앵글 (Locked-Off Static Wide Frame)`**: 카메라가 패닝하거나 컷 전환하지 않고 완벽히 고정된 프레임을 유지하여 발레리나의 물리적 이동 궤적과 글자 조립의 시각적 안정감을 극대화
* **`건식 붓터치 텍스처 (Dry-Brush Ink-Wash)`**: 부드러운 물 흐림(Liquid Morph)을 배제하고, 단단한 미립자 잉크 응고(Hard Particulate Ink-Assembly)로 날카로운 폰트 가독성 확보
* **`미니멀 오디오 동기화 (Pizzicato & Piano Note Sync)`**: 발레리나의 발걸음마다 단음 피치카토 현악이 울리고, 5개 글자가 바닥에 안착할 때마다 묵직한 피아노 건반 타건음(`Ink-Snap Hit`)이 1:1로 타격

### 4-12. 💥 [모션그래픽 카테고리 12] 핑크 옵스타클 & 건축물 파괴 돌파 키네틱 타이포 MV (Pink Obstacle & Architectural Kinetic Typography MV)

실사 영화 + 하이패션 화보 + 3배속 키네틱 타이포그래피가 결합된 15초 초고속 액션 뮤직비디오 기법입니다. **"글자를 바닥, 벽, 무한 계단, 거울 터널, 유리 벽, 장애물(Obstacle)"**로 물리 실체화하고, 인물이 계단을 뛰어오르고, 발차기로 글자를 날리고, 거대한 문자 벽을 몸으로 부수며 돌파(Breakthrough & Smash)하는 최고급 파쿠르/액션 연출 기법입니다.

#### 💡 9개 씬(9-Scene) 건축 장애물 상호작용 및 파괴 공식:
1. **`Scene 1: 거대 문자 발판 (Giant Letter Foothold)`** $\rightarrow$ 거대 3D 문자 `"YOU ARE THE AUTHOR"` 위에 인물이 서 있고, 상공에서 글자가 충격과 함께 낙하 적층
2. **`Scene 2: 세로 패널 슬릿 (Vertical Panel Slit)`** $\rightarrow$ `"DECIDE"`가 6개의 좁은 세로 패널로 쪼개져 얼굴 앞뒤를 슬라이드하며 창문처럼 마스킹
3. **`Scene 3: 건축물 회전 관통 (Architectural Traversal)`** $\rightarrow$ `"MOVE"` 글자가 건물처럼 양옆에 늘어서고 O가 바닥으로 가라앉으며 인물이 글자 사이를 돌파
4. **`Scene 4: 무한 계단 붕괴 런 (Endless Staircase Shatter Run)`** $\rightarrow$ 발을 디딜 때마다 `"NO PERMISSION"` 계단이 실시간 생성되다 최상단 도약 시 일제히 산산조각 폭발
5. **`Scene 5: 발차기 충격파 방사 (Kick Impact Shockwave)`** $\rightarrow$ 초광각 앵글로 카메라를 향해 발차기를 날리자 `"TAKE THE LEAD"` 글자가 렌즈 방향으로 날아가 정렬
6. **`Scene 6: 거울 터널 & 90도 롤 회전 (Mirror Tunnel & Gravity Flip)`** $\rightarrow$ 거울 반사 터널 `"MAKE IT YOURS"` 속에서 카메라가 90도 롤 회전하며 벽과 바닥이 체인지
7. **`Scene 7: 유리 문자 벽 돌파 (Glass Letter-Wall Breakthrough)`** $\rightarrow$ `"CUT YOUR OWN PATH"` 벽을 인물이 몸으로 들이받자 CUT은 찢어지고 YOUR는 유리처럼 박살
8. **`Scene 8: 4단 나선 링 상승 (4-Tier Ring Ascent)`** $\rightarrow$ 발 $\rightarrow$ 허리 $\rightarrow$ 가슴 $\rightarrow$ 머리 높이의 링 텍스트 `"BECOME WHO YOU CHOOSE"`가 분리 회전 후 스파이럴 타워 완성
9. **`Scene 9: 3D 서라운드 락업 & 동공 흡수 (3D Surround & Pupil Implosion)`** $\rightarrow$ 좌/상/우 3방향에서 날아온 `"CHOOSE YOUR LIFE"`가 인물을 감싸다 동공 속으로 광속 흡수 $\rightarrow$ 암전

#### 🎨 건축 장애물 액션 설계 핵심 규칙 (Action Design Rules):
* **`물리적 파괴 & 충돌 인터랙션 (Physical Shatter & Impact)`**: 계단 폭발, 유리 파쇄음, 발차기 연동, 벽면 돌파 등 거친 충돌(Impact)을 텍스트와 1:1로 매핑
* **`거울 반사 & 90도 중력 왜곡 (Mirror & Gravity Flip)`**: 텍스트가 거울에 다방향으로 반사되고 카메라는 회전하되 인물만 중력을 유지하는 초현실 트릭 연출
* **`극태 산세리프 3색 한정 (Bold Sans-serif 3-Color Constraint)`**: 형광 핑크(Neon Pink), 블랙(Black), 화이트(White) 단 3색으로 제한하여 영상 밀도가 극도로 높아도 시각적 피로감 제어

### 4-13. 🎴 [모션그래픽 카테고리 13] 5인 5초 2D 애니 캐릭터 카드 사선 와이프 몽타주 (5-Character 5s Anime Card Diagonal Wipe Montage)

서로 다른 5명의 2D 애니메이션 캐릭터 레퍼런스(`Image1`~`Image5`)를 사용하여, 5초 동안 **1초당 1명씩 초고속 5비트 사선 그래픽 와이프(Diagonal Graphic Wipe)**로 캐릭터 카드를 넘기듯 소개하는 애니메이션 오프닝/아이캐치 기법입니다.

#### 💡 5인 5초 1:1 독립 몽타주 공식 (5-Character 1-Second Rhythmic Beats):
1. **`0.0–1.0s | Image 1 (다크 바이올렛)`**: 딥 바이올렛 사선 띠 스냅 $\rightarrow$ 흑발 중2병 소녀의 드라마틱 턴 & 머리 넘기며 미소 + 배경에 연보라 모노크롬 거대 초상화
2. **`1.0–2.0s | Image 2 (레드 오렌지)`**: 강렬한 레드 오렌지 사선 와이프 $\rightarrow$ 흑갈색 피부 체육계 소녀의 어깨 너머 턴 & 주먹 불끈 미소 + 배경에 연오렌지 모노크롬 초상화
3. **`2.0–3.0s | Image 3 (브라이트 골드)`**: 스파클링 골드 사선 띠 $\rightarrow$ 트윈테일 여고생의 우아한 턴 & 트윈테일 매만지며 윙크 + 배경에 연골드 모노크롬 초상화
4. **`3.0–4.0s | Image 4 (모스 그린)`**: 무심한 모스 그린 사선 슬라이드 $\rightarrow$ 후드티 남학생의 느긋한 뒤돌아보기 & 냉소적 반미소 + 이어폰 줄 흔들림 + 배경에 연그린 모노크롬 초상화
5. **`4.0–5.0s | Image 5 (더스티 로즈)`**: 망설이는 듯한 핑크 사선 띠 $\rightarrow$ 핑크머리 소심한 남학생의 웅크린 턴 & 뒷머리 긁적이기 + 배경에 연로즈 모노크롬 초상화

#### 🎨 캐릭터 카드 와이프 설계 핵심 규칙 (Anti-Morphing Rules):
* **`인물 간 모핑 0% 절대 차단`**: 5명이 한 화면에 겹치거나 얼굴이 서로 섞이는(Morphing/Blending) 현상을 원천 방지하기 위해 **사선 그래픽 밴드가 화면 전체를 100% 덮어 지우며 다음 인물로 전환(Hard Wipe Cut)**
* **`클로즈업 규격 고정 (35~50% Frame Height)`**: 전신 롱샷을 배제하고 인물 얼굴이 화면 높이의 35~50%를 차지하는 바스트/페이스 클로즈업으로 통일하여 표정 연기 극대화
* **`배경 모노크롬 초상화 듀얼 레이어`**: 전경의 움직이는 2D 셀셰이딩 캐릭터 뒤에 동일 인물의 거대한 연한 단색 모노크롬 초상화를 깔아 그래픽 디자이너블한 카드 레이아웃 완성

### 4-14. 🏛️ [모션그래픽 카테고리 14] 스키마 구조화 형광 핑크 볼륨 타이포 MV (JSON/Schema Structured Fluorescent Pink Volumetric Typography MV)

글로벌 AI 영상 스튜디오/API에서 사용하는 **`subject_definitions` + `retention_analysis` + `detailed_description (초단위 밀리초 샷 분할)` + `overall_soundscape`** JSON/스키마 메타데이터 기반의 초정밀 15초 하이패션 키네틱 타이포그래피 프롬프트 포맷입니다.

#### 💡 구조화 스키마 4대 핵심 블록 (4-Block Schema Architecture):
1. **`subject_definitions`**: `<Subject 1>`이 `<Picture 1>`의 인물(얼굴, 헤어, 의상, 체형, 메이크업, 레드 선글라스)임을 100% 동일하게 정의.
2. **`retention_analysis`**: `[Shot 1]-[Shot 9]` 전체 씬에서 `<Subject 1>`의 정체성과 외형이 단 1%도 변하지 않고 완전히 보존(`fully_preserved`)됨을 선언.
3. **`detailed_description (초단위 밀리초 9-Shot 분할)`**:
   - `[Shot 1] 00:00.000`: 핑크 구름 위 거대 볼륨 텍스트 `"YOU ARE THE CREATOR"` 래피드 로켓 줌
   - `[Shot 2] 00:01.500`: 얼굴 초근접 + 6개 패널 분할 `"DECIDE"` 슬릿 슬라이드 + 무음 립싱크(Syballic Mouth Movement)
   - `[Shot 3] 00:03.000`: 유광 핑크 바닥 `"MOVE"` 4글자 궤적 분리 $\rightarrow$ 무한 1점 투시 문자 돌파
   - `[Shot 4] 00:04.500`: 무한 핑크 계단 레이스 + 발 착지마다 `"NO PERMISSION"` 폭발 비산
   - `[Shot 5] 00:06.000`: 초광각 킥 액션 + 180도 채찍 회전 + 3단어 정렬 `"TAKE THE LEAD"`
   - `[Shot 6] 00:08.000`: 거울 반사 터널 `"MAKE IT YOURS"` + 90도 롤 회전(중력 유지)
   - `[Shot 7] 00:09.500`: 거대 4단어 문자 벽 돌파 `"MAKE OUR OWN PATH"` + 유리 파쇄 비산
   - `[Shot 8] 00:11.000`: 4중 밴드 텍스트 `"BECOME WHO YOU CHOOSE"` 나선 회전 타워 상승
   - `[Shot 9] 00:13.000`: 3D 서라운드 락업 `"CHOOSE YOUR LIFE"` $\rightarrow$ 동공 속 초광속 수축 $\rightarrow$ 깜빡임 암전
4. **`overall_soundscape (전문 폴리 사운드 디자인)`**:
   - 텍스트 착지 타격음, 서브 베이스 저음 타격, 고속 바람 가르는 소리, 유리 파쇄음, 발소리, 찰나의 디지털 글리치 스터터를 초단위 동작과 1:1로 매핑.

### 4-15. 🗞️ [모션그래픽 카테고리 15] 다크팝 사이버그랑지 제록스 진(Zine) 콜라주 3-레이어 MV (Cyber-Grunge 90s Xerox Zine 3-Layer MV)

90년대 언더그라운드 음악 잡지(Zine) 콜라주, 16mm 거친 그레인, 제록스 복사기 스캔 오차(Scan Misregistration), 찢어진 종이 질감(Ripped Paper Edges)과 118–122 BPM 트랩 랩을 결합한 15초 8-샷 다크팝 MV 기법입니다. **3개 레이어 분리(3-Layer Composite Architecture)**를 통해 인물 얼굴은 온전히 보존하면서 표면만 예술적으로 해체(Controlled Surface Deconstruction)하는 최고급 에디토리얼 연출입니다.

#### 💡 3-레이어 분리 합성 시스템 (3-Layer Composite Architecture):
* **`Layer A (배경/타이틀)`**: 붉은색 타이틀 페이퍼 블록 `"MiniMax H3"` (잡지 제호 마스트헤드)
* **`Layer B (인물 주체)`**: 정면 바스트 포즈, 젖은 흑발 곱슬머리, 좌측 딥 블랙 섀도우, 안정적인 실사 얼굴
* **`Layer C (질감/이펙트)`**: 스캔 라인, 하프톤 도트, 찢어진 종이 파편, 잉크 스플래시, 블랙 타르 파티클

#### 💡 8-샷 에디토리얼 타임라인 (8-Shot Editorial Breakdown):
1. **`Shot 1 (0–1.5s) | 정적 긴장감`**: 정면 커버 포트레이트, 젖은 곱슬머리, 좌측 암부, 거대 텍스트 `"MiniMax H3"`
2. **`Shot 2 (1.5–3.0s) | 스캐닝`**: 우측 뺨과 머리를 가로지르는 수직 스캔선 + 찰나의 레드 채널 오프셋
3. **`Shot 3 (3–4.5s) | 찢어짐(Tear)`**: 하단 얼굴을 가로지르는 1프레임 잡지 찢김 인서트 + 복사기 파편
4. **`Shot 4 (4.5–6.0s) | 표면 균열`**: 우측 뺨/턱에 붉은 균열과 블랙 타르 파티클 부유 (얼굴 골격 100% 보존)
5. **`Shot 5 (6–7.5s) | 표면 해체 익스트림`**: 더 타이트한 크롭, 우측 뺨에서 붉은 파편과 잉크 방울 분출
6. **`Shot 6 (7.5–10s) | 에너지 빌드업`**: 무너지는 잡지 커버처럼 붉은 타이틀 블록이 분할되나 여전히 `"MiniMax H3"` 판독
7. **`Shot 7 (10–13s) | 발화 액션`**: 인물이 정면을 응시하며 깊고 건조한 가슴소리로 대사 발화: `"This is H3."` (단 1회의 보컬 프레이즈)
8. **`Shot 8 (13–15s) | 커버 동결 & 푸시인`**: 파티클이 가라앉으며 완벽한 잡지 표지 컷으로 재정렬 $\rightarrow$ 슬로우 푸시인 $\rightarrow$ 테이프 스톱 하드 암전

#### 🎨 다크팝 사이버그랑지 설계 핵심 규칙 (Dark-Pop Rules):
* **`악기 트랙-트랜지션 1:1 결합`**: 스네어(1프레임 찢김 인서트), 하이햇(점프 컷/스캔 라인), 808 베이스(파편 폭발 및 테이프 스톱)
* **`그로테스크/고어 완전 차단`**: 신체 변형이나 괴물화, 피/내장을 절대 금지하고 오직 종이/잉크/라커/타르 질감의 표면 해체(Controlled Surface Deconstruction)로만 제한

### 4-16. 🥤 [모션그래픽 카테고리 16] 일본 플랫 일러스트 2D 음료 모션 커머셜 (Japanese Flat-Illustration 2D Beverage Motion Commercial)

산토리/포카리스웨트 감성의 **2D 플랫 벡터 일러스트레이션(Flat 2D Vector), 굵은 네이비 외곽선, 팝아트 솔리드 컬러 필(Solid Color Fills), 탄력 있는 오버슈트 컷아웃 애니메이션**이 결합된 15초 6-샷 생수/음료 TVC 상업 광고 기법입니다. **"여름의 열기(옐로우) $\rightarrow$ 시원한 청량감(아쿠아/딥블루)"**의 명확한 색채 대비와 경쾌한 마림바 BGM(128 BPM)을 1:1로 결합했습니다.

#### 💡 6-샷 청량 음료 스토리보드 (6-Shot Refreshment Storyboard):
1. **`Shot 1 (00:00.000)`**: 채도 높은 옐로우 배경 + 백색 태양 펄스 $\rightarrow$ 0.8초에 `"AOI WATER"` 보틀이 하단에서 솟구치며 오버슈트 착지 + 플래시 프레임 + 3중 물결 링 + 타이틀 조립 `"この夏、あつい。"`
2. **`Shot 2 (00:02.400)`**: 아쿠아 물결이 좌측에서 옐로우를 쓸어내며 전환 $\rightarrow$ 보틀 1/4 회전 + 라벨에 글자 조립 `"AOI WATER"` + 결로 물방울 6개 팝업 + 얼음 2조각 텀블링
3. **`Shot 3 (00:05.000)`**: 딥블루 와이프 $\rightarrow$ 보틀이 기울어지며 유리잔에 시원한 물줄기 낙하 $\rightarrow$ 얼음 3조각 바운스 + 물방울 방사형 버스트 + 키네틱 의성어 스탬프 `"キンッ。"`
4. **`Shot 4 (00:07.600)`**: 아쿠아 하드 셰이프 와이프 $\rightarrow$ 단발머리 일본 여배우 벡터 캐릭터가 보틀을 들고 3모금 시원하게 마심 (몸에 청록색 물이 차오름) + 볼 옆에 의성어 팝업 `"ごくっ"`
5. **`Shot 5 (00:10.200)`**: 옐로우 와이프 $\rightarrow$ 보틀을 치켜들고 점프 $\rightarrow$ 기하학 파티클 링 버스트 $\rightarrow$ 2단 헤드라인 조립 `"夏に、" "負けない。"` + 볼드 옐로우 언더라인
6. **`Shot 6 (00:12.600)`**: 웜 화이트 엔드 카드 $\rightarrow$ 보틀 중앙 슬라이드 + 로고타입 `"AOI WATER / アオイ・ウォーター"` 안착 + 일본어 성우 나레이션 발화 `<d>[Japanese] 夏に、負けない。</d>` $\rightarrow$ 15.000초까지 완벽 정지 유지

#### 🎨 플랫 일러스트 커머셜 설계 핵심 규칙 (Flat Commercial Rules):
* **`3D/실사/그라디언트 0% 완전 배제`**: 실사나 3D CGI 광택을 엄격히 금지하고 오직 굵은 네이비 라인과 깔끔한 단색 솔리드 면(Flat Solid Fills)으로만 렌더링
* **`스프링 컷아웃 애니메이션 (Springy Cutout & Overshoot)`**: 기하학적 파티클과 보틀이 통통 튀는 오버슈트 이징(Overshoot Easing) 물리 모션 적용
* **`128 BPM 마림바 & 우쿨렐레 BGM`**: 마림바, 우쿨렐레, 핸드클랩의 경쾌한 어쿠스틱 비트에 맞춰 물 따르는 소리, 꿀꺽 마시는 소리, 엔드 카드 챠임벨 사운드를 정밀 결합

### 4-17. 📄 [모션그래픽 카테고리 17] 핸드메이드 2D 찢어진 종이 콜라주 일본 광고 (Handmade 2D Paper Collage Japanese Commercial)

인물/캐릭터를 0% 배제하고 오직 **찢어진 종이(Torn-paper), 리소그래프 질감(Risograph Texture), 복사기 그레인, 거친 잉크 라인, 스톱모션 프레임 지터**만으로 구성된 15초 세로(9:16) 일본 비즈니스/출판 바이럴 광고 기법입니다. **`Visible-text whitelist`**를 선언하여 6개의 정확한 일본어 문구 외에 모든 환각 텍스트를 원천 차단했습니다.

#### 💡 4-샷 핸드메이드 콜라주 타임라인 (4-Shot Collage Storyboard):
1. **`Shot 1 (00:00.000) | 문제 제기 (Pain Point)`**: 오프화이트 종이 위 목탄색 종이 조각 슬라이드 $\rightarrow$ 찢어진 마스크 사이로 볼드 타이틀 `"集客に疲れていませんか？"` 노출 $\rightarrow$ 여성 성우 보이스오버: `<d>[Japanese] 集客に疲れていませんか？</d>`
2. **`Shot 2 (00:03.500) | 3중 텍스트 스택 (Problem Overload)`**:
   - 1비트: 찢어진 아이보리 띠 슬라이드 `"SNS集客"` 스톰프
   - 2비트: 산호색 블록 낙하 슬램 `"広告"`
   - 3비트: 옐로우 띠 롤업 언폴드 `"無料セミナー"`
   - 3개 띠가 겹쳐진 불안정한 스택 형성 $\rightarrow$ 비트에 맞춰 흔들리다 일제히 뒤집히며(Flip) 전체화면 찢어진 종이 와이프로 전환
3. **`Shot 3 (00:08.000) | 해결의 섬광 (Epiphany)`**: 코발트 블루 레이어 등장 $\rightarrow$ 오디오 순간 무음(Hold) $\rightarrow$ 중앙이 찢어지며 웜 옐로우 노출 $\rightarrow$ 타이틀 폭발 `"そうだ！"` + 나레이션: `<d>[Japanese] そうだ！</d>`
4. **`Shot 4 (00:10.500) | 솔루션 & CTA (Solution Landing)`**: 종이 스택이 책 모양으로 언폴드 $\rightarrow$ 중앙에서 볼드 타이틀 `"本を書こう！"` 상승 + 확신에 찬 보이스오버: `<d>[Japanese] 本を書こう！</d>` $\rightarrow$ 마지막 1.5초간 완벽 정지 유지

#### 🎨 종이 콜라주 설계 핵심 규칙 (Handmade Paper Rules):
* **`텍스트 화이트리스트 선언 (Visible-text Whitelist)`**: `"集客に疲れていませんか？"`, `"SNS集客"`, `"広告"`, `"無料セミナー"`, `"そうだ！"`, `"本を書こう！"` 단 6개 문자열만 허용하고 기타 자막/로고/워터마크 100% 차단
* **`인물 0% 순수 그래픽 락`**: 인물, 얼굴, 손, 몸, 캐릭터를 절대 넣지 않고 종이와 타이포그래피 모션만으로 시선 장악
* **`104 BPM 드럼 브러시 & 비브라폰 BGM`**: 업라이트 베이스, 테이프 클릭, 종이 찢는 소리, 마커 긁는 소리, 복사기 기계음이 결합된 아날로그 오디오 동기화

### 4-18. ⚡ [모션그래픽 카테고리 18] AAA급 시네마틱 캐릭터 스킬 16초 무한 루프 (AAA Character Skill 16s Seamless Loop)

**2.39:1 아나모픽 와이드스크린(Anamorphic Widescreen)** 규격에서 펼쳐지는 게임 시네마틱(원신/스타레일/나루토급) 최고 난이도의 16초 무한 루프 액션 쇼케이스 기법입니다. **"부채/검/마법 등의 무기를 활용한 2초 단위 8-샷 칼박자 연계 + 샷 간 환경 파괴 누적 + 1초 절대 정적(Silence) 후 궁극기 대폭발 + 100% 무한 루프 복귀"**가 핵심입니다.

#### 💡 2초 단위 8-샷 무한 루프 타임라인 (8-Shot Seamless Loop Breakdown):
1. **`Shot 1 (0–2s) | 기세 축적 (Charge Up)`**: 40mm 레일 트랙 돌진 $\rightarrow$ 부채 끝에 쌀알 크기의 백색 발광점 명멸(0.5초 간격 호흡) $\rightarrow$ 번개가 바닥에서 다리를 타고 올라옴
2. **`Shot 2 (2–4s) | 부채 전개 (Unfurl & Arc)`**: 50mm 로우앵글 스테디캠 상승 $\rightarrow$ 부채 1/3 오픈 $\rightarrow$ 거미줄 번개 방사 $\rightarrow$ 눈빛이 정적에서 날카롭게 변화
3. **`Shot 3 (4–6s) | 횡베기 광인 (Horizontal Slash)`**: 35mm 고속 패닝 $\rightarrow$ 3m 초승달 번개 참격 날림 $\rightarrow$ 공기 왜곡 열파 $\rightarrow$ 대사: `"散れ"`
4. **`Shot 4 (6–8s) | 3단 콤보 연타 (3-Hit Combo)`**: 50mm 핸드헬드 초천경 $\rightarrow$ **1타: 상단 분수 번개 $\rightarrow$ 2타: 수직 낙하 지면 거미줄 균열 $\rightarrow$ 3타: 360도 링 충격파** $\rightarrow$ 대사 3연타: `"雷", "鳴", "華"`
5. **`Shot 5 (8–10s) | 공중 도약 & 풍차 회전 (Aerial Windmill)`**: 28mm 광각 지미집 상승 $\rightarrow$ 공중 도약 후 부채 풍차 회전 $\rightarrow$ 원형 에너지 디스크로 천장 강타 $\rightarrow$ 쇄석 낙하
6. **`Shot 6 (10–12s) | 지면 소용돌이 수렴 (Vortex Focus)`**: 40mm 360도 회전 궤도 $\rightarrow$ 착지 후 바닥에 번개 소용돌이 형성 $\rightarrow$ 동공이 고양이 세로눈으로 각성 $\rightarrow$ 긴장감 극대화
7. **`Shot 7 (12–14s) | 궁극기 대폭발 (Ultimate Burst)`**: 50mm 초고속 전방 돌진 $\rightarrow$ **1초간 절대 무음(Absolute Silence 0dB)으로 극적 긴장감 형성** $\rightarrow$ 4m 원추형 번개 빔 대폭발 $\rightarrow$ 공기 플라즈마 이온화 $\rightarrow$ 대사: `"雷華閃"`
8. **`Shot 8 (14–16s) | 무한 루프 완벽 복귀 (Loop Climax)`**: 50mm 완전 정지 카메라 $\rightarrow$ 지면에 남은 전투 파괴 흔적(균열, 그을음, 파편)이 은은히 발광 $\rightarrow$ **Shot 1의 시작 자세와 100% 동일하게 복귀하여 영원한 무한 루프 완성** $\rightarrow$ 대사: `"また、始めるわ"`

#### 🎨 시네마틱 스킬 연출 설계 4대 핵심 규칙:
* **`환경 파괴 누적 시스템 (Environment Damage Accumulation)`**: 1~7샷에서 부순 돌바닥 균열, 천장 그을음, 번개 자국이 사라지지 않고 8번 샷까지 누적 보존
* **`1초 절대 무음 연출 (1s Absolute Silence Drop)`**: 궁극기 폭발 직전 1초간 모든 BGM/효과음을 완전히 차단하여 폭발 타격감 300% 증폭
* **`2.39:1 아나모픽 광학 룩`**: 타원형 보케(Oval Bokeh), 수평 블루 플레어, 코닥 5219 16mm 필름 그레인 12% + 할레이션 6% 주입으로 CG 이질감 완벽 제거
* **`카메라 제약`**: 롱샷/대원경을 금지하고 인물 무릎 위~바스트 샷(화면 높이 70% 이상)으로 유지하여 액션의 몰입감과 밀도 유지

---

## 5. 레딧(Reddit) 커뮤니티 검증 대사 & 샷 전환 특수 태그

레딧(r/StableDiffusion, r/comfyui) 사용자들이 정리한 MiniMax H3 전용 대사 및 컷 제어 구문 수칙입니다.

1. **대사 음성 태그 표준화 (`<d>[Language]Spoken text</d>`)**:
   * 대사를 단순히 큰따옴표로 적는 것보다 레딧 커뮤니티 태그를 사용할 때 AI의 TTS 발화 정확도와 인공지능 입모양(Lip-sync) 매칭율이 극대화됩니다.
   * *기본 구문*: `<d>[English]Hello, welcome to the show!</d>`
   * *한국어 구문*: `<d>[Korean]사람을 치고 가면 어떡하오!</d>`
2. **인라인 감정/톤 주입 (`* tone indicator *`)**:
   * 대사 중간에 별표(`*`)로 톤 지시어를 삽입하면 오디오 렌더러가 캐릭터의 감정 상태를 정밀하게 음성에 반영합니다.
   * *예시*: `<d>[English]What are you doing here? * annoyed tone * I told you to leave!</d>`
   * *예시*: `<d>[Korean]너 지금 뭐 하는 거야? * whispering softly * 조용히 해... * panicked *</d>`
3. **아날로그 점프 컷 명시 (`[Abrupt jump cut]`)**:
   * AI 비디오 특유의 물처럼 흐물거리는 트랜지션(Liquid morphing)을 막기 위해 샷 전환 지점마다 `[Abrupt jump cut to Shot 2]` 키워드를 넣습니다.


## 5. 아날로그 시네마틱 & 결함 주입 (MiniMax H3 Film & Imperfection Integration)

MiniMax H3의 고해상도 렌더링에 **가짜 CG 느낌(AI Slop)**을 없애고 아날로그 실사 질감을 구현하는 융합 지시법입니다.

* **DV 16mm 결함 주입 키워드**:
  `DV 16mm camcorder aesthetic, slow autofocus hunting, awkward micro-zoom, accidental face crop, subtle uneven framing`
* **아날로그 광학 텍스처**:
  `Soft analog tape texture, faint tape grain, blooming highlight glow, auto-exposure flicker, muted soft contrast`
* **유기적 공간 조명 다이내믹스**:
  `Lighting shifts naturally per beat: warm indoor tungsten bulbs → cool window daylight → high-contrast stage lights`

---

## 6. 15초 타임라인 비트(Timed Beats) 분할 구문

MiniMax H3는 초단위 타임라인 비트를 직접 인식합니다. 15초 연출은 아래와 같이 타임라인을 나누어 작성합니다.

```text
Timeline Beats:
- 00:00–00:04 [Beat 1]: [초반 훅 & 의문 텍스트 "TEXT A" 등장]
- 00:04–00:10 [Beat 2]: [3D 제품 팝업 & 하이라이트 타이포 "TEXT B" 슬라이드]
- 00:10–00:15 [Beat 3]: [엔딩 브랜드 로고 안착 & 영업 완료 스탬프 "TEXT C"]
```

---

## 7. 실전 MiniMax H3 프롬프트 템플릿 예시

### 🎬 시네마틱 DV 브이로그 (15초)
```markdown
15-second 16mm analog DV camcorder vlog aesthetic for @character.

Camera & Look: First-person POV, DV 16mm camcorder aesthetic, natural handheld micro-shake, slow autofocus lag, awkward micro-zoom, and accidental frame crops. Soft analog tape texture, faint tape grain, blooming highlight glow, auto-exposure flicker, muted soft contrast.

Lighting: Lighting shifts naturally: warm vanity bulbs -> cool window daylight -> dim backstage lighting.

Timeline Beats:
- 00:00–00:05 [Beat 1: Dressing Room]: @character looking into mirror with soft smile. Audio Pass: Soft room ambient noise and gentle exhalation sound.
- 00:05–00:10 [Beat 2: Moving Van]: Handheld shot watching city passing through window. Audio Pass: Low road hum and gentle wind.
- 00:10–00:15 [Beat 3: Backstage Stage Entrance]: Stepping toward bright stage lights with genuine smile. Audio Pass: Distant crowd cheering sound growing louder.
```

### 🎬 해먹에서의 오후 낮잠 (Afternoon Nap in a Hammock - 내추럴 일상 다큐 & 한국어 구어체 대사)
```markdown
[Main Subject]
Young Korean woman, early 20s, oversized soft cardigan over shorts, hair loose and slightly messy, relaxed sleepy expression, natural unguarded energy.

[Setting & Location]
Small backyard with a hammock strung between two trees, early afternoon. Dappled sunlight through leaves, a small side table with a book, quiet garden sounds. No modern clutter.

[Visual & Camera Style]
Ultra-realistic documentary realism, intimate candid feeling, soft warm afternoon light. Early 2000s DV camcorder, handheld gentle drift, autofocus adjusting slowly to shifting light through leaves, warm faded color cast, soft grain. No stabilization.

[Timeline (30 sec)]
- 00:00–00:03: She climbs into the hammock carefully, adjusting her position.
- 00:03–00:06: She picks up a book from the side table, flipping to her page.
- 00:06–00:09: She reads quietly for a moment, then yawns softly.
- 00:09–00:12: She sets the book on her stomach, then closes her eyes briefly.
- 00:12–00:15: A breeze sways the hammock gently; she smiles without opening her eyes.
- 00:15–00:18: She peeks one eye open at camera saying "여기 진짜 시원하다" ("It's really cool here").
- 00:18–00:21: She stretches one arm lazily, then lets it dangle off the hammock.
- 00:21–00:24: Dappled light shifts across her face as leaves move overhead.
- 00:24–00:27: She murmurs sleepily, then closes her eyes again, fully relaxed.
- 00:27–00:30: She whispers to camera "나 좀 잘게..." ("I'm going to sleep a bit..."), drifting off as it fades.

[Audio Pass]
Leaves rustling, hammock creaking softly, distant birds, faint wind. Her spoken Korean dialogue as noted above ("여기 진짜 시원하다", "나 좀 잘게..."). No music.

[Goal]
A calm, drowsy afternoon rest moment—intimate, soft, deeply believable.
```

### 🎬 35,000달러급 하이패션 3D 타이포그래피 상업 광고 (15초)
```markdown
[Core Concept]
15s 9:16 vertical high-fashion video commercial. Industrial Hyperpop x Deconstructed Club aesthetic: metallic 3D typography, sharp kicks, metallic snares, distorted bass. A timeline-based reality where audio controls 3D architecture.

[Character Identity]
Single fashion model with short cropped black hair, silver eyebrow accent, asymmetric black crop jacket, wide trousers, red contrast stitching. Maintain identical face, hairstyle and outfit. Multiple figures are strictly past-frame projections.

[Visual & Spatial Typography]
Black, metallic chrome silver, glowing warning red. Glass timelines, scanning laser grids, impossible 3D metallic architecture. Massive 3D metallic words "TREND", "SAME", "OUTSIDE" exist as physical architectural walls and tunnels in the environment, NOT flat subtitles.

[Timeline Beats]
- 00:00–00:05 [Beat 1]: Model steps out from behind massive 3D chrome metallic text "TREND" as red laser grids sweep the metallic structure. Audio Pass: Industrial kick drum and metallic snare impact.
- 00:05–00:10 [Beat 2]: Dynamic camera orbiting through 3D architectural letters "SAME". Past-frame projections step behind the model. Audio Pass: Distorted bass rumble with glitch vocal slices.
- 00:10–00:15 [Beat 3]: Camera plunges forward through 3D metallic "OUTSIDE" architecture into bright red lighting burst. Audio Pass: Heavy bass drop explosion and crisp metallic chime.

### 🎬 인터랙티브 UI 디지털 크리처 백과사전 (15초)
```markdown
[Reference Mapping]
Use Image 1 as exact UI layout, typography, and interface style reference.
Use Image 2–9 as exact creature model references:
Image 2 = Card A (LUMI HARE), Image 3 = Card B (CLOUD WISP), Image 4 = Card C (EMBER FENNEC), Image 5 = Card D (TIDE BEHEMOTH), Image 6 = Card E (PETAL VULPIN), Image 7 = Card F (ORCHARD EYE), Image 8 = Card G (MEADOW CROWN), Image 9 = Card H (FROST GLIDER).

[UI & Camera Rules]
15s 16:9 vertical/horizontal UI video. Keep camera strictly static. Maintain clean minimal digital Creature Encyclopedia UI layout (sleek Pokédex aesthetic). No camera motion, no UI distortion, no scene cuts, no extra text.

[Timeline Beats]
- 00:00–02:05 [Beat 1]: Cursor clicks Card A. Main creature updates to LUMI HARE, main title updates to "LUMI HARE". Creature blinks and rotates slightly. Audio Pass: Crisp UI click sound.
- 02:05–05:00 [Beat 2]: Cursor clicks Card C. Main creature updates to EMBER FENNEC, main title updates to "EMBER FENNEC". Cursor drags horizontally to rotate creature. Audio Pass: Soft hover UI sound.
- 05:00–07:05 [Beat 3]: Cursor clicks Card E. Main creature updates to PETAL VULPIN, main title updates to "PETAL VULPIN". Cursor pokes creature, creature reacts with mild annoyance. Audio Pass: Subtle creature squeak SFX.
- 07:05–10:00 [Beat 4]: Cursor clicks Card G. Main creature updates to MEADOW CROWN, main title updates to "MEADOW CROWN". Cursor taps near horns, creature flinches. Audio Pass: Low creature murmur.
- 10:00–12:00 [Beat 5]: Cursor clicks Card D. Main creature updates to TIDE BEHEMOTH, main title updates to "TIDE BEHEMOTH". Cursor continues poking.
- 12:00–15:00 [Beat 6]: TIDE BEHEMOTH suddenly gets angry, opens massive mouth, lunges forward and swallows the cursor whole, returning to idle. Title stays "TIDE BEHEMOTH". Audio Pass: Aggressive creature roar exploding into comical swallow gulp sound.
### 🎬 시트콤 모큐멘터리 대화 & 스냅 줌 씬 (15초)
```markdown
[Genre & Setting]
The Office (US) mockumentary style, Dunder Mifflin conference room, mid-afternoon, harsh fluorescent light, cheap office chairs. Handheld documentary camera, slightly unstable, abrupt reframing and fast snap-zooms to reacting characters.

[Character Dynamics & Scene Action]
MICHAEL SCOTT stands before a whiteboard holding a marker, overly excited about a messy diagram. Employees sit around table looking exhausted. STANLEY HUDSON sits at the end, wearing glasses, head down over a crossword puzzle, completely indifferent.

[Dialogue & Reaction Beats]
- 00:00–00:04 [Beat 1]: MICHAEL (loudly, proudly): "Listen up, everyone. Large Language Models. L-L-Ms. This is the future of paper industry." Pause. Nobody reacts. Audio Pass: Crisp speech, silence, fluorescent light hum.
- 00:04–00:08 [Beat 2]: Camera slowly dollies toward Stanley—head down, unblinking, filling out crossword. MICHAEL: "That's why company gives bonuses to anyone—" Audio Pass: Speech continuation, soft paper friction sound.
- 00:08–00:11 [Beat 3]: Fast snap-zoom to Stanley! He lifts head, takes off glasses, deadpan serious. STANLEY: "I'm listening." Audio Pass: Sharp camera zoom SFX, calm deep voice.
- 00:11–00:15 [Beat 4]: Fast snap-zoom back to Michael waving hand away. Instantly snap-zoom back to Stanley putting glasses back on and returning to crossword. Cut to JIM turning head slowly to stare directly into camera lens with deadpan expression for 2 seconds. Audio Pass: Speech, paper sound, room ambient.

[Style Rules]
Single-camera sitcom, natural organic acting, no laugh track, muted office color palette, characters occasionally glancing at the camera lens.
### 🎬 아방가르드 오트퀴튀르 원테이크 수채화 패션 필름 (15초)
```markdown
[Core Concept]
AQUARELLE No.7 — an avant-garde haute couture film where watercolor becomes a living medium. 15-second continuous cinematic sequence. The rhythm controls the visual world: 0–4s: restrained silence and negative space, 4–8s: gradual density buildup, 8s: drop moment expanding into fluid motion, 12–15s: transition into a final fashion poster composition.

[Character Identity Lock]
Young woman with long black hair, calm and refined facial features, wearing a white high-neck pigment dress with a black wide belt. Maintain strict identity consistency. Any new colors must only appear through watercolor gradually absorbing into fabric. Her fingertips extract transparent watercolor ribbons from the air to pull camera, transform environment, and shape physical typography.

[Camera Direction]
Strict one-take continuous shot. No cuts, no teleportation, no hidden transitions.
Camera journey: Macro shot of floating water droplet → watercolor ribbon emerges → camera pulls back to reveal the woman → camera circles around her → enters paper art gallery → passes through dimensional typography → rises into a final overhead fashion poster.

[Typography & Physical Texture]
Allowed words: "LET SILENCE BLOOM", "AQUARELLE No.7", "WEAR THE UNSEEN". Letters must have physical depth, wet watercolor reflections, paper fiber edges, shadows, and material interaction (NOT a flat 2D overlay).

[Storyboard Timeline Beats]
- 00:00–01:00 [Beat 1]: Macro shot of transparent water droplet floating in air, reflecting blurred silhouette of woman. Droplet stretches with vocal becoming a pale cyan watercolor thread. Audio Pass: Soft breath-like vocal.
- 01:00–03:00 [Beat 2]: Camera travels backward along thread wrapping around lens. Focus shifts to her raised fingertip, revealing her face and white dress. Audio Pass: Soft fluid motion sound.
- 03:00–08:00 [Beat 3]: She moves wrist to guide smooth camera arc. Paper folds, typography forms physical 3D text "LET SILENCE BLOOM". Audio Pass: Wooden snare paper folding sound.
- 08:00–12:00 [Beat 4]: Drop moment! Camera passes through transparent paper flower structure into an endless ivory paper gallery. Dress absorbs watercolor naturally as ribbons form sculptural forms around her body. Audio Pass: Deep sub-bass pulse.
- 12:00–15:00 [Beat 5]: Camera cranes upward transforming into luxury fashion ad poster. Physical typography "AQUARELLE No.7" and "WEAR THE UNSEEN" stamps into place. Final museum-level fashion poster composition. Audio Pass: Clean resolution chime and ambient reverb.

[Negative Prompt]
No cuts, no scene changes, no identity change, no face swap, no extra limbs, no deformed hands, no random costume changes, no explosive paint effects without physical cause, no incorrect typography, no watermarks.
### 🎬 키네틱 리릭 퍼포먼스 뮤직비디오 (15초)
```markdown
[Core Concept]
16:9 Kinetic lyric performance music video using Audio1 for vocals, timing, and lyrics, and Image1 for sole performer and style reference. Typography is the main event and the singer is the visual anchor. Preserve performer's flat editorial vector look, oversized pink sunglasses, long braids, microphone, jewelry, and clean light background.

[Lyric Timeline Beats & Image Mapping]
- 00:00–02:00 [Beat 1]: "Follow my steps, let's move together" (Image2). Bold neo-brutalist typography collision motion.
- 02:00–04:00 [Beat 2]: "Catch the rhythm, light as a feather" (Image3). Fast scale shifts and feather-light float motion.
- 04:00–06:00 [Beat 3]: "Start a wave, make it last forever" (Image4). Wave kinetic typography with glitch accents.
- 06:00–08:00 [Beat 4]: "One by one, we make it better" (Image5). Progressive typography stack and editorial layout.
- 08:00–15:00 [Beat 5]: She dance (Image6). Energetic dance performance with lyrics dominating visual rhythm.

[Motion & Visual Rules]
Make each lyric visually behave according to its meaning with strong graphic wordplay and semantic motion design. Use bold neo-brutalist typography, fashion editorial layout, glitch accents, analog texture, sharp cuts, fast scale shifts, collision motion, and premium readability. The singer remains present throughout, but the lyrics dominate the visual rhythm.
### 🎬 다크팝 사이버그랑지 필름 스캔 잡지 MV (15초)
```markdown
[Style & Concept]
Dark-pop / cyber-grunge / rap music video with photoreal high-fashion polish and the texture of a scanned film magazine—high contrast without looking cheap. Reference late-1990s to early-2000s indie magazines, photocopies, film scans, underground-music posters, and zine collage.

[Texture & Optics]
Add coarse grain, subtle gate weave, halftone dots, rough print edges, and slight scan misregistration. Keep the edit fast and use hard cuts only—no fades or soft transitions. Match the typographic treatment and surface texture of reference images.

[Timeline Beats]
- 00:00–00:05 [Beat 1]: Three female K-pop/fashion performers in 2000s grunge fur coats step forward under high-contrast flash. Massive bold kinetic 3D typography "DETONATE" explodes behind them with halftone dot grain. Audio Pass: Heavy bass hit and sharp snare drop.
- 00:05–00:10 [Beat 2]: Hard glitch cut into grid zine collage layout! Words "ONE HIT", "MOVE FAST", "HARD CUT", "스타틱 인덱스" stamp down in high contrast print edges. Audio Pass: Distorted vocal slice with metallic percussive hit.
- 00:10–00:15 [Beat 3]: Fast hard cuts between 90s underground music poster layouts. Bold red typography "BASS DROP" and "NOISE INDEX" flashing with slight scan misregistration. Final frame locks into a high-fashion indie magazine cover. Audio Pass: Explosive sub-bass drop and crisp vinyl crackle.
### 🎬 초현실주의 모노크롬 아트팝 옴니 레퍼런스 댄스 필름 (15초)
```markdown
[Omni-Reference Mapping]
Use @Image1 as the man reference.
Use @Image2 as the woman reference.
Use @Image3 as the horse reference.

[Core Concept & Choreography]
Surreal 15-second fashion-film sequence inside a minimalist monochrome blue studio. The woman performs elegant contemporary dance. The man casually walks into frame in a suit with serious expression, awkward ritualistic choreography. The woman never acknowledges him. The horse wanders through studio, runs behind them, appears from impossible places, looks directly into camera. Sometimes all three performers accidentally synchronize for one beat before drifting apart.

[Spatial Kinetic Typography & Motion Graphics]
Throughout sequence, premium kinetic typography appears as part of composition (NOT subtitles), inspired by high-end After Effects title design. Animated words flash for a few frames: "THE GARDENER", "THE DRIVER", "THE HORSE", "THE WOMAN", "KNIFE", "MOVE", "FASTER", "AGAIN", "THE EXIT". Words slam into frame, wrap around dancers, disappear behind bodies, stretch with motion blur, rotate in 3D, pulse with bass. Abstract editorial graphics: animated arrows, blueprint lines, tape labels, halftone textures, chromatic aberration, graphic wipes.

[Ending Resolution & Audio Pass]
Music evolves into strange electronic art-pop with analog synths, mechanical breathing, heavy bass. Final close-up: Woman whispers "Again." Man quietly smiles. Horse suddenly sprints directly toward camera. Word "AGAIN" fills screen before instant cut to black.
### 🎬 유아 교육용 3D 미니멀 숫자 변형 애니메이션 (15초)
```markdown
[Target & Learning Pattern]
15-second animated educational video teaching numbers 1, 2, 3, 4 for children ages 3 to 6.
Learning pattern per number: NUMBER → COUNT → OBJECTS → PLAYFUL ACTION → NUMBER NAME.

[Visual Style & Geometry]
Adorable rounded 3D characters, soft pastel colors, gentle smiling faces, simple recognizable objects. Minimalist tech aesthetic: clean off-white background, studio lighting, soft reflections, rounded geometry, crisp typography. Smooth shape morphing shows how numbers physically become objects.

[Timeline Beats]
- 00:00–00:01 [Intro]: Smiling cloud mascot floats into center. Text "Let's count!". Mascot waves creating gentle ripple. Audio Pass: Soft ripple SFX.
- 00:01–00:04 [Number 1]: Large & small rounded "1". Narrator: "One. One is for One apple." Number 1 stretches & morphs into 1 shiny red apple with smiling face. Displays "ONE" (red highlight). Audio Pass: Soft pop sound.
- 00:04–00:07 [Number 2]: Apple splits into 2 smiling apples rolling side-by-side forming rounded "2". Narrator: "Two. Two is for Two apples." Apples bounce with squash-and-stretch. Displays "TWO" (orange highlight). Audio Pass: Two soft musical notes.
- 00:07–00:10 [Number 3]: 3rd apple joins forming rounded "3". Narrator: "Three. Three is for Three apples." 3 apples hop in sequence. Displays "THREE" (green highlight). Audio Pass: Three rhythmic musical notes.
- 00:10–00:13 [Number 4]: 4th apple pops in forming square and rounded "4". Narrator: "Four. Four is for Four apples." 4 apples form square & bounce once. Displays "FOUR" (blue highlight). Audio Pass: Cheerful chime & sparkles.
- 00:13–00:15 [Recap]: All 4 tile groups line up under "1 2 3 4". Mascot points as each group bounces. Narrator: "One, two, three, four. Great job!". Displays "Great job!". Audio Pass: Warm musical chime.

[Animation Rules]
Keep numbers visible before morphing. Instant countable groups. Gentle squash-and-stretch, soft motion blur, precisely synchronized sound effects. No fast camera moves, no warped numbers, no extra duplicated objects outside exact count.
### 🎬 하이엔드 애니메이션 오프닝 타이틀 시퀀스 (15초)
```markdown
[Reference & Character Setup]
Image1, Image2, Image3 = Overall visual, ensemble, and color-style references.
Image4 = Pink-haired swordswoman, Image5 = Red-haired swordswoman, Image6 = Black-haired swordswoman.
Preserve exact faces, hairstyles, outfits, proportions, colors, and katana weapon designs.

[Visual Style & Optics]
Real high-energy anime opening + premium motion graphics. Palette: black, crimson, wine red, dusty pink, pale ivory, cool gray-blue. Angular split screens, diagonal masks, torn-paper shapes, manga-style framing, ink textures, sakura petals, crimson moon, torii silhouettes. Kinetic tracking shots, whip pans, rapid push-ins, low angles, short orbits. Never show duplicated copies of same character in one shot.

[Audio & Timeline Beats]
Audio Pass: Audio1 as exact timing reference. Synchronize every cut, action, and title reveal to beats. Add subtle sword swishes, cloth movement, and transition impacts.
- 00:00–01:05 [Beat 1]: Crimson line cuts through black as petals burst. Pink/red/black graphic panels snap as crimson moon assembles.
- 01:05–04:03 [Beat 2: Pink Swordswoman]: Runs, plants foot, draws katana in continuous motion. Tracking shot + push-in on eye, hand, blade.
- 04:03–07:02 [Beat 3: Red Swordswoman]: Low-angle tracking shot as she pivots and performs powerful sword strike. Large crimson sun disc + black-red panels strike on heavy beat.
- 07:02–10:02 [Beat 4: Black Swordswoman]: Close-up of crescent earring → orbit camera as she changes stance and redirects blade. Moon masks + precise rhythmic cuts.
- 10:02–12:07 [Climax Ensemble]: All three characters enter together in shared scene forming triangular composition. Crimson moon, torii silhouette, and petals align behind them.
- 12:07–15:00 [Title Reveal]: Alternate rapid close-ups. Final major hit reveals title "MINIMAX" through diagonal masks and sword-line wipes. End on clean ensemble pose.
### 🎬 AAA FPS 밀리터리 게임플레이 & HUD (15초)
```markdown
[Camera & Gameplay Perspective]
First-person POV at eye level with authentic handheld player movement, as if recorded directly from a modern AAA military FPS shooter. Player carries detailed assault rifle with weapon sway, tactical gloves, dynamic reload mechanics, and muzzle flash.

[Environment & Visual Quality]
Modern military base with sandbags, armored vehicles, smoke plumes, burning debris, and blast barriers. Cool daylight mixed with smoke. Ultra-photorealistic AAA graphics, PBR materials, volumetric smoke, and dynamic particles.

[HUD & UI Overlay]
Display realistic modern FPS HUD: central dynamic crosshair, ammo counter with reserve, compass at top, squad status panel, mini-map in corner, health bar, hit markers on impact, kill notification feed.

[Timeline Beats]
- 00:00–00:05 [Beat 1: Firefight]: Aiming down sights (ADS) along roadway. Track enemies, fire controlled bursts. Realistic shell ejection, muzzle flash, recoil, and dust impacts. Audio Pass: Gunshot bursts, metallic shell drops.
- 00:05–00:10 [Beat 2: Tactical Advance]: Lower from ADS, advance cautiously along concrete barriers. Check left/right corners, reacquire targets, fire additional bursts when enemies appear. Audio Pass: Heavy combat boots, tactical gear friction.
- 00:10–00:15 [Beat 3: Push & Clear]: Push forward with deliberate player-controlled movement using cover. Smooth target tracking and realistic recoil. Final kill notification popup. Audio Pass: Distant explosion and radio chatter.
```

### 🎬 스마트폰 바이럴 숏폼 해프닝 (15초 - 노 컷 원테이크 핸드헬드)
```markdown
[Style & Footage Aesthetic]
15-second, 16:9 vertical, continuous single-take video that looks like authentic smartphone footage accidentally captured by a passerby in a city park. Overcast natural daylight, subtle handheld shake, limited phone stabilization, occasional autofocus adjustment, and realistic smartphone compression. The absurd event is filmed with a completely serious, unscripted documentary feeling.

[Timeline Beats & Action Mechanics]
- 00:00–03:00 [Handheld Medium Shot]: A middle-aged man wearing a dark business suit and tie crouches beside the stone edge of a pond. With a completely serious expression, he slowly scatters pieces of bread from a paper bag to several ordinary koi. Small ripples spread across the water as the fish gather in front of him. Audio Pass: Natural park ambient, water ripples.
- 03:00–07:00 [Camera Instinctively Moves Closer]: An abnormally huge orange-and-white koi suddenly surges out of the murky water, briefly lifting its upper body above the surface and biting down on the entire bread bag in the man’s left hand. He freezes for half a second, then grips the bag with both hands and leans backward. Startled, the person filming steps back. The image briefly loses focus before locking onto the man and the giant fish again. Audio Pass: Water splash, sudden gasping gasp.
- 07:00–11:00 [Close Handheld Action Shot]: The giant koi pulls violently toward the deeper part of the pond. The wet paper bag stretches, the man’s arms tense, and his leather shoes slide repeatedly across the wet stone. His knee strikes the edge of the pond. He tries to brace himself with his right foot, but the sole loses traction and his center of gravity moves past the edge. Water, pieces of bread, and fallen leaves scatter from the force as the camera operator hurriedly moves sideways. Audio Pass: Wet paper tearing SFX, heavy shoe sliding on wet stone.
- 11:00–15:00 [Impact and Final Hold]: The paper bag suddenly tears. The man loses all support and pitches forward into the pond, creating one heavy, realistic splash. The camera quickly tilts downward while keeping the center of the pond visible. The man resurfaces with duckweed covering his head and his wet tie stuck across his face. The giant koi calmly swims past him with the remains of the bread bag still in its mouth. The camera holds on the man’s stunned expression while the koi casually swims away beside him. Audio Pass: Heavy realistic splash, water dripping.

[Consistency & Constraints]
Keep the man’s face, dark suit, tie, and paper bag visually consistent throughout. The koi must retain the same orange-and-white markings and enormous size. The pulling, sliding, loss of balance, and fall must show believable weight, inertia, traction, and water displacement. Natural park ambience and a realistic splash only. No dialogue, no subtitles, no music. Avoid cuts, character teleportation, changes in the fish’s size, extra limbs, and cartoonish acting.
```

### 🎬 클레이메이션 스톱모션 애니메이션 (10초)
```markdown
[Material Texture & Clay Physics]
Claymation stop-motion animation. Visible fingerprints, tool marks, and material imperfections in sculpted clay. Slightly stepped, handmade 24fps movement. Sea is sculpted clay with rolling modelled waves and white clay foam.

[Animation Storyboard]
A massive sculpted clay whale breaches from a stormy clay sea, rising in a slow-motion arc above the waves with body fully extended and clay water sheeting off flanks. At top of arc, it rolls onto one flank, hangs for a beat, then falls back toward surface. Midair, camera sweeps beneath its belly in a bold dynamic move revealing vast churning clay ocean below. Crashes down as white clay foam bursts outward across frame.

[Audio Pass]
Deep rush of water, wind, dull slap of clay on clay, distant gulls. Composition: subject centered within central third of frame.
### 🎬 초현실 코인빨래방 미니어처 바다 (15초)
```markdown
[Format & Setting]
15-second 16:9 surreal live-action scene inside a quiet laundromat at night. Cold flickering fluorescent lights, wet glass reflections, deep blue storm light inside washer. Photoreal phone-camera texture. Miniature ocean exists strictly inside washing machine drum.

[Timeline Beats]
- 00:00–03:00 [Beat 1]: Slow handheld push toward a running front-loading washing machine drum. Audio Pass: Washing-machine rumble, water splashes.
- 03:00–06:00 [Beat 2]: Inside the drum, water morphs into a miniature stormy ocean with churning waves, lightning strikes, and a tiny operating lighthouse. Audio Pass: Distant thunder, mystery drone building.
- 06:00–11:00 [Beat 3]: Lighthouse beam shines brightly through wet glass door as storm grows stronger inside drum. Audio Pass: Swirling water and intense drone.
- 11:00–15:00 [Beat 4]: Washer door suddenly pops open! Miniature storm vanishes and only ordinary wet laundry falls onto tile floor. Audio Pass: Loud door click, mystery drone stops abruptly, wet laundry hitting floor.

[Camera & Constraints]
One continuous handheld push-in ending on falling laundry. Photorealistic laundromat. No people, text, subtitles, logos, watermarks, monsters, or cartoon styling.
### 🎬 21:9 아나모픽 사이버펑크 해커 홀로그램 스트레스 테스트 (15초)
```markdown
[Cinematic Setup & Optics]
Cinematic anamorphic 21:9 (2.35:1) 15s 24fps. Subject: young man in dark t-shirt and black face mask seated at desk, hands on keyboard (only living entity in frame).
Color Palette: Near-black base. Teal-cyan = panel frames/wireframe, Spring green = data/text, Amber = alert status, Ultraviolet = connection lines. Max 2 accents at once.
Lighting & Focus: Screens are sole light source after 2.5s. Face lit from below, shadow climbing upward under brow. Soft teal rim on shoulder. Mid-plane panels stay sharp, face slightly soft, background bokeh soft. Crushed blacks, cool blue shadows, desaturated cooled skin.

[Physics & Glitch Laws]
Depth Law: Panels anchored in room void. Motion Law: Panels blur ONLY while in transit, razor-sharp when settled. Glitch Law: Two-frame tearing occurs ON INTERFACE CONTENT ONLY. Face, hands, mask, and bokeh NEVER tear or displace.

[Phase Breakdown & Timeline]
- 00:00–02:05 [Phase 1 - Real]: Dark room, one desk lamp. Man sits, hands on keys. Presses one key. Teal line crawls out across desk surface.
- 02:05–05:00 [Phase 2 - Transport]: Unbroken shot. Camera pushes in on back. Room surfaces resolve into wireframe, solid material falls away into void. Holographic panels ignite in sequence. He stays, room leaves.
- 05:00–08:00 [Phase 3 - Reveal]: Slow orbit right. He turns head looking at stacked panels. Screen glow climbing face. POV of panels receding into black.
- 08:00–13:00 [Phase 4 - The Hack]: Rapid cut on beat! Hands slam keys. Panels flip green to amber. 6 panels tear for 2 frames. Panels multiply in wave. Camera pushes through panel glass. Ultraviolet lines shoot. Hard tearing on panels (face untouched). Total 1-second freeze stillness.
- 13:00–15:00 [Phase 5 - Lock]: Panels snap inward & lock into single wall of light. Shockwave ripples outward. Camera recoils & locks. One amber status line reads across central panel. Hold to black.

[Negative Prompt]
No other people, no desk clutter, no cables, no plants, no subtitles, no watermarks, no logos, no smoke, no dust, no lens flare, no orange grade, no glitching on face/hands/mask.
### 🎬 루미 명언 철학적 페이퍼 아트 시네마틱 타이포그래피 (15초)
```markdown
[Concept & Aesthetic]
Visually stunning 15s 16:9 cinematic typography video for Rumi quote: "Don't be satisfied with stories, how things have gone with others. Unfold your own myth."
Palette: Deep lapis blue, aged ivory paper, black ink, muted copper, luminous gold. Elegant editorial design influenced by illuminated manuscripts, geometric architecture, and folding paper.

[Typography Rules]
Refined serif typography with small uppercase accents. Display exact quote phrases only. Each phrase has one primary animation, then becomes solid and motionless upon formation.

[Timeline Storyboard]
- 00:00–03:05 [Beat 1]: Closed ivory manuscript floating in vast lapis-blue space opens to blank pages. Copper light passes revealing: "DON'T BE SATISFIED WITH STORIES," through page-turn mask. Audio Pass: Quiet room tone, paper movement, low plucked string.
- 03:05–07:00 [Beat 2]: Page divides into corridor of repeating rectangular frames with small anonymous silhouette walking circular path. Reveal: "HOW THINGS HAVE GONE WITH OTHERS." Typography detaches and settles in foreground. Audio Pass: Restrained rhythmic pulse.
- 07:00–10:05 [Beat 3]: Corridor stops. Blank sheet floats toward camera and unfolds along geometric creases into paper mountains, stairways, arches, and golden horizon. Reveal: "UNFOLD YOUR OWN MYTH." ("MYTH" rises in monumental gold). Audio Pass: Wind, resonant strings, widening harmonics.
- 10:05–12:00 [Beat 4]: Paper landscape continues unfolding into vast night sky. Gold paths become constellations as repeating frames collapse. Audio Pass: Harmonic resonance.
- 12:00–15:00 [Beat 5]: Resolve to clean lapis-blue background with thin gold fold line. Display full centered quote with "Unfold your own myth" set in gold and "RUMI" below. Final composition holds perfectly still and readable. Audio Pass: One warm strike and sustained open chord.
### 🎬 초고속 스텔스 전투기 광학 미채 은폐 VFX (10초)
```markdown
[Format & Identity]
10-second 16:9 photoreal cinematic wide-shot flyby of a stealth aircraft activating optical camouflage at extreme speed.
Identity: Wide tailless delta wing, sharp faceted edges, flat wedge nose, recessed dark cockpit, matte charcoal surface, twin buried exhausts, rigid non-morphing geometry.

[Camera & Lighting]
One continuous wide lateral tracking shot. Fast pan tracking, broad environmental scale, strong background parallax, subtle handheld vibration, realistic motion blur. No close-up, no chase-cam. High-altitude bright daylight, cool blue sky, cloud field, natural haze.

[Timeline Beats]
- 00:00–02:00 [Beat 1]: Vast open sky above clouds. Stealth aircraft enters from far left, racing laterally across wide frame at extreme speed. Audio Pass: High-altitude wind rush, jet roar.
- 02:00–04:00 [Beat 2]: Camera performs fast controlled tracking pan. Background parallax emphasizes extreme velocity. Audio Pass: Powerful Doppler flyby sound.
- 04:00–06:00 [Beat 3]: Optical camouflage sweeps from nose across wings. Solid aircraft rapidly vanishes without slowing down or changing trajectory. Audio Pass: Brief vacuum-like sound as camouflage activates.
- 06:00–08:00 [Beat 4]: Camera tracks same trajectory. Invisible delta wing remains perceptible as sky/clouds inside exact volume ripple and bend like concentrated heat haze refraction. Audio Pass: Low sub-bass pulse, metallic air textures.
- 08:00–10:00 [Beat 5]: Refractive aircraft streaks toward horizon leaving narrow turbulent distortion wake before exiting frame. Audio Pass: Audio fading into low sustained tone.

[Negative Prompt]
Do not show empty sky after cloaking. Maintain coherent delta-wing background refraction inside exact volume. No glowing outline, force-field bubble, pixel dissolve, smoke, teleportation, or reappearance. No text, subtitles, logos, or watermarks.
### 🎬 3D 그래픽노블 스타일 러닝 브랜드 다이내믹 광고 (15초 - 9:16)
```markdown
[Style & Concept]
15-second 9:16 vertical stylized 3D animation blended with graphic-novel visuals for dynamic sports advertisement ("Outrun the Static"). Vibrant neon and daylight contrast, expressive motion blur, bold geometric lighting, fluid movement. Polished 3D animation (Fortnite/Spider-Verse aesthetic).

[Character & Narrative]
Urban runner frozen in slouching stance inside monochrome grey static city. Floating grey glitch words "SOMEDAY", "TOO TIRED", "NOT TODAY" orbit like heavy fog. Runner stomps foot, tightens laces, cyan electric energy flares from shoes, and explodes into an all-out sprint, shattering negative words into glowing neon sparks.

[Timeline Beats & Camera]
- 00:00–03:00 [Beat 1 - Hook]: Monochrome grey street filled with glitch static. Frozen runner surrounded by orbiting grey words "SOMEDAY", "TOO TIRED", "NOT TODAY". Fast camera push-in. Overlay Text: "STUCK IN THE STATIC?". Audio Pass: Glitch hum ambient.
- 03:00–06:05 [Beat 2 - Flare]: Rapid macro close-up of shoe sole hitting pavement & laces snapping tight! Cyan energy sparks out. Posture transforms from sluggish to razor-sharp. Audio Pass: Sharp lace snap, heavy bass drop at 3.0s.
- 06:05–11:05 [Beat 3 - Sprint Shatter]: High-speed parallel side-tracking run! Each footstrike shatters floating 3D words into glowing neon sparks and transforms dreary alley into vibrant motion light-trails. Audio Pass: Heavy footfall impacts, glass shatter FX synced to beat.
- 11:05–15:00 [Beat 4 - Summit Climax]: Runner leaps through final static wall into warm golden sunlight over elevated city skyline. Fast pullback as they land empowered under bright skies. Bold text snaps onto screen: "BREAK THE STATIC / RUN YOUR DAY". Audio Pass: Wind rush, crisp final bass thump.

[Negative Prompt]
photorealistic characters, slow opening, dramatic trailer tone, long pauses, cluttered camera motion, unreadable text.
### 🎬 하이패션 사막 메탈릭 드레스 천 물리 연산 (12초)
```markdown
[Style & Cinematic Quality]
12s cinematic luxury fashion ad, 4K, 24fps, ultra-photorealistic. Vogue-style editorial. High-fashion model wearing a flowing iridescent metallic gown walking along a minimalist desert runway at golden hour.

[Lighting & Optics]
HDR lighting, golden sun flare, shimmering specular reflections on metallic fabric, soft ambient wind. Cinematic shot flow: aerial wide -> side tracking -> orbit camera -> macro detail close-up -> empowering hero shot.

[Cloth Physics & Motion Rules]
Realistic fluid cloth physics, realistic weight and flowing motion of iridescent metallic fabric responding to model's stride and natural wind. Seamless continuity, perfectly consistent face and outfit, no flicker, no warping, no extra limbs, fade to black.
### 🎬 하이스피드 프리미엄 푸드 광고 (4계절 매치 컷 & 센터 락 렌더링 - 15초)
```markdown
[Style & Concept]
Premium food commercial. Extreme macro shot of a single ripe red strawberry falling vertically toward a white ceramic bowl. Photorealistic food texture, high-speed Phantom Flex product cinematography, clean studio commercial lighting.

[Center Lock & Match Cut Mechanics]
Before landing, the background environment changes through four seamless seasonal match cuts:
1. Sunlit spring greenhouse
2. Hot summer picnic
3. Warm autumn kitchen
4. Candlelit winter dining room
Rule: The strawberry stays in EXPLICITLY THE SAME screen position, size, orientation, and downward speed through every transition.

[Fluid Splash Climax & Audio Pass]
In the winter scene, the strawberry lands in fresh white cream, sending one graceful crown-shaped splash upward.
Audio Pass: Each season has distinct environmental sound (birds -> cicadas -> crackling hearth -> quiet winter chime), connected by one continuous fluid musical phrase.
No hands, no labels, no extra fruit.
### 🎬 동양 수묵화 붓터치 & 무협 초식 타이포그래피 (15초 - 1,987자 마스터피스)
```markdown
[Reference & Core Concept]
15秒 | 16:9 | 1440p | 24fps [核心概念 · 全墨]
The world is a living Sumi-e ink wash painting on bright Xuan paper background (#F2EDE0). The floor is blank paper. She, her ink, and everything summoned consist of brushstrokes. Hair ends, robe edges, and effect boundaries disperse into flying white and ink threads. Palette: Ink Black (#14161A), Paper White (#F2EDE0), Vermilion Red (#C6262E).

[Character & Anatomy Lock (High Priority)]
Strictly reference @image1. Single character throughout: exactly two arms, two hands, five fingers per hand. Speed-sealing and motion blur trails MUST NOT render as extra limbs. Translucent ink beasts/shadows must remain semi-transparent ink creations with no face/clothing detail.
Features: Wild black wavy hair ending in ink brushstrokes, crimson eyes, quiet sharp gaze, pale skin. White wide-sleeve haori with ink splatters & vermilion spots, inner black, crimson collar/belt, 4 glowing red rune rings on right forearm, floating talismans. Bone-white Oni mask on left head with vermilion stripe.

[Composition & 4 Ink Shades]
Follow traditional ink painting layout: Over 50% of the frame MUST remain empty paper space (Negative Space) in every frame.
Four distinct ink shades: Burnt Ink (pure black), Dark Ink, Light Ink, Clear Ink (water trace).
Timeline ink progression: Start (Clear/Light) -> Talisman Array (Dark) -> Ink Dragon (Burnt/Dark) -> Masking Phase (Deeper) -> Combo Phase (Burnt vs White High Contrast) -> Ultimate Phase (All 4 shades) -> Ending Phase (Fade back to Clear Ink).

[Martial Arts Calligraphy Stamp System (招式名)]
Action name cards stamped in bold cursive/kaishu calligraphy with physical paper debossing & vermilion red square seals behind character:
- 0.8s 「墨」 (Vertical, right third)
- 2.6s 「符」 (Slam from left)
- 4.8s 「龍」 (Slam from top)
- 7.0s 「鬼」 (Center, thickest stroke)
- 9.2s 「墨」 (Rendered in negative space paper white within ink splatter)
- 11.0s 「百鬼夜行」 (Horizontal 4 characters across screen, paper shakes on each stamp)
- 13.8s Bottom-right small vermilion red seal stamp reading "Cia0" (Number 0 at end), pressing into paper with subtle ink bleed. Hold to fade.
### 🎬 할리우드 블록버스터 IMAX 수성 소용돌이 VFX 타이포 리빌 (10초)
```markdown
[Camera trajectory & Environment Scale]
Epic scale, impossible speed, Hollywood blockbuster, IMAX cinematography.
The camera launches vertically from the surface of the ocean and rockets upward between towering tropical cliffs as enormous waterfalls crash on both sides. It narrowly avoids collapsing rock arches before bursting through clouds into brilliant sunlight.

[Atmospheric Vortex & Water Text Compression Mechanics]
Moisture, mist, and billions of illuminated water droplets spiral rapidly behind the camera, creating a colossal atmospheric vortex. The liquid cyclone naturally compresses and shapes itself into physical 3D water text reading "ASCEND" before exploding into a dazzling halo of water droplets and sunlight.

[Visual Quality & Lighting]
Photorealistic water physics, volumetric cloud lighting, lens moisture, dynamic refraction, high speed camera movement, IMAX 70mm film polish.
### 🎬 3x3 그리드 스토리보드 옴니 레퍼런스 비디오 애니메이션 (15초)
```markdown
[Visual Reference & Grid Lock]
Epic desert sci-fi, harsh golden-hour light, volumetric sand haze, anamorphic lens flares, subtle handheld drift, heavy atmospheric particles, 35mm film texture.
Use the provided 3x3 grid image (@Image1) as the ONLY visual reference. Lock the exact same character (face, scars, green eyes, headscarf, desert armor, cape) and environments from every panel. Do not invent new outfits or faces.

[Timeline Storyboard & Panel Mapping]
- 00:00–01:07 [Panel 1 - Wide Establishing]: Lone figure walking across endless dunes toward twin massive suns. Heat shimmer, long shadow stretching behind her.
- 01:07–03:04 [Panel 2 - Extreme Close-up]: Her scarred face fills the frame. Eyes locked on camera, wind tugging dirty headscarf, grit on skin, unblinking intensity.
- 03:04–05:01 [Panel 3 - Tight Detail Insert]: Gloved hand grips rusted multi-tool weapon. Metal catches orange light, cable dangling, fingers adjusting grip with quiet precision.
- 05:01–06:08 [Panel 4 - Low Wide Silhouette]: Towering industrial structure rises against giant sun. Dust storms swirl at base, ancient and oppressive scale.
- 06:08–08:05 [Panel 5 - Medium Tracking]: She advances through thick sandstorm, lower face wrapped, cape and scarf whipping hard. Eyes visible above cloth, determined stride.
- 08:05–10:02 [Panel 6 - Hero Wide]: She stands alone on rocky outcrop, cape flowing, surveying empty desert below. Wind howls, silhouette sharp against hazy sky.
- 10:02–11:09 [Panel 7 - Dynamic Tracking + Low Angle]: She charges down steep dune face, boots kicking up thick clouds of sand, body leaning forward with full momentum.
- 11:09–13:06 [Panel 8 - Macro Atmospheric]: Golden sand particles explode and float in extreme slow motion, backlit by blazing sun, pure texture and light.
- 13:06–15:00 [Panel 9 - Intimate Close-up]: Inside dark cave, shafts of light cut through. She sits against rock, armor dusted, breathing controlled, eyes sharp watching entrance.

### 🎬 5개 이미지 멀티모달 연동 SF 사막 버기카 추격 액션 (15초 - 마스터피스)
```markdown
[Multimodal 5-Image Reference Mapping]
- Image 1: Strict facial identity (female racer, dark tied-back hair, amber goggles, dusty skin, black tactical suit, shoulder armor).
- Image 2: Full costume, body proportions, armored black dune buggy, tire scale, exposed suspension, cyan headlights, roll cage, Outpost 07 background.
- Image 3: Pursuit drones action reference, vehicle speed, dust plumes, fire, debris, chase intensity, camera proximity.
- Image 4: Outpost 07 environment (rusted towers, pipelines, bridges, rocky terrain, distant mountains, sunset atmosphere).
- Image 5: Cockpit POV & driving posture (steering wheel, open roll cage, goggles, gloves, interior).

[Timeline Action Sequence]
- 00:00–02:05 [Phase 1 - Aerial Entry]: Open on Image 4 aerial view of Outpost 07 at sunset. Buggy bursts beneath pipeline throwing dust plume. Audio: Dry wind, distant machinery, engine approaching.
- 02:05–05:00 [Phase 2 - Cockpit Alert]: Cut to Image 5 tight cockpit shot. Vehicle vibrates, hands firm on wheel, red warning light reflects as targeting alarm sounds.
- 05:00–08:00 [Phase 3 - Drone Attack & Drift]: Cut to Image 3 low tracking shot. 3 drones fire into sand causing dirt eruptions. Buggy steers sharply around impact with realistic suspension lean and wheel drift.
- 08:00–11:00 [Phase 4 - Handbrake Slide & Drone Crash]: Racer pulls mechanical handbrake rotating vehicle through narrow passage. Drone clips overhead pipe and tumbles into sand behind. Audio: Tire scrape, metal tearing, failing rotors.
- 11:00–13:00 [Phase 5 - EMP Shockwave]: Wheel macro shot as sand fires backward. Racer flips guarded switch emitting restrained blue-white EMP wave disrupting remaining drones.
- 13:00–15:00 [Phase 6 - Outpost Leap Climax]: Low frontal hero shot as buggy clears gate & launches from ridge. Tight close-up on racer's face (Image 1) during jump. Hard landing, engine roars, sharp cut to black.

[Visual & Audio Constraints]
Realistic CGI integration, warm orange sunset light, restrained steel-blue tech accents, native stereo audio (combustion engine, tire friction, suspension rattles, drone rotors, heavy bass impact on landing). No subtitles, logos, extra racers, weightless motion, or camera spins.
### 🎬 킨츠기 바록 검 재생 수묵 무한 루프 (15초 - Seamless Loop)
```markdown
[Format & Concept]
15s 16:9 1440p 24fps seamless loop video.
The world is a fusion of Sumi-e ink wash painting and photorealistic glass. Sky is painted in translucent blue-gray ink with ink clouds and golden foil ribbons floating.
Character Lock: Strictly reference @image1. Blue-gray wavy short hair, coral vermilion wide-sleeve robe, dark inner lining, gloves, holding a baroque silver-gold sword.

[Seamless Loop & Kintsugi Mechanics]
From frame 1, the sword blade is covered in fixed golden kintsugi veins from previous shatters. The sword splits along exact same gold veins, fragments scatter, and molten gold flows back into the same cracks to restore the exact identical form. Last frame must match first frame perfectly.

[Lens & Paper Interaction]
- 0.9s: Fine glass crack spreads across lens when sword splits, slowly healing and vanishing by 13.8s.
- 3.2s: Ink drops from sword arc splash directly onto lens, slowly dispersing and drying completely by 13.8s.
- 7.0–8.8s: Lens sinks into dense ink cloud and breaks surface at 8.8s.
All effects clear completely by 13.8s to allow seamless 15s looping.
```

### 🎬 하이엔드 럭셔리 퍼포먼스 5-Scene 연속 전환 광고 (15초)
```markdown
[Format & Style]
15-second 16:9 luxury perfume commercial video. Ultra-realistic macro reflections, golden particle lights, high-end commercial cinematography.

[Timeline Scene Flow]
- Scene 1 (0–3s) [Luxury Reveal]: Perfume bottle slowly emerges from darkness on glossy black pedestal. Soft golden beams reveal crystal glass with volumetric mist. Extreme macro shot. Audio Pass: Deep warm bass pad.
- Scene 2 (3–6s) [Precision Details]: Extreme close-up as golden liquid gently swirls inside. Camera orbits capturing glass craftsmanship and sparkling highlights. Audio Pass: Crystal chime sound.
- Scene 3 (6–9s) [AI Transformation]: Bottle seamlessly dissolves into glowing golden particles before reforming into futuristic luxury edition maintaining proportions. Audio Pass: Fluid particle transformation SFX.
- Scene 4 (9–12s) [Environment Transition]: Without a single cut, background transforms from dark studio into futuristic neon metropolis while bottle stays consistent. Audio Pass: Rhythmic synth build.
- Scene 5 (12–15s) [Hero Finale]: Slow-motion hero shot of perfume bottle rotating as golden particles float around. Clean logo reveal, premium ending. Audio Pass: Majestic resolution chime.
```

### 🎬 사헬 라디오 오퍼레이터 대피 교량 전쟁 스릴러 (15초)
```markdown
[Format & Setting]
15-second 16:9 photoreal live-action war thriller set in a Sahelian city at blue-hour dawn. Grounded, human, urgent suspense.

[Reference Control]
- Image 1: Locked AMINA identity (face, cropped hair, deep brown skin, navy field jacket, earpiece, satchel, analogue radio).
- Image 2: Locked environment (concrete bridge, dry riverbed, low-rise city, dusty atmosphere, cool blue shadows, amber dawn).

[Timeline Story Beats]
- 00–02s [Channel Offline]: Dark communications room. Amina grips radio as red lights pulse. Automated voice: "Emergency channel offline."
- 02–04s [Bridge Closing]: Wide aerial-oblique view. Civilians cross bridge through dust as checkpoint signal flickers red.
- 04–06.5s [Corridor Run]: Low handheld tracking behind Amina running through damaged service corridor as emergency lights flash.
- 06.5–09s [Rooftop Alignment]: Flashback to 2 minutes earlier. Medium side profile as Amina rotates antenna and connects backup power under first amber sunlight.
- 09–12.5s [Transmission]: Rapid cross-cut montage (dial locks -> antenna aligns -> cables vibrate -> red signal flashes). Amina speaks: "Channel Seven, keep the bridge open."
- 12.5–15s [Signal Restored]: Audio drops. Radio tone clears, signal turns steady green. Civilians continue crossing. Amina exhales on rooftop. Cut to black.
### 🎬 80년대 레트로 시티팝 애니메이션 데스밸리 스케이트보드 MV (15초)
```markdown
[Reference & Visual Style]
80s retro anime citypop aesthetic. Use @Image1 as sole reference for 2D hand-drawn anime style, character identity (dark curly hair, red headband, blue jacket, denim shorts, high-top sneakers), and desert highway background with palm trees & mountains.

[Audio & Lyric Syncing Pass]
Audio Pass: Native 80s synthpop / Fleetwood Mac "Dreams" vibe with vocal lyrics:
"Now here you go again you say... you want your freedom... Well who am I to keep you down?"

[Camera Arc & Timeline Beats]
- 00:00–03:00 [Beat 1 - Wide Frontal Tracking]: Wide front shot tracking backward. Girl skateboards down open Death Valley road at golden hour. Glides smoothly, raises both hands in the air, wind blowing through hair.
- 03:00–06:00 [Beat 2 - Medium Close-up Singing]: Medium close-up. She sings "Now here you go again you say...". Eyes close briefly, soft smile, hands raised. Intimate framing.
- 06:00–09:00 [Beat 3 - 360 Camera Orbit & Side Shot]: Camera smoothly orbits around her as she sings "you want your freedom...". Transitions to side angle showing open road and mountains beside her.
- 09:00–12:00 [Beat 4 - Rear Orbit to Low Crouch]: Camera spins into back shot showing hands lifted, then reaches side shot as she sings "Well who am I to keep you down?". She lowers into playful crouched skateboard pose riding close to board with bent knees.
- 12:00–15:00 [Beat 5 - Aerial Crane Outro]: She lifts back up standing, moving to rhythm. Camera cranes upward into aerial view spinning slowly, revealing vast Death Valley landscape. Final wide sense of freedom.
```
```

---

## 참고 문서
* [SKILL.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/AI-video-prompt/SKILL.md): 실사형 비디오 프롬프트 생성기 (Realistic Video Prompt Generator)


