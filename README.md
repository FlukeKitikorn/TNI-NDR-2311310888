# 🍃 Leaf Trade

> A powerful Python-based stock market analysis tool for visualizing Thai stock market data with interactive candlestick charts and technical indicators.

---

## ✨ Features

### 📡 Real-Time Data Integration
- **Settrade API Connection**: Automatically fetch historical stock market data from Settrade Open APIs
- **Multiple Time Intervals**: Support for various timeframes (1m, 5m, 15m, 1h, 1d, etc.)
- **Customizable Data Range**: Select the number of candles to display

### 📊 Advanced Visualization
- **Interactive Candlestick Charts**: Professional-grade charts powered by Plotly
- **Bar Chart Alternative**: Switch between candlestick and bar chart formats
- **Responsive Design**: Optimized for both desktop and mobile viewing
- **Beautiful UI**: Gradient background with clean, modern interface

### 📈 Technical Analysis Tools
- **Simple Moving Average (SMA)**: Track price trends with customizable periods
- **Exponential Moving Average (EMA)**: More responsive to recent price changes
- **MACD Indicator**: Identify momentum and trend direction
- **Volume Analysis**: Monitor trading volume alongside price action

### 📋 Data Management
- **Summary Statistics**: View key metrics including open, high, low, close prices
- **Percentage Change**: Track daily/period performance
- **Volume Metrics**: Analyze trading activity
- **Excel Import/Export**: Upload XLS/XLSX files for custom analysis

### 📁 File Upload Support
- Import your own historical data
- Support for Excel formats (XLS, XLSX)
- Analyze custom datasets with the same powerful tools

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**Core Libraries:**
- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive charting library
- `numpy` - Numerical computing
- `matplotlib` - Static plotting
- `altair` - Declarative visualization
- `scikit-learn` - Machine learning utilities
- `settrade-v2` - Settrade API integration
- `openpyxl` - Excel file handling
- `streamlit-option-menu` - Enhanced navigation

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/FlukeKitikorn/TNI-NDR-2311310888.git
cd TNI-NDR-2311310888
```

2. **Install dependencies**
```bash
pip install -r requirement.txt
```

3. **Run the application**
```bash
streamlit run Home.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

---

## 📖 Usage

### Main Dashboard
1. Enter a stock symbol (e.g., PTT, KBANK, AOT)
2. Select your preferred time interval
3. Choose the number of candles to display
4. Add technical indicators as needed
5. Analyze the interactive chart

### Excel Import
1. Navigate to the "Import Excel" page
2. Upload your XLS/XLSX file
3. Map columns to required fields (Date, Open, High, Low, Close, Volume)
4. Visualize and analyze your custom data

---

## 📁 Project Structure

```
TNI-NDR-2311310888/
├── Home.py                 # Main application entry point
├── pages/
│   └── import_excel.py    # Excel import functionality
├── src/
│   └── components/        # UI components
├── Datahandle/
│   └── settrade/          # API integration
├── .streamlit/            # Streamlit configuration
└── requirement.txt        # Project dependencies
```

---

## 🎥 Demo

https://github.com/user-attachments/assets/7a16527b-5ea8-4a2a-a313-1ee2952dd883



