import sys
sys.path.append('/Users/wisdom/Library/Python/3.9/lib/python/site-packages')
import os
from PIL import Image, ImageDraw, ImageFont

# 비디오 기본 설정
fps = 30
total_frames = 1588  # 52.93초
width, height = 1920, 1080

# 영화 자막에 어울리는 엄선된 4구간 시네마틱 요약 자막
cinema_subtitles = [
    (1, 8, "대한민국의 대세가 되어버린 1인 가구 트렌드"),
    (10, 17, "정확한 1인 가구 수치를 확인할 수 있는 지표의 필요성"),
    (19, 26, "국가통계포털(KOSIS)을 통한 정확한 데이터 조회"),
    (38, 48, "통계 속 수치 너머, 우리 곁에 살아 숨 쉬는 이웃들의 이야기")
]

def render_cinema_frame(frame_idx, font_sans, font_bold):
    """하이엔드 시네마 HUD 스타일 프레임 렌더러"""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    current_time_sec = frame_idx / fps
    
    # ----------------------------------------------------
    # 1. 네 모퉁이 미니멀 크롭 코너 가이드 (Cinematic Corner Marks)
    # ----------------------------------------------------
    offset = 40
    length = 30
    line_w = 2
    # 좌상단
    draw.line([offset, offset, offset + length, offset], fill="white", width=line_w)
    draw.line([offset, offset, offset, offset + length], fill="white", width=line_w)
    # 우상단
    draw.line([width - offset, offset, width - offset - length, offset], fill="white", width=line_w)
    draw.line([width - offset, offset, width - offset, offset + length], fill="white", width=line_w)
    # 좌하단
    draw.line([offset, height - offset, offset + length, height - offset], fill="white", width=line_w)
    draw.line([offset, height - offset, offset, height - offset - length], fill="white", width=line_w)
    # 우하단
    draw.line([width - offset, height - offset, width - offset - length, height - offset], fill="white", width=line_w)
    draw.line([width - offset, height - offset, width - offset, height - offset - length], fill="white", width=line_w)

    # ----------------------------------------------------
    # 2. 좌상단: PREMIER VIEWING SCREEN [HDR] (미니멀 화이트 라인)
    # ----------------------------------------------------
    font_hud = ImageFont.truetype(font_bold, 18)
    draw.text((60, 60), "✦ SHINHAN PREMIER MONITORING MODE [HDR]", fill="white", font=font_hud)
    
    # ----------------------------------------------------
    # 3. 우상단: 영화 촬영용 고정밀 타임코드 (HH:MM:SS:FF)
    # ----------------------------------------------------
    hours = int(current_time_sec // 3600)
    minutes = int((current_time_sec % 3600) // 60)
    seconds = int(current_time_sec % 60)
    frames = int((frame_idx % fps))
    timecode_str = f"TCR {hours:02d}:{minutes:02d}:{seconds:02d}:{frames:02d}"
    
    draw.text((width - 320, 60), timecode_str, fill="#00ff66", font=font_hud) # 네온 그린 타임코드
    
    # ----------------------------------------------------
    # 4. 하단: 촬영용 카메라 설정 메타데이터 (ISO, Aperture, Res 등)
    # ----------------------------------------------------
    # 좌하단 배치
    draw.text((60, height - 80), "ISO 800  |  F/2.8  |  1/48s  |  24.00 fps", fill="#a1a1a6", font=font_hud)
    # 우하단 배치
    draw.text((width - 320, height - 80), "4K RAW DCI  |  BATT 98%  |  REC", fill="#a1a1a6", font=font_hud)
    # 우하단 REC 점멸 도트
    if (frame_idx // 15) % 2 == 0:
        draw.ellipse([width - 80, height - 76, width - 68, height - 64], fill="#ff3b30")
        
    # ----------------------------------------------------
    # 5. 하단 중앙: 영화관 스타일 시네마틱 한글 자막 (그림자 최소화 가독성 극대화)
    # ----------------------------------------------------
    font_sub = ImageFont.truetype(font_sans, 36)
    
    for start, end, sub_txt in cinema_subtitles:
        if start <= current_time_sec < end:
            # 영화 자막 규격: 화이트 컬러에 얇은 다크 섀도우 테두리로 영화 톤 방해 배제
            draw.text((width // 2, 930), sub_txt, fill="white", font=font_sub, anchor="mm", stroke_width=3, stroke_fill="black")
            break
            
    # 프레임 임시 저장
    frame_path = f"scratch/frames/frame_{frame_idx:04d}.png"
    img.save(frame_path)

def generate_cinema_frames():
    os.makedirs('scratch/frames', exist_ok=True)
    font_sans = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    
    print("Start rendering cinematic HUD overlay frames...")
    for i in range(total_frames):
        render_cinema_frame(i, font_sans, font_bold)
        if i % 300 == 0:
            print(f"Progress: {i}/{total_frames} frames...")
    print("Cinematic HUD overlay frames rendering complete.")

if __name__ == "__main__":
    generate_cinema_frames()
