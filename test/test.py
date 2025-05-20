import pandas as pd


df = pd.read_excel('D:/Trading analysis/Datahandle/malee.xlsx' , skiprows=1)
df.columns = [
        "วันที่", "ราคาเปิด", "ราคาสูงสุด", "ราคาต ่าสุด", "ราคาเฉลี่ย", "ราคาปิด",
        "เปลี่ยนแปลง", "เปลี่ยนแปลง(%)", "ปริมาณ(พันหุ้น)", "มูลค่า(ล้านบาท)",
        "SET Index", "SET เปลี่ยนแปลง(%)"
    ]
thai_months = {
        "ม.ค.": "01", "ก.พ.": "02", "มี.ค.": "03", "เม.ย.": "04",
        "พ.ค.": "05", "มิ.ย.": "06", "ก.ค.": "07", "ส.ค.": "08",
        "ก.ย.": "09", "ต.ค.": "10", "พ.ย.": "11", "ธ.ค.": "12"
    }
def convert_thai_date(date_str):
    try:
        day, month_th, year_th = date_str.replace(",", "").split()
        year = int(year_th) - 543
        month = thai_months[month_th]
        return f"{year}-{month}-{int(day):02d}"
    except:
        return None

df["วันที่"] = df["วันที่"].apply(convert_thai_date)
df["วันที่"] = pd.to_datetime(df["วันที่"], errors='coerce') 
df = df.dropna()
df.head(5)

# print(df["ราคาปิด"].describe())
# print(df[df["ราคาปิด"] == df["ราคาปิด"].max()])
# print(df[["ราคาปิด", "SET Index"]].corr())