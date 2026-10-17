import sys
sys.path.append('/Users/wisdom/Library/Python/3.9/lib/python/site-packages')
import os
from PIL import Image, ImageDraw, ImageFont

def create_overlays():
    # 저장 경로 설정
    os.makedirs('scratch', exist_ok=True)
    
    # 폰트 설정
    font_sans = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
    font_bold = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    
    # 기본 크기 정의
    width, height = 1920, 1080
    
    # ----------------------------------------------------
    # 1. 공통 UI 오버레이 (상시 노출: CHROMA CAM & REC 00:07)
    # ----------------------------------------------------
    ui_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ui_draw = ImageDraw.Draw(ui_img)
    
    # 좌상단 배너 (CHROMA CAM EP.03)
    # 둥근 사각형 배경
    ui_draw.rounded_rectangle([40, 40, 360, 100], radius=15, fill="white", outline="#ff6b8b", width=4)
    # 텍스트 폰트 로드
    font_logo = ImageFont.truetype(font_bold, 20)
    # ✦ 기호 및 텍스트 그리기
    ui_draw.text((60, 58), "✦ CHROMA CAM", fill="black", font=font_logo)
    ui_draw.text((260, 58), "EP.03", fill="#ff6b8b", font=font_logo)
    
    # 우상단 배너 (REC 00:07)
    ui_draw.rounded_rectangle([1680, 40, 1880, 100], radius=15, fill="black")
    # 빨간 녹화 아이콘
    ui_draw.ellipse([1710, 62, 1726, 78], fill="#ff3b30")
    # REC 텍스트
    ui_draw.text((1745, 58), "REC 00:07", fill="#ffcc00", font=font_logo)
    
    ui_img.save("scratch/ui.png")
    print("Created scratch/ui.png")
    
    # ----------------------------------------------------
    # 2. 자막 1 (0초 ~ 15초용): "콕콕" & "출격 전 최종 점검은 필수"
    # ----------------------------------------------------
    t1_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    t1_draw = ImageDraw.Draw(t1_img)
    
    # 스티커 자막 "콕콕" (인물 머리 우측 부근)
    font_sticker = ImageFont.truetype(font_sans, 42)
    t1_draw.text((1120, 320), "콕콕", fill="#ffea00", font=font_sticker, stroke_width=6, stroke_fill="#d84315")
    
    # 하단 자막
    font_sub = ImageFont.truetype(font_sans, 52)
    # 그림자 효과 (약간 빗겨난 검은색 오프셋)
    t1_draw.text((width // 2, 930), "출격 전 최종 점검은 필수", fill="#ff7a00", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
    # 투명 자막 바 느낌을 위해 텍스트 뒤에 얇은 쉐도우 한 겹 더 추가
    t1_img.save("scratch/text1.png")
    print("Created scratch/text1.png")
    
    # ----------------------------------------------------
    # 3. 자막 2 (15초 ~ 30초용): "반짝반짝" & "눈부신 비주얼과 압도적인 분위기"
    # ----------------------------------------------------
    t2_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    t2_draw = ImageDraw.Draw(t2_img)
    
    t2_draw.text((1150, 300), "반짝", fill="#ffea00", font=font_sticker, stroke_width=6, stroke_fill="#d84315")
    t2_draw.text((width // 2, 930), "눈부신 비주얼과 압도적인 분위기", fill="#ff7a00", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
    t2_img.save("scratch/text2.png")
    print("Created scratch/text2.png")
    
    # ----------------------------------------------------
    # 4. 자막 3 (30초 ~ 45초용): "심쿵" & "이것이 바로 신한 Premier의 클래스"
    # ----------------------------------------------------
    t3_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    t3_draw = ImageDraw.Draw(t3_img)
    
    t3_draw.text((820, 420), "심쿵", fill="#ffea00", font=font_sticker, stroke_width=6, stroke_fill="#d84315")
    t3_draw.text((width // 2, 930), "이것이 바로 신한 Premier의 클래스", fill="#ff7a00", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
    t3_img.save("scratch/text3.png")
    print("Created scratch/text3.png")
    
    # ----------------------------------------------------
    # 5. 자막 4 (45초 ~ 53초용): "당신만을 위한 자산관리, 신한 Premier"
    # ----------------------------------------------------
    t4_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    t4_draw = ImageDraw.Draw(t4_img)
    
    t4_draw.text((width // 2, 930), "당신만을 위한 자산관리, 신한 Premier", fill="#ff7a00", font=font_sub, anchor="mm", stroke_width=8, stroke_fill="white")
    t4_img.save("scratch/text4.png")
    print("Created scratch/text4.png")

if __name__ == "__main__":
    create_overlays()
