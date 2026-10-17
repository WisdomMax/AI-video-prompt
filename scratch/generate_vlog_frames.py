import sys
sys.path.append('/Users/wisdom/Library/Python/3.9/lib/python/site-packages')
import os
import math
from PIL import Image, ImageDraw, ImageFont

# 비디오 기본 설정
fps = 30
total_frames = 1588  # 52.93초
width, height = 1920, 1080

# 4대 예능 포인트 요약 자막 타임라인 싱크 매핑
vlog_subtitles = [
    # (시작초, 종료초, 상단 캡슐, 중앙 임팩트 타이틀, 하단 요약 서브)
    (1, 8, "골목길 토크", "요즘 대세는 1인 가구?! 🏠", "원룸 건물은 이미 나 혼자 산다 전성시대"),
    (10, 17, "갑자기 궁금", "정확히 몇 명일까? 🤔", "집집마다 직접 세어 볼 수도 없고 답답한 순간"),
    (19, 26, "해결사 등판", "국가통계포털 검색 ON! 💻", "엔터 한 번에 모든 통계가 다 나오는 신세계"),
    (38, 48, "할머니 생각", "주말 안부 전화 필수! ☎️", "이번 주말에는 따뜻하게 목소리 들으러 갑니다")
]

def draw_heart(draw, cx, cy, size, color):
    """PIL로 그리는 깔끔한 예능형 분홍 하트 벡터 스티커"""
    points = []
    for t in range(0, 360, 5):
        rad = math.radians(t)
        # 하트 수학 공식 적용
        x = 16 * (math.sin(rad) ** 3)
        y = 13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad)
        # 좌표 스케일링 및 위치 보정
        points.append((cx + x * (size / 16), cy - y * (size / 16)))
    draw.polygon(points, fill=color)

def draw_sparkle(draw, cx, cy, r, color):
    """PIL로 그리는 4포인트 노란색 반짝이 별 스티커"""
    points = [
        (cx, cy - r),
        (cx + r * 0.25, cy - r * 0.25),
        (cx + r, cy),
        (cx + r * 0.25, cy + r * 0.25),
        (cx, cy + r),
        (cx - r * 0.25, cy + r * 0.25),
        (cx - r, cy),
        (cx - r * 0.25, cy - r * 0.25)
    ]
    draw.polygon(points, fill=color)

def render_vlog_frame(frame_idx, font_sans, font_bold):
    """클로드 예능 감성 레이아웃 프레임 렌더러"""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    current_time_sec = frame_idx / fps
    
    # ----------------------------------------------------
    # 1. 좌상단 CHROMA CAM 브랜드 뱃지 (핑크/화이트 배너)
    # ----------------------------------------------------
    draw.rounded_rectangle([60, 60, 420, 120], radius=18, fill="white", outline="#ff7597", width=4)
    font_logo = ImageFont.truetype(font_bold, 24)
    draw.text((85, 76), "✦ CHROMA CAM", fill="#1c1c1e", font=font_logo)
    
    # EP.03 점멸 효과
    ep_color = "#ff7597" if (frame_idx // 15) % 2 == 0 else "#c7c7cc"
    draw.text((320, 76), "EP.03", fill=ep_color, font=font_logo)
    
    # ----------------------------------------------------
    # 2. 우상단 동적 REC 타이머 (시간이 실제로 흐름)
    # ----------------------------------------------------
    draw.rounded_rectangle([1580, 60, 1860, 120], radius=18, fill="#1c1c1e")
    
    # RED 도트 점멸
    dot_color = "#ff3b30" if (frame_idx // 15) % 2 == 0 else "#48484a"
    draw.ellipse([1610, 84, 1626, 100], fill=dot_color)
    
    # 실제 재생시간 포맷팅 (REC MM:SS)
    minutes = int(current_time_sec // 60)
    seconds = int(current_time_sec % 60)
    time_str = f"REC {minutes:02d}:{seconds:02d}"
    draw.text((1650, 76), time_str, fill="#ffcc00", font=font_logo)
    
    # ----------------------------------------------------
    # 3. 예능 하이라이트 요약 자막 세트 (매칭 타이밍에만 노출)
    # ----------------------------------------------------
    for start, end, capsule_txt, main_txt, sub_txt in vlog_subtitles:
        if start <= current_time_sec < end:
            # A. 상단 캡슐 ("무대 5분 전" 스타일)
            font_capsule = ImageFont.truetype(font_sans, 24)
            # 텍스트 길이에 맞춰 유동적으로 캡슐 가로폭 조절
            cap_w = draw.textlength(capsule_txt, font=font_capsule) + 40
            cx = width // 2
            draw.rounded_rectangle([cx - cap_w/2, 170, cx + cap_w/2, 224], radius=15, fill="white", outline="#ff7597", width=3)
            draw.text((cx, 197), capsule_txt, fill="#ff7597", font=font_capsule, anchor="mm")
            
            # B. 중앙 메인 자막 ("대기실 셀프캠 ON" 스타일)
            font_main = ImageFont.truetype(font_sans, 64)
            # 핑크 그라데이션 대신 산뜻한 예능 핑크(#ff4a7d) 적용 및 매우 두꺼운 흰색 테두리
            draw.text((width // 2, 280), main_txt, fill="#ff4a7d", font=font_main, anchor="mm", stroke_width=12, stroke_fill="white")
            
            # C. 데코레이션 스티커 흩뿌리기 (자막 좌우에 분홍 하트와 노란 반짝이 배치)
            draw_heart(draw, width // 2 - 320, 240, 25, "#ff7597")
            draw_heart(draw, width // 2 + 300, 310, 20, "#ff7597")
            draw_sparkle(draw, width // 2 - 270, 300, 22, "#ffea00")
            draw_sparkle(draw, width // 2 + 250, 220, 18, "#ffea00")
            
            # D. 하단 서브 자막 ("오늘의 카메라 담당은 막내 유하" 스타일)
            font_sub = ImageFont.truetype(font_sans, 42)
            draw.text((width // 2, 920), sub_txt, fill="#ff5e97", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
            break
            
    # 프레임 임시 저장
    frame_path = f"scratch/frames/frame_{frame_idx:04d}.png"
    img.save(frame_path)

def generate_vlog_frames():
    os.makedirs('scratch/frames', exist_ok=True)
    font_sans = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    
    print("Start rendering vlog-style overlay frames...")
    for i in range(total_frames):
        render_vlog_frame(i, font_sans, font_bold)
        if i % 300 == 0:
            print(f"Progress: {i}/{total_frames} frames...")
    print("Vlog overlay frames rendering complete.")

if __name__ == "__main__":
    generate_vlog_frames()
