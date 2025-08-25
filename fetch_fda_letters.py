import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def fetch_letters():
    url = "https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # 模拟抓取逻辑（实际需解析表格或JSON）
    letters = []  # 这里应填充实际数据
    with open("letters.json", "w", encoding="utf-8") as f:
        json.dump(letters, f, ensure_ascii=False, indent=2)
