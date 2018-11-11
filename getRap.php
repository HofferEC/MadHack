<?php

$myfile = fopen("lyrics.txt", "r") or die("Unable to open file!");
if(filesize("lyrics.txt") == 0){
    fclose($myfile);
    echo ("An unexpected error has occured, try a different word. Make sure that it is only one word and not a phrase.");
} else {
    echo fread($myfile, filesize("lyrics.txt"));
    fclose($myfile);
}

?>
