---
name: realistic-video-prompting
description: AI 비디오 생성 모델(Kling 3.0, Runway Gen-3, Seedance 등)을 위한 사실감(Realism) 극대화, AI 느낌 배제, 다큐멘터리 및 명작 영화 질감의 구조화된 비디오 프롬프트를 작성합니다.
version: 1.2.0
author: zhouwei713 & zhouwei713_custom
license: MIT
metadata:
  hermes:
    tags: [ai-video, prompt, realistic-video, kling, runway, seedance]
---

# 사실적인 비디오 프롬프트 생성기 (Realistic Video Prompt Generator)

사용자의 모호한 아이디어를 고밀도의 정교하고 인위적인 느낌이 제거된 실사급 구조화 비디오 프롬프트로 변환합니다.

## 核心哲学 (핵심 철학)

고품질 실사형 비디오 프롬프트의 본질은 다음 질문에 답하는 것입니다.
> **"이 영상은 누가(Who), 어떤 장비로(What camera), 어떤 시대에(When), 무슨 목적으로(Why) 촬영한 것인가?"**

AI 비디오 모델은 특유의 기본 미학(완벽한 대칭, 짐벌 스테빌라이징, 광택 있는 3D 질감, 상업적 색감)으로 영상을 자동 보정하는 경향이 있습니다. 이를 억제하기 위해 강력한 부정 문구(Negative Constraints)와 실제 물리 반응을 명시해야 합니다.

---

## 💡 고급 물리 및 표기 연출 기법 (Advanced Motion & Micro-Expression Rules)

### 1. 🎬 AI 물리 연산 구동 영문 키워드 (Physics Simulation Keywords)
AI 모델(Kling, Runway 등)이 어색한 동작이나 공중 부양을 하지 않고 실제 아날로그 물리학을 적용하도록 프롬프트에 주입하는 영어 물리 지시어입니다.

* **중력 및 체중 이동**: `realistic physical gravity`, `center of mass shift`, `heel-first footstrike` (발뒤꿈치 선 착지)
* **의류 및 머리 관성**: `natural fabric drape`, `realistic cloth dynamics`, `hair movement inertia` (머리카락 관성)
* **유체 및 기체 물리학**: `liquid viscosity and surface tension` (점성 및 표면장력), `volumetric water splash dynamics`

### 2. 🎭 4중 미세 표기 연기 지시법 (4-Part Micro-Expression Acting)
배우의 단순한 감정("슬퍼한다") 대신, AI가 세밀한 얼굴 근육과 시선을 연산하도록 4단계 결합 방식으로 연기를 지도합니다.

* **구조**: `[시선 착지점(Eye Landing)] + [눈썹/눈 주변 변화] + [입술 및 호흡 멈춤] + [손/몸의 미세 반응]`
* **실전 예시**: 
  - `gaze fixed on the letter, brows furrowing with mounting dread, sharp intake of breath with trembling lips, hands freezing mid-air`
  - (시선은 편지에 고정, 커지는 공포로 눈썹이 일그러짐, 떨리는 입술로 거친 호흡을 삼킴, 손은 허공에서 순간 정지)

### 3. 📹 DV 16mm 아날로그 결함 주입 및 유기적 조명 연출 수칙 (DV 16mm Camcorder & Imperfection Optics)
AI 특유의 가짜 CG 감성(AI Slop/Plastic Look)을 완벽히 지우고, 광고/드라마/영화의 감성적인 현장감과 리얼리티를 부여하는 3대 필수 연출 지시 수칙입니다.

* **인간적 카메라 결함(Human Imperfections Injection)**: 완벽하고 깨끗한 렌더링 대신 일부러 미완성된 듯한 구식 캠코더 조작 실수를 프롬프트에 주입하여 실제 테이프 필름 데이터셋을 연산하도록 유도합니다.
  - *필수 키워드*: `DV 16mm camcorder aesthetic`, `slow autofocus lag/hunting`, `awkward micro-zoom`, `accidental face crop`, `natural handheld micro-shake`, `uneven framing`
* **아날로그 필름/테이프 광학 텍스처 (Analog Tape Texture & Optics)**:
  - *필수 키워드*: `Soft analog tape texture`, `faint tape grain`, `blooming highlight glow`, `auto-exposure flicker`, `muted soft contrast`, `lifelike natural skin tone`
* **유기적 공간 조명 다이내믹스 (Dynamic Organic Lighting Shifts)**: 고정된 조명 대신, 장소 이동에 따라 광원과 색온도가 시시각각 전환됨을 선언하여 반사광과 깊이감을 인위적이지 않게 연산시킵니다.
  - *지시 템플릿*: `Lighting shifts naturally by location: [장소1 광원] → [장소2 광원] → [장소3 광원]`
* **보이스오버(VO) 이원화를 통한 립싱크 에러 방지**:
  - 인물이 직접 말하는 장면 대신 반성적인 보이스오버(Reflective Voiceover) 서사를 채택하여 AI 비디오 렌더링 시 고질적으로 발생하는 입 모양 뭉개짐(Lip-sync glitch)을 원천 차단합니다.

### 3-1. 📱 Old iPhone 1x 렌즈 기반 폰카 극실사 8대 통제 기법 (Old iPhone 1x Phone-Cam Photorealism)
AI 특유의 미끈거리는 3D CG 렌더링(Plastic Slop Look)을 완전히 지우고, 사용자가 직접 일반 스마트폰으로 찍은 듯한 극강의 현장감과 실사감을 구현하기 위한 **8대 구조화 통제 법칙**입니다.

1. **카메라 optical 렌즈 지정 (`Lens Optics`)**:
   - `Old iPhone 1x standard lens`: 왜곡 없는 저화질 폰카 1배율 표준 렌즈 명시
2. **매체 결함 & 압축 노이즈 (`Media Texture`)**:
   - `heavy constant noise/compression, unedited low-quality phone footage`: 센서 노이즈와 비디오 압축 결함 주입
3. **고정 앵글 배치 (`Fixed Anchor Framing`)**:
   - `static propped-on-sink angle` / `static propped-on-table angle`: 폰을 세워둔 거치 앵글로 AI의 화면 붕괴 통제
4. **현실적 조명 왜곡 (`Harsh Realistic Lighting`)**:
   - `harsh cool-green fluorescent lighting` / `uneven dim tungsten bulb`: 영화 같은 예쁜 조명 대신 칙칙한 현실적 조명 사용
5. **레퍼런스 제한 (`Material Mapping`)**:
   - `Person from Image1: face and hairstyle must match exactly. Ignore reference outfit/background/pose`: 오직 얼굴/헤어만 계승
6. **실제 모공 & 생리 디테일 (`Physical Realism`)**:
   - `Real pores, sweat, flushed skin, wet hair`: 피부 모공, 땀, 붉어진 피부, 젖은 머리칼 물리반응 명시
7. **현장 울림음 오디오 (`Spatial Phone Audio`)**:
   - `Bathroom echo, tap/splash, heavy breathing, muffled voice`: 폰 마이크 특유의 공간 울림과 숨소리
8. **강력한 부정어 차단 (`Phone-Cam Negative Constraints`)**:
   - `No BGM, text, cinematic grading, beauty filter, fisheye, distortion, vignette, scene skipping`: BGM, 뷰티 필터, 시네마틱 색보정을 완전 금지하여 가짜 느낌 차단

#### 📋 폰카 극실사 템플릿 (Phone-Cam Realism Template):
```markdown
Person from Image1: face and hairstyle must match exactly. Ignore reference outfit/background.

16s [Location]: Old iPhone 1x standard lens, static propped-on-[surface] angle, heavy constant noise/compression, harsh cool-green fluorescent lighting, unedited low-quality phone footage.

Timeline Beats:
- 00:00–00:03: [Action 1: Entrance/Approach]
- 00:03–00:07: [Action 2: Physical Interaction/Water/Wiping]
- 00:07–00:11: [Action 3: Mirror Glance/Resting]
- 00:11–00:14: [Action 4: Self-Muttering/Muffled Voice "...dialogue..."]
- 00:14–00:16: [Action 5: Exit/Freeze mid-turn]

Audio Pass: Spatial room echo, physical interaction sounds, heavy breathing, muffled voice. Real pores, sweat, flushed skin, wet hair.

Negative Constraints: No BGM, text, legible signage, cinematic grading, beauty filter, fisheye, distortion, vignette, scene skipping, or cut consolidation.
```

### 3-2. 📹 2000년대 초반 MiniDV 캠코더 & 파운드 푸티지 결함 미학 수칙 (Early-2000s Consumer DV & Found Footage)
완벽하고 차가운 현대 4K/8K 디지털 질감과 AI 특유의 3D CG 느낌(Plastic Look)을 영구 박멸하고, 2000년대 초반 가정용 캠코더(소니 핸디캠, 파나소닉 MiniDV 등)로 실제 친구/가족이 찍은 듯한 극강의 레트로 실사감(Found Footage)을 구현하는 공식입니다.

#### 1. 광학 및 센서 결함 6대 수칙 (Optics & Sensor Defect Rules)
* **`Raw consumer DV footage`**: 2000년대 초반 가정용 디지털 비디오 테이프의 원본 압축 텍스처 호출
* **`Autofocus hunting / lag`**: 구형 콘트라스트 AF의 초점 헤맴(포커스가 앞뒤로 살짝 흐려졌다가 잡히는 물리적 지연)
* **`Exposure shifts / hunting`**: 피사체 이동이나 회전 시 자동 노출이 급격히 밝아졌다 어두워지는 현상
* **`Soft digital detail & faded colors`**: 인위적인 피부 선명도를 죽이고 채도가 살짝 빠진 초기 CCD 센서 색감
* **`Mild digital noise & motion blur`**: 셔터 스피드 한계로 생기는 자연스러운 모션 블러와 저조도 디지털 노이즈
* **`Accidental / hesitant micro-zooms`**: 캠코더 줌 버튼을 미숙하게 툭 건드렸다가 멈추는 비전문가의 실수 연출

#### 2. 인간 카메라맨 신체화 4대 물리 수칙 (Physical Cameraman Embodiment Rules)
카메라를 공중에 뜬 기계가 아닌, **"현장에 발을 딛고 서 있는 제3의 인물(친구/목격자)"**로 완벽히 육체화합니다.
1. **보행 충격 전이 (`Footstep Shake`)**: `Walking creates visible footstep shake` — 발바닥이 땅에 닿는 충격이 렌즈 상하좌우 롤링으로 즉각 전이.
2. **인간 반응 지연 오버슈트 (`Latency Drift & Overshoot Correction`)**: `When subject stops unexpectedly, camera briefly drifts past them before correcting` — 인물이 급정거할 때 카메라맨의 인지 반응 지연(0.3초)으로 관성 오버슈트 발생 후 재보정.
3. **공간 배려 블로킹 (`Spatial Courtesy Staging`)**: `Stops near the bench's right end, leaving the subjects space` — 다른 사람에게 시야나 자리를 내어주며 멈추는 인간적인 배려 동선.
4. **망설이는 관찰자 시선 (`Quietly Observed`)**: 피사체에 무리하게 파고들지 않고 적절한 거리를 유지하며 엿보는 다큐멘터리/홈비디오 구도.

#### 📋 2000년대 캠코더 실전 마스터 템플릿 (Early-2000s DV Template):
```markdown
[Camera & Texture]: Raw early-2000s consumer DV footage filmed by a friend: strong natural handheld shake, spontaneous imperfect framing, occasional autofocus hunting, exposure shifts, natural motion blur, faded colors, soft digital detail, mild noise, and brief accidental zooms. The camera follows the activity with natural amateur movements.

[Cameraman Physical Blocking]: The friend begins one step behind the subject, walking with visible footstep shake. When the subject stops unexpectedly, the camera briefly drifts past before correcting with a hesitant short zoom. Keep the interaction readable, natural, and quietly observed.

[Negative Constraints]: modern sharp digital video, cold clinical 4K sharpness, harsh digital contrast, clean digital sensor look, tripod stability, smooth gimbal motion, cinematic color grading, beauty filter.
```

### 4. ⚡ 오디오-시각 물리학 & 공간 3D 타이포 연출 수칙 (Audio-Visual Physics & Spatial Architecture Typography)
음악의 비트(BPM)와 시각 공간의 물리학을 1:1로 결합하고, 자막 붕괴 현상을 원천 차단하는 하이엔드 MV/광고 전용 프롬프팅 공식입니다.

* **악기 비트별 공간 물리 법칙 분정 (Audio-Visual Physics Mapping)**:
  - 단순 "음악에 반응한다"는 무의미하며, 악기 소리별 공간 연산 법칙을 정의합니다.
  - `Kick`: 공간 압축 (`Spatial timeline compression toward the subject`)
  - `Snare`: 프레임 분율 및 잔상 복제 (`Duplicate previous movements into adjacent frames`)
  - `Bass`: 시간왜곡 및 렌즈 굴곡 (`Distort and bend timeline velocity`)
  - `Hi-hat/Glitch`: 마이크로 파편 팝업 (`Animate UI cursors and fragmented particles`)
* **자막 붕괴를 피하는 공간 3D 건축물 타이포 (Spatial Architecture Words)**:
  - 화면 위 2D 자막/텍스트는 AI가 100% 뭉개므로, 공간 속에 세워진 3D 건축물 구조물로 정의합니다.
  - *지시어*: `3D words "COPY", "TREND", "FREE" exist as physical 3D architectural structures, NOT subtitles or 2D text overlays.`
* **과거 프레임 잔상 분신 통제 (Past-Frame Projection Lock)**:
  - 여러 잔상이 보일 때 AI가 새로운 엑스트라 인물을 임의 생성하는 오류를 차단합니다.
  - *지시어*: `Multiple visible figures are strictly past-frame projections of @tag, maintaining identical character identity.`
* **애니메이션 4단계 모션 궤적 (Anticipation to Settle Dynamics)**:
  - *지시어*: `Movement follows motion dynamics: Anticipation → Attack → Overshoot → Settle. Explode into a continuous dynamic long take during the audio drop.`

### 5. 🏭 중국 전문 제작팀 AI 숏드라마 팩토리 프로덕션 수칙 (Chinese Shortdrama Factory Production Rules)
도우인·콰이쇼우·빌리빌리 등에서 방영되는 80편 이상의 상업용 숏드라마를 실패/재생성(Re-roll) 없이 공장처럼 고속 양산하는 **4대 핵심 엔지니어링 규칙**입니다. (자세한 프롬프트 전문은 [chinese_shortdrama_factory_prompts.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/AI-video-prompt/resources/chinese_shortdrama_factory_prompts.md) 참조)

* **1. 고의적 캐릭터 시트 훼손 (Intentional Face-Obscured Character Sheet)**:
  - 캐릭터 시트의 얼굴 정면에 **그물망 격자 패턴(Lattice Mesh)**을 씌워 얼굴을 고의로 훼손 전달.
  - 모델이 얼굴을 2D 이미지 그대로 '복사-붙여넣기'하여 표정이 굳는 현상을 원천 방지하고, 헤어/의상/체형 아이덴티티만 파싱하여 자연스러운 실시간 표정 연기를 유도.
* **2. 재질별 하이라이트 상대 비율 수치화 (Material Highlight Multipliers)**:
  - 형용사 대신 광영 설계 블록에서 재질별 반사광 비율을 수치로 고정: `장도 금속 ×1.5, 피부 ×0.5, 천 ×0.3` (`长刀金属高光×1.5、皮肤高光×0.5、布料高光×0.3`).
  - 피부와 천을 누르고 금속만 튀게 만들어 수십 번 재생성해도 캐릭터 룩과 명암 관계성이 100% 일정하게 유지.
* **3. 더빙 지시의 상수(Constant) / 변수(Variable) 분리 체계**:
  - `【더빙 지시: 캐릭터[@태그] | 음색 & 기본 성격 (상수) | 상태 & 어조 (변수) : "대사"】`
  - *예시*: `【더빙 지시: 고야[@참고도1] | 차갑고 맑은 소년 음색 | 눌러 참고 자제함, 말수 적고 낮게 (상수) | 상태(조롱) | 어조(차갑게/느리게/끝 올림)(변수): "대사 내용"】`
  - 80화 전체에서 성우 음색과 캐릭터성은 고정하되 컷별 감정 연기만 자유자재로 스위칭.
* **4. 특정 단어 시점 기반 동작/표정 액션 싱크 (Word-by-Word Action Sync)**:
  - 단순 초단위 지시 대신 대사의 특정 단어 발화 시점과 표정/시선/손동작을 1:1로 결합.
  - *예시*: `“괴상한”이라 말할 때 웃음주름 전개, “그 신발”이라 말할 때 손가락이 신발로 낙하, “변경”이라 말할 때 눈 들어 반응 관찰.`
* **5. 앞뒤 에피소드 양방향 인계 헤더/푸터 (Bi-directional Clip Handoff)**:
  - **시작부 (0~2초)**: 이전 컷의 마지막 동작/카메라 앵글을 이어받아 시작 (`S04의 신발 밑창이 화면을 채운 상태에서 착지하며 시작...`).
  - **종료부 (【종료 프레임과 S06 연결】)**: 다음 컷으로 넘겨줄 인물의 고정 포즈와 다음 씬의 첫 대사를 텍스트로 박제 (`청죽 지팡이를 짚고 눈웃음을 띠며 입술이 열리려는 상태. S06은 "동파가 여기 있소..."부터 시작`).
  - 편집자의 컷 연결 확인 공정 없이 생성 즉시 완벽한 컷 투 컷 자동 연결 보장.

### 6. 🥋 시댄스 2.5 현실 기반 맨몸 액션 & 학원 액션물 수칙 (Seedance 2.5 Realistic Grounded Combat Rules)
판타지/마법/초능력(CGI, 빔, 순간이동)을 0% 배제하고, 한국 학원물·드라마·영화(예: 약한영웅, 무빙, 아저씨) 특유의 **극실사 맨몸 격투(Grounded Physical Action)와 본능적 반사 무술 연출**을 구현하는 전문 수칙입니다.

* **1. 초인적 이펙트 배제 & 신체 역학 기반 격투 (Pure Kinetic Mechanics)**:
  - 장풍, 안광, 궤적 이펙트를 완전 차단하고 오직 **체중 이동(Weight Shift), 관절 레버리지(Joint Leverage), 관성 회전(Momentum Redirection), 중심축 회전(Center-of-Mass Pivot)**으로만 공격과 회피를 묘사합니다.
  - *지시어*: `Fast, physical, believable action. No superpowers, no magic, no CGI glowing effects. Leverage, momentum redirection, and realistic joint kinematics.`
* **2. 5단계 심리/감정 변화 아크 (5-Stage Emotional Arc Acting)**:
  - 격투 중 표정이 마네킹처럼 굳는 것을 막기 위해 주인공의 감정 상태를 5단계로 점진 전환합니다.
  - `공포(Fear, "그만해...") ➔ 혼란(Confusion) ➔ 본능 각성(Instinct) ➔ 냉정한 집중(Concentration) ➔ 자신의 힘에 대한 불신/충격(Disbelief, "나... 방금 뭐 한 거야?")`
* **3. 목격자 시점 핸드헬드 폰카 결함 룩 (Witness Smartphone Camera Look)**:
  - 완벽한 영화용 짐벌 트래킹 대신, 실제 현장 목격자가 스마트폰으로 다급하게 찍는 듯한 결함을 주입하여 리얼리티를 300% 극대화합니다.
  - *지시어*: `Handheld smartphone/operator footage, imperfect framing, focus hunting, natural motion blur, brief overshoot, exposure hunting. Feels like a real witness recording an incident.`
* **4. 배경 사물 물리 충돌 & 파편화 (Environmental Physics Collisions)**:
  - 텅 빈 공간에서 허공에 주먹질하는 것을 막고, 한국 체육관/교실/복도의 실제 기물(배드민턴 카트 전도, 셔틀콕 비산, 매트 벽면 충돌, 관람석 진동)과 충돌하도록 결합합니다.
  - *지시어*: `Attackers collide and stumble naturally into surroundings. A badminton cart tips over, shuttlecocks scatter across wooden floor, body thuds against padded wall.`
* **5. 노-뮤직 현장 생음 폴리 100% 락 (Raw Native Foley Lock)**:
  - BGM을 완전 배제하고, `신발 바닥 마찰음(Shoe squeaks on polished wood), 거친 호흡, 옷깃 스치는 소리, 매트 벽 타격음, 셔틀콕 흩어지는 소리, 한국어 생목소리 독백`으로만 오디오를 채웁니다.

---

## 작업 흐름 (Workflow)

### 1단계: 4대 핵심 요소 정의 (Four Key Elements)
1. **촬영자 (Shooter)**: 친구, 가족, 행인, 1인 크리에이터, 고정형 CCTV, 전문 다큐멘터리 제작팀?
2. **장비 및 시대 (Device & Era)**: DV 캠코더, VHS, 8mm 필름, 스마트폰 폰카, 전문 35mm 영화 카메라?
3. **주체 및 공간 (Subject & Scene)**: 인물 스펙과 촬영 위치, 시간대
4. **감성적 목표 (Emotion)**: 아날로그 향수, 비극적 낭만, 평온함, 자연스러운 생활감?

---

### 2단계: 범용 마스터 비디오 프롬프트 템플릿 (Universal Master Prompt Template)

공장형 숏드라마의 핵심 연계 기술(재질 상대 비율, 더빙 상수/변수, 단어 액션 싱크, 앞뒤 컷 양방향 인계)이 통합된 표준 템플릿입니다.

```
Part-N [Aspect Ratio: 16:9, 1920x1088]
[Image References] @tag1, @tag2 ...
[Lighting & Material] Lighting specs & Material Highlight Multipliers (e.g. Metal x1.5, Skin x0.5, Fabric x0.3)
[Camera & Optics] Camera specs, movement, lens, and film texture
[Roles Binding] Reference image roles 1:1 binding
[Location & Environment] Scene and spatial description
[Characters] Subject identity lock and costuming
[Start State] 00:00: Seamless connection from previous part's ending angle & posture
[Timeline & Acting] Shot-by-shot timeline with Word-by-Word Action Sync & Dubbing (Constant/Variable)
[End State] 00:15: Fixed ending pose & next part handoff anchor
[Audio & Foley] Physical SFX, raw voices, no BGM, Foley SFX only
[Negative Constraints] Watermark, subtitles, text overlay, BGM, etc.
```

#### ✍️ 문단별 작성 수칙 (4대 실전 핵심 표준 통합)

**1. 조명 및 재질 상대 비율 (Lighting & Material Multipliers) — [표준 1]**
* 형용사 대신 광영 설계에서 **재질별 반사광 비율(Multipliers)**을 수치로 선언하여 수십 번 뽑아도 명암 관계성을 불변으로 고정합니다.
* *지시어 예시*: `5000K neutral light, 45° key light + 180° rim light; Metal/Jewelry Highlight x1.5, Skin Highlight x0.5, Fabric/Background Highlight x0.3.`

**2. 시작/종료 상태 양방향 인계 (Start/End State Anchoring) — [표준 2]**
* **[Start State]**: 컷편집 병목을 없애기 위해 이전 컷의 마지막 자세/각도를 이어받아 시작함을 1줄로 박제합니다.
  - *예시*: `00:00 [Start State]: Seamlessly continues from Part-1's ending motion, white sneaker stepping onto mossy stone step.`
* **[End State]**: 다음 컷으로 넘겨줄 인물의 고정 포즈와 다음 씬의 첫 대사를 텍스트로 박제합니다.
  - *예시*: `00:15 [End State]: Bamboo staff planted by side, smiling eye contact, lips about to part. Handoff to Part-2 opening.`

**3. 단어 단위 표정/동작 액션 싱크 (Word-by-Word Action Sync) — [표준 3]**
* 대사를 칠 때 특정 단어 발화 시점과 표정/손동작/시선 처리를 1:1로 묶어 자연스러운 립싱크와 물리 연기를 유도합니다.
* *예시*: `when saying "really?", brows raise in curiosity; when saying "look at this", index finger points directly to the product; maintains direct eye contact as line ends.`

**4. 더빙 지시의 상수(Constant) / 변수(Variable) 구조 — [표준 4]**
* 캐릭터의 고유 음색/성격은 1화부터 끝까지 잠가두고, 그 씬에 필요한 감정만 변수로 교체합니다.
* *지시 포맷*: `【Voice: @character | Warm resonant baritone, restrained and calm (Constant) | State: Playful (Variable) | Tone: Sarcastic, rising finish (Variable) : "대사 내용"】`

**5. 주요 캐릭터 및 일관성 락 (Main Character & Consistency Lock)**
* 이미 레퍼런스 이미지 태그(`@tag`)가 존재하면 구구절절한 외모/복장 텍스트 중복 설명을 배제한다.
* 클립별 **단 1명의 메인 추적 인물 태그만** 선언한다.
* **캐릭터 일관성 락(Consistency Lock) 문구 필수 추가:**
  - `In entire video, maintain consistent identity, clothing, hair, and appearance of @tag.`

**6. 카메라 & 렌즈 스타일 (Camera & Lens Style)**
* 렌즈 특성, 셔터 수차, 아날로그 필름 질감 표기.
* `No digital sheen, no artificial glow, organic physical optics.`

**3. 시간선 (Timeline)**
* 파트당 총 5~10초 분량을 2~4초 단위의 짧은 샷들로 나열 (`00:00–00:03 [Shot 1: Tight Framing Close-up]: ...`).
* 글씨 쓰기 등 AI가 뭉개는 동적 연산은 배제하고, **완성된 정적 상태(Static State)**에서 4중 미세 표기 연기로 지시한다.

**4. 파트당 글자 수 제한 (Prompt Length Limit)**
* 비디오 생성기(Kling 등)의 텍스트 슬롯 입력 제한을 준수하기 위해, 하나의 파트 코드 블록 내 총 글자 수는 **반드시 2,450자 미만 (안전 기준 2,400자 이내)**으로 철저히 맞춘다.

---

## 🎬 Kling AI 전용: 시네마틱 대화 & 감성 씬 연출 수칙 (Kling Dialogue & Emotional Scene Rules)

Kling AI 모델은 인물의 미세 표정, 자연스러운 립싱크, 시네마틱 카메라 움직임(Dolly Push-in, Framing)을 정밀하게 연산합니다. 대화나 감성적 씬을 연출할 때 다음 수칙을 참조하세요.

### 1. 🎭 대사-액션 3단계 바인딩 (3-Step Micro-Expression Dialogue Binding)
AI 인물이 입만 뻐끔거리는 동상 현상을 차단하고 자연스러운 대사 호흡을 유도하기 위해 `[사전 미세 행동/시선] ➔ [대사 발화] ➔ [사후 미세 표정/여운]` 3단계 구조로 연기 지시를 결합합니다.
* **작성 패턴**:
  * `[사전 연기]`: `swirling orange juice in a glass while gazing toward the forest, then...`
  * `[대사]`: `Woman: "These trees will turn yellow in a month."`
  * `[사후 연기]`: `lowers head with a thoughtful smile, whispering back...`

### 2. 📹 감정선에 맞춘 샷 앵글의 단계적 축소 (Camera Framing Arc)
시네마틱 대화 씬에서는 서사의 몰입도에 따라 카메라 앵글을 단계적으로 좁혀 들어가는 구조를 적용합니다.
* **Medium-wide Angle + Dolly Push-in**: 공간과 인물 전체를 잡으며 천천히 다가감 (분위기 형성)
* **Close-up (Single)**: 반응하는 상대방의 얼굴과 상반신에 집중 (감정 교환)
* **Tight Close-up**: 눈빛, 떨리는 입술, 미세 표정에 밀착 (감정의 클라이맥스)
* **Lingering Close-up**: 대사 후 잔상이 남는 표정을 아웃포커싱 배경과 함께 지속 (여운)

### 3. 🍃 프레임 생동감을 주는 미세 동적 요소 (Live Atmosphere Micro-Motion)
대화 중 인물이 멈춰 있어도 화면이 굳지 않도록 자연스러운 환경적 미세 움직임을 프롬프트에 지속적으로 포함합니다.
* **의류/머리칼**: `Soft natural breeze gently moves hair and clothing`
* **조명 효과**: `Warm golden sunlight creating soft shadows and subtle lens bloom`
* **소품 연출**: `Subtle liquid swirl inside glass`, `Flickering candlelight`

### 4. 🔊 오디오 청정화 및 환경음(Ambient) 매핑
Kling 오디오 렌더링 시 오류를 방지하기 위해 `[Audio]` 필드에는 대사 텍스트를 절대로 적지 않고, 풍부한 환경음만 명사구로 기재합니다.
* **권장 표기 예시**: `Natural ambient birdsong, distant wind through trees, subtle glass movement, film-quality ambient sound.`

---

## 📹 Kling AI 전용: 다큐멘터리 & 일상 Vlog 씬 연출 수칙 (Kling Documentary & Vlog Scene Rules)

현장 취재 다큐멘터리, 직업 일상, 리얼리티 Vlog 스타일의 자연스러운 실사(Realism) 영상 연출을 위한 Kling AI 전용 수칙입니다.

### 1. ⚙️ 절차적 워크플로우 명시 (Sequential Operational Workflow)
단순 인물 묘사에 그치지 않고, 실제 직업이나 일상의 동작 절차(Procedure)를 순서대로 명시하여 인위적인 포즈나 AI 특유의 부자연스러운 동작을 차단합니다.
* **작성 패턴**: `WORKFLOW: Step 1 (Arrival) ➔ Step 2 (Preparation) ➔ Step 3 (Main Task) ➔ Step 4 (Completion)`

### 2. 🚫 카메라 불의식 연기 통제 (No Camera Acknowledgment)
인물이 카메라를 정면으로 쳐다보거나 연기하듯 부자연스러워지는 오류를 원천 제어하기 위한 필수 수칙입니다.
* **필수 지시어**: `Strict occupational behavior. No one acknowledges the camera. Operations continue naturally.`

### 3. 🎥 다큐멘터리 3인칭 렌즈 & 카메라 무빙 (Docu-Vlog Camera Framing)
삼각대 고정이 아닌, 현장 취재진이나 Vlog 카메라맨이 인물을 어깨 높이에서 뒤따라가는 아날로그 시점감을 부여합니다.
* **카메라 시점**: `Shoulder-level documentary following the subject` (어깨 높이 추적 샷)
* **카메라 움직임**: `Natural operator movement, subtle handheld organic shake`
* **대기/광학 현상**: `Occasional heat distortion (아지랑이 왜곡)`, `natural lens bloom`, `organic motion blur`

### 4. ⏰ 구체적 시간대 및 분위기 조명 설정 (Shift Time & Lighting)
이른 아침(5:45 AM)이나 노을녘 등 구체적인 시각을 지정하여 새벽의 푸른빛(Blue-hour)과 유도등/현장 조명의 사실적인 대비를 연산하게 만듭니다.
* **작성 예시**: `SHIFT TIME: 5:45 AM. Blue-hour morning light with visible runway guidance lights.`

### 5. 🎧 현장 직업 노이즈 & 오디오 레이어 (Operational Ambient Audio)
BGM을 배제하고 현장에서 실제로 발생하는 직업 기계음과 노이즈를 명사구 형태로 레이어링합니다.
* **작성 예시**: `Jet engines, ground vehicles, radio headsets, hydraulic equipment sound, airport announcements.`

### 6. 🌧️ 카메라 렌즈 광학 반응 & 대기 효과 (Lens Optical FX)
날씨나 탐험/익스트림 현장을 묘사할 때, 단순 환경 설명에 그치지 않고 **카메라 렌즈에 미치는 물리적/광학적 반응**을 기재하여 실사감을 극대화합니다.
* **렌즈 빗방울/습기**: `Occasional raindrops on lens`, `lens fogging from high humidity`
* **번개/조명 노출 변화**: `Natural exposure shifts during lightning spikes`, `sudden shutter brightness variation`
* **시점 혼합 (Multi-Camera)**: `Combination of dashboard camera (GoPro view) and handheld roadside footage`

### 7. ⚖️ 과장 억제 & 과학적 사실주의 통제 (Realism Standard)
자연재해, 탐험, 익스트림 현장 연출 시 CG 영화 같은 과장된 액션을 배제하고 National Geographic / Discovery급 다큐 톤앤매너를 강제합니다.
* **필수 제약어**: `Scientific observation over sensationalism. No impossible physical or weather behavior. Natural human reactions only.`

### 8. 🪖 1인칭 바디캠/헬멧캠 & 무-손떨방 연출 (Bodycam & Unstabilized Optics)
구조대, 경찰, 군인, 극지 탐험가 등 1인칭 바디캠/고프로 시점 연출 시 디지털 손떨림 보정을 의도적으로 제거하여 날것(Raw)의 시점감을 부여합니다.
* **시점 명시**: `Helmet-mounted / Chest-mounted action camera with natural head movement`
* **손떨방 제거**: `No digital stabilization, raw unedited bodycam aesthetic`
* **숨소리 결합**: `Heavy ragged breathing audio/visual motion sync during physical exertion`

### 9. ❄️ 환경에 따른 렌즈 결로/김서림 (Condensation & Weathering)
추위, 습기, 화염 등 극한 환경 촬영 시 카메라 렌즈 테두리에 나타나는 아날로그 물리 현상을 기재합니다.
* **김서림/결로**: `Condensation forming on lens edges from extreme cold`, `lens fogging`
* **이물질 착착**: `Snowflakes / mud splatters / water droplets adhering to lens surface`

### 10. 🚶 체력적 피로감 & 이동 속도 가변성 (Physical Exhaustion & Varying Speed)
인물이 로봇처럼 일정한 속도로 움직이지 않고, 체력 저하에 따라 걸음 속도가 자연스럽게 둔해지고 달라지는 현실적 생체 연기를 지시합니다.
* **속도 변화 지시**: `Physical exhaustion must be visible. Walking speed naturally varies with fatigue.`
* **바디캠 톤앤매너**: `No heroic speeches or cinematic posing. Should resemble authentic raw training/bodycam footage.`

---

## 🎭 Kling AI 전용: 고밀도 심리 & 감정 연출 수칙 (High-Density Psychological & Emotional Acting Rules)

AI 비디오 모델에서 단호함, 망설임, 고통, 체념 등 인물의 복잡한 심리적 전환을 100% 실사 영화 필름 수준으로 연출하기 위한 고급 연기 지시 수칙입니다.

### 1. 🫀 생리적 미세 반응 지시법 (Micro-Physiological Reaction Rules)
감정 단어("슬퍼한다", "화낸다")를 절대로 직접 쓰지 말고, 인간이 극도의 심리적 갈등 속에서 실제 보이는 **신체 생리 현상(Physiological Signals)**으로 감정을 번역하여 지시합니다.
* **호흡의 3단계 변화**: `Controlled breathing with subtle chest rise (통제)` ➔ `Shortened breath with heaving chest (가빠짐)` ➔ `Suppressed deep exhalation (억눌린 날숨)`
* **목/입술 연기**: `Natural swallowing motion (자연스러운 침 삼킴)`, `lower lip tightening (아랫입술 미세 긴장)`
* **시선 & 눈물 묘사**: `Gaze briefly shifting away then re-locking on lens`, `glistening eyes with a tear pooling at lower eyelid`
* **손/신체 미세 떨림**: `Involuntary physiological micro-tremor in fingers, wrist, and held object`

### 2. ⚡ 카메라 흔들림 vs 인물 신체 떨림 레이어 분리 (Camera Shake vs Subject Tremor Separation)
카메라의 핸드헬드 미세 떨림과 인물 손/신체의 감정 떨림을 명확히 분리하여 지시해야 AI가 화면 구도를 뭉개지 않고 정밀 연산합니다.
* **카메라 미세 떨림 (전체 프레임)**: `Handheld camera micro-drift acting on the ENTIRE frame`
* **인물 감정 떨림 (국소부)**: `Emotional micro-tremor acting ONLY on fingers, wrists, and held object`

### 3. 📉 심리 전환을 대변하는 동작 하향 궤적 (Action Trajectory for Emotional Shift)
갑작스러운 동작 전환(물건을 툭 떨어뜨리거나 갑자기 던지는 현상)을 방지하고, 심리적 포기/체념을 보여주기 위해 **단계적 하향 궤적(Trajectory)**을 명시합니다.
* **단계별 궤적 지시 예시**: `Maintaining aim with micro-tremor ➔ Gradual hand/wrist relaxation ➔ Slow continuous downward trajectory ➔ Resting at bottom frame without dropping`

### 4. 🎨 쿨/웜 색채 심리학 대비 (Color & Lighting Psychology)
인물의 이성/절제와 내면의 갈등/온기를 조명 레이어로 분리하여 공간의 비극성을 극대화합니다.
* **쿨 톤 측면광 (이성/절제/비극)**: `Cool-gray soft side-light from window`
* **웜 톤 아웃포커싱 background (과거/미련/온기)**: `Small out-of-focus warm lamp in deep background`

### 5. 🔊 감정 노이즈 & 오디오 텍스처 (Emotional Audio Texture)
BGM과 대사를 100% 배제하고, 인물의 호흡과 소품/의상의 극미세 마찰음으로만 오디오를 구성하여 시네마틱 긴장감을 배가시킵니다.
* **오디오 레이어**: `Ambient room noise, rain on window, gasping/ragged breathing, micro-friction of hands gripping object, subtle fabric friction of clothing`

---

## 💃 Seedance 2.0 전용: 숏폼 패션 & 비트 싱크 연출 수칙 (Seedance 2.0 High-Fashion & Fast Beat Sync Rules)

Seedance 2.0 모델(최대 9개 레퍼런스 지원) 및 9:16 세로비율 트렌디 패션 커머셜, Y2K 레트로 아날로그 패션 필름 연출을 위한 전용 수칙입니다.

### 1. 🎵 드럼/기타 비트와 컷의 동기화 (Beat-Synced Fast Cuts)
음악의 특정 악기 드롭 시점에 컷 포인트를 강제로 기재하여 박자감과 속도감을 극대화합니다.
* **지시어 수칙**: `Fast cuts synced to drums`, `Cut hard on a guitar drop`, `Cut sharp on the beat`

### 2. 🎞️ Y2K 패션 필름 아날로그 광학 연출 (Retro Film Optics)
90년대~2000년대 패션 화보 비하인드 씬 및 MTV 뮤직비디오 특유의 감각적인 아날로그 렌즈 질감을 주입합니다.
* **렌즈/카메라 효과**: `Whip pans`, `snap zooms`, `white strobe flash transition frames`, `frame skips`, `subtle glitch effects`
* **아날로그 텍스처**: `High contrast lighting`, `shallow depth of field`, `erratic handheld camera`

### 3. 🔒 단일 레퍼런스 일관성 강제 락 (Strict Single Reference Lock)
빠른 컷 전환 시 인물 얼굴이나 의상 붕괴를 방지하기 위해 단 하나의 레퍼런스 태그를 유일한 기준으로 선언합니다.
* **지시어 수칙**: `Use @tag as the ONLY face and outfit reference; keep facial likeness, hairstyle and exact outfit consistent in every shot.`

### 4. ⏱️ 4단계 서사 리듬 구조화 (HOOK ➔ BURST ➔ PLAYFUL ➔ ENDING)
10초 내외의 숏폼 프롬프트를 성격에 따라 4단계로 쪼개어 서사 완급조절을 지시합니다.
* **0-2s HOOK**: 시선 직시 및 후크 발화 (`"Hey, look here."`)
* **2-4s BURST**: 드럼 비트에 맞춘 쾌속 샷 & 로우앵글 쿵
* **4-7s PLAYFUL**: 광각 왜곡 & 회전 글리치 & 위트 발화 (`"Keep up with me."`)
* **7-10s ENDING**: 슬로모션, 디테일 크롭 & 여운 발화 (`"This is my vibe."`)

### 5. 👗 패션 에디토리얼 구도 제약 (Fashion Editorial Framing)
패션 화보(Editorial) 특유의 감각적인 구도를 유지하고 불필요한 인체 크롭이나 과도한 성적 묘사를 방지합니다.
* **제약 수칙**: `High-fashion editorial style, tasteful and confident, focus on outfit styling and attitude, NOT a body-part closeup, no sexualized framing.`

---

## ⚔️ Kling AI / 애니 전용: 극상 타격감 셀셰이딩 칼싸움 연출 수칙 (Cel-Shaded Anime Sword Fight & Impact Frame Rules)

귀멸의 칼날, 진격의 거인 등 고품질 액션 애니메이션(Ufotable 스타일) 및 셀셰이딩(3D-to-2D) 무협/SF 검술 액션을 연출할 때 적용하는 전용 수칙입니다.

### 📌 언제 사용해야 하는가? (Use Cases)
1. **화려하고 속도감 넘치는 2D/3D 하이브리드 애니메이션 검술 액션을 연출할 때**
2. **칼이 부딪힐 때 묵직한 손맛과 전기 스파크/충격파 타격감이 필요한 클라이맥스 격돌 씬**
3. **잔상 회피, 360도 쾌속 오비팅 회전 컷, 찰나의 엇갈린 착지 정지 포즈(Cross-step freeze) 등 역동적인 시퀀스**
4. **선형 빗방울, 공중 부유 돌가루, 역광 림라이트(Rim Light)가 얽힌 어두운 시네마틱 톤앤매너 씬**

### 1. 💥 3대 타격감 물리 지시어 (3-Key Impact Directives)
AI 애니메이션 렌더링 시 타격감이 밋밋해지는 현상을 차단하기 위한 필수 지시어 세트입니다.
* **임팩트 프레임 (충격파 순간 섬광)**: `Instant white/black impact frames on weapon collision`
* **카메라 화면 흔들림**: `Maximum impact feedback with camera screen shake`
* **유선형 모션 블러**: `Heavy streamlined motion blur during fast sword swings`

### 2. ⚡ 쿨 틸 & 에너제틱 스파크 조명 대비 (Teal & Electrical Energy Lighting)
전체 배경 톤과 칼싸움 충격 지점의 광원을 명확히 분리하여 시각적 쾌감을 극대화합니다.
* **배경 기본 톤**: `Cool Teal color palette with strong backlighting and sharp rim light`
* **충격 지점 광원**: `Golden sparks and blue-white electrical arc energy feedback`

### 3. 🌧️ 고속 모션 빗방울 & 부유 파티클 (High-Speed Particle FX)
* **선형 빗방울**: `Raindrops featuring elongated linear motion blur under high-speed movement`
* **공중 돌가루**: `Floating rock debris and volumetric smoke particles rising in mid-air`

### 4. 🎬 14초 칼싸움 타임라인 패턴 (14s Sword Fight Pattern)
* `0-1s`: 광각 실루엣 대치 + 부유 돌가루 압박감
* `1-3s`: 두 검객의 날카로운 눈빛 및 검 손잡이 근경 교차
* `3-5s`: 스피드 줌인 폭발적 돌진 + 유선형 모션블러 베기
* `6-9s`: 클라이맥스 격돌 (스파크 & 임팩트 프레임 + 쌍검 패링 청백색 전기 에너지)
* `9-12s`: 잔상 회피 + 쾌속 교차 공방 컷
* `12-14s`: 근접 360도 오비팅 회전 ➔ 엇갈린 정지 포즈(Cross-step freeze) 및 망토 휘날림

---

## 참고 문서
* [references/camera-aesthetics.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/references/camera-aesthetics.md): 기기별 특유의 화면 왜곡 및 결함 영문 템플릿
* [references/atmosphere-dictionary.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/references/atmosphere-dictionary.md): 감성 언어를 구체적인 물리적 묘사 영문으로 바꾸는 사전
* [references/anti-ai-checklist.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/references/anti-ai-checklist.md): 흔히 범하는 AI 비디오 오류와 촬영자의 실수 라이브러리


### 4. 🔊 Sound 오디오 지문 통제 및 작성 규격 수칙 (Sound Control & Format Rules)
AI 비디오 생성기(Seedance / MiniMax / Kling)의 오디오 파서가 배경 음악(BGM)을 오버레이하는 현상을 차단하고, 생생한 Foley 현장음을 구현하는 4대 표준 규격입니다.

1. **위치 원칙**: `- Sound: <...>` 라인은 **오직 `[BEAT 1]`, `[BEAT 2]`, `[BEAT 3]` 비트 블록 내부의 샷 목록 바로 아랫줄**에만 1:1 배치. `[Negative Constraints]` 아랫줄 배치 절대 금지!
2. **풍부한 SFX 묘사**: 조잡한 1~2단어 대신 **4~6단어 이상의 구체적 물리 사운드 명사구** 사용.
3. **BGM 차단어 필수 주입**: 지문 태그 내 최후반에 **`no BGM, Foley SFX only`** 필수 명시.
4. **올바른 포맷 예시**:
   - `- Sound: <Heavy dough thud impact on wood, flour cloud poof, table vibration, no BGM, Foley SFX only>`
   - `- Sound: <Sub-bass impact thud, iron skewer impale crunch, glowing charcoal pop, no BGM, Foley SFX only>`

---

## 🏆 SF & 액션 블록버스터 거장 전용 스킬북 (Master Sci-Fi & Action Production Playbook)

감독님의 레퍼런스 검증 및 30년 경력 SF 액션 거장 분석을 통해 도출된 **AI 비디오 생성기(Seedance 2.0 / 2.5 / Kling 3.0) 전용 마스터 액션 연출 법칙 7선**입니다. 액션, SF, 판타지, 커머셜 영상 기획 시 필수 적용합니다.

### 1. 🎯 2단어 카메라 헤더 선언 기법 (2-Word Camera Shot Headers)
* **원칙**: 모든 비트 샷 지문 첫머리에 카메라 구도/앵글을 **정확히 2단어 영문 명사구**로 축약 선언하여 AI 파서의 카메라 제어를 1초 만에 픽스합니다.
* **필수 샷 헤더 라이브러리**:
  - `Profile push` (측면 밀착 푸시) / `Low wide` (로우 앵글 와이드)
  - `Macro burst` (초근접 매크로 폭발) / `Overhead orbit` (공중 360도 오빗)
  - `Asphalt insert` (바닥 스키밍 인서트) / `Portrait pause` (정적 호흡 정지)
  - `Hero finish` (히어로 피니시 착지) / `Dolly zoom` (현기증 현사 줌)
  - `Whip pan` (쏜살같은 채찍 패닝) / `Macro sizzle` (초근접 푸드 시즐)
  - `Ground roll` (바닥 360도 더치 롤) / `Sealing outro` (결계 봉인 아우트로)

### 2. 🔗 프레임 연쇄 연결 법칙 (Frame-to-Frame Action Anchoring)
* **원칙**: 파트 및 샷 전환 시 이전 샷의 파티클/궤적/시각적 앵커를 차기 샷 오프닝으로 이어받아 컷 전환 시 인물 자세와 파티클이 리셋되지 않는 100% 심리스(Seamless) 연결 유도.
* **지시어 포맷**: `[Connecting from previous shot's particle/action trail]` (영어) 또는 `承接...` (중문).
* **실전 예시**:
  - `[Connecting from previous shot's rising steam]` (이전 샷의 올라오는 수증기를 이어받아)
  - `[Connecting from flying cloth fragments]` (이전 샷의 튀는 옷자락 파편을 이어받아)
  - `[Connecting from floating ice crystals]` (이전 샷의 공중 얼음 결정을 이어받아)

### 3. 🔒 캐릭터 무기 & 아이덴티티 철통 잠금 (Weapon & Identity Iron Lock)
* **원칙**: 고속 액션 중 AI의 무기 증발/변형 결함을 차단하기 위해 무기 개수, 종류, 손 위치를 프롬프트 상단과 네거티브에 이중 족쇄로 강제 잠금.
* **지시어 포맷**: `strictly N weapons in hand, never drop, never vanish, never morph`
* **실전 예시**:
  - `Character A strictly holds two katanas in hand, never drop, never vanish, never morph.`
  - `Character B uses strictly bare hands with lightning claws, never hold swords or daggers.`

### 4. 📹 렌즈 물리 마찰 & 거장 특수 광학 연출 (Lens Physics & Special Optics)
* **렌즈 물리 충돌 (Lens Collision)**: 흙가루, 먼지, 불꽃, 장어 기름방울이 카메라 렌즈 표면에 부딪히는 물리 현상을 주입하여 가짜 CG 느낌 파괴.
  - `Dirt/mud/ash/grease splatter directly on camera lens`
  - `Ash collision on anamorphic camera lens`
  - `Steam condensation & micro-grease splatter on 100mm macro lens`
* **Dolly Zoom (Vertigo Effect)**: 인물 크기는 고정하고 배경만 기하급수적으로 늘려 압도적 아찔함 유도.
* **Barrel Roll & Pass-Through**: 360도 공중 회전하며 구조물/용 날개 틈새를 카메라가 관통.
* **Reverse Cloud-Piercing Pull-Out**: 카메라가 역방향으로 초고속 후퇴하며 구름을 뚫는 에픽 와이드 아우트로.

### 5. 🌋 누적 이펙트 중첩 법칙 (Cumulative FX Engine)
* **원칙**: 컷이 지날수록 수증기, 부적 재, 아스팔트 균열, 전기 밀도가 리셋되지 않고 **지속 중첩 누적(Continuous Accumulation)**되도록 지문 상단 선언.
* **지시어 포맷**: `Continuous accumulation of steam, floating ice crystals, asphalt cracks, torn clothing, and aura density without reset.`

### 6. 🛑 미드 액션 기습 흑전 마감 (Mid-Action Hard Cut to Black)
* **원칙**: 액션 씬의 끝은 밋밋한 페이드 아웃이나 정지 포즈가 아니라, 동작 진행 중(Mid-motion) 기습 흑전으로 끝내어 영화적 쾌감 보장.
* **지시어 포맷**: `Mid-action hard cut to black during weapon collision / attack motion.`

### 7. 👑 비전투 지배자 연출법 (Non-Combat Dominator Awakening Presence)
* **언제 써야 하는가 (Use Cases)**: 
  1. 직접 칼/몸싸움을 하지 않고도 **보스/지배자 캐릭터의 절대적 위엄과 압도감**을 뿜어내야 할 때 (예: 구미호 사당 회상, 봉인 해제, 마법 각성).
  2. 캐릭터의 능력이 개방되면서 공간 전체를 지배하는 정적인 서스펜스 클라이맥스 연출 시.
* **4대 핵심 지시 기법**:
  - **극단적 최소 동작 수직 부유 (Minimal Motion Vertical Elevation)**: 뛰어다니지 않고 `Slow elegant vertical floating + minimal finger gesture`만으로 압도감 형성.
  - **저각 수직 추적 ➔ 360도 아우라 오빗 (Low-Angle Elevate → 360 Aura Orbit)**: 바닥 아스팔트/지면에서 카메라가 수직으로 쫓아 오른 뒤, 공중 파티클을 360도 전방위 오빗 회전.
  - **동공 안광 회전 & 미소 쾌속 줌인 (Eye-Ring Spin & Macro Smile Push-In)**: 동공의 특수 문양/안광이 점등·회전할 때 얼굴로 `Fast crash push-in`하여 조용하고 서늘한 실소 포착.
  - **나직한 속삭임(Whisper)과 거대 이펙트의 대비**: 고성을 지르지 않고, 화면 전체에 파티클 폭풍을 터뜨리면서 대사는 `Calm quiet whisper`로 차갑게 읊조려 전율 극대화.

---

## ⚡ Seedance 2.0 × Higgsfield 액션 & 파이트 안무 거장 스킬북 (Seedance 2.0 Fight Choreography Engine)

Seedance 2.0 (Higgsfield) 신경망 파서가 가장 강력하게 연산하는 **10대 액션 오프닝 훅(2-Second Action Hooks)**, **무술 안무 표준 용어(Choreography Verbs)**, **카메라 전투 참여 법칙(Camera as Active Combatant)**, **4중 물리 레이어(4-Layer Impact & Atmosphere Engine)** 공식입니다.

### 1. ⏱️ 2초 액션 오프닝 훅 라이브러리 (2-Second Action Hooks)
영상의 첫 0~2초에 AI가 멍때리거나 정적인 포즈로 굳는 현상을 차단하고 시선을 강탈하는 8대 시작 패턴입니다.
* `Mid-Action Freeze Frame`: 공격 동작의 정점(Apex of strike)에서 근육과 관절이 최대치로 응축된 상태로 0.5초 정지 후 폭발 시작.
* `Shockwave from Ground Slam`: 발/신체 지면 강타 시 방사형 원을 그리며 지면 균열과 충격파 먼지가 퍼져나감.
* `Blade Light Flash on Steel`: 칼날에 빛이 번쩍이며 터지는 광학 섬광과 함께 발도/겨눔 시작.
* `Radial Spark Explosion`: 두 무기가 화면 중앙에서 충돌하며 오렌지/청백색 스파크가 방사형으로 폭발.
* `Aggressor Linear Charge`: 공격자가 카메라를 향해 광속으로 직진 돌진하며 근접 진동 유발.
* `Slow-Motion Impact Contact (0.25x)`: 타격 순간 피부 변형, 고개 꺾임, 충격파가 0.25배속으로 극도로 강조됨.
* `Dual-Wield Twirl`: 무기를 쾌속 회전시키며 잔상을 만든 후 크로스 파워 스탠스로 안착.
* `Evasive Sidestep Dodge`: 직선 돌진을 찰나의 피벗으로 회피하며 상대의 관성이 카메라를 스쳐 지나감.

### 2. 🥋 Seedance 2.0 공인 무술 안무 지문 사전 (Choreography Action Verbs)
추상적인 묘사("멋있게 싸운다")를 배제하고, 모델이 정밀 연산할 수 있는 1:1 무술 물리 지시어입니다.
* **타격계 (Strikes)**:
  - `Cross`: 뒷발 축과 골반을 완전히 회전시키는 직선 강타 (`rear-hand straight strike with full hip rotation`).
  - `Spinning Heel Kick`: 몸 전체 회전 관성을 실은 뒤꿈치 타격 (`full-body rotation with trailing heel strike`).
  - `Axe Kick`: 수직으로 내리찍는 파쇄각 (`vertical descending leg strike with downward crushing force`).
  - `Supersonic Linear Dash`: 지면을 박차고 일직선으로 광속 비상 (`supersonic straight linear dash toward target`).
* **방어 및 반격 (Defense & Counters)**:
  - `Lateral Parry`: 칼날로 적의 무기를 측면으로 빗겨내며 공격 흐름 유지 (`blade-to-blade lateral deflection`).
  - `Riposte`: 패링 직후 끊김 없이 이어지는 즉각적인 반격 (`parry followed by immediate counter-strike`).
  - `Evasive Pivot Roll`: 몸을 굴려 공중/직선 궤적을 벗어나는 회전 회피 (`full-body evasive rotation`).
* **검술 안무 궤적 (Sword Kinetics)**:
  - `Full Crescent Arc`: 우하단에서 좌상단으로 공간을 찢는 거대 반원 궤적 (`draws a full crescent blade arc`).
  - `Overhead Cleave`: 위에서 아래로 수직 양단하는 참격 (`overhead vertical cleave slicing through air`).

### 3. 📹 카메라 전투 참여 법칙 (Camera as Active Combatant)
카메라가 제3자 구경꾼이 아니라 전투의 물리적 한 축으로 작동하도록 제어합니다.
* `Dolly Forward on Attack`: 공격 돌진 시 카메라가 타격 지점으로 급격히 함께 밀고 들어감.
* `Reverse Dolly on Advance`: 캐릭터가 전진할 때 카메라가 후퇴하며 상대적 속도 왜곡감 극대화.
* `Snap Zoom on Impact`: 타격/충돌 순간 찰나의 줌인-아웃으로 충격량 시각화.
* `Rack Focus Duel`: 전경의 검 손잡이/얼굴에서 배경의 돌진하는 적에게로 초점 쾌속 전환.
* `Low-Angle Worm Tracking`: 무릎/지면 높이에서 공격자의 거대한 위압감을 쫓아 오르는 로우앵글 추적.

### 4. 💥 4중 물리 & 환경 반응 레이어 (4-Layer Impact & Atmosphere Engine)
단순 무기 묘사에 그치지 않고, 공격이 일어날 때 주변 환경의 물리적 파괴와 대기 반응을 동시 연산시킵니다.
1. `Fabric snap & ripple`: 타격 및 돌진 풍압에 도포와 옷자락이 팽팽하게 찢어지듯 펄럭임 (`fabric violently snaps from kinetic air pressure`).
2. `Radial shockwave crater`: 발을 디디거나 지면 박차는 순간 생기는 원형 크레이터와 부유 파티클 (`ground crater with weightless floating rock debris`).
3. `Centrifugal sweat & hair spray`: 회전 타격 시 원심력으로 사방에 흩뿌려지는 땀방울과 머리칼 (`sweat droplets and hair violently whipping outward`).
4. `Anamorphic lens collision`: 파편, 검기 꽃잎, 빗방울이 카메라 렌즈 표면에 직접 부딪혀 튀는 광학 효과 (`particles and energy petals violently collide on anamorphic camera lens`).

---

## 🥋 Seedance 2.0 초고속 0.8~1.5초 템포 격투 액션 & 인체역학 5대 엔진 (0.8-1.5s High-Speed Kinetic Combat Engine)

중국 최상위 Seedance 2.0 액션 제작팀의 초고속 격투 프롬프트로부터 리버스 엔지니어링한 **5대 핵심 액션 아키텍처**입니다. 
빠르기만 한 것이 아니라 **물리적 개연성(Causality), 인체역학(Biomechanics), 렌즈 다이내믹스(Lens Choreography)**가 완벽하게 결합되어 유기적인 명작 전투를 연출합니다.

### 1. ⏱️ 0.8~1.5초 초고속 컷 전환 템포 공식 (0.8-1.5s Micro-Pacing Formula)
* **원칙**: 전투의 지루함을 없애고 타격감을 극대화하기 위해 15초 클립을 1초 내외의 극단적 마이크로 컷으로 쪼갭니다.
* **표준 비트 템포 구조**:
  - `0–1s`: **오프닝 훅 (Low-angle CU)** ➔ 안면/가슴을 강타하는 첫 공격과 물리 반응(고개 꺾임, 충격파)
  - `1–2s`: **피벗 반격 (Whip Pan)** ➔ 타격 흡수 후 무릎/팔꿈치를 꽂는 즉각적 리포스트
  - `2–4s`: **지면 밀착 연타 & 벽면 파쇄 (Ground Tracking → Wall Collision)** ➔ 콤보 타격 후 건축물/지면 충돌
  - `4–6s`: **360도 오빗 육탄전 (360 Orbit CQC)** ➔ 엘보, 니킥, 잡기, 공중 회전이 뒤엉키는 전방위 액션
  - `6–9s`: **공중 텐션 & 낙하 충돌 (Airborne Grapple → Crater Slam)** ➔ 폭발 반동으로 공중 격돌 후 지면 강타
  - `9–11s`: **상호 궁극기 차지 (Heroic Charge Overload)** ➔ 전신 에너지 과부하 및 대기/환경 붕괴
  - `11–13s`: **정면 초음속 대격돌 (Climax Head-On Clash)** ➔ 에너지 폭발로 인한 1프레임 백화(White Flash) & 충격파
  - `13–15s`: **상흔 누적 정적 엔딩 (Torn Exhaustion Freeze)** ➔ 연기 속 헐떡임, 누적된 상처와 옷 손상 직시

### 2. 🧬 인체역학 & 관절 물리 락 (Human Biomechanics & Joint Dynamics)
* AI의 고질적인 관절 꼬임, 미끄러짐(Sliding), 어색한 동작을 방지하기 위해 실제 인체역학 표준어를 선언합니다.
* `Joint and limb kinematics strictly adhere to realistic human biomechanics.`
* `Kinetic energy transfer: rear-foot plant → hip pivot rotation → shoulder snap → terminal fist impact.` (후족 지지 ➔ 골반 회전 ➔ 어깨 스냅 ➔ 주먹 타격의 운동 역학 전달)

### 3. 💥 타격 인과관계 1:1 결합 법칙 (Strict Strike-Impact-Damage Causality)
* 공격 지문 작성 시 반드시 **[공격 부위] ➔ [접촉 순간 에너지 폭발] ➔ [피격자의 인체 반작용] ➔ [가시적 물리 상흔]** 4단계를 1세트로 작성합니다.
  - *예시*: `Right knee drives deep into solar plexus → purple electric arc detonates on impact point → upper body doubles over in agonizing recoil → fabric singed and burned with char marks.`

### 4. 🩸 상흔 & 환경 파괴 점진 누적 엔진 (Progressive Wound & Environmental Decay)
* 컷이 바뀔 때마다 캐릭터의 상처나 배경 파손이 리셋되는 오류를 차단합니다.
* `Cumulative damage engine: bruises, split lips, torn sleeves, and facial abrasions continuously accumulate without resetting.`
* `Environmental destruction escalates: from cracked glass → fractured walls → shattering roof tiles → pulverized stone ground.`

### 5. ⚡ 고유 속성 에너지 이중 오버레이 (Dual-Element Signature Energy Layer)
* 각 캐릭터 고유의 시그니처 에너지(예: 청명의 백청색/매화 진기 vs 상대의 칠흑 요기/자색 번개)를 모든 펀치, 킥, 패링 접촉면에 1:1로 결합하여 시각적 대비감을 극대화합니다.

---

## 👥 Seedance 2.0 & 2.5 다인원 복제 인간(Cloning) 방지 및 공간 슬롯 락 수칙 (Multi-Character Anti-Cloning Engine)

AI 비디오 모델(Seedance 2.0/2.5, Kling 3.0 등)에서 3인 이상의 다인원 씬 렌더링 시 발생하는 **인물 복제(Cloning), 인물 뒤섞임(Identity Drift), 엑스트라 무단 증식(Hallucinated Extra People)**을 100% 원천 차단하기 위한 엔지니어링 표준 프롬프트 아키텍처입니다.

### 1. 공간적 좌우 좌표 슬롯화 (Spatial Zone Allocation & Spatial Blocking)
* `walk together` 같은 모호한 복수 지칭어를 절대 금지하고, 화면의 물리적 좌우/전후 슬롯에 인물 태그를 1:1로 정확히 배치합니다.
```markdown
[Spatial Character Slots: Exactly N Unique Individuals]
STRICT HEADCOUNT: Exactly N characters total, each appears strictly ONCE.
- Front Row: @tag1 (left, black robe, carrying sack), @tag2 (right, female swordsman, empty hands).
- Rear Row (Left-to-Right): @tag3 (left), @tag4 (center-left), @tag5 (center-right), @tag6 (far-right).
```

### 2. 헤드카운트 및 단일 인스턴스 하드 락 (Strict Headcount & Single Instance Lock)
* 프롬프트 선언부에 총 인원수와 각 캐릭터의 단 1회 등장 원칙을 수학적으로 못 박습니다.
* `STRICT HEADCOUNT: Exactly N characters total, each appears strictly ONCE. Strictly single instance of each character.`

### 3. 역할별 비경합 고유 시각 앵커 1:1 결합 (Non-Negotiable Visual Anchors)
* 각 태그마다 서로 절대 겹치지 않는 1~2단어의 고유 시각적 외형(예: `black robe`, `white robe`, `fur coat`, `female swordsman`)을 태그 바로 뒤 괄호 안에 고정 결합하여 가중치 간섭(Feature Bleeding)을 차단합니다.

### 4. 대사 제외 본문 100% 순수 영문화 원칙 (100% Pure English Body Rule)
* 본문 설명에 한국어와 영어가 혼용되면 AI 토크나이저가 인물 태그를 파싱하지 못하고 복제 인간을 만듭니다. **성우 발화 대사(`{}`)를 제외한 모든 본문/카메라/환경/캐스트 묘사는 100% 순수 영어**로만 작성합니다.

### 5. 글로벌 표준 안티클론 네거티브 락 (Global Standard Anti-Clone Negative Lock)
* *필수 Negative 키워드*: `more than N people, duplicates, clones, copies, ghosting, twin characters, extra unnamed characters, background doubles, crowd, mob`


---

## ⚔️ 🔥 AAA급 시네마틱 액션 블록버스터 7대 마스터 엔지니어링 수칙 (AAA Cinematic Action Blockbuster Rules)

중국 최정상급 3D 국만(Donghua) 및 AAA급 게임 시네마틱(UE5.4 Path Tracing / Nanite / Lumen PBR) 비디오 프롬프트에서 도출된 **초고밀도 7대 물리·시각·안전 제어 엔지니어링 수칙**입니다.

### 1. 🩸 100% 안전 통과: 무혈 탄화 소멸 프로토콜 (Incineration ZeroBlood Safety Protocol)
AI 비디오 모델(Runway, Kling, Seedance)의 텍스트 안전 검열(Safety Classifier)을 100% 무력화하면서 압도적인 타격감과 시각적 파괴 쾌감을 달성하는 인과율 타격 공식입니다.
* **엄격한 5단계 피격 인과 체인 (5-Stage Causality Chain)**:
  - `무기/검기 적중 ➔ 적중 부위에 백황색 초고온 낙인 ➔ 화염 균열이 전신으로 확산 ➔ 외피가 새까맣게 탄화(Carbonization) ➔ 전체가 불타며 백열 불꽃, 흑색 재, 탄화 파편, 열풍으로 산산조각 붕괴`
  - *지시어*: `Hits with ZeroBlood protocol: impact point creates white-orange heat brand → flame veins spread across armor → shell carbonizes pitch black → disintegrates into glowing embers, black ash, carbonized fragments and thermal shockwave. No blood, no internal organs, no flesh cut.`

### 2. ⚡ 무기 전용 3중 혼합 물리 FX (Weapon 3-Layer Physics FX Blend)
단순한 2D 광선이나 얇은 수묵 이펙트를 배제하고, 무기의 묵직한 중량과 질량을 공기/환경과 상호작용시키는 3단 레이어링 기법입니다.
* **레이어 1 (에너지 & 압력 50%)**: `적금색 압축 검기, 부채꼴 초고압 충격파, 공간 굴절, 음폭 링(Sonic Boom Ring), 관성에 의한 공기 함몰(Air Collapse)`
* **레이어 2 (소각 & 탄화 30%)**: `적중점 백황색 낙인 ➔ 화염 균열 ➔ 표면 탄화 ➔ 흑색 연기와 불티 폭발`
* **레이어 3 (환경 유체 역학 20%)**: `모래벽, 모래 회오리, 용융 유리 파편(Vitrified Glass Shards), 고압 먼지 파도`

### 3. ⏱️ 1초 3동작 제한 & 관성 동역학 (1-Sec 3-Action Cap & Inertia Mechanics)
AI가 인물 골격을 뭉개거나 로봇처럼 뚝뚝 끊기는 현상을 차단하는 속도 제어 법칙입니다.
* **동작 수 제한**: 1초당 주요 동작은 **최대 3개 이하**로 엄격 제한.
* **제로 정지(Zero-Stall)**: 멈춰 서는 정지 동작을 배제하고 `슬라이딩(Slide), 롤링(Roll), 몬스터 밟고 반동 도약(Step-off Pivot), 무기 지지 브레이킹(Blade Ground Braking)`으로 연속 가속 유지.
* **무기 관성 연산**: `허리/골반 발력 ➔ 어깨 리드 ➔ 무기 가속 ➔ 타격 ➔ 관성 회수(Inertia Recovery)` 5단계 물리 명시.

### 4. 📹 3단계 충격 프레임 & 렌즈 반동 시스템 (3-Tier Impact Frames & Recoil Camera)
타격의 강도에 따라 카메라 흔들림과 광학 섬광을 수치화하여 타격 손맛을 극대화합니다.
* **1단계 충격 (일반 횡베기/역수 베기)**: `Tier-1 Impact Frame, 1-frame orange flash, 1200°/s Whip Pan.`
* **2단계 충격 (엘리트 충돌/패링)**: `Tier-2 Impact Frame, 0.1s blind-spot debris transition, 1.2Hz breathing micro-shake.`
* **3단계 충격 (바닥 내려찍기/궁극기)**: `Tier-3 Impact Frame, ±4.5cm elastic camera recoil, 3-frame white flash, momentary radial blur.`

### 5. 👁️ 0.1초 시야 사각 트릭 (Visual Blind-Spot Decoy Transitions)
카메라 컷을 억지로 자르지 않고, 화면 앞을 지나가는 파편/모래/깃털로 0.1초 동안 렌즈를 가렸다가 벗겨내며 자연스럽게 앵글과 피사체를 스위칭하는 원테이크 연속 촬영 기법입니다.
* *지시어*: `0.1s flying sand/debris blind-spot transition wiping across lens, switching visual focus seamlessly.`

### 6. 🏛️ 강성 기하학적 공간 앵커 (Rigid Geometric Spatial Anchors)
초고속 카메라 이동 중 배경이 엿가락처럼 휘거나 형태가 붕괴되는 것을 방지하기 위해 배경 원경에 불변의 기하학적 랜드마크를 고정합니다.
* *지시어*: `Distant ruined monoliths, wind turbines, and ridge lines remain rock-solid rigid geometric anchors throughout dynamic camera moves.`

### 7. 🚫 레퍼런스 에셋 오염 방지 (Asset Extraction Clean Lock)
캐릭터/배경 레퍼런스 이미지를 업로드할 때, 이미지 내부의 턴어라운드(3뷰), 회색 스튜디오 배경, 무기 설명 텍스트, 자막이 영상에 묻어나오는 것을 차단합니다.
* *지시어*: `Extract strictly the visual character design and weapon model from reference. Never generate 3D model turntables, grey studio backgrounds, weapon display sheets, UI, letterboxes, or watermark text.`

### 8. 🦾 단일 상지/외팔이 해부학 잠금 수칙 (Strict Asymmetrical Anatomy Lock)
AI 비디오 모델이 신체 결손(외팔이) 인물을 렌더링할 때 인체 대칭성 본능(Bilateral Symmetrical Bias)으로 인해 달리기/점프/공격 시 팔을 자동 복원(Regeneration Glitch)하는 치명적 오류를 완벽히 통제하는 4대 헌법적 프롬프팅 수칙입니다.

1. **`severed/missing arm` 단어 전면 금지 ➔ `ONE upper limb total` 단일 상지 선언**:
   - `left arm severed`라고 쓰면 모델이 먼저 `left arm` 객체에 주의(Attention)를 집중하여 팔을 만들어 버립니다.
   - 반드시 **"이 인물은 처음부터 상지가 1개(오른팔)뿐이다(This character has ONE upper limb total. ONLY the RIGHT ARM exists)"**라고 선언해야 합니다.
2. **`empty sleeve` ➔ `no arm-shaped sleeve volume` 치환**:
   - 소매(sleeve) 단어는 AI가 '안에 팔이 들어있다'고 추론하게 만듭니다. 옷감은 **"왼쪽 어깨의 옷은 몸통에 완전히 밀착되어 평평하게 접혀 있으며, 팔 모양의 소매 볼륨이 전혀 없다(Robe is folded flat against torso with no arm-shaped volume)"**로 묘사합니다.
3. **액션 비트별 비대칭 역학 재잠금 (Action-Beat Re-locking)**:
   - 질주/도약/공격 시 모델이 양팔 균형을 맞추지 못하도록 매 샷마다 **`asymmetrical one-armed body mechanics`, `do not restore bilateral anatomy`**를 반복 주입합니다.
4. **구조적 결함 네거티브 차단어**:
   - `left arm` 대신 구조적 결함 단어인 **`second arm, second hand, duplicated limb, regenerated limb, prosthetic arm, arm-shaped sleeve, bilateral arms, two-handed grip`**을 네거티브에 배치합니다.

---

## 🧴 Wan 3.0 럭셔리 코스메틱 & 뷰티 커머셜 마스터 스킬북 (Wan 3.0 Luxury Beauty Commercial Engine)

Wan 3.0은 **최대 30초 단일 롱테이크/멀티샷 렌더링**과 **최대 19,500자의 방대한 프롬프트 컨텍스트**를 지원하는 초고해상도 비디오 모델입니다. 샤넬, 디올, 이솝(Aesop), 설화수 감성의 최고급 화장품/향수/프리미엄 F&B 비주얼 필름 제작 시 비주얼 붕괴 없이 극강의 하이엔드 미학을 구현하는 6대 프로덕션 수칙입니다.

### 1. ⚙️ Wan 3.0 모델 하드웨어 & 프롬프트 스펙
* **최대 영상 길이**: **최대 30초** (단일 클립 기준)
* **글자 수 한도**: **최대 19,500자 미만** (안전 권장 19,000자 이내)
* **레퍼런스 태그 체계**: 고유 식별자 이름 직접 바인딩 (`@Image 1`, `@protagonist`, `@bg_greenhouse` 등)
* **최적 화면비**: `16:9` (가로 시네마틱), `9:16` (모바일 럭셔리 쇼츠)

### 2. 🎗️ 단일 시각 모티프 인계 법칙 (Continuous Visual Motif - Light Ribbon)
* **원리**: AI 영상의 고질적 결함인 '샷 전환 시 톤과 연결성 붕괴'를 차단하기 위해, 영상 전체를 관통하는 단 하나의 광학적 매개체를 선언합니다.
* **지시어 포맷**:
  ```markdown
  Use one continuous visual motif throughout the film: a delicate pale-green and warm-gold ribbon of refracted sunlight. It begins as sunlight reflected through greenhouse glass, passes through fruit skin and moisture, moves across the protagonist's cheek, and finally becomes the highlight on the real hero product. Each scene inherits the direction and flow of this light from the previous scene.
  ```
* **효과**: 빛의 궤적(Highlight Sweep)이 샷과 샷을 자연스럽게 꿰뚫으며 단절감 없는 유기적 연결성을 완성합니다.

### 3. 🌀 물리 기하학 기반 '아트 트랜지션' 공식 (Art Transition Formula)
억지스러운 3D 모핑이나 크로스 디졸브 대신, 현실 피사체의 매크로(초근접)와 마이크로(원경) 기하학 선을 일치시켜 카메라가 공간을 투과하는 고급 트랜지션을 연출합니다.
* **패턴 A (매크로 표면 투과 ➔ 공간 기하학 확장)**:
  - *지시어*: `Continue camera movement through the surface of that intact berry into a luminous volumetric world of translucent seedless flesh and delicate moisture. The internal green-gold fibers gradually elongate into graceful parallel lines. Those lines slowly become the real geometry of greenhouse rows and pale beige stone paths, expanding smoothly until the camera reaches high overhead.`
* **패턴 B (과육/텍스처 윤광 ➔ 인물 뷰티 하이라이트)**:
  - *지시어*: `Follow one distinctive curved pale-green and champagne-gold highlight travelling across the moist flesh. Camera stays with that exact curve while the macro fruit texture becomes creamy and abstract, resolving naturally into the protagonist's cheek as beauty light.`

### 4. 💎 럭셔리 뷰티 광학 & 초점면 단일화 수칙 (Single Sharp Focal Plane)
AI에게 모든 피사체를 선명하게 그리라고 지시하면 화면 전체가 플라스틱 3D CG처럼 변질됩니다.
* **단일 초점면(Single Focal Plane)**: 매 샷마다 *"At each moment, only one important focal plane becomes critically sharp (architecture, an eye, wicker texture, one grape berry, moisture or hero product)"*를 선언하여 AI의 연산 초점을 한곳에 집중시킵니다.
* **광학 렌즈 디퓨전 콤보**: `Black Pro-Mist / Glimmerglass aesthetic, extremely shallow depth of field, creamy pale-green and ivory bokeh, warm champagne backlight, gentle halation, optical bloom, soft highlight roll-off, slightly lifted blacks.`

### 5. 🔤 통일된 단일 에디토리얼 타이포그래피 (Unified Editorial Serif Typography)
영상 중간에 텍스트가 깨지거나 철자가 왜곡되는 현상을 원천 방지합니다.
* **폰트 패밀리 단일화**: Didot 스타일의 하이콘트라스트 럭셔리 세리프 폰트 1종으로만 전체 텍스트 고정.
* **광학 블러 ➔ 포커스 등장 기법**:
  - *원칙*: 글자가 허공에서 어설프게 나타나면 철자가 깨집니다.
  - *지시어*: `Every word appears already fully and correctly formed, then gently moves from a soft optical blur into clear focus. A narrow green-gold refracted light sweeps across the completed lettering.`

### 6. 🎼 72–76 BPM 드림 앰비언트 & 동적 덕킹 (Dynamic Ducking Audio)
* **템포 및 질감**: `72–76 BPM refined modern dream-ambient soundscape, soft glassy ambient tones, warm analog pads, delicate breath-like textures, subtle reversed tonal swells, minimal abstract melody.`
* **보이스오버 인터랙션**: `Korean narration intimate and clearly foregrounded. Music naturally ducks beneath every spoken line and gently opens during silent visual transitions.`
* **앰비언스 블렌딩**: 현장 온실 앰비언스, 발걸음, 직물 소리, 라탄 바구니 텍스처, 과일 수분감 소리가 자연스럽게 음향에 레이어링됩니다.

---

## 📸 80~90년대 아날로그 극실사 캐릭터 사진 & 히어로 포트레이트 수칙 (Gritty Analog Character Photography & Hero Portrait Engine)

AI 이미지/비디오 생성기 특유의 미끈거리는 3D CG 질감(Plastic Slop), 인형 같은 에어브러시 피부, 과도한 디지털 뷰티 필터를 완벽히 차단하고, **80~90년대 아날로그 영화 스틸컷이나 내셔널지오그래픽 다큐멘터리 포트레이트** 같은 압도적 실재감의 캐릭터 사진(히어로 레퍼런스 이미지)을 제작하는 4대 엔지니어링 법칙입니다.

### 1. ⚙️ 극실사 캐릭터 구현 4대 기둥 (The 4 Pillars of Tactile Photorealism)

1. **수작업 실물 소품 & 물리적 결함 강제 (`Handcrafted Props & Imperfections`)**:
   - 매끄럽고 완벽한 3D 메탈/의류 렌더링을 완전히 배제합니다.
   - 도색이 벗겨지고 긁힌 크롬(`chipped paint`, `battered reflective chrome`, `deep metal scratches`), 소금기와 기름때가 찌든 고무 작업복(`stained with dried sea salt and grime`), 올이 풀린 니트 등 **세월과 현장의 손때**를 반드시 명시합니다.
2. **생체 반응 & 특수분장 텍스처 (`Biological Realism & Practical FX Makeup`)**:
   - 뷰티 필터를 끄고 인물의 **생생한 피부 모공(`visible skin pores`), 흘러내리는 땀방울(`glistening beads of sweat`), 뺨을 가로지르는 긁힌 핏자국(`dried blood scratches`), 흙먼지(`mud grime splatters`)**를 1:1로 주입합니다.
   - 머리카락은 땀에 젖어 이마와 관자놀이에 엉겨 붙은 디테일(`sweat-dampened strands of hair clinging to forehead`)을 사용하여 살아있는 인물임을 각인시킵니다.
3. **가차 없는 한낮 직사광 & 35mm 광학 콘트라스트 (`Harsh Direct Sunlight & 35mm Optics`)**:
   - 스튜디오의 인위적인 소프트박스 조명 대신 **거친 한낮의 직사광(`harsh direct midday coastal sunlight`)**을 사용하여, 젖은 고무와 크롬에 맺히는 강렬한 스펙큘러 하이라이트와 깊고 짙은 암부(`deep velvety shadows`)를 만듭니다.
   - 35mm 컬러 네거티브 필름 입자(`gritty 1980s 35mm cinematic film still`)와 얕은 심도(`shallow depth of field, f/2.0 ~ f/2.8`)를 결합합니다.
4. **삶의 무게가 실린 인물 표정과 시선 (`Grounded Human Emotion & Expression`)**:
   - 아이돌 같은 카메라 응시 대신, 세월의 풍파를 겪은 호탕한 웃음주름(`deep laugh lines around warm crinkling eyes, broad hearty grin`)이나 전장의 비장하고 결연한 눈빛(`intense piercing resolute warrior gaze`)을 부여합니다.

---

### 2. 📋 카테고리별 실전 프롬프트 템플릿 (Copy-Paste Prompts)

#### [템플릿 A] 80년대 배틀 데미지 SF/판타지 전사 (Gritty Battle-Damaged Knight/Warrior)
> 고전 애니메이션(세인트 세이야, 건담 등)의 갑옷을 80년대 헐리우드 실사 특촬 세트장에서 찍은 듯한 극실사 매크로 클로즈업 포트레이트.
```text
Extreme tight macro close-up portrait of a fierce young East Asian warrior wearing battle-damaged pegasus-knight chrome armor, live-action gritty 1980s cinematic movie still. 

The handcrafted helmet has an ornate white and red bird crest, battered reflective chrome cheek-plates covered in real mud splatters, chipped lacquer, and scratches. The warrior has intense, piercing dark eyes staring directly at the camera with unwavering resolve, dark sweat-dampened bangs clinging to forehead. Realistic textured human skin with visible pores, glistening beads of sweat, faint cuts with dried blood across cheekbone, covered in battle grime and dust. 

Shot on 35mm film, harsh direct midday sunlight creating blinding specular highlights on polished chrome metal and deep dramatic shadows, extreme macro shallow depth of field, tactile practical special effects makeup, zero CGI. --ar 9:16 --style raw
```

#### [템플릿 B] 거친 바다와 삶의 터전 노동자/어부 상체 샷 (Authentic Working-Class / Fisherman Portrait)
> 다큐멘터리 감성의 리얼 라이프 인물 사진. 비디오 생성기(Wan 3.0, Kling 등)의 인물 레퍼런스 이미지로 최적화.
```text
Medium upper-body portrait of a rugged, middle-aged Korean fisherman on a weathered harbor dock, gritty 1980s 35mm cinematic film still matching the raw, tactile aesthetic of analog cinema photography. 

The fisherman stands proudly from the waist up, wearing a battered, faded yellow rubber fishing bib apron stained with dried sea salt and grime over an aged knit sweater, with a blue knit beanie. His sun-bronzed, deeply weathered face features prominent laugh lines around his warm, crinkling dark eyes, a broad hearty grin, and beads of real sweat and ocean spray glistening on his textured skin pores and salt-and-pepper stubble. A coiled hemp rope hangs over his shoulder. 

Shot on 35mm vintage film, harsh direct midday coastal sunlight creating strong specular highlights on wet rubber fabric and deep velvety shadows. In the soft-focus background, rustic wooden fishing boats, coiled hemp mooring ropes, and a glimpse of the sparkling sea complete the scene. Tactile physical reality, raw candid documentary aesthetic, zero CGI, zero digital smoothing. --ar 9:16 --style raw
```

#### [템플릿 C] 조선 무사 / 동양 무협 배틀 포트레이트 (Gritty East Asian Martial Warrior)
```text
Intimate chest-up portrait of a fierce Korean Joseon warrior after a brutal battle, gritty 1980s 35mm historical cinema film still. 

He wears battered iron-scale armor (두정갑) with oxidized iron rivets, frayed indigo silk trim, and chipped black lacquer. His sun-hardened face is streaked with dried blood, soot, and perspiration; intense, unbroken warrior gaze; unruly black topknot hair coming loose with damp strands clinging to his temples and jawline. 

Shot on 35mm analog lens, harsh angled afternoon sunlight piercing through battlefield smoke, high chiaroscuro contrast, palpable skin texture with distinct pores and sweat drops, zero CGI, zero digital smoothing. --ar 9:16 --style raw
```

---

### 3. 📐 표준 16:9 스튜디오 3분할 캐릭터 턴어라운드 시트 수칙 (16:9 3-Panel Studio Character Sheet Rules)

AI 비디오 모델(Wan 3.0, Kling, Seedance 등)에 캐릭터 레퍼런스를 주입할 때, 배경 간섭을 원천 차단하고 인물의 **얼굴 이목구비(Front Close-up) + 전신 정면(Full-body Front) + 전신 후면(Full-body Back)**을 단 1장의 이미지로 완벽히 바인딩하기 위한 **표준 캐릭터 시트 헌법**입니다.

1. **화면비 16:9 가로 규격 강제 (`16:9 Aspect Ratio`)**:
   - 3개 패널이 여유롭고 왜곡 없이 배치되도록 반드시 가로 16:9 비율(`--ar 16:9`)로 생성합니다.
2. **뉴트럴 스튜디오 배경 통일 (`Neutral Minimal Studio Backdrop`)**:
   - 야외 풍경이나 복잡한 배경 오브젝트를 100% 배제합니다.
   - 배경이 화려하면 비디오 AI가 배경 요소까지 캐릭터 복장이나 얼굴로 오인하므로, 오직 부드러운 조명의 **단색/미니멀 스튜디오 배경(`neutral seamless light-grey studio cyclorama backdrop, soft diffuse studio lighting`)**으로 고정합니다.
3. **엄격한 3분할 컷 레이아웃 (`3-Panel Horizontal Split Screen`)**:
   - **[좌측 패널 1 - 얼굴 확대 정면 샷 (Extreme Frontal Face Close-up)]**:
     - 가슴 위~머리끝까지 타이트하게 프레이밍. 피부 모공, 눈가 주름, 수염, 땀방울, 눈빛, 헤어스타일/모자 디테일을 현미경 수준으로 기록.
   - **[중앙 패널 2 - 전신 정면 샷 (Full-Body Front View Standing Pose)]**:
     - 머리끝부터 신발/장화 끝까지 서 있는 정면 샷. 전체 신체 비율, 상하의 복장 전면, 멜빵/주머니/소품 착용 상태를 온전히 기록.
   - **[우측 패널 3 - 전신 후면 샷 (Full-Body Back View Standing Pose)]**:
     - 뒤돌아선 전신 샷. 모자/헤어 뒷모습, 상하의 등판 주름, 멜빵 교차 구조, 장화 뒷굽 디테일을 온전히 기록.

#### 📋 16:9 스튜디오 3분할 시트 표준 프롬프트 템플릿:
```text
A professional 3-panel character turnaround reference sheet, 16:9 aspect ratio, horizontal split into three distinct side-by-side shots of the exact same character against a clean, neutral seamless light-grey studio cyclorama backdrop. Gritty 1980s 35mm film photography aesthetic with tactile analog realism, zero CGI.

- Panel 1 (Left): Extreme tight macro frontal face close-up, showcasing ultra-detailed realistic skin pores, weathered laugh lines, glistening sweat, authentic stubble, and intense expressive eyes.
- Panel 2 (Center): Full-length front view standing pose from head to toe, clearly showing the complete front outfit, worn fabric textures, weathered rubber/leather details, body proportions, and work boots.
- Panel 3 (Right): Full-length rear back view standing pose from behind, showing the back of the headwear, rear jacket/overalls construction, strap alignment, and boots from behind.

Even, soft studio portrait lighting with subtle edge separation, razor-sharp focus on subject, completely neutral empty background. --ar 16:9 --style raw
```

---

### 4. 🚫 철통 네거티브 차단 공식 (Universal Anti-Plastic Negative Rules)
AI 모델이 '3D 플라스틱'과 '인형 같은 뷰티 필터'로 회귀하는 것을 100% 차단하는 필수 네거티브 키워드 세트입니다.
```text
outdoor background, messy scenery, natural environment, 3d render, CGI, digital illustration, anime, cartoon, smooth airbrushed skin, plastic skin, plastic armor, flawless clean armor, studio beauty filter, porcelain skin, videogame asset, oversaturated, shiny plastic skin, doll-like, flat lighting, fake reflections, modern digital sensor, clean chrome.
```


## 프로젝트 공통 인물 시트 및 참조 태그 규칙
인물 시트·이미지 참조 작업에는 루트의 `PRODUCTION_RULES.md`를 따른다. 기본 시트는 16:9 3분할(얼굴 정면 클로즈업 / 전신 정면 / 전신 후면), 야외 자연광과 흐린 배경을 사용한다. @참조 태그는 영어 식별자로 18자 이하이며 이미지 파일의 확장자 제외 이름과 일치시킨다.
