<?php
//  GET的方式
//    $account=$_GET['account'];
//    $password=$_GET['password'];
//  POST的方式
    $account=$_POST['account'];
    $password=$_POST['password'];
//    echo $account;
//    echo "</br>";
//    echo $password;
    $dbAccount="user";
    $dbPassword="password";
    $conn=new mysqli("localhost", $dbAccount, $dbPassword, "cloud");
    if($conn->connect_error){
        die('Error connected');
    }
    $cmd=sprintf("select * from 會員資料表 where 帳號='%s' and 密碼='%s'", $account, $password);
    $result=$conn->query($cmd);
    if($result->num_rows>0){
        echo sprintf('{"dbAccount":"%s", "dbPassword":"%s"}', $dbAccount, $dbPassword);
    }
    else{
        echo "Error";
    }
?>