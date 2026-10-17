#!/usr/bin/env python3
import subprocess
import json

prompt_text = """Part-1 [Aspect Ratio: 16:9]

[Tags]
@Image 1
@Image 2

[Roles]
@Image 1: Exactly as in reference photo.
@Image 2: Exactly as in reference photo.

[Style]
Apple keynote meets BBC science documentary aesthetic, 35mm anamorphic film texture, high-key clean white studio, ultra-crisp 4K resolution, soft volumetric white ambient lighting, razor-sharp optical focus, smooth cinematic camera tracking.

[Start State]
00:00 Eye-level wide shot anchored directly on the initial frame of @Image 1 inside the pristine white minimalist physics laboratory. The steel rail track runs horizontally across the polished epoxy floor.

[Timeline]
00-08s [Shot 1: Dynamic medium push-in on science host]:
@Image 2 strides smoothly forward into frame toward the camera at eye level, smiling with sharp intellectual enthusiasm, gesturing expressively with his right hand toward the rail track. In the soft-focus background, lab technicians in coats monitor digital screens.
Dialogue: {시속 60km로 달리는 물체가 갑자기 멈추면 어떤 일이 벌어질까요? 오늘, 가속도의 힘을 눈앞에서 증명해 드립니다!}
<Upbeat modern scientific synth pulse, subtle pneumatic servo hums>

08-16s [Shot 2: Low-angle tracking pan across test apparatus]:
Camera tracks low along the gleaming steel rail toward @Image 1. The matte-black platform cart carrying the dense 70kg block is illuminated by vibrant green laser calibration grid lines. A countdown chime sounds as pneumatic valves hiss.
Dialogue: {레일 위에 얹힌 물체의 무게는 70kg. 인간의 평균 체중입니다. 발사 카운트다운 들어갑니다!}
<Pneumatic air release hiss, mechanical countdown beep: Three, Two, One>

16-24s [Shot 3: High-speed linear tracking chase]:
The black platform cart of @Image 1 accelerates violently down the track with linear electromagnetic propulsion, reaching 60 km/h in an instant. Floor-mounted sensor lights blur into glowing streaks as wind whips through the room.
Dialogue: {가속도와 관성의 법칙. 속도가 붙기 시작합니다!}
<Magnetic catapult blast, whistling high-velocity wind rush>

24-30s [Shot 4: Close side-profile tracking into seamless dissolve]:
Smooth side-profile tracking shot following parallel with the rapidly moving black cart of @Image 1 at eye level. As speed peaks, a seamless cinematic dissolve gradually transforms the moving black metal edges into the sleek metallic side profile of a black premium sedan cruising at 60 km/h along an open highway under natural daylight.
<Whistling wind rush seamlessly dissolves into the low rumbling hum of vehicle tires on asphalt>

[End State]
00:30 Clean, steady side-profile shot of the black sedan traveling at 60 km/h on an open scenic highway under daylight.

[Audio]
Upbeat modern electronic scientific synth intro, robotic countdown beeps, magnetic propulsion whoosh, cross-fading into highway tire rumble. Strictly physical SFX and ambient only.

[Negative]
gore, blood, plastic skin, distorted faces, 3D cartoon, dark grimy lighting, jittery frames, BGM, music, soundtrack, melody, instruments, singing, blurry, watermark, subtitles."""

js_code = f"""
await attachActiveBrowserTab();
let s = await snapshot(page, {{ interactive: true }});

// 1. Check & change Aspect ratio
const aspectMatch = s.tree.match(/button \\"Aspect ratio\\" \\[ref=(e\\d+)\\]: \\"([^\\"]+)\\"/);
if (aspectMatch && aspectMatch[2] !== '16:9') {{
  console.log('Current aspect ratio:', aspectMatch[2], '-> Changing to 16:9...');
  await page.locator(aspectMatch[1]).click();
  s = await snapshot(page, {{ interactive: true }});
  const opt16_9 = s.tree.match(/option \\"16:9\\" \\[ref=(e\\d+)\\]/);
  if (opt16_9) {{
    await page.locator(opt16_9[1]).click();
    console.log('Aspect ratio 16:9 selected!');
  }}
}} else {{
  console.log('Aspect ratio already 16:9');
}}

// 2. Fill prompt
s = await snapshot(page, {{ interactive: true }});
const pMatch = s.tree.match(/textbox \\"Prompt\\" \\[ref=(e\\d+)\\]/);
if (pMatch) {{
  await page.locator(pMatch[1]).fill({json.dumps(prompt_text)});
  console.log('Prompt successfully filled!');
}}

await sleep(1500);

// 3. Click Generate
s = await snapshot(page, {{ interactive: true }});
const genMatch = s.tree.match(/button \\"Generate\\" \\[ref=(e\\d+)\\]/);
if (genMatch) {{
  console.log('Clicking Generate button:', genMatch[1]);
  await page.locator(genMatch[1]).click();
  console.log('GENERATE_TRIGGERED_SUCCESSFULLY');
}} else {{
  console.log('Error: Generate button not found');
}}
"""

p = subprocess.Popen(['/Users/wisdom/.local/bin/aside', 'repl'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = p.communicate(input=js_code)
print(stdout)
if stderr:
    print('ERR:', stderr)
