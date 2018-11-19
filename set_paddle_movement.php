<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$paddle = $_GET['paddle'];

$redis->set($paddle . "_paddle_movement", $_GET['movement']);

// Reset the game if needed when clicking up/down
if($paddle == 'left') {
  $left_score = $redis->get('left_paddle_score');
  $right_score = $redis->get('right_paddle_score');
  
  if($left_score >= 3 || $right_score >= 3) {
    $redis->set('left_paddle_score', 0);
    $redis->set('right_paddle_score', 0);
    $redis->set('loops', 0);
  }
}

echo "OK";
