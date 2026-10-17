import sys
sys.path.append('/Users/wisdom/Library/Python/3.9/lib/python/site-packages')
import os
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 비디오 스펙 설정
fps = 30
total_frames = 1588  # 52.93초 * 30fps
width, height = 1920, 1080

def get_audio_levels(wav_path, target_frames):
    """오디오 레벨 미터 시뮬레이션을 위해 WAV 파일 볼륨을 프레임 단위로 추출"""
    try:
        with wave.open(wav_path, 'rb') as w:
            frames = w.readframes(-1)
            data = np.frombuffer(frames, dtype=np.int16)
            # 프레임당 오디오 샘플 크기 계산
            samples_per_frame = len(data) // target_frames
            levels = []
            for i in range(target_frames):
                chunk = data[i * samples_per_frame : (i + 1) * samples_per_frame]
                if len(chunk) == 0:
                    levels.append(0)
                    continue
                # RMS(제곱평균제곱근) 계산으로 볼륨 척도 생성 (0 ~ 100 범위로 정규화)
                rms = np.sqrt(np.mean(chunk.astype(float)**2))
                val = min(int(rms / 150), 100)
                levels.append(val)
            return levels
    except Exception as e:
        print("Audio level calculation failed, using random simulation:", str(e))
        return [np.random.randint(20, 80) for _ in range(target_frames)]

# 음성인식 결과 기반의 실제 대사 타임라인 싱크 매핑
subtitles = [
    # (시작초, 종료초, 상단스티커, 하단 대사자막)
    (0, 5, "수다 중", "야 요즘 길 가다 보면 진짜 혼자 사는 사람들\n엄청 많아 보이지 않냐?"),
    (5, 10, "끄덕끄덕", "나 사는 원룸 건물만 해도 다 혼자 살던데..."),
    (10, 15, "궁금증", "근데 우리나라에 정확히 몇 명이나\n혼자 사는지는 어떻게 알지?"),
    (15, 20, "갸우뚱", "야 그러게. 그걸 다 집집마다\n세어 볼 수도 없고 진짜 궁금하네."),
    (20, 24, "검색 중!", "국가통계포털에 다 나옵니다!"),
    (24, 27, "대박!!", "진짜? 검색해 봐. 엔터!"),
    (27, 34, "퇴근길", "지친 몸으로 혼자 걷는 퇴근길에..."),
    (34, 40, "저녁 식사", "홈 파티를 준비하는 저녁 밥상도..."),
    (40, 46, "할머니 생각", "생각해 보니까 우리 시골 할머니도\n지금 혼자 계시는데..."),
    (46, 50, "주말 약속", "이번 주말엔 꼭 전화드리고 놀러 가야겠다!"),
    (50, 53, "원팀 통계", "그래, 통계 속 숫자가 결국 다\n우리 가족이고 우리 이웃들이야.")
]

def render_frame_overlay(frame_idx, audio_level, font_sans, font_bold):
    """매 프레임마다의 시간 및 오디오 볼륨에 따른 Dynamic UI & 자막을 투명 이미지로 렌더링"""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    current_time_sec = frame_idx / fps
    
    # ----------------------------------------------------
    # 1. 왼쪽 상단 살아있는 캠코더 로고 배너
    # ----------------------------------------------------
    # 네온 브이로그 핑크 테두리
    draw.rounded_rectangle([60, 60, 400, 120], radius=18, fill="#ffffff", outline="#ff2d55", width=4)
    # 로고 폰트
    font_logo = ImageFont.truetype(font_bold, 22)
    # ✦ 특수기호 및 텍스트 그리기
    draw.text((85, 78), "✦ CHROMA CAM", fill="#1c1c1e", font=font_logo)
    # EP.03 핑크 깜빡임 애니메이션 (1초 주기)
    if (frame_idx // 15) % 2 == 0:
        draw.text((310, 78), "EP.03", fill="#ff2d55", font=font_logo)
    else:
        draw.text((310, 78), "EP.03", fill="#a1a1a6", font=font_logo)

    # ----------------------------------------------------
    # 2. 오른쪽 상단 흐르는 실시간 REC 타임코드
    # ----------------------------------------------------
    draw.rounded_rectangle([1580, 60, 1860, 120], radius=18, fill="#1c1c1e")
    
    # 빨간색 녹화 도트 0.5초 주기로 점멸
    if (frame_idx // 15) % 2 == 0:
        draw.ellipse([1615, 84, 1631, 100], fill="#ff3b30")
    else:
        draw.ellipse([1615, 84, 1631, 100], fill="#3a3a3c")
        
    # 실시간 시간 환산 계산 (HH:MM:SS.f)
    minutes = int(current_time_sec // 60)
    seconds = int(current_time_sec % 60)
    centiseconds = int((current_time_sec % 1) * 100)
    time_str = f"REC {minutes:02d}:{seconds:02d}.{centiseconds:02d}"
    
    draw.text((1655, 78), time_str, fill="#ffcc00", font=font_logo)
    
    # ----------------------------------------------------
    # 3. 우측 오디오 레벨 미터 (볼륨 크기에 반응하여 출렁거리는 오디오 바)
    # ----------------------------------------------------
    # 오디오 미터 배경 레일
    draw.rounded_rectangle([1810, 200, 1830, 450], radius=5, fill="#2c2c2e")
    # 볼륨 게이지 바 (audio_level 값에 따라 세로 높이 가변 상승)
    bar_height = int((audio_level / 100) * 230)
    if bar_height > 10:
        # 볼륨이 임계치를 넘으면 빨간색, 평상시는 초록/노란색 그라데이션 느낌의 높이
        bar_color = "#34c759" if bar_height < 180 else "#ffcc00" if bar_height < 210 else "#ff3b30"
        draw.rounded_rectangle([1810, 450 - bar_height, 1830, 450], radius=5, fill=bar_color)
    
    # DB 텍스트 데코레이션
    font_db = ImageFont.truetype(font_bold, 14)
    draw.text((1812, 465), "CH1", fill="#a1a1a6", font=font_db)
    
    # ----------------------------------------------------
    # 4. 하단 및 스티커 한글 자막 (타임라인 매핑)
    # ----------------------------------------------------
    font_sticker = ImageFont.truetype(font_sans, 42)
    font_sub = ImageFont.truetype(font_sans, 48)
    
    for start, end, sticker_txt, sub_txt in subtitles:
        if start <= current_time_sec < end:
            # 말풍선 스티커 자막 (여주인공 얼굴 부근)
            draw.text((1120, 320), sticker_txt, fill="#ffea00", font=font_sticker, stroke_width=6, stroke_fill="#d84315")
            
            # 메인 자막 (줄바꿈 지원)
            lines = sub_txt.split('\n')
            y_offset = 890 if len(lines) > 1 else 920
            
            for line in lines:
                # 입체감을 위해 검은색 그라데이션 섀도우를 뒤에 먼저 깔아 가독성 확보
                draw.text((width // 2, y_offset), line, fill="#ff7a00", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
                y_offset += 60
            break

    # 임시 이미지 프레임 저장
    frame_path = f"scratch/frames/frame_{frame_idx:04d}.png"
    img.save(frame_path)

def generate_all_frames():
    os.makedirs('scratch/frames', exist_ok=True)
    
    font_sans = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    
    levels = get_audio_levels("scratch/audio.wav", total_frames)
    
    print("Start rendering overlay frames...")
    # 매 100프레임마다 진행 상황 로그 출력
    for i in range(total_frames):
        render_frame_overlay(i, levels[i], font_sans, font_bold)
        if i % 200 == 0:
            print(f"Rendered {i}/{total_frames} frames...")
    print("Overlay frames rendering complete.")

if __name__ == "__main__":
    generate_all_frames()
