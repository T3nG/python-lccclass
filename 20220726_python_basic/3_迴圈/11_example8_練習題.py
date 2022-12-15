'''
        *
      * *
    * * *
  * * * *
* * * * *
先印空格，再印*
'''

for i in range(5):
    for j in range(4-i):
        print("  ", end="")
    for j in range(i+1):    # 前面的迴圈跑完, 跑下一個迴圈; 上一個處理空格, 下一個處理*
        print("* ", end="")
    print()
