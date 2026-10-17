---
name: cinematic-film-directing
description: 거장 영화감독(David Fincher, Steven Spielberg, Sven Nykvist, 박찬욱, 봉준호)의 연출·블로킹·커버리지 문법과 Seedance 2.5/Wan 3.0 디렉터-퍼스트 프레임워크를 기반으로, "Make AI video feel photographed, not generated"를 구현하는 시네마틱 연출 전문 가이드입니다.
---

# 🎬 거장 영화감독 연출 & 디렉터-퍼스트 스킬북 (Cinematic Director-First Framework)

> **"Make AI video feel photographed, not generated."**  
> (AI 비디오를 생성된 그래픽이 아닌, 실제 촬영된 영화 필름처럼 느껴지게 하라.)  
> 
> 필름 그레인, 할레이션, 빈티지 렌즈 같은 '질감(Texture)'을 아무리 나열해도 **샷 구성과 편집 리듬이 평평하면 '옛날 필터 씌운 스톡 영상'**에 불과합니다.  
> 좋은 감독은 "카메라 기법 전시장"을 만들지 않습니다. **"왜 지금 이 샷이어야 하는가"**라는 감정의 목적이 먼저이고, 기법은 그 뒤를 따릅니다.

---

## 🌐 0. 공식 시네마틱 비주얼 바이블 (Melies Cinematic Techniques 424)

> **📖 공식 참조 URL**: **[https://melies.co/cinematic-techniques](https://melies.co/cinematic-techniques)**  
> **용도**: 카메라 구도, 무빙, 렌즈, 조명, 샷 사이즈 등이 헷갈릴 때 **가장 먼저 열어보고 복사해 쓸 수 있는 424개 영화 기법의 시각적 공식 바이블**입니다.

### 🗂️ 12대 핵심 시네마틱 카테고리 인덱스
1. **Camera Movement (86개)**: Slow Zoom In/Out, Crash Zoom In/Out, Dolly In/Out/Left/Right, Pan Left/Right, Tilt Up/Down, Whip Pan/Tilt, Pedestal Up/Down, Crane Up/Down/Over, Jib, 360-Degree Orbit, Arc Left/Right, Tracking Shot, Follow Shot, Steadicam, Handheld, Gimbal, FPV Drone 등
2. **Framing & Shot Size**: Extreme Close-up (ECU), Close-up (CU), Medium Close-up (MCU), Medium Shot (MS), Cowboy Shot, Full Shot, Wide Shot (WS), Extreme Wide Shot (EWS), Over-the-Shoulder (OTS), Point-of-View (POV), Two-Shot, Insert Shot, Cutaway 등
3. **Camera Angles**: Low Angle, High Angle, Eye-Level, Dutch Angle / Canted Tilt, Worm's-Eye View, Bird's-Eye / God's-Eye Top-Down, Ground-Level, Overhead 등
4. **Lighting**: Chiaroscuro, Rembrandt Lighting, Split Lighting, Rim/Backlight, Silhouette, Volumetric God Rays, Practical Light, High-Key, Low-Key, Film Noir, Golden Hour, Blue Hour 등
5. **Composition**: Rule of Thirds, Leading Lines, Symmetry, Center Framing, Frame within a Frame, Negative Space, Deep Focus, Shallow Focus, Foreground Occlusion 등
6. **Lenses & Optics**: Anamorphic, Macro, Fisheye, Telephoto, Wide-Angle, Tilt-Shift, Lens Flare, Creamy Bokeh, Soft Focus, Chromatic Aberration, Split-Diopter 등
7. **Color & Film Look**: Bleach Bypass, Technicolor, 35mm Film Grain, Kodak Vision3, Monochromatic, Teal and Orange, Pastel Wash, Desaturated Noir 등
8. **Time & Motion**: Slow-Motion, High-Speed (120fps/1000fps), Time-Lapse, Hyper-Lapse, Stop-Motion, Freeze-Frame, Speed Ramp, Bullet Time 등
9. **In-Camera & Optical Effects**: Dolly Zoom (Vertigo Effect), Rack Focus, Lens Distortion, Shutter Angle Motion Blur, Prism Flare, Motion Smear 등
10. **Editing & Transitions**: Match Cut, Smash Cut, Jump Cut, Cross-Dissolve, Whip Transition, L-Cut, J-Cut, Invisible Cut 등
11. **Atmosphere & Weather**: Volumetric Haze/Fog, Heavy Rain, Steam, Atmospheric Dust Motes, Wind-Blown Smoke 등
12. **Genre & Viral Looks**: Cyberpunk, Retro 80s Horror, Classic Hollywood Romance, Prestige Documentary, Surrealist Dreamscape 등

*※ **프롬프트 작성 지침**: 카메라 지시어 작성 시 "cinematic" 같은 모호한 수식어를 남발하지 말고, 위 Melies 바이블의 구체적인 테크닉 명칭(예: `35mm shallow-depth rack focus`, `85mm optical crash vertigo dolly-zoom`, `overhead 90-degree God's-eye crane ascent`)을 1:1로 정밀 바인딩합니다.*

---

## 🏛️ 1. 거장 감독의 10대 프로덕션 헌법 (The 10 Director-First Rules)

### 1. 감정의 목적부터 정의 (Emotional Objective First)
* 사건을 설명하지 않는다. "수희가 밥을 준다"가 아니라 **"여행자가 잊고 있던 기억을 맛으로 되찾는 순간"**처럼 씬의 핵심 감정을 먼저 정의한다.
* 관객에게 그 감정을 어떤 순서로 전달할 것인가(Emotional Escalation)를 설계한다.

### 2. 한 장면을 한 샷으로 퉁치지 않는다 (Coverage & Rhythm)
* **Master/Wide**: 공간과 고립감 전달
* **Medium**: 물리적 행동과 상호작용
* **Close-up**: 감정의 무게와 눈빛
* **Extreme Close-up (ECU)**: 결정적 깨달음, 떨리는 눈물, 튼 입술
* **Insert Shot**: 단순 장식이 아닌, 관객의 시선을 특정 정보와 상징으로 강제하는 장치 (손, 밥그릇, 시계, 병, 손잡이)
* **Reaction Shot**: 상대방의 표정을 통해 감정을 소화하고 리듬을 만드는 쉼표

### 3. 동기화된 카메라 문법 (Motivated Camera Movement - David Fincher)
* 아무 이유 없는 "cinematic tracking"은 삼류의 증거다.
* 인물이 결심해서 다가가면 **Push-in**, 시선이 다른 곳으로 향하면 **Pan**, 공간의 권력관계가 바뀌면 **Framing shift**. 모든 카메라는 인물의 심리와 행동에 의해 100% 동기화된다.

### 4. 카메라보다 블로킹이 먼저다 (Blocking & Staging - Spielberg & Kubrick)
* 사람이 어디 서 있고, 누구를 보며, 누가 전경/후경에 있고, 언제 앉고 일어나는지가 장면의 서브텍스트다.
* 배우의 위치 변화와 프레임 안의 물리적 거리 자체가 곧 인물 간의 심리적 권력과 친밀도를 웅변한다.

### 5. 얼굴 클로즈업은 아끼되, 결정적 순간에 확실히 (Nykvist's ECU)
* 감정이 폭발하는 순간을 어설픈 미디엄 샷으로 방치하지 않는다.
* ASC 거장 스벤 닉비스트(Sven Nykvist)처럼 아주 타이트한 익스트림 클로즈업을 길게 유지하며, 미세한 눈빛과 입술 떨림으로 감정을 극대화한다.

### 6. 소품을 '주연 배우'처럼 대우하라 (Props as Visual Poetry)
* 밥그릇, 숟가락, 눈물병, 괘종시계, 화산석 뚝배기, 젖은 손, 문손잡이는 각 장면의 의미를 이어주는 시각적 문장이다.
* 중요한 소품의 클로즈업으로 씬을 열거나 닫아 대사의 서브텍스트와 직결시킨다.

### 7. 불균등한 편집 리듬 (Uneven Editing Rhythm)
* 모든 샷을 기계적으로 3~4초씩 자르는 균등 분할은 스톡 영상의 지름길이다.
* **0.8초 인서트 ➔ 3초 얼굴 ➔ 1초 리액션 ➔ 4초 롱테이크 여운**처럼 감정의 호흡에 따라 샷의 길이를 과감하게 비대칭으로 짠다.

### 8. 한 쇼트에 욕심을 덜어내라 (One Beat, One Action - Seedance 2.5 룰)
* 한 구간에 너무 많은 정보를 몰아넣으면 동작이 뭉개지거나 편집이 급해진다.
* **한 Beat에는 오직 [핵심 행동 1개 + 카메라 무빙 1개]**만 배치하여 모델이 물리적 리얼리티를 완벽히 연산하게 한다.

### 9. 시작 상태(Start State)와 끝 상태(End State)의 엄격한 연결
* "수희가 움직인다" 식의 모호한 서술 금지.
* **Start State**: "밥그릇을 쥔 손" ➔ **End State**: "그릇이 나무 테이블에 놓이고 여행자의 젖은 손이 프레임에 들어온다." 다음 컷이 이어받을 수 있는 바톤 터치 상태를 선언한다.

### 10. 9:16 세로 프레임의 공간 깊이 (Depth over Centering)
* 인물을 가운데 세우는 틱톡식 구도를 영구 퇴출한다.
* **Foreground(문틀, 어깨 OTS, 김)** / **Midground(인물)** / **Background(조명, 창문, 괘종시계)**의 3단 깊이를 만들고, 프레임 한쪽의 여백(Negative Space)으로 고독과 여운을 빚어낸다.

---

## 🎬 2. 10단계 마스터 씬 설계 파이프라인 (The 10-Step Pipeline)

프롬프트 작성 시 기술 용어를 먼저 쓰지 말고, 반드시 아래 10단계 순서대로 설계한다:

1. **감정의 목적 (Emotional Objective)**: 이 씬에서 관객이 느껴야 할 단 하나의 감정
2. **블로킹 (Blocking)**: 인물의 위치, 시선, 물리적 거리, 자세 변화
3. **쇼트 크기 (Shot Sizes)**: Wide ➔ Medium ➔ Close-up ➔ ECU의 조합
4. **앵글 (Angles)**: Low, High, OTS, Profile, Reflection
5. **렌즈 (Lens)**: 35mm(환경), 50mm(인간 시야), 85mm(인물 내면)
6. **동기화된 무빙 (Motivated Movement)**: Push-in, Static, Pan
7. **소품 인서트 & 리액션 (Inserts & Reactions)**: 감정의 쉼표와 복선
8. **편집 호흡 (Uneven Rhythm)**: 불균등한 초 단위 리듬 배분
9. **사운드 (Sound & Silence)**: 현장음(SFX)과 대사 후 2초의 침묵
10. **질감 (Texture - 마지막 레이어)**: 35mm 필름, 조명 톤앤매너
