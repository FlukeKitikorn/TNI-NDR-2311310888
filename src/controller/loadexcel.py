import streamlit as st
import pandas as pd

def format_date_thai(dt):
    thai_months = {
        "ม.ค.": "01", "ก.พ.": "02", "มี.ค.": "03", "เม.ย.": "04",
        "พ.ค.": "05", "มิ.ย.": "06", "ก.ค.": "07", "ส.ค.": "08",
        "ก.ย.": "09", "ต.ค.": "10", "พ.ย.": "11", "ธ.ค.": "12"
    }
    
    # กรณี dt เป็น datetime object (Excel อาจอ่านเป็น datetime)
    if pd.isnull(dt):
        return None
    
    # ถ้าเป็น datetime.datetime ให้แปลงตรง ๆ
    if hasattr(dt, "year") and hasattr(dt, "month") and hasattr(dt, "day"):
        year_ad = dt.year
        # ตรวจสอบถ้า year > 2500 ให้ลบ 543 เพื่อเป็น ค.ศ.
        if year_ad > 2500:
            year_ad -= 543
        month_num = dt.month
        return f"{year_ad}-{month_num:02d}-{dt.day:02d}"
    
    # กรณี dt เป็น string เช่น "19 พ.ค. 2568"
    dt_str = str(dt)
    for th_month, num in thai_months.items():
        if th_month in dt_str:
            # สมมุติรูปแบบเป็น "19 พ.ค. 2568" หรือ "19 พ.ค. 2568 00:00:00"
            parts = dt_str.split()
            if len(parts) >= 3:
                day = parts[0]
                month = num
                year_th = parts[2]
                year_ad = int(year_th) - 543
                return f"{year_ad}-{month}-{int(day):02d}"
    return None
    
def excel_to_pandas(file):
    try:
        df = pd.read_excel(file, skiprows=1)

        df.columns = [
            "วันที่", "ราคาเปิด", "ราคาสูงสุด", "ราคาต ่าสุด", "ราคาเฉลี่ย", "ราคาปิด",
            "เปลี่ยนแปลง", "เปลี่ยนแปลง(%)", "ปริมาณ(พันหุ้น)", "มูลค่า(ล้านบาท)",
            "SET Index", "SET เปลี่ยนแปลง(%)"
        ]

        # ลบแถวว่างและแถว header ซ้ำ
        df = df[~df["วันที่"].isna() & ~df["วันที่"].astype(str).str.contains("วันที่")]

        # แปลงวันที่ไทยเป็น ค.ศ. และรูปแบบ yyyy-mm-dd
        df["วันที่"] = df["วันที่"].apply(format_date_thai)

        # แปลงเป็น datetime สำหรับการวิเคราะห์ต่อ
        df["วันที่"] = pd.to_datetime(df["วันที่"], errors='coerce')

        if df.empty:
            st.error("❌ DataFrame is empty!")
        else:
            st.success("✅ DataFrame loaded successfully!")
            st.dataframe(df.head(10))

        return df

    except Exception as e:
        st.error(f"❌ Error processing Excel file: {e}")
        return None