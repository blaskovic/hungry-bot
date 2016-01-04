<?php
$menu = preg_replace("/[^0-9\-\w]+/", "", $_GET['menu']);

if(!file_exists('../restaurants/'.$menu))
{
    echo "Menu " . $menu . " does not exist. Use 'menu list' for the list or submit a patch: https://github.com/blaskovic/hungry-bot";
}
else
{
    $cmd = "../restaurants/".$menu;
    echo shell_exec($cmd);
}
