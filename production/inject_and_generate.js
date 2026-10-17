const promptText = `Part-1 [Aspect Ratio: 16:9]

[Tags]
@Image 1
@Image 2
@Image 3

[Roles]
@Image 1: Exactly as in reference photo.
@Image 2: Exactly as in reference photo.
@Image 3: Exactly as in reference photo.

[Style]
Apple keynote meets BBC science documentary aesthetic, 35mm anamorphic film texture, high-key clean white studio, ultra-crisp 4K resolution, soft volumetric white ambient lighting, razor-sharp optical focus, smooth cinematic camera tracking.

[Start State]
00:00 Eye-level wide shot anchored directly on the initial frame of @Image 1 inside the pristine white minimalist physics laboratory. The steel rail track runs horizontally from left to right across the polished epoxy floor.

[Timeline]
00-08s [Shot 1: Dynamic medium push-in on veteran science host]:
@Image 2 strides smoothly forward into frame toward the camera at eye level, smiling with sharp intellectual enthusiasm and grave scientific curiosity, gesturing expressively with his laser pointer toward the rail track. In the soft-focus background, lab technicians in coats monitor digital screens.
Dialogue: {시속 60km로 달리는 물체가 벽에 부딪히면 어떤 충격이 발생할까요? 오늘, 가속도와 관성의 물리 법칙을 눈앞에서 증명해 드립니다!}
<Upbeat modern scientific synth pulse, subtle pneumatic servo hums>

08-16s [Shot 2: Low-angle tracking pan across test apparatus]:
Camera tracks low along the gleaming steel rail toward @Image 1. The matte-black platform cart carrying the dense 100kg titanium-steel block is illuminated by vibrant green laser calibration grid lines. A countdown chime sounds as pneumatic valves hiss.
Dialogue: {레일 위에 거치된 물체의 질량은 100kg. 단단한 고밀도 금속 블록입니다. 발사 카운트다운 들어갑니다!}
<Pneumatic air release hiss, mechanical countdown beep: Three, Two, One>

16-24s [Shot 3: High-speed linear rightward tracking chase]:
The black platform cart of @Image 1 accelerates violently down the track toward the right side of the screen with linear electromagnetic propulsion, reaching 60 km/h in an instant. Floor-mounted sensor lights blur into glowing streaks as wind whips through the room.
Dialogue: {가속도의 힘. 속도가 60km에 도달합니다!}
<Magnetic catapult blast, whistling high-velocity wind rush>

24-30s [Shot 4: Close side-profile rightward tracking into seamless dissolve]:
Smooth side-profile tracking shot following parallel with the rapidly moving black cart of @Image 1 moving forward toward the right. As speed peaks, a seamless cinematic dissolve gradually transforms the moving black metal cart and block into the sleek metallic rightward-cruising black sedan from @Image 3 traveling smoothly along an open scenic highway under natural daylight.
<Whistling wind rush seamlessly dissolves into the low rumbling hum of vehicle tires on asphalt>

[End State]
00:30 Clean, steady side-profile shot of the black sedan from @Image 3 traveling rightward at 60 km/h on an open scenic highway under daylight.

[Audio]
Upbeat modern electronic scientific synth intro, robotic countdown beeps, magnetic propulsion whoosh, cross-fading into highway tire rumble. Strictly physical SFX and ambient only.

[Negative]
gore, blood, plastic skin, distorted faces, 3D cartoon, dark grimy lighting, jittery frames, reverse driving, opposite direction driving, BGM, music, soundtrack, melody, instruments, singing, blurry, watermark, subtitles.`;

async function run() {
  const tabs = await listBrowserTabs();
  const t = tabs.find(tab => tab.title.includes('Runway'));
  if (!t) {
    console.log('No Runway tab');
    return;
  }
  await attachBrowserTab(t.targetId);

  // Set Aspect ratio to 16:9 and duration to 30s
  const arBtn = page.getByRole('button', { name: 'Aspect ratio' });
  if (await arBtn.count() > 0 && (await arBtn.innerText()).includes('Auto')) {
    await arBtn.click();
    await sleep(500);
    const ar169 = page.getByRole('menuitem', { name: '16:9' }).first();
    if (await ar169.count() > 0) await ar169.click();
  }

  const durBtn = page.getByRole('button', { name: 'Duration' });
  if (await durBtn.count() > 0 && !(await durBtn.innerText()).includes('30s')) {
    await durBtn.click();
    await sleep(500);
    const dur30 = page.getByRole('menuitem', { name: '30s' }).first();
    if (await dur30.count() > 0) await dur30.click();
  }

  const tb = page.getByRole('textbox', { name: 'Prompt' });
  await tb.fill(promptText);
  console.log('Filled prompt');

  await sleep(1000);
  const genBtn = page.getByRole('button', { name: 'Generate', exact: true });
  console.log('GenBtn count:', await genBtn.count());
  await genBtn.click();
  console.log('Generate clicked!');
  await sleep(3000);
  const s = await snapshot(page);
  console.log(s.tree);
}

await run();
