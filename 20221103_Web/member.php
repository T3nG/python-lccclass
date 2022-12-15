<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <!-- id=> css , name=> 變數-->
        <form action="mem_process.php" method="get" name="form1" id="form1" onsubmit="return check();">
            <table border="1" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td colspan="2">會員註冊</td>
                </tr>
                <tr>
                    <td width="80">姓名</td>
                    <td width="80"><input type="text" name="userName"></td>
                </tr>
                <tr>
                    <td width="80">帳號</td>
                    <td width="80"><input type="text" name="userAccount"></td>
                </tr>
                <tr>
                    <td width="80">密碼</td>
                    <td width="80"><input type="password" name="userPassword"></td>
                </tr>
                <tr>
                    <td width="80">確認密碼</td>
                    <td width="80"><input type="password" name="userConfirm"></td>
                </tr>
                <tr>
                    <td width="80">國別</td>
                    <td width="80">
                        <select name="country" id="country">
                            <option value="none" selected disabled hidden>請輸入國別</option>
                            <option value="台灣">台灣</option>
                            <option value="日本">日本</option>
                            <option value="韓國">韓國</option>
                            <option value="美國">美國</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td width="80">性別</td>
                    <td width="80">
                        <input type="radio" name="sex" value="男" checked>男</input>
                        <input type="radio" name="sex" value="女">女</input>
                    </td>
                </tr>

                <tr align="center">
                    <td colspan="2"><input type="submit" value="註冊"/></td>
                </tr>
            </table>
        </form>
        <script>
            // 判定不可為空白, 密碼與確認密碼, 確認完畢後才送到資料庫
            function check(){
                f=document.getElementById('form1');
                cols=["姓名","帳號","密碼","確認密碼"];
                if(f['country'].value=="none"){
                    window.alert("請輸入國別");
                    return false;
                }
                for (i=0;i<f.length-3;i++){  // exclude 國別,性別,註冊
                    if(f[i].value===""){  // 第i個若是空值, 則不送出 == 為None ===為空值
                        window.alert(cols[i]+"不可為空白");
                        return false;
                    }
                }
                if(f['userConfirm'].value!=f['userPassword'].value){
                    window.alert("密碼不符合");
                    return false;
                }
                if(f[i].value.include("$","!","@")){
                    window.alert(cols[1]+"不可含有特殊字元");
                    return false;
                }
                return true;
            }
        </script>
    </body>
</html>

<!--
由網址啟動: Apache 執行php 然後送出 html
直接點兩下: Apache 直接送出文字檔

在客戶端進行檢查填入資料是否正確-> JavaScript

傳送驗證碼到 email: Server需要自己架 mail Server, 通常會被當成垃圾信件而被擋住
數字驗證:
    a. 需於server建立session紀錄驗證碼
    b. 前端傳入驗證碼到後端, 再跟session的驗證碼比對
-->