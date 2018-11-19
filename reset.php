<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->set("left_paddle_score", 333);
$redis->set("right_paddle_score", 333);
$redis->set("loops", 0);

echo 'OK';
