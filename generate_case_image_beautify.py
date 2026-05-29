from PIL import Image, ImageDraw, ImageFont
import json

# 讀取 JSON 檔案
with open("case_diagnosis.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 設定圖片尺寸與樣式
width = 1000  # 寬度加大以容納更多文字
height = 800  # 高度自動調整
background_color = "#F5F5F5"
border_color = "#003366"  # 外框藍色
text_color = "#000000"  # 黑色字

# 創建圖像並填充背景
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# 設定字體
try:
    font = ImageFont.truetype("PMingLiU.ttf", 20)  # 細明體 字號較大
except IOError:
    try:
        font = ImageFont.truetype("NotoSansTC-Regular.otf", 20)  # Noto Sans TC
    except IOError:
        font = ImageFont.truetype("MicrosoftYaHeiTC.ttf", 20)  # 微軟雅黑
    except IOError:
        font = ImageFont.load_default()  # 如果未安裝這些字型

# 描繪外框
border_thickness = 10
draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=border_thickness)

# 添加標題區塊
title = "診療病例報告"
title_font = font
title_size = draw.textsize(title, font=title_font)
title_x = (width - title_size[0]) // 2
draw.text((title_x, 20), title, font=title_font, fill=border_color)

# 書寫患者資料與費用詳細
y = 80  # 起始高度
line_spacing = 30

# 患者資料
patient_info = (
    f"患者姓名：{data['patient_info']['name']}\n"
    f"身份證號：{data['patient_info']['id_number']}\n"
    f"病例號碼：{data['patient_info']['case_number']}\n"
    f"診療日期：{'，'.join(data['patient_info']['dates'])}\n"
)
draw.text((50, y), "患者資料：", font=font, fill=text_color)
y += line_spacing
draw.multiline_text((70, y), patient_info, font=font, fill=text_color)
y += len(patient_info.split("\n")) * line_spacing + 20  # 多行自動高度調整

# 費用詳細
fees_info = (
    f"藥品費：{data['fees']['medication_fee']} 元\n"
    f"材料費：{data['fees']['materials_fee']} 元\n"
    f"護理費：{data['fees']['nursing_fee']} 元\n"
    f"治療費：{data['fees']['treatment_fee']} 元\n"
    f"自費金額：{data['fees']['out_of_pocket_expenses']} 元\n"
    f"應繳金額：{data['fees']['balance_due']} 元\n"
)
draw.text((50, y), "費用詳細：", font=font, fill=text_color)
y += line_spacing
draw.multiline_text((70, y), fees_info, font=font, fill=text_color)
y += len(fees_info.split("\n")) * line_spacing + 20

# 醫師資料
physician_info = (
    f"醫師姓名：{data['physician']['name']}\n"
    f"科別：{data['physician']['department']}\n"
    f"就診編號：{data['physician']['visit_number']}\n"
)
draw.text((50, y), "醫師資訊：", font=font, fill=text_color)
y += line_spacing
draw.multiline_text((70, y), physician_info, font=font, fill=text_color)

# 儲存為圖片
output_filename = "病例報告_美化版.jpg"
image.save(output_filename, "JPEG")
print(f"圖像已儲存為 {output_filename}")