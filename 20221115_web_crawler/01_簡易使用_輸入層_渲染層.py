# pip install selenium
# 下載 跟 Chrome相同版本的 ChromeDriver, https://chromedriver.chromium.org/
# ChromeDriver: 類似一個 Chrome瀏覽器, 但功能比 Chrome 更強
# selenium: Python 與 ChromeDriver 溝通的語言
# Chrome 版本須和 ChromeDriver 一致

# Linux Server ubuntu/樹莓派的人: Server沒有圖形介面
# sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub
# sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt
# sudo apt-get -y update
# sudo apt-get -y install google-chrome-stable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "http://localhost/web/99.html"
# url2 = "http://localhost/web/99.php"
ops = Options()
# ops.add_argument("--headless")  # 無頭模式, 沒有視窗
ops.add_argument("--disable-gpu")  # 也可以註解掉不使用, 預設啟用GPU
browser = webdriver.Chrome("E:/ChromeDriver/chromedriver.exe", options=ops)
browser.get(url)
try:
    # (By.TAG_NAME, 'td') 是 tuple 形式
    # 預設每500ms檢查一次, 若超過20秒都沒結果, 就跑except
    # WebDriverWait(browser, 20(等待秒數), 0.1(每0.1秒=100ms檢查一次)
    # 沒有WebDriverWait的話, 直接抓取瀏覽器的輸入層 資料, 若有等待 則抓取渲染層 的資料
    # 什麼時候需要Wait: 使用 JavaScript或ajax產生的資料, 就需要wait
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME,'td')))
except:
    print("連線錯誤")
print(browser.page_source)
a = input("請按任何按鍵.....")
