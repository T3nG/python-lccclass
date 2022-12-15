<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <!--
        <?php
            // 變數要加 $
            // echo "this is php program";
            $name=$_GET["userName"];
            echo $name;
            echo "</br>";
            $account=$_GET["userAccount"];
            echo $account;
        ?>
        -->
        <!--
        <table border="1" cellspacing="0" cellpadding="0">
        <?php
            // 利用表格來format
            // for (起始值;結束值;步進值){}
            // for i in range(1,10,1)
            // . 的意義, 字串相加
            for ($i=1;$i<=9;$i++){
                echo "<tr>";
                for ($j=1;$j<=9;$j++){
                    echo "<td width='30'>";
                    echo $i*$j."  ";
                    echo "</td>";
                }
                echo "</tr>";
            }
        ?>
        </table>
        -->
        <?php
            $userName=$_GET['userName'];
            $userAccount=$_GET['userAccount'];
            $userPassword=$_GET['userPassword'];
//            echo $userName;
//            echo "</br>";
//            echo $userAccount;
//            echo "</br>";
//            echo $userPassword;
//          與資料庫連線, mysql設定中的, host name, user, password, database
            $conn=new mysqli("localhost", "user","password","database");
            if(!$conn){
                die("連線失敗");
            }
            $cmd=sprintf("insert into 會員資料表 (姓名, 帳號, 密碼) values ('%s', '%s', '%s')",
                $userName, $userAccount, $userPassword);
            echo $cmd;
            // 再寫進資料庫前, 先確認是否可以正確列出
            // 格式化列印
            // python
            // 1. conn
            // 2. cursor=conn.cursor()
            // 3. cmd SQL 字串
            // 4. cursor.execute(cmd)
            // 5. conn.commit()
            // 6. conn.close()
            if(!$conn->query($cmd)){
                echo "</br>";
                die("註冊失敗");
            }
            $conn->close();
        ?>
    </body>
</html>
