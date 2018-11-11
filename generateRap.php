<?php
    $keyword = $_GET["keyword"];
    echo $keyword;
    echo shell_exec("C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe generate.py " . $keyword);
?>
