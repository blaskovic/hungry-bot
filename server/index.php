<?php

if(!file_exists('../restaurants/'.$_GET['menu']))
{
    echo "Menu " . $_GET['menu'] . " does not exist. Use 'menu list' for the list or submit a patch: https://github.com/blaskovic/hungry-bot";
}
else
{
    echo exec("../restaurants/".$_GET['menu']);
}
