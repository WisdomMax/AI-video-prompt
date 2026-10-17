---
name: micro-cinematic-prompting
description: Seedance 2.0/2.5, Kling, Wan, Runway 등에서 복잡한 타임라인 없이 단 1개 문단(100단어/600자)으로 형태 붕괴 0%의 극실사 3초 훅(Hook), 살아있는 시네마틱 포스터(Living Portrait), 패션/MV 씬을 뽑아내는 초간결 숏 프롬프트 전문 가이드입니다.
version: 1.0.0
author: Antigravity
license: MIT
metadata:
  tags: [micro-prompting, short-prompt, seedance-2.0, living-portrait, vertical-9-16, hero-shot, fashion-mv, hook-video]
---

# ⚡ 시네마틱 숏 프롬프트 가이드 (Micro-Cinematic Prompting Guide)

본 가이드는 AI 비디오 모델(Seedance 2.0/2.5, Wan, Kling 등)에서 복잡한 초단위 롱 타임라인을 배제하고, **단 1개 문단(5단 모듈러 뼈대, 100단어 내외)**만으로 인스타그램 릴스·틱톡·유튜브 숏츠용 **초고화질 3초 훅(Hook) 및 살아있는 시네마틱 스틸(Living Portrait)**을 완성하는 공식 스킬북입니다.

---

## 🎯 1. 숏 프롬프트의 3대 핵심 원리 (The 3 Golden Rules)

1. **사건(복잡한 연속 동작)을 버리고 "단일 물리 상태(Single State)"에 집중**:
   - 다관절 격투, 달리기, 춤동작을 묘사하면 형태가 뭉개집니다.
   - 오직 **"바람에 날리는 머리칼(`hair moving in the wind`)"**, **"들여다보는 손끝 소품(`examining a glowing device`)"**, **"정적인 댄스 멈춤 자세(`synchronized dance poses`)"** 1개만 지시합니다.
2. **얼굴 붕괴 방지용 불변 표정 앵커**:
   - 웃거나 오열하는 표정은 안면 왜곡을 유발합니다.
   - 무조건 **`intense focused expression` / `tense focused expression` / `powerful confident expression`**을 사용하여 눈동자와 미간 근육을 단단히 고정합니다.
3. **영화 카메라 렌즈 스펙(35mm / 85mm f/1.8)의 강제 주입**:
   - 모델에게 "싸구려 비디오가 아닌 헐리우드 극장판 스틸컷"임을 선언하여 아웃포커싱(심도)과 질감을 극대화합니다.

---

## 📐 2. 5단 모듈러 조립 템플릿 (The 5-Block Modular Template)

아래 5개 블록을 순서대로 연결하여 단 하나의 단락으로 작성합니다.

```text
[Block 1: 오프닝 장르 앵커]
Ultra-realistic cinematic [scene / fashion performance scene] of [피사체 정의],

[Block 2: 복장 & 헤어/소품]
wearing [구체적인 의상 및 액세서리], [헝클어지거나 바람에 흩날리는 헤어 디테일],

[Block 3: 단일 마이크로 액션 (소품/정적 포즈)]
[standing confidently in the center / carefully examining a glowing device / striking a synchronized pose],

[Block 4: 배경 & 조명 & 표정]
[배경 공간 묘사], [dramatic warm sunlight / dramatic night setting with bright backlighting], subtle [atmospheric haze / motion blur], [intense focused / powerful confident] expression,

[Block 5: 카메라 광학 불변 블록 (복붙 전용)]
photorealistic skin and fabric details, shallow depth of field, cinematic lighting, high contrast, 8K, HDR, [35mm lens / 85mm lens, f/1.8], professional film still, vertical [9:16] composition.
```

---

## 렌즈 스위칭 공식:
- **전신 + 주변 배경 공간과의 조화**: `35mm lens`
- **인물 모공/눈빛 집중 및 배경 극단 아웃포커싱**: `85mm lens, f/1.8`

---

## 👥 3. 다인원(Group) / 댄스 MV 씬 특수 수칙 (Center Lock Rule)

여러 명이 등장하는 패션/뮤직비디오 씬은 AI가 얼굴을 서로 섞어버리는 치명적 오류가 발생합니다. 이를 통제하기 위해 다음 수칙을 강제합니다:

1. **센터 1인 명도 대비 락 (Brightness Contrast)**:
   - 주인공은 **화이트 톤(예: white strapless corset top)**으로 중심에 세우고,
   - 주변 댄서/엑스트라는 **블랙 가죽(black leather outfits)**으로 통일하여 시선과 연산력을 센터에 집중시킵니다.
2. **주변 인물 동작 동기화 박제**:
   - 주변 댄서들은 개별 동작을 주지 말고 **`synchronized dance poses`** 단어 하나로 고정하여 배경 장치화합니다.
3. **강력한 자동차 헤드라이트 역광 (Headlight Rim-Lighting)**:
   - `dramatic night setting with cars and bright headlights behind them, warm backlighting`을 주어 인물들의 실루엣을 칼같이 분리합니다.
