# 自動抓取 ChromeDriver.exe 相對應的版本
# 當系統更新Chrome瀏覽器時, 我們並不知道, 所以也不知要手動更改ChromeDriver.exe的版本
# pip install webdriver-manager packaging
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

ops = Options()
ops.add_argument("--disable-gpu")
# ops.add_experimental_option('detach',True)  # 待程式完成後註解掉
# 自動下載ChromeDriver.exe
# 預設位置 C:\Users\登入名稱\.wdm\drivers\chromedriver\win32\107.x.xxxx.xx\chromedriver.exe
driver = webdriver.Chrome(ChromeDriverManager(path="E:\ChromeDriver").install(), options=ops)
driver.get("http://tw.yahoo.com")

# 解決新版ChromeDriver 在除錯時自動關閉的問題, 在程式碼最後加入 input, 或於 options 加入參數 add_experimental_option('detach',True)
# a = input("Press any key...")