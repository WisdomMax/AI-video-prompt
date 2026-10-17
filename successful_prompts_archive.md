# DNA Motors Lumi 125cc — Victory Master Prompt & Success Blueprint

---

## 🏆 성공 요인 분석 및 튜닝 블루프린트 (Why This Prompt Succeeded)

이 프롬프트가 기존의 시행착오(인물 겉돎, 얌전히 앉아있기, 촌스러운 자막, 배경 텔레포트)를 극복하고 **공모전 대상급(500만 원) 비주얼 완성도**를 낸 5대 핵심 성공 요인 분석입니다.

---

### 1. 물리 동작의 3단계 샷 칼분리 (Physical Action Decoupling)
* **문제점**: AI 비디오 모델(Seedance 2.5)은 한 컷 안에 `도망치기` + `스쿠터 달리기` + `뛰어타기`를 다 묶으면 복잡한 다관절 연산을 무시하고 **"처음부터 오토바이에 여유롭게 착석해 있는 병맛 정적 프레임"**을 생성함.
* **성공 해결책**: 
  - `Shot 1`: 오토바이를 아예 치우고 **오직 두 발로만 전속력 도망치는 풋 스프린트 단독 샷**.
  - `Shot 2`: 주차된 Lumi에 다급하게 몸을 던져 뛰어타는 하드 컷 단독 샷.
  - `Shot 3`: `@img3` 7번 카울 다이얼을 돌려 파란 LED를 켜는 시동 클로즈업 샷.
  - **결과**: 인물이 오토바이에 얌전히 앉아있는 에러를 100% 차단하고 긴박한 액션 훅 완성.

---

### 2. 공간 텔레포트 없는 '50% 궤적 환경 시프트' (Environmental Wave Shifting)
* **문제점**: `European boulevard`, `Paris` 같은 고유 장소 명사를 프롬프트에 기재하면, AI가 화면 전체를 통째로 바꾸는 **3D 공간 순간이동(Teleportation Error)**을 일으킴.
* **성공 해결책**: 
  - 장소 이동을 명시하는 대신 `50 percent of the frame behind her rear wheel transforms into a sunlit romantic Italian cobble boulevard` 구문 채택.
  - 오토바이 전방은 어두운 디스토피아를 유지하되, **뒷바퀴 궤적 뒤쪽 50% 레이어만 이탈리아 돌길로 변신**하도록 유도.
* **결과**: 배경 붕괴 없이 잿빛 도시에서 이탈리아 낭만 거리로 이어지는 극적인 분위기 반전 성공.

---

### 3. 멀티라인 우측 배치 & 순백색 무테두리 타이포그래피 (Stacked Solid White Typography)
* **문제점**: 3D 골드 폰트나 외곽선(Stroke)이 들어간 글자, 화면 중앙/바닥 인쇄 지시는 촌스럽고 가독성을 심각하게 해침.
* **성공 해결책**:
  - `Pure solid flat white 2D graphic text overlays WITHOUT any outline border, stroke, drop shadow`.
  - 가로 1줄 길게 뻗는 폰트를 지우고 `Stacked in 2 thick lines on the right side`로 오토바이 우측에 두껍고 단단하게 2줄 배치.
* **결과**: PPT 기본 자막 느낌을 지우고 명품 자동차 TVC 느낌의 웅장한 3D/2D 자막 아트 완성.

---

### 4. BGM 강제 사살 & 현장 폴리 오디오 패스 (Foley Audio & BGM Prohibition)
* **문제점**: AI 비디오 모델이 임의로 촌스러운 템플릿 배경음악(BGM)을 섞어 오디오 퀄리티를 저하시킴.
* **성공 해결책**:
  - `STRICTLY NO BGM. NO MUSIC. Background music is strictly BANNED`.
  - 오직 현장 Foley 오디오(`tense sirens, zombie growls, heavy running footsteps, 125cc engine ignition roar, tire screeching brake friction, spoken dialogue`)만 바인딩.
* **결과**: 지저분한 음악이 제거되고 엔진음, 브레이크 마찰음, 한국어 대사(`루미`)가 명확히 들리는 생생한 현장감 확보.

---

### 5. 실사 한국인 배우 캐릭터 락 (`@img5` Character Consistency)
* **문제점**: 3D/CG 캐릭터 시트는 미끈거리는 AI 텍스처(CGI Slop)를 유발하여 광고 실사감을 망침.
* **성공 해결책**: 35mm 카메라 톤의 실사 한국인 배우 레퍼런스 시트(`@img5`)를 독립 슬롯에 배치하고 프롬프트 전반에 `@img5` 바인딩.
* **결과**: 10개 샷 전반에서 여주인공의 얼굴, 이목구비, 포니테일, 전사 복장의 일치성(Consistency) 100% 유지.

---

## 🎬 [Master Prompt Code Block] — 30s Final Verified Version

```markdown
Part-1
Strict 16:9 widescreen aspect ratio, 30s cinematic duration, 4K 24fps resolution.

[Image References] @img1, @img2, @img3, @img4, @img5

[Main Character & Vehicle]
@img1 represents the DNA Motors Lumi 125cc urban scooter featuring a glossy pearl white body, a luxurious burgundy leather seat, classic round LED headlamp, matte brown side accents, and black wheels. The exact design, proportions, color scheme, metallic finish, curves, headlamp shape, and wheel dimensions of @img1 must be strictly maintained without any distortion, alteration, or morphing.
@img2 represents the official metallic chrome cursive script 'Lumi' logo emblem.
@img3 represents the 9-panel detail reference sheet showing the exact Lumi handlebar housing, color LCD digital speedometer dashboard, silver right-side hazard and ignition switch assembly, left-side headlight switch, and blue LED ring smartkey rotary knob. Panel 7 of @img3 shows the white front inner cowl housing with the smartkey dial assembly on the right.
@img4 represents the final signature ending frame featuring a dark studio background, sleek rim lighting on the Lumi scooter silhouette on the right, clean typography '도시 속 나의 오브제', and the metallic chrome cursive @img2 logo in the center.
@img5 represents the exact real-world Korean heroine character reference photo showing her face, natural skin texture, hairstyle, sand-beige utility cargo pants, tan leather harness, brown combat boots, dark olive leather jacket, and forehead riding goggles. The driver's face, body features, facial structure, skin tone, hairstyle, and costume in all shots MUST strictly match @img5 with 100 percent character consistency.

[Location & Visual Vibe]
Starts in a dark ruined post-apocalyptic city with ash, smoke, and wet dark asphalt. As @img1 accelerates smoothly, 50 percent of the frame behind her rear wheel transforms into a sunlit romantic Italian cobble boulevard with classical Italian architecture, warm golden sunlight, and blooming flower balconies, while the front remains dark. Ends in an ultra-dynamic dark luxury studio showcase matching @img4 with active movement. Cinematic 4K quality, 16:9 widescreen, 30s duration, 24fps, high contrast.

[Typography Specifications]
Pure solid flat white 2D graphic text overlays MUST be designed WITHOUT any outline border, stroke, drop shadow, or double edge lines. Clean solid white fill, neatly stacked in 2 lines on the right side beside the vehicle frame:
1. 'SMART KEY SYSTEM': Pure solid flat white tech typography art stacked in 2 lines near inner cowl as smartkey dial turns.
2. 'ABS & TCS / DUAL SAFETY': Pure solid flat white 2D kinetic typography art stacked in 2 thick lines ('ABS & TCS' on top line, 'DUAL SAFETY' on bottom line) with NO text outline, floating large on the right side beside the leaning front wheel.
3. 'LIGHT 115kg / ECO 45km/L': Pure solid flat white 2D kinetic spec typography art stacked in 2 thick lines ('LIGHT 115kg' on top line, 'ECO 45km/L' on bottom line) with NO outline border or double stroke line, floating cleanly on the right side beside the scooter body.
4. Living Dynamic Signature Ending Motion (@img4): Final Shot 10 features full active motion matching @img4. The white @img1 scooter physically rolls and glides into frame from the far right side to the center right position with wheels spinning and gleaming edge rim lighting. Simultaneously, Korean typography "도시 속 나의 오브제" animates dynamically scaling down from large 2D spatial scale to center position, while the 3D metallic chrome cursive @img2 logo ignites with a brilliant sparkling light flare as the ultimate living brand sign-off.

[Camera & Lens Style]
Dynamic multi-angle camera language. High-angle sky dive tracking, cornering lean tracking shots, fast proximity diving tracking, ground-skimming low angles, whip pans, and 360-degree rotational orbit. Anamorphic 35mm lens, dramatic depth of field, optical lens flare, high-speed motion blur, photorealistic lighting. Abrupt jump cuts between camera angles without morphing transitions.

[Timeline]
00:00–00:02 [Shot 1: High-Speed Foot Sprint Pursuit Hook]: Abrupt jump cut. High-speed camera plunges rapidly from a bird's-eye view looking straight down. On the dark wet asphalt road below, the heroine matching @img5 is running frantically on foot with absolutely NO vehicle, fleeing for her life in intense sprint as terrifying zombies chase right behind her in the same frame.

00:02–00:04 [Shot 2: Desperate Mounting Action]: Abrupt jump cut to a medium tracking shot. The fleeing heroine matching @img5 hurriedly reaches parked @img1 on the street and frantically leaps onto the burgundy leather seat of @img1 to escape the approaching zombies.

00:04–00:06 [Shot 3: Inner Cowl Smartkey Dial Ignition]: Abrupt jump cut to a medium close-up matching panel 7 of @img3 showing the white front inner cowl. In urgent panic, her hand grips and turns the black circular smartkey dial knob clockwise on the right side of the inner cowl, instantly illuminating the vibrant blue LED ring surrounding the dial knob as the 125cc engine roars to life. Pure solid flat white typography stacked in 2 lines "SMART KEY / SYSTEM" floats near the dial.

00:06–00:09 [Shot 4: High-Speed Hard Braking Cornering Lean & ABS Action]: Abrupt jump cut to an ultra-dynamic aggressive action tracking shot. To escape pursuing zombies, @img5 pulls the brake levers hard while leaning @img1 sharply into a tight corner at high speed, creating tire friction smoke and a powerful stable deceleration controlled by ABS. Pure solid flat white 2D kinetic typography stacked in 2 thick lines ("ABS & TCS" on top line, "DUAL SAFETY" on bottom line) with NO outline border floats dynamically on the right side beside the leaning front wheel.

00:09–00:13 [Shot 5: Straight Acceleration & Right-Side Solid White ECO Spec]: Low-angle tracking shot behind @img1 as @img5 rides straight at high speed. Behind @img1's rear wheel, 50 percent of the frame continuously transforms into a bright sunlit Italian cobble boulevard under golden sunlight, while pure solid flat white 2D kinetic typography stacked in 2 thick lines ("LIGHT 115kg" on top line, "ECO 45km/L" on bottom line) with NO outline border floats on the right side beside the scooter body.

00:13–00:16 [Shot 6: Zombie Human Transformation & Italian Reaction]: Dynamic side tracking cut in the same frame. As the golden light wave catches up to the pursuing zombies directly behind her, they stop chasing, smile warmly, and transform into innocent smiling Italian citizens and happy children waving joyfully at @img5.

00:16–00:19 [Shot 7: 360-Degree Rotational Orbit Sweep]: 360-degree rotational orbit shot around @img1 ridden by @img5 (pearl white body with burgundy leather seat) cruising through the sunlit Italian boulevard under a golden sky.

00:19–00:24 [Shot 8: Italian Cafe Halt & Goggles Lift]: Crash zoom in as @img1 halts smoothly in front of a sunlit Italian gallery cafe. The heroine gracefully lifts her riding goggles onto her forehead as smiling Italian citizens gather around, admiring the white Lumi scooter as an urban objet.

00:24–00:28 [Shot 9: Hero Dialogue Focus]: Close-up in front of the Italian cafe matching facial features of @img5. With goggles on her forehead, the heroine looks straight into the camera lens with a confident, charismatic smile and says with mouth wide open: "어때? 이 삭막한 세상도, 루미 위에선 낭만이잖아."

00:28–00:30 [Shot 10: Living Dynamic Signature Ending Motion]: Abrupt jump cut to a dark luxury studio showcase matching @img4. In full active motion, the white @img1 scooter physically rolls and glides into the frame from the far right side with spinning wheels and gleaming rim lighting. In the center, crisp white Korean typography "도시 속 나의 오브제" dynamically scales down from large spatial scale to center, while the 3D metallic chrome cursive @img2 logo ignites with a brilliant sparkling light flare reflection as the living sign-off.

[Audio]
STRICTLY NO BGM. NO MUSIC. Background music is strictly BANNED. Only photorealistic Foley audio pass: tense sirens, zombie growls, heavy running footsteps, 125cc engine ignition roar, tire screeching brake friction, ambient crowd laughter, spoken dialogue, and engine rev sound.

[Negative Constraints]
watermark, low quality, distortion, morphing vehicle shape, alteration of @img1 proportions, alteration of @img5 facial structure, ugly text distortion, erratic camera motion, all-black clothing, static frozen image, pushing a button, traditional metal key, text printed on asphalt, text on road, zombies melting, separate character cuts, detached subjects, already seated on scooter, sitting on vehicle at start, riding at start, weird neon pastel colors, pink neon lights, static ending frame, frozen picture ending, small thin subtitles, tiny text font, single horizontal line text, text stroke, text outline, double edge line text, text border, text shadow, text centered above head, BGM, background music, musical score, background track, melody, song, instrumental music, soundtrack.
```
