from PIL import Image, ImageDraw, ImageFont
import json

# 讀取 JSON 檔案
with open("case_diagnosis.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 設定圖片寬和高
width = 800
height = 600

# 創建白色背景的圖像
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# 設定字體（更換成系統中存在的字體檔案路徑）
try:
    font = ImageFont.truetype("arial.ttf", 18)
except IOError:
    font = ImageFont.load_default()

# 填寫資料到圖像
text = (
    f"Patient Info:\n"
    f"Name: {data['patient_info']['name']}\n"
    f"ID Number: {data['patient_info']['id_number']}\n"
    f"Case Number: {data['patient_info']['case_number']}\n"
    f"Date: {', '.join(data['patient_info']['dates'])}\n\n"
    f"Fees:\n"
    f"Medication Fee: {data['fees']['medication_fee']}\n"
    f"Materials Fee: {data['fees']['materials_fee']}\n"
    f"Nursing Fee: {data['fees']['nursing_fee']}\n"
    f"Treatment Fee: {data['fees']['treatment_fee']}\n"
    f"Meal Fee: {data['fees']['meal_fee']}\n"
    f"Out-of-Pocket Expenses: {data['fees']['out_of_pocket_expenses']}\n"
    f"Balance Due: {data['fees']['balance_due']}\n\n"
    f"Physician:\n"
    f"Name: {data['physician']['name']}\n"
    f"Department: {data['physician']['department']}\n"
    f"Visit Number: {data['physician']['visit_number']}\n"
)
draw.multiline_text((10, 10), text, fill="black", font=font)

# 保存為 JPEG 圖像
image.save("case_diagnosis.jpg", "JPEG")
print("Image saved as case_diagnosis.jpg")