<!--
    http://cosmowhale.asuscomm.com/web/99.php
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <table border="1" cellpadding="0" cellspacing="0">
        <?php
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
    </body>
</html>