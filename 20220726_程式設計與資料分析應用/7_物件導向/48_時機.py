# 程式執行的時機點
# 編譯時期 : Compile , 也就是在設計程式的時期
# 執行時期 : Runtime , 開始執行時
a=10
b=0
# prin(a, b) # 編譯時期 error 出現紅色底線
print(a/b) # 無法除以 0 , 執行時期 error 造成程式閃退
