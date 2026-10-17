---
name: hongkong-cinema-prompting
description: 80~90년대 쇼브라더스(Shaw Brothers) 무협 영화 및 초기 홍콩 느와르 드라마 감성의 아날로그 필름 질감, 세트장 조명, 테크니컬러 색수차를 재현하기 위한 AI 비디오 프롬프트 스타일 가이드입니다.
version: 1.0.0
author: Antigravity
license: MIT
metadata:
  hermes:
    tags: [hongkong-cinema, shaw-brothers, wuxia-style, retro-tv, analog-film, veo, runway, kling]
---

# 홍콩 영화 스타일 비디오 프롬프트 가이드 (Hong Kong Cinema Prompting Guide)

본 가이드는 AI 비디오 생성 모델(Runway, Kling, Veo 등)에서 80~90년대 쇼브라더스 무협 영화 및 홍콩 TVB 드라마 특유의 복고풍 아날로그 질감과 연출을 재현하기 위한 프롬프트 스타일 및 핵심 속성 프리셋을 제공합니다.

---

## 1. 핵심 비주얼 스타일 프리셋 (Core Style Specs)

비디오 프롬프트의 `[Visual Vibe]` 및 `[Camera & Lens Style]` 문단에 아래 영문 프리셋들을 그대로 복사하여 삽입하면, 모델이 레트로 홍콩 영화 질감을 정확하게 재현합니다.

### 🎨 색감 및 조명 (Color & Lighting)
* `80s-90s Shaw Brothers movie style` (80~90년대 쇼브라더스 영화 스타일)
* `early Hong Kong wuxia drama aesthetics` (초기 홍콩 무협 드라마 미학)
* `warm and high-saturation color palette` (따뜻하고 채도 높은 테크니컬러 색감)
* `classic studio backdrop feel` (인위적인 옛날 스튜디오 세트장 배경 느낌)
* `soft stage lighting` (부드러운 스튜디오 무대 조명 효과)
* `strong bloom on highlight surfaces` (광원이 번지는 강한 하이라이트 블룸 현상)

### 📹 필름 및 화질 결함 (Film & Lens Artifacts)
* `vintage TV quality` (80-90년대 브라운관 TV 화질 질감)
* `35mm film photography` (35mm 필름 촬영 느낌)
* `retro film grain texture` (거친 레트로 필름 입자 노이즈)
* `physical film defects` (아날로그 필름 스크래치, 먼지, 잡티)
* `slight Technicolor chromatic aberration` (테크니컬러 특유의 미세한 색수차)
* `slight light flickering` (아날로그 영사기 특유의 미세한 광량 깜빡임)
* `soft focus effect` (인물 주변이 뿌옇게 번지는 소프트 포커스 효과)

---

## 2. 7단식 템플릿 결합 가이드

홍콩 영화 스타일을 극대화하기 위해, 프롬프트 작성 시 아래 포맷을 권장합니다.

```text
[Main Character] -> 80s period drama makeup, traditional Hanfu/wuxia costume, classic sideburns.
[Location] -> Classic studio backdrop wuxia set, warm and high-saturation color palette.
[Visual Vibe] -> 80s-90s Shaw Brothers movie style, nostalgic Chinese wuxia film.
[Camera & Lens Style] -> 35mm film photography, vintage film texture, slight Technicolor chromatic aberration.
[Timeline] -> Sitcom editing logic or dynamic wuxia action sequences, physical white smoke effects.
[Audio] -> TVB dubbing style accent, retro martial arts sounds, nostalgic background music.
[Target Goal] -> Capturing vintage wuxia scene mimicking a raw 80s film, soft bloom, authentic retro feel.
```

---

## 3. 연출 팁 및 모범 사례 (Best Practices)

1. **인공 연기 효과 (Physical Smoke)**:
   * 순간적인 캐릭터 변신이나 등장 시 CG 효과 대신 수작업 백색 스모그 느낌을 유도하기 위해 `retro white physical smoke effects`를 타임라인에 명시합니다.
2. **배경의 인위성 강조 (Studio Backdrop)**:
   * 지나치게 실사적이고 깔끔한 현대식 배경을 억제하고, 무대 세트장 질감을 강조하기 위해 `classic studio backdrop feel`과 `No clean modern CGI background` 부정어구를 함께 사용합니다.
3. **오디오 및 더빙 가이드**:
   * 나레이션 및 보이스오버 렌더링 시 아날로그 라디오 필터와 더빙 성우 톤을 명시하여 아날로그 비디오 감성을 오디오 지문에 바인딩합니다.
