# AI 비디오 프롬프트 프로젝트 커스텀 규칙 (AI Video Prompting Project Rules)

이 문서는 AI 비디오 생성 모델(Wan 3.0, Seedance, MiniMax H3, Runway, Kling 등)에서 발생할 수 있는 비주얼 변형, 캐릭터 락 붕괴, 대사 싱크 불일치 문제를 방지하기 위해 실전 튜닝을 통해 정립한 최적화 규칙입니다.

---

# Part I. AI 비디오 공통 마스터 헌법 & 워크플로우

## 1. 영구 불변 핵심 헌법 (The Immutable Core Directing Directives)

> **⚠️ 절대 원칙**: 모든 AI 비디오 프롬프트는 아래 5대 헌법을 1초도 어기지 않고 100% 준수해야 한다.

### 1-1. 피드백 반영 시 '과잉 금지어(A ➔ B 교체 시 A 블랙리스트화) 금지 헌법' (Zero Over-Filtering Rule) 🔴 필수
* **A ➔ B 단순 교체 원칙 (Pure Contextual Replacement)**:
  - 감독님이 "A 대신 B로 해줘", "A는 빼자", "맑은 날씨로 가자"라고 수정 지시를 내리면, 이는 **"해당 씬의 연출 내용을 B로 바꾸라"는 뜻일 뿐, 이전 요소(A)를 범죄 단어 취급하여 Negative나 전역 금지어로 등록하라는 뜻이 절대 아니다.**
  - 프롬프트 본문에서 A를 지우고 자연스러운 B 연출로만 문장을 우아하게 고쳐 쓴다.
* **Negative(부정 프롬프트) 남용 영구 금지**:
  - 감독님이 직접 "이거 Negative에 넣어"라고 명시하지 않는 한, 수정한 이전 단어(A)를 `[Negative]`에 기계적으로 처넣는 멍청한 과잉 대응을 100% 금지한다.
  - 불필요한 부정 단어가 Negative에 늘어날수록 AI 모델의 신경망 주의력(Attention)이 꼬여서 화면 왜곡(Artifact)이 심해진다.
* **극단적 흑백논리 차단 (No Reactionary Blacklisting)**:
  - "이거 빼"라는 피드백에 놀라서 관련된 정상적인 단어들까지 싹 다 날리거나 금지어로 묶어버리는 과잉 검열(Reactionary Overkill)을 엄격히 금지한다.

### 1-2. 소설식 은유·미사여구 100% 영구 박멸 (Zero Literary Fluff Rule)
* **금지 대상**: `like a broken dam`, `heavens`, `infrasound`, `scrap metal`, `vortex`, `mysterious aura`, `tempest` 등 소설적 비유, 추상 명사, 관용구를 작성하는 행위를 100% 영구 금지한다.
* **이유**: 소설식 형용사가 들어가는 순간 비디오 AI는 인물의 연기를 버리고 하늘에 회오리 먹구름을 치거나 엉뚱한 CG 파편을 렌더링하여 화면을 뭉갠다.
* **강제 원칙**: 오직 **물리적 눈에 보이는 팩트(Action Verbs & Physical Facts)**만 기술한다.

### 1-3. 프롬프트 본문 3대 요소 강제 집중 공식 (The 3-Pillar Staging Formula)
모든 씬 플로우(`[Scene Flow]`) 문장은 오직 아래 **3가지 요소** 외에는 1글자도 적지 않는다:
1. **[카메라 워크 & 전환]**: 직관적 카메라 앵글/무빙 및 전환 효과 (크래쉬 줌, 90도 오빗, 핸드헬드, 휩팬, 랙 포커스 등 장면에 맞춘 역동적 카메라 이동).
2. **[인물 연기]**: 감정 형용사("슬프다", "화가 난다") 대신 얼굴 근육(저작근/눈빛), 시선 처리, 손/발의 물리적 이동 동사 및 구어체 대사.
3. **[상대/주변 물리 반응]**: 상대방의 방어 동작(X자 가드 등), 물보라, 주변 기물의 상호작용 (멍때리거나 사라지지 않게 1:1 바운딩).

### 1-4. 외형 묘사 제로 & 극단 간결 역할·스케일 룰 (Zero Appearance & Scale-Only Role Rule)
* 레퍼런스 이미지(`@Image 1`, `@Image 2` 등)나 비디오(`@Video 1`)가 있으면 외형(얼굴, 의상, 헤어)을 텍스트로 안 쓰는 것 자체가 완벽한 외형 락이다. `photo locked`, `strictly matches photo` 같은 군더더기 말도 일절 쓰지 않는다.
* `[Roles]`는 오직 **[극 중 역할]**과, 사진만으로 알 수 없는 **[물리적 크기/스케일]**만 2~3단어로 초간결하게 작성한다:
  - *일반 인물*: `@protagonist: Lead detective.`
  - *배경 영상*: `@background_video: Busy downtown intersection footage.`
  - *소품/음식*: `@hero_prop: Key evidence briefcase.`
  - *거대 크리처/메카닉*: `@kraken: 120-meter giant octopus leviathan.` (크기/스케일 지정이 필요할 때만)
* 본문 `[Scene Flow]` 역시 옷/얼굴 묘사는 100% 영구 배제하고 오직 **카메라, 연기/대사, 물리적 상호작용 반응**에만 집중한다.

### 1-5. 원작자 의도 충실 & 과잉 수식어 증폭 금지 헌법 (Intent Fidelity & Anti-Embellishment Rule) 🔴 절대 필수
* **원문 의도 1:1 보존 (Preserve Core Intent & Zero Speculative Expansion)**:
  - 감독님이 지시한 자연어의 핵심 의도와 말맛을 1:1로 정확하게 계승한다.
  - "디테일을 보강한다", "전문적으로 포장한다"는 명목으로 원문에 없는 주관적 수식어, 자극적이거나 관능적인 형용사, 불필요한 생체/육체적 묘사를 임의로 덧붙이는 과잉 각색(Hallucinatory Amplification)을 100% 영구 금지한다.
* **성적 다의어 및 위험 어휘 원천 차단 (Zero Innuendo & Risk Vocabulary)**:
  - 텍스트 번역 및 영문화 과정에서 성인물(NSFW) 안전 검열기가 오해할 수 있는 이중적 의미의 단어(Double Entendre), 신체 분비물 및 관능적 수식어를 원천 배제한다.
  - 인물의 표정이나 행동을 묘사할 때는 감각적 형용사 대신 **명확한 물리적 행동 동사(Physical Action Verbs)**와 **객관적 사실 팩트**만으로 담백하고 명료하게 기술한다.
* **다국어 네이티브 모델 언어 존중 (Multilingual Native Directing)**:
  - Wan 3.0, Kling 등 최신 비디오 생성 모델은 한국어 자연어와 일상 구어체를 네이티브 수준으로 정밀하게 이해한다.
  - 억지스러운 기계적 영문 번역으로 인한 뉘앙스 왜곡과 어휘 필터링 위험을 방지하기 위해, 감독님이 전달한 직관적인 한국어 디렉팅과 구어체 대사를 최우선으로 존중하여 반영한다.
* **시각 참조 자산(Visual Assets) 수식어 잉여 배제**:
  - 이미 레퍼런스 이미지나 영상(`@태그`)으로 외형이 확정된 인물, 소품, 배경, 음식에 형태적·감각적 수식어를 텍스트로 중복 기재하지 않는다. 오직 해당 자산의 [역할 명칭]과 [필요시 크기/스케일]만을 건조하고 명확하게 바인딩한다.

---

## 2. 3단계 표준 프로덕션 워크플로우 (Production Workflow)

> **⚠️ 최우선 규칙**: 새 영상 주제나 아이디어가 들어왔을 때 즉시 프롬프트를 작성하는 행위를 절대 금지한다. 반드시 아래 3단계를 순서대로 밟은 후에만 프롬프트 작성에 진입한다.

### Phase 1 — 기획 핑퐁 & 스킬 맵 라우팅 (Planning & Skill Routing) 🔴 즉시 시작 금지
새 주제/아이디어를 받으면 프롬프트 작성 전에 [SKILL_MAP.md](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/SKILL_MAP.md)를 먼저 스캔하여 가장 적합한 스킬/카테고리를 식별하고, 채팅으로 아래 항목을 확인하며 기획을 구체화한다.

* **타깃 스킬 및 최적 카테고리 매칭**:
  - `cinematic-film-directing` (거장 영화감독 시네마틱 / 블로킹 / 서브텍스트 물리화 / 85mm 얼굴 클로즈업 / 소품 인서트 / 침묵의 여운)
  - `minimax-h3-prompting` (18대 모션그래픽/타이포그래피/커머셜/MV)
  - `realistic-video-prompting` (Wan 3.0 실사 / 시댄스 2.5 맨몸 액션 / 중국 숏드라마 팩토리 룰 / 폰카 8대 수칙 / DV 16mm 결함)
  - `hongkong-cinema-prompting` (80~90년대 무협/느와르 레트로)
  - `scifi-techno-baroque` (SF 테크노 바로크 / 70s 아날로그 SF 판타지 / 고대 유물 기계 & 의식용 바이오메카닉)
  - `micro-cinematic-prompting` (시네마틱 숏 프롬프트 / 100단어 초압축 5단 뼈대 / 릴스·숏츠 3초 훅 / Living Portrait)
  - `kinetic-beat-montage` (키네틱 비트 몽타주 / 0.3~0.8s 초고속 컷 / 4대 미장센 앵커링 / 힙합 몽타주 / 안티 모핑)
  - `15대 도메인별 특화 스킬` (`01-cinematic` ~ `15-real-estate`)
* **스토리 & 감정 흐름**: 주인공은 누구인가? 어떤 감정 변화를 담을 것인가? 핵심 장면(Hook/클라이맥스/엔딩)은 무엇인가?
* **타깃 생성기 확인** (반드시 명시):
  - `Wan 3.0` — 글자 수 한도: **19,500자 미만** (최대 30초 지원), 레퍼런스 태그: 고유 식별자 이름 직접 사용 (`@image_name`, `@protagonist` 등)
  - `Runway Gen-3 / Gen-4` — 레퍼런스 태그: 고유 식별자 이름 직접 사용 (`@young_chungmyung`, `@bg_gate` 등)
  - `MiniMax H3` (Hailuo 3.0) — 글자 수 한도: **5,900자 미만** (안전 권장 5,500자 이내), 레퍼런스 태그: 고유 식별자 이름 직접 사용 (`@young_chungmyung`, `@bg_gate` 등)
  - `Seedance 2.5` (Artlist) — 글자 수 한도: **15,000자 이내**, 레퍼런스 태그: 고유 식별자 이름 직접 사용
  - `Seedance 2.0` — 글자 수 한도: **3,450자 미만**, 레퍼런스 태그: 고유 식별자 이름 직접 사용 (`@young_chungmyung`, `@bg_gate` 등)
  - `Kling 3.0 Pro` — 글자 수 한도: **2,450자 미만**, 레퍼런스 태그: `@tag1`~`@tag7` (최대 7개)
* **레퍼런스 이미지 보유 여부**: 업로드 가능한 실제 이미지가 있는가? 없으면 `@` 태그 없이 텍스트 묘사로만 가야 함
* **화면 방향**: 가로(16:9) / 세로(9:16)
* **영상 길이**: 15초 / 29초 / 60초 등
* **히어로 이미지 필요 여부**: 레퍼런스용 이미지를 AI로 먼저 생성해야 하는가?

### Phase 2 — 콘티 승인 (Storyboard Approval) 🟡 기획 완료 후
기획이 구체화되면 **씬 구성표(타임라인 스케치)**를 채팅 텍스트로 간결하게 공유하고, 감독님의 **명시적 승인**("이대로 만들어", "프롬프트 작성해" 등)을 받은 후에만 Phase 3으로 진입한다. 승인 없이 프롬프트를 선제 작성하지 않는다.

### Phase 3 — 프롬프트 제작 & 프로젝트별 영구 보관 (Prompt Production & Archiving) 🟢 승인 후 진입
승인된 콘티를 바탕으로 해당 생성기 스펙(글자 수 한도, `@` 태그 형식, Aspect Ratio 필드 등)에 맞춰 프롬프트를 작성하고, **파이썬으로 글자 수를 정밀 검증**한 후 최종 출력한다.

* **프로젝트 특별 폴더(`projects/`) 영구 누적 저장 의무화 (Zero-Overwrite Rule)**:
  - `video_prompts.md` 등 단일 파일에 다음 작업 프롬프트를 덮어써서 이전 프롬프트를 유실하는 행위를 100% 영구 금지한다.
  - 새 프롬프트 제작 시 무조건 **`projects/[프로젝트제목]/`** 전용 폴더를 생성하고, 그 안에 `prompts_[생성기].md` (및 `storyboard.md`, `story.md`)로 독립 분리하여 차곡차곡 누적 보관한다.
  - 프롬프트 작성이 완료되면 채팅창에 프롬프트를 출력함과 동시에, 저장된 프로젝트 파일의 **클릭 가능한 링크(`[projects/...](file:///...)`)**를 반드시 함께 안내하여 유실 없이 관리한다.

---

# Part II. 프롬프트 표준 규격 & 직관형 오가닉 연출 수칙 (Intuitive Organic Directing Rules)

## 3. 프롬프트 레이아웃 및 6대 오가닉 표준 헤더 (Organic Headers)
비디오 생성기(Wan 3.0, Seedance 2.5, Runway, Kling 등) 입력용 프롬프트 파일(`projects/[프로젝트명]/prompts_[생성기].md`)은 인위적인 초 단위 족쇄와 복잡한 수식어를 걷어내고, **단 1개의 직관형 오가닉 표준 규격**만을 사용합니다.

* **최상단 파트 넘버링 및 화면 비율(Aspect Ratio) 명시**:
  - 마크다운 코드 블록( ```text ~ ``` ) 내의 가장 첫째 줄은 무조건 **`Part-N [Aspect Ratio: 16:9]`** 또는 **`Part-N [Aspect Ratio: 9:16]`** 단일 규격으로 시작합니다.
* **6대 오가닉 단일 표준 헤더 (Organic Standard Headers)**:
  - 복잡한 중복 헤더를 통합하고 오직 아래 6개 표준 헤더로 통일합니다.
    1. **`[Tags]`**: 생성기 UI에 매핑할 이미지/비디오 레퍼런스 태그 리스트 (`@Image 1, @Image 2...`)
    2. **`[Roles]`**: 각 태그의 인물/배경 역할 1:1 바인딩
    3. **`[Style]`**: **질감(Texture 100%) & 톤/조명(Tone & Lighting 100%) 퍼센트(%) 분할 필수** (카메라 무빙 일절 기재 금지)
    4. **`[Scene Flow]`**: **시간표(00-03s) 없는 자연스러운 연속 씬 서술** (각 씬마다 필요한 카메라 무빙 및 역동적 전환 현장 직접 지시)
    5. **`[Audio]`**: 순수 물리 효과음(SFX), 현장음, 대사 전용 (BGM 일절 금지)
    6. **`[Negative]`**: BGM, 자막, 워터마크, 3D 렌더, 왜곡 배제
* **생성기별 글자 수 한도 의무화 (Strict Char Limit by Generator)**:
  - `Wan 3.0`: **19,500자 미만** (최대 30초 지원, 직관형 권장 3,000~8,000자 이내)
  - `Seedance 2.5` (Artlist): **15,000자 이내** (직관형 권장 3,000~6,000자 이내)
  - `MiniMax H3` (Hailuo 3.0): **5,900자 미만** (안전 권장 4,000자 이내)
  - `Seedance 2.0` (Artlist): **3,450자 미만** (안전 권장 2,000자)
  - `Kling 3.0 Pro`: **2,450자 미만** (안전 권장 2,000자 이내)

---

## 4. `[Style]`의 '질감 vs 톤' 퍼센트(%) 분할 의무 헌법 (Percentage Style Rule)
`[Style]` 영역에 모호한 영화적 수식어나 카메라 무빙을 섞어 기재하는 행위를 **100% 영구 금지**합니다. 
AI의 신경망 주의력(Attention Weight)을 수학적으로 분리하기 위해 오직 **질감(Texture 100%)**과 **톤/조명(Tone & Lighting 100%)**의 지분을 퍼센트로 명확히 분할 기재합니다:

* **단일 표준 [Style] 템플릿**:
  ```text
  [Style]
  - Texture (질감 100%): 70% tactile physical 35mm film grain with natural skin pores and asphalt dust, 30% crisp high-shutter practical impact definition (0% plastic CGI render).
  - Tone & Lighting (톤/조명 100%): 65% bright neutral daylight sun, 25% vibrant comic-book primary colors (saturated cobalt blue and crimson red), 10% high-contrast deep black shadows.
  ```
* **수칙**:
  1. `Texture 100%`: 실사 아날로그 필름, 모공, 직물, 먼지 등 물리적 실사 비율 명시 (플라스틱 3D CG 0% 락).
  2. `Tone & Lighting 100%`: 자연광, 인공 조명, 메인 컬러 팔레트, 그림자 콘트라스트 비율 명시.
  3. **카메라 무빙 절대 배제**: 카메라 앵글과 무빙은 Style에서 100% 제외하고, 오직 아래 `[Scene Flow]`의 각 장면에서 현장 직접 지시합니다.

---

## 5. 자연스러운 씬 플로우 (`[Scene Flow]`) & 현장 카메라 무빙 연출 규칙
초 단위(`00-03s`)로 컷을 잘게 쪼개어 AI의 연산을 구속하던 낡은 타임라인 족쇄를 폐기하고, 사건과 행동이 물 흐르듯 이어지는 **자연스러운 순차적 씬 플로우(`[Scene Flow]`)**를 사용합니다.

* **표준 [Scene Flow] 작성 포맷**:
  ```text
  [Scene Flow]
  1. [장면 1 도입 & 카메라 지정]: 카메라 앵글/무빙(예: wide static shot)과 함께 피사체의 초기 상태 및 배경 상황 직관적 서술.
  2. [장면 2 사건 & 카메라/전환 지정]: 사건의 발생, 물리적 충돌, 필요한 카메라 무빙(예: rapid handheld crash-zoom in, 90-degree orbit) 및 전환 효과 서술.
  3. [장면 3 인물 리액션 & 대사]: 인물의 표정 연기, 시선 처리, 대사 발화.
     Dialogue: "대사 내용"
  4. [장면 4 피날레]: 최종 액션 및 엔딩 카메라 구도.
  ```
* **현장 즉시 카메라 워크 & 역동적 전환 효과 복원 (Dynamic Transitions & Moves)**:
  - 기계적인 하드 컷만 강제하지 않으며, 영상의 장르와 리듬감에 맞춰 **크래쉬 줌(Crash-Zoom), 90도 오빗 회전(Orbit Arc Shot), 랙 포커스(Rack Focus), 휩팬(Whip-Pan), 오브젝트 패싱 와이프(Object Pass Wipe)** 등 현장에 필요한 카메라 무빙과 전환 효과를 각 번호 씬에서 자유롭고 역동적으로 직접 지시합니다.
* **직관적인 명령 언어 (Simple & Punchy Fact-First Directing)**:
  - 복잡한 렌즈 광학 메타데이터나 문학적 비유("마치 폭풍 같은 분노")를 완전히 배제하고, **"누가 ➔ 어디서 ➔ 무슨 물리적 행동(착지, 타격, 줌, 미소)을 하고 ➔ 카메라는 어떻게 움직이는가"**의 명확한 팩트와 동사 중심으로 직관 서술합니다.

---

## 6. 레퍼런스 이미지 태그(@) 및 외형 통제 수칙 (Image Tags & Costume Control)
일치하는 이미지 소스 없이 `@` 기호를 남발하여 발생하는 AI의 이미지 렌더링 붕괴와 캐릭터 간 간섭을 완벽히 통제합니다.

* **[Roles] 및 본문 '외형/복장 텍스트 묘사 통제 및 연기·카메라 집중 원칙' (Visual Economy & Action Focus Rule)**:
  - **기본 대원칙 (사진 100% 일임)**: 이미 업로드한 `@태그` 레퍼런스 이미지 그대로 연출하는 일반적인 경우에는 `[Roles]`와 타임라인 본문에 옷감(`white robes`, `brown silk`), 머리모양(`long hair`, `ponytail`), 나이, 외모 등의 **외형적 텍스트를 기재하는 행위를 100% 엄격 금지**합니다. (텍스트를 쓰는 순간 AI가 사진 데이터를 버리고 텍스트에 낚여 엉뚱한 중국 드라마 배우나 이상한 옷을 렌더링하는 치명적 오염 오류 발생)
  - **유일한 예외 (변신 및 특수 복장 변경 시)**: 레퍼런스 사진과 복장이 완전히 달라지거나(예: 일상복 ➔ 전신 갑옷 전투 변신 모드), 특정 부위의 특수 상태를 강제로 강조해야 하는 극히 예외적인 경우에만 차이점을 텍스트로 명시합니다.
  - **표준 프롬프트 집중 영역**:
    - `[Roles]`는 `photo locked` 등 군더더기 없이 오직 **`@[태그명]: [극 중 역할]`** (필요 시 물리적 크기/스케일만 추가) 단 2~3단어로 초간결하게 기재합니다.
      - 예: `@mother: Protagonist mother.`, `@kraken: 120-meter giant octopus leviathan.`
    - 프롬프트의 모든 문장은 외형 묘사를 싹 빼고, 오직 **[카메라 앵글/렌즈/무빙]**과 **[인물의 표정 연기, 물리적 동선, 상호작용 동작 동사]**에만 100% 집중하여 작성합니다.
* **이미지 소지 대상만 `@` 적용**:
  - 실제로 생성기에 업로드하여 연동할 '물리 레퍼런스 이미지 파일'이 명백히 존재하는 기획 개체만 `@` 기호를 붙입니다. (예: 캐릭터 설정, 장벽 입구 근경/원경, 쉘터 내부, 스마트 시티 등). 이미지가 없는 텍스트 상상 개념(예: 몬스터, 일반 미로 배경 등)은 `@` 기호를 떼고 일반 영어 묘사로만 기재합니다.
* **파트별 레퍼런스 이미지 수량 제한 및 단일 이미지 표기법**:
  - **단일 이미지 업로드 시 (`1장 사용`)**: `@` 태그 생략 가능. 프롬프트 본문에서 `the reference model`, `the model in the uploaded reference image`로 지칭하여 태그 매핑 오류를 방지하고 간결하게 기재합니다.
  - **다중 이미지 연동 시 (`2장 이상 사용`)**:
    - `Runway / Seedance / MiniMax H3 / Wan 3.0`: 고유 식별자 이름 태그 사용 (`@young_chungmyung`, `@bg_gate`, `@baekcheon` 등 직관적 고유명사 또는 `@Image 1`, `@Image 2` 직접 바인딩).
    - `Kling 3.0 Pro`: `@tag1`~`@tag7` 형식 사용 (**최대 7개**).
* **캐릭터 복장 최소화 및 변신 스위칭 강제**: 이미 태그 이미지에 세부 외형이 존재하므로 구구절절한 텍스트 묘사는 최소화합니다. 대신 보스전 진입 전(일반 모드: `Normal casual pre-transformation state`)과 보스전 격돌 중(전투 변신 모드: `Transformed battle state` - 전신 갑옷 및 마법 코트 장착)의 스위칭 상태를 `[Main Character]` 필드 최상단에 극도로 명시하여 AI가 다른 모드 복장을 섞어서 그리는 현상을 차단합니다.

---

## 7. 긍정적 묘사 중심의 지시 원칙 (Positive Description First)
AI 비디오 모델은 부정 지시어(`No ...`, `Don't ...`)가 많을수록 프롬프트의 지시 맥락을 왜곡하거나 렌더링 품질을 급감시킵니다. 
따라서 "하지 마라"식의 부정적인 통제 대신, **"무엇을 어떻게 그리고 행동해야 하는지"**를 정밀하게 명시하는 **긍정 묘사(Positive Description)**에만 초점을 맞춥니다.

* **원치 않는 것의 배제 방식**: 무작정 부정 명령어를 나열하기보다는 카메라의 앵글, 캐릭터의 동적 액션, 특수 효과의 구체적인 움직임을 확실한 동작 동사와 목적어의 긍정문 형태로 묘사하여 원천적으로 불량 생성을 예방합니다. (예: '안개 없음' 대신 '맑은 노을 하늘과 선명한 가시성의 골짜기'로 표현)
* **부정 제약어(`[Negative]`) 내 안전 필터 단어(Gore, Blood 등) 기재 100% 영구 금지**:
  - `[Negative]` 필드에 `gore`, `blood`, `wounds`, `injury`, `corpse`, `decapitation` 같은 단어를 기재하는 행위를 **100% 영구 금지**합니다.
  - 비디오 AI의 텍스트 안전 검열기(Safety Classifier)는 긍정/부정을 구분하지 않고 **프롬프트 텍스트 전체에 `gore`, `blood`라는 영단어가 존재하는 순간 즉시 시스템 거부(Safety Block)를 발생**시킵니다.
* **빈티지/필름 장르에서의 고화질 단어 및 [Negative] blurry 기재 100% 영구 금지 (Vintage Exclusivity Rule)**:
  - 1970~90년대 아날로그 시네마, 빈티지, 필름 질감 프로젝트에서는 **현대 디지털의 고화질 단어(`crisp`, `sharp`, `laser-sharp`, `pristine`, `ultra-clear`)를 100% 영구 금지**합니다. (고화질 단어가 들어가는 순간 빈티지의 광학적 블룸과 부드러운 유제 질감이 전멸함)
  - `[Negative]`에 **`blurry`를 기재하는 행위를 영구 금지**합니다 (소프트한 빈티지 렌즈 블룸을 AI가 삭제하는 원인).
  - 대신 **`modern sharp digital video, cold clinical 4K sharpness, harsh digital contrast, clean digital sensor look`**을 Negative에 필수 기재하여 차갑고 쨍한 디지털 질감을 원천 차단합니다.

---

## 8. 순수 현장 오디오(Foley) 및 사운드 지문 작성 규격 (Sound & Foley Rules)
AI 비디오/오디오 모델의 오디오 파서 오작동을 차단하고 생생한 현장 효과음(SFX)을 유도하기 위해 다음 작성 규격을 엄격 준수합니다.

* **1. 음악(BGM) 및 악기/BPM/드럼 단어 프롬프트 기재 100% 영구 금지 (Zero Music Word Rule)**:
  - `[Style]`, `[Scene Flow]`, `[Audio]` 등 프롬프트 어디에도 `160 BPM`, `rock MV`, `drum crash`, `melody`, `brass`, `music`, `soundtrack` 같은 음악 관련 단어를 기재하는 행위를 **100% 영구 금지**합니다.
  - 음악 단어가 1개라도 들어가는 순간, 비디오 AI의 오디오 엔진이 "BGM을 합성하라"는 명령으로 오해하여 지멋대로 엉뚱한 BGM/악기 소리를 생성하여 실제 OST 음원 합성을 100% 망치게 됩니다.
  - `[Audio]` 필드와 Foley `<...>`에는 오직 **발걸음, 바람소리, 칼 부딪히는 소리 등 순수 물리 효과음(SFX)과 현장음(Ambient), 캐릭터 대사(Dialogue)**만 기재하며, `[Negative]`에 무조건 **`BGM, music, soundtrack, melody, instruments, singing`**을 명시합니다.
* **2. 씬 플로우 내부 1:1 배치 원칙 (Scene-Level Placement)**:
  - Dialogue 및 Sound 지문 라인은 `[Scene Flow]` 내 각 번호 씬 블록 내부의 동작 묘사 바로 아랫줄에 1:1로 정확히 배치하거나 독립된 `[Audio]` 필드에 명확히 집약합니다.
* **3. 풍부한 4~6단어 물리 SFX 묘사 수칙 (Rich Physical Sound Spec)**:
  - `<thud>`, `<flour poof>` 같은 단답형 1~2단어 표기를 엄금합니다. 장면 속 실제 물리 충돌, 마찰, 액체 분사, 열기 팽창 등 생생한 현장 동작을 묘사하는 **4~6단어 이상의 풍부한 물리 명사구/형용사구**로 기재합니다.
* **4. `no BGM, Foley SFX only` 필수 주입 수칙 (Mandatory BGM Suppression)**:
  - 오디오 지문 태그 내 최후반에는 항상 **`no BGM, Foley SFX only`**를 필수로 포함하여 오디오 생성 엔진의 BGM 작곡 오작동을 이중 차단합니다.
    - *예시*: `Sound: <Heavy dough thud impact on wood, flour cloud poof, table vibration, no BGM, Foley SFX only>`

---

## 9. 토큰 절약 및 480p 영상 자동 아카이빙 수칙 (Efficiency & Archiving)

* **1. 토큰 절약 및 무분별한 파일 수정 통제 수칙 (Token Efficiency & Editing Control)**:
  - 아이디어 기획, 대사 핑퐁, 톤 조율 단계에서는 대형 프롬프트 파일들을 매 턴마다 지체 없이 덮어써서 토큰을 소모하는 행위를 금지합니다.
  - 기획 변경점은 채팅을 통해 핵심만 간결하게 설명·메모하고, 감독님이 명시적으로 "파일 수정해라" 또는 "최종 파일로 정리해라"고 요청할 때만 단 한 번에 한꺼번에 묶어서 업데이트합니다.
* **2. 프롬프트 & 480p 영상 자동 아카이빙 수칙 (Prompt & 480p Video Auto-Archiving Rules)**:
  - 감독님이 `archive/inbox/`에 폴더를 생성하거나 파일(영상, `@Image 1`, `@Image 2` 레퍼런스, 프롬프트 텍스트)을 넣고 "정리해줘"라고 요청하면 즉시 인제스트를 수행합니다.
  - `archive/tools/ingest.py`를 실행하여 영상을 480p(가로 `854x480` 또는 세로 `480x854`, H.264 CRF 26, AAC 오디오)로 압축하여 3~5MB 수준으로 경량화합니다.
  - 모든 레퍼런스 이미지(`@Image 1`, `@Image 2` 등)와 포스터 썸네일(`thumb.webp`)은 **WebP 포맷 품질 75%(Quality 75)**로 자동 변환하여 **장당 50~150KB 수준으로 극강의 다이어트**를 수행합니다.
  - `archive/data/<ID>_<SLUG>/`에 `meta.json` 생성 및 `archive/data/index.json`에 최신 등록순으로 인덱스를 자동 업데이트합니다.

---

# Part III. AI 생성 엔진별 전용 마스터 헌법 (Engine-Specific Directives)

## 10. Wan 3.0 전용 극실사 튜닝 및 DiT 신경망 제어 헌법 (Wan 3.0 Dedicated Engine Directives)

> **⚠️ WAN 3.0 단독 적용 원칙**: 본 섹션의 5대 수칙은 타 모델(Seedance, Runway, Kling 등)과 절대 혼용하지 않으며, **오직 Wan 3.0 엔진의 DiT(Diffusion Transformer) 아키텍처와 텍스트 인코더, 오디오 생성기 특성에 100% 최적화된 Wan 3.0 전용 마스터 헌법**입니다.

### 10-0. Wan 3.0 기본 사양 및 용량 한도
* **최대 지원 길이**: 최대 30초 단일 롱테이크 지원
* **글자 수 한도**: **19,500자 미만** (안전 권장 19,000자 이내)
* **레퍼런스 태그**: 고유 식별자 이름 직접 사용 (`@image_name`, `@protagonist`, `@runner_face` 등)

### 10-1. Wan 3.0 시각 룩 극실사화 2대 원칙 (Visual Photorealism Look)
* **광학적 불완전성 긍정 주입 (Optical Imperfections vs. Digital Sheen)**:
  - Wan 3.0 비디오가 인위적으로 보이는 원인은 깨끗하고 매끄러운 디지털 CG 질감 때문이다.
  - 프롬프트 `[Style]`에 반드시 실제 아날로그 필름 스톡의 물리적 질감(`16mm Kodak Tri-X silver-halide grain, 35mm Kodak Vision3 500T aesthetic, optical lens softness, soft anamorphic bloom`)을 긍정으로 선언하여, Wan 3.0이 쨍한 디지털 비디오 픽셀 대신 실제 화학 필름 현상 시뮬레이션을 가동하도록 강제한다.
* **생체 미세 텍스처 바인딩 (Anti-Wax & Micro-Texture Rule)**:
  - 인물의 실리콘 마네킹/뷰티 필터 피부를 박멸하기 위해, 인물 등장 시 반드시 **`matte skin micro-texture, visible natural pores, fine vellus hair, realistic subsurface scattering` (무광 미세 모공, 잔솜털, 피부 속 혈색 투과)**을 물리적 팩트로 강제 바인딩한다.
  - Wan 3.0 렌더러가 미세 모공과 솜털을 물리적으로 계산해 그려 넣느라 인공 광택을 칠할 틈을 100% 차단한다.

### 10-2. Wan 3.0 DiT 텍스트 인코더 모션 안정화 헌법 (Motion Stability & Affirmative Syntax)
* **타임라인 본문 내 부정어 100% 영구 금지 (Zero Negatives in Body Rule) 🔴 필수**:
  - `never`, `do not`, `does not`, `no`, `without`, `zero`, `never stop`, `never pause`, `never fall` 같은 **부정어를 Wan 3.0 타임라인 본문에 적는 행위를 100% 영구 금지**한다.
  - Wan 3.0의 텍스트 인코더는 부정어를 인식하지 못하고 그 뒤의 단어(`fall, stop, pause`)에 주의력(Attention)이 쏠려 오히려 인물이 비틀거리거나 모션이 멈칫거리는 치명적 아티팩트를 렌더링한다.
  - 오직 화면에 **보여져야 할 정방향 물리 행동 동사(Affirmative Action Verbs, 예: `sprints forward at sustained full velocity`, `pushes continuously`, `slides smoothly`)**만 쓴다.

### 10-3. Wan 3.0 신경망 주의력(Attention) 관리 & Negative 다이어트 (Negative Token Hygiene)
* **Negative 프롬프트 극강의 다이어트 (Max 8~10 Core Words Rule)**:
  - 수십 개씩 중복 부정어를 도배하는 행위를 100% 금지한다. Wan 3.0은 Negative가 길어질수록 DiT 어텐션 맵이 왜곡되어 화면이 뭉개진다.
  - 본문(긍정 묘사)에서 이미 완벽히 방어하므로, `[Negative]`는 오직 핵심 급소 8~10개 단어로만 압축한다:
  - *표준 권장*: `music, BGM, singing, vignette, film border, digital sheen, waxy skin, static camera, text, watermark.`

### 10-4. Wan 3.0 순수 현장 오디오(Zero-BGM Foley) 엔진 제어 수칙 (Pure Foley Audio Protocol)
* **오디오 엔진 BGM 오염 단어 전면 차단 (Zero Audio Trigger Words Rule)**:
  - Wan 3.0 내장 오디오 엔진에서 배경음악(BGM)을 배제하고 순수 현장 효과음(Foley)만 유지할 때, 음악을 유발하는 트리거 단어(`rhythmic, tempo, beat, hum, drone, resonance, whistle, vocal, beep`)를 본문과 오디오 필드에서 100% 영구 배제한다.
  - 오직 순수 거친 물리 접촉음(`footstep stomp, metal clang, air exhaust, wind rush`)만 기술한다.

### 10-5. Wan 3.0 프롬프트 안전 수정 및 순차 백업 수칙 (Sequential Auto-Backup Rule)
* **수정 시 순차 백업 의무화 및 핀포인트 교체 수칙**:
  - 프롬프트 수정 지시를 받을 때마다 무조건 기존 파일을 **`prompts_wan_backup01.md`, `backup02.md` 순으로 넘버링 복사 백업**을 먼저 생성한 후 수정에 착수한다.
  - 감독님이 지시하신 딱 그 특정 부위만 핀포인트로 수정하며, 지시하지 않은 정상적인 앞뒤 씬의 순서나 연출은 단 1글자도 임의 변경하지 않는다.

---

## 11. Seedance 2.0 & 2.5 전용 마스터 프로덕션 헌법 (Seedance Dedicated Directives)
Seedance 2.0 및 Seedance 2.5 (Artlist AI Toolkit) 모델의 멀티모달 오디오/비주얼 신경망 파서 성능을 극대화하고 텍스트 교차 오염을 방지하기 위한 핵심 규격입니다.

### 11-1. 4대 특수 괄호 파싱 문법 (Technical Parentheses Cues)
* `{}` (중괄호): 성우 나레이션 및 캐릭터 대사 (TTS 스피치 전용 트랙 ➔ 로봇 같은 낱글자 끊어읽기 예방 및 부드러운 발화 보장)
  - *예시*: `Dialogue: {1973년. 대한민국의 뜨거운 철의 역사가 시작되었습니다.}`
* `<>` (꺾쇠): 현장 사운드 효과음 (SFX 및 앰비언스 전용 트랙)
  - *예시*: `Sound: <Deafening blast furnace roar, heavy metal crash impact>`
* `()` (소괄호): 음악 장르, BPM, 오디오 템포 및 마스터링 튜닝 전용
  - *예시*: `Audio: (Epic 120 BPM Taiko Drums, 48kHz 24-bit Studio Quality, +9dB Gain Boost)`
* `[]` (대괄호): Production Brief 파트 식별자, Aspect Ratio 선언 및 타임라인 비트 구분
  - *예시*: `Part-1 [Aspect Ratio: 16:9]`, `[BEAT 1: 00:00 - 00:06]`

### 11-2. 16배수 매크로블록 해상도 락 & 모델 편향 억제 수칙 (Seedance 16-Pixel Macroblock Lock)
* 일반적인 `1080p`는 16으로 나누어떨어지지 않아(1080 / 16 = 67.5) 위아래 8픽셀이 강제 크롭되는 위치 오차가 발생합니다.
* 파트 식별자 최상단에 **16으로 정확히 나누어떨어지는 황금 해상도**를 선언합니다:
  - **가로형 (16:9)**: `Part-N [Aspect Ratio: 16:9, 1920x1088]` (1088 / 16 = 68 딱 떨어짐 ➔ 크롭 0%)
  - **세로형 (9:16)**: `Part-N [Aspect Ratio: 9:16, 1088x1920]` (1088 / 16 = 68 딱 떨어짐 ➔ 크롭 0%)
* **비전투/평화 씬의 모델 편향 다중 억제**: 거대 영물/맹수 캐릭터 등장 시 사냥/공격 본능을 억제하기 위해 "공격하지 마라", "온순하게 부유"를 다중 명시합니다.

### 11-3. 다인원 복제 인간(Cloning) 방지 및 공간 슬롯 락 수칙 (Multi-Character Anti-Cloning)
* **공간적 좌우 좌표 슬롯화 (Spatial Zone Allocation)**:
  - `6 people walk together` 같은 모호한 문장을 절대 금지하고, 화면의 물리적 좌우/전후 슬롯에 인물 태그를 1:1로 정확히 배치합니다.
  ```markdown
  [Spatial Character Slots: Exactly N Unique Individuals]
  - Front Row: @tag1 (left, black robe), @tag2 (right, female swordsman).
  - Rear Row (Left-to-Right): @tag3 (left), @tag4 (center-left), @tag5 (center-right), @tag6 (far-right).
  ```
* **헤드카운트 및 단일 인스턴스 하드 락**: `STRICT HEADCOUNT: Exactly N characters total, each appears strictly ONCE. Strictly single instance of each character.`
* **역할별 비경합 고유 시각 앵커 1:1 결합**: 태그 바로 뒤 괄호 안에 고유 시각적 외형(`black robe`, `white robe`, `fur coat`)을 고정 결합.
* **대사 제외 본문 100% 순수 영문화**: 성우 발화 대사(`{}`)를 제외한 모든 본문/카메라/환경 묘사는 100% 영어로 작성.
* **글로벌 표준 안티클론 네거티브 락**: `more than N people, duplicates, clones, copies, ghosting, twin characters, extra unnamed characters, background doubles` 필수 탑재.

### 11-4. 초고속 0.8~1.5초 템포 격투 액션 & 인체역학 수칙 (Seedance High-Speed Kinetic Combat)
* **0.8~1.5초 마이크로 컷 분할**: `0-1s(Low-angle CU 안면 강타)`, `1-2s(Whip Pan 리포스트)`, `2-4s(Ground Tracking 연타)`, `4-6s(360 Orbit 난투)` 등 극단적 템포 전환.
* **인체역학 락**: `Joint and limb kinematics strictly adhere to realistic human biomechanics` 문구 장착.
* **타격 인과관계 4단계 결합**: `[공격 부위] ➔ [접촉 순간 스파크/에너지 폭발] ➔ [피격자 인체 꺾임 반작용] ➔ [옷 찢어짐/상처 발생]`.
* **상흔 점진 누적**: `Cumulative damage and environmental cracks continuously accumulate without reset`.

### 11-5. Seedance 2.0 × Higgsfield 액션 & 파이트 안무 4대 연출 수칙
* **2초 오프닝 훅**: 파트 첫머리 0~2초에 `Mid-Action Freeze Frame`, `Shockwave from Ground Slam`, `Aggressor Linear Charge` 중 하나 선제 배치.
* **공인 안무 용어 사용**: `rear-hand straight strike with full hip rotation`, `draws a full crescent blade arc`, `blade-to-blade lateral deflection`.
* **카메라 전투 참여**: `Dolly Forward on Attack`, `Reverse Dolly on Advance`, `Snap Zoom on Impact`.
* **4중 환경 물리 반응 레이어**: 옷자락 풍압 찢김, 지면 크레이터 파편 부유, 렌즈 충돌 광학을 SFX와 바인딩.

### 11-6. Seedance 2.5 극실사 맨몸 격투 & 학원 드라마 액션 수칙
* **초인적 이펙트 배제 & 신체 역학 기반**: `Fast, physical, believable action. No superpowers, no magic, no CGI glowing effects. Leverage, momentum redirection, and realistic joint kinematics.`
* **5단계 심리/감정 아크 연기**: `공포(Fear) ➔ 혼란(Confusion) ➔ 본능 각성(Instinct) ➔ 냉정한 집중(Concentration) ➔ 자신의 힘에 대한 불신/충격(Disbelief)`.
* **목격자 시점 핸드헬드 폰카 결함 룩**: `Handheld smartphone/operator footage, imperfect framing, focus hunting, natural motion blur. Feels like a real witness recording an incident.`
* **배경 사물 물리 충돌 & 파편화**: 한국 체육관/교실 기물(배드민턴 카트 전도, 셔틀콕 비산, 매트 벽 충돌)과 상호작용.
* **노-뮤직 현장 생음 폴리 100% 락**: BGM 완전 배제, 신발 바닥 마찰음, 거친 호흡, 옷깃 스치는 소리로만 구성.

### 11-7. Seedance 상업 숏드라마 고속 양산 4대 프로덕션 수칙 (Commercial Shortdrama Production Protocol)
연속 상업용 숏드라마를 재생성(Re-roll) 없이 공장처럼 고속 양산하기 위한 Seedance 전용 핵심 엔지니어링 규칙입니다.
* **1. 재질별 하이라이트 상대 비율 수치화 (Material Highlight Multipliers)**:
  - 광영 설계 블록에서 수치 고정: `장도 금속 ×1.5, 피부 ×0.5, 천 ×0.3` (`长刀金属高光×1.5、皮肤高光×0.5、布料高光×0.3`). 피부를 누르고 금속만 튀게 하여 일관성 유지.
* **2. 더빙 지시의 상수(Constant) / 변수(Variable) 분리 체계**:
  - `【더빙 지시: 캐릭터[@태그] | 음색 & 기본 성격 (상수) | 상태 & 어조 (변수) : "대사"】`
  - 전 에피소드에서 성우 음색/캐릭터성은 고정하고 컷별 감정 연기만 자유롭게 스위칭.
* **3. 특정 단어 시점 기반 동작/표정 액션 싱크 (Word-by-Word Action Sync)**:
  - 단순 초단위 지시 대신 대사의 특정 단어 발화 시점과 표정/동작을 1:1 결합 (`“괴상한”이라 말할 때 웃음주름 전개, “그 신발”이라 말할 때 손가락이 신발로 낙하`).
* **4. 앞뒤 에피소드 양방향 인계 헤더/푸터 (Bi-directional Clip Handoff)**:
  - 시작부(0~2초)는 이전 컷의 마지막 동작을 이어받고, 종료부는 다음 씬 첫 대사와 고정 포즈를 텍스트로 박제하여 무검수 자동 컷 연결 완성.

---

## 12. MiniMax H3 (Hailuo 3.0) 전용 마스터 헌법 (MiniMax H3 Dedicated Directives)
MiniMax H3 모델의 2K 24FPS 15초 연출, 3D 타이포 가독성, 네이티브 오디오 패스(Audio Pass) 성능을 극대화하기 위한 전용 고급 수칙입니다.

* **무컷 원테이크 심리스 카메라이동 (Strict One-Take Seamless Trajectory)**:
  - 15초 연속 렌더링 장점을 활용해 중간 컷 없이 단 하나의 무빙으로 완주 (`Strict one-take shot. No cuts. No teleportation. No hidden transitions.`).
* **동적 수채화 리본 인터랙션 (Interactive Living Medium Physics)**:
  - 수채화 물감이 단순 배경이 아닌 살아있는 매체로 동작하며 의상에 자연스럽게 흡수되도록 지시.
* **공간 3D 입체 건축 타이포그래피 (Spatial 3D Architecture Words)**:
  - 2D 자막/텍스트 오버레이를 100% 금지하고, 텍스트가 공간 속 입체 질감을 갖도록 지정 (`Physical depth, wet watercolor reflections, shadows, occlusion`).
* **네이티브 오디오 비트-공간 물리학 동기화 (Audio Pass & Visual Physics Mapping)**:
  - Kick(카메라 이동 및 접힘), Wooden Snare(종이 구조 트랜스폼), Sub-bass(공간 스케일 확장) 1:1 바인딩.
* **4단계 서사 완급조절 리듬 (4-Phase Narrative Rhythm)**:
  - `0–4s`: 절제된 정적과 여백 ➔ `4–8s`: 수채화/종이 구조 밀도 증가 ➔ `8–12s`: 드롭 순간 유체 연속 무빙 ➔ `12–15s`: 패션 포스터 구도 전환.
* **초간결 현상 나열식 기법 (Ultra-Short Phenomenon-Based Prompting)**:
  - 빠른 실험 시 `[Audio1] + [Image1]` 지정 후 5~7줄 불렛포인트로만 직관적 작성.
* **내추럴 일상 다큐 & 한국어 구어체 대사 발화 수칙 (Native Spoken Dialogue & Dappled Light)**:
  - 큰따옴표로 한국어 구어체 직접 지정 (`peeks one eye open at camera saying "여기 진짜 시원하다"`).
  - 나뭇잎 사이 투과광, 2000년대 초기 DV 캠코더 드레이프, 무-삼각대 미세 흔들림, 환경음(노 뮤직) 조합으로 극실사 다큐 구현.

---

# Part IV. 장르 & 연출 스타일 특화 스킬 라우팅 (Genre & Directing Skills)

> **💡 모듈화 원칙**: 특정 장르/도메인의 세부 프롬프트 연출 공식은 전역 헌법 파일에 중복 기재하지 않고, 전용 스킬북으로 분리 관리합니다. 해당 장르 작업 시 아래 스킬 파일을 참조하여 프롬프트를 작성합니다.

* **🎬 거장 영화감독 시네마틱 연출 & 블로킹**:
  - 서브텍스트 물리화, 85mm 얼굴 익스트림 클로즈업, 동기화된 카메라 문법, 소품 단독 인서트, 대사 후 2초의 침묵
  - 👉 [`.agents/skills/cinematic-film-directing/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/cinematic-film-directing/SKILL.md) 참조
* **📱 숏폼 크리에이터 OS & 바이럴 훅 (Adrian Per Style)**:
  - 7단계 시네마틱 결정 스택, 6비트 숏폼 감정 엔진, 동작 매치 이음새 컷, 사운드 압력 아크(`Riser ➔ Climax ➔ Silence`), 9:16 세로 3단 깊이감
  - 👉 [`.agents/skills/adrian-per-directing/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/adrian-per-directing/SKILL.md) 참조
* **⚔️ AAA급 게임 시네마틱 & 대형 액션 블록버스터**:
  - ZeroBlood 무혈 탄화 5단계 안전 체인, 50/30/20 무기 물리 FX, 1초 3동작 제한 및 5단계 관성 발력, 3단계 충격 프레임, 0.1초 시야 사각 트릭
  - 👉 [`.agents/skills/05-fight-scenes/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/05-fight-scenes/SKILL.md) 참조
* **📹 극실사 일상물, 폰카 & 2000년대 캠코더 결함 미학**:
  - Old iPhone 1x 저화질 폰카 8대 수칙, MiniDV 구형 캠코더 AF 헤맴/오버슈트 지연 보정, 중국 숏드라마 팩토리 양산 룰
  - 👉 [`.agents/skills/AI-video-prompt/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/AI-video-prompt/SKILL.md) 참조
* **👗 패션 룩북 & 시니어 여성 패션 쇼츠 커머스**:
  - 60~75세 시니어 패션 쇼츠, 단일 공간 원테이크 짐벌 무빙, 화이트 스튜디오 컷 금지, 상품 카테고리별 맞춤 샷
  - 👉 [`.agents/skills/13-fashion-lookbook/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/13-fashion-lookbook/SKILL.md) 참조
* **🥩 하이엔드 식음료(F&B) 시네마틱 & 의미론적 환각 방어**:
  - 고기/바비큐 그릴 씨즐, 3대 환각(화로/꽃잎/로켓) 배제, 시그니처 메뉴 매크로 바인딩, 멀티클립 비디오 연속성
  - 👉 [`.agents/skills/14-food-beverage/SKILL.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/skills/14-food-beverage/SKILL.md) 참조
* **🗺️ 전체 15대 도메인 및 24개 스킬 종합 색인**:
  - 👉 [`.agents/SKILL_MAP.md`](file:///Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools/.agents/SKILL_MAP.md) 참조

