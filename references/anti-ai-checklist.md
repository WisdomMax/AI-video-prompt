# 안티 AI 체크리스트 및 촬영 실수 라이브러리 (Anti-AI Checklist)

이 가이드는 AI 비디오 모델의 완벽하고 인위적인 3D 그래픽 느낌을 제거하고, 현실적인 날것의 질감을 구현하기 위한 체크리스트와 영문 묘사 템플릿을 제공합니다.

---

## 1. AI 디폴트 미학 탈피용 부정 프롬프트 매핑

AI는 지시가 없으면 기본적으로 가장 대중적이고 완벽한 화면을 그리려고 합니다. 아래의 매핑 표를 참고하여 해당하는 **부정 묘사(Negative Constraints)**를 프롬프트에 추가하세요.

| AI 디폴트 성향 | 화면에 나타나는 문제점 | 사용해야 할 영문 부정 문구 (Negative Prompts) |
| :--- | :--- | :--- |
| **영화 같은 부드러운 운경** | 짐벌이나 로봇암을 쓴 것 같아 인위적임 | `No smooth camera gimbal movement, no professional track shot` |
| **삼각대 같은 완벽한 고정** | 손으로 들고 찍는 일상적인 느낌과 안 맞음 | `No tripod stabilization, no locked-off camera mount` |
| **현대적인 상업 필름 색감** | 지나치게 쨍한 톤과 대비, 광고 영상 같음 | `No modern professional color grading, no commercial color palette` |
| **완벽한 대칭/센터构图** | 계산된 연출 티가 나며 스냅 사진 같지 않음 | `No perfect center composition, imperfect framing, off-center subject` |
| **지나치게 정돈된 배경** | 배경에 자동으로 화려한 카페나 깔끔한 매장 배치 | `No clean commercial studio background, no luxury storefronts` |
| **자동으로 깔리는 BGM** | 다큐멘터리나 실감 나는 현장감을 훼손함 | `No music, no studio sound design, no voiceover` |
| **과도한 밀착 필터(磨皮)** | 인형 피부처럼 모공이 없고 뭉개진 질감 | `No airbrushed plastic skin, realistic skin texture, natural pores` |
| **컷 교체 시 일관성 붕괴** | 프레임이 바뀔 때 얼굴이나 옷이 미세하게 바뀜 | `In entire video, maintain consistent identity, clothing, and appearance` |

---

## 2. 촬영 실수 영문 라이브러리 (Imperfect Events)
*시간선(`[Timeline]`) 문단을 짤 때, 매 컷마다 아래의 영문 묘사 중 **하나씩**을 배치하여 비디오에 자연스러운 질감을 얹으세요. (중복 사용 금지)*

### 🎥 촬영자의 미숙함 및 장비 오작동 (Shooter's Errors)
* `autofocus hunting back and forth between the subject and the foreground objects` (오토포커스가 인물과 전경 사이를 헤매며 징징거리는 동작)
* `imperfect tracking, camera pan slightly lags behind the subject's sudden turn` (인물이 급하게 돌 때 카메라 앵글이 한 템포 느리게 따라가는 현상)
* `abrupt and clumsy manual zoom in and out, focus temporarily blurring` (속도 조절이 매끄럽지 않은 수동 줌 인/아웃과 순간적인 초점 흐려짐)
* `handheld camera shake and motion blur due to walking step vibration` (걸어가는 발걸음 진동으로 인한 거친 손떨림과 잔상 모션 블러)
* `flicker in exposure as the camera adjusts to changing light sources` (조도가 변할 때 카메라 센서의 노출이 어색하게 껌벅이며 조절되는 현상)
* `a thumb or finger briefly blocking the corner of the camera lens` (촬영자의 손가락이나 카메라 끈이 화면 구석에 아주 잠깐 걸쳐 찍히는 현상)

### 🍃 우연한 환경의 간섭 (Environmental Interference)
* `a sudden gust of wind blowing stray hair across the subject's face` (갑작스러운 미풍으로 인해 몇 가닥의 머리카락이 인물의 얼굴을 가리는 현상)
* `shadow of a large cloud passing over, dimming the sunlight briefly` (지나가는 구름 그림자가 햇빛을 가려 화면이 일시적으로 어두워지는 현상)
* `a stray cat crossing the path, causing the subject to naturally look down` (길고양이가 발밑을 스쳐 지나가 인물이 자연스럽게 아래를 내려다보는 반응)
* `a random passerby briefly walking straight through the camera's line of sight` (전혀 무관한 행인이 카메라 앞을 휙 지나쳐 인물을 가리는 현상)
* `dappled sunlight flashing unevenly on the lens, creating a soft orange flare` (햇빛 각도가 꺾이면서 렌즈에 부드러운 오렌지색 플레어 잔상이 남는 현상)

---

## 3. 완성 전 체크리스트 (Self-Checklist)
프롬프트를 다 쓴 뒤 다음 항목들을 최종 점검하세요.
- [ ] **캐릭터 락**: 인물 묘사 끝자락에 `maintain consistent identity, clothing...` 문구가 잘 들어갔는가?
- [ ] **장소 배경**: 광고판이나 과한 세트장 느낌을 걷어내는 `No commercial...` 등의 부정 프롬프트가 포함되었는가?
- [ ] **카메라 사양**: 사용하는 기기(DV, 폰카 등)에 맞는 물리적 오작동 묘사가 6개 이상 들어갔는가?
- [ ] **부정문 삼총사**: 문단 끝에 `No stabilization, no cinematic camera movement, no modern color grading`을 삽입했는가?
- [ ] **시간선 구성**: 각 컷별로 단 하나의 촬영 실수(Imperfect Event)가 겹치지 않고 자연스럽게 들어갔는가?
- [ ] **영상 마무리**: 녹화가 뚝 끊기거나 카메라가 땅을 비추는 식(`Cuts abruptly to black...` 또는 `Camera pans down to ground...`)의 사실적인 마무리 문구가 적용되었는가?
- [ ] **추상어 필터링**: "아름다운(Beautiful)", "시네마틱(Cinematic)" 같은 주관적인 미사여구가 완전히 지워졌는가?

---

## 4. 시각 룩 극실사화 2대 원칙 (Visual Photorealism Look)

Wan 3.0 모델에서 화면의 인위적인 컴퓨터 그래픽 질감과 성형 인형 피부를 없애기 위한 렌더링 규칙:

1. **광학적 불완전성 긍정 주입 (Optical Imperfections vs. Digital Sheen)**:
   - 16mm Kodak Tri-X 은염 필름 입자, 35mm Kodak Vision3 텅스텐 질감 등 아날로그 필름 스톡의 물리적 질감을 긍정 선언하여 디지털 비디오 광택(`digital sheen`) 원천 박멸.
2. **생체 미세 텍스처 바인딩 (Anti-Wax & Micro-Texture Rule)**:
   - `matte skin micro-texture, visible natural pores, fine vellus hair, realistic subsurface scattering` (무광 미세 모공, 잔솜털, 피부 속 혈색 투과)을 명시하여 실리콘/뷰티필터 마네킹 피부 100% 차단.

---

## 5. AI 모션 안정화 및 정방향 동사 수칙 (Motion Stability & Affirmative Syntax)

1. **타임라인 본문 내 부정어 100% 영구 금지 (Zero Negatives in Body Rule)**:
   - `never`, `do not`, `does not`, `no`, `without`, `zero`, `stop`, `pause`, `fall` 등 부정어 일절 금지! AI 어텐션 분산을 막고 오직 100% 정방향 물리 행동 동사(`sprints forward at sustained full velocity`, `pushes continuously`)만 서술하여 모션 왜곡/비틀거림 차단.

---

## 6. Negative 프롬프트 다이어트 수칙 (Negative Token Hygiene)

1. **Negative 프롬프트 극강의 다이어트 (Max 8~10 Core Words Rule)**:
   - 중복 부정어 도배를 100% 금지하고 오직 `music, BGM, singing, vignette, film border, digital sheen, waxy skin, static camera, text, watermark` 등 8~10개 급소 단어로만 묶어 AI 신경망 주의력(Attention) 왜곡 방지.

---

## 7. 순수 현장 오디오(Zero-BGM Foley) 및 백업 수칙

1. **오디오 엔진 BGM 오염 단어 전면 차단 (Zero Audio Trigger Words)**:
   - `rhythmic`, `tempo`, `beat`, `hum`, `drone`, `resonance`, `whistle`, `vocal`, `beep` 등 비트/신스/BGM을 연상시키는 단어 전면 배제, 오직 거친 현장 물리 효과음(Raw Dry Foley SFX)만 기재.
2. **수정 시 순차 백업 의무화 및 핀포인트 교체 수칙 (Sequential Auto-Backup Rule)**:
   - 프롬프트 수정 지시마다 무조건 기존 파일을 `prompts_wan_backup01.md`, `backup02.md` 순으로 넘버링 복사 백업을 생성한 후 지시받은 부위만 핀포인트 수정.
