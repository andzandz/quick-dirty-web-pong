<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

echo json_encode([
  'ball' => [
    'x' => $redis->get('ball_pos_x'),
    'y' => $redis->get('ball_pos_y'),
    'bounced' => $redis->get('ball_bounced')
  ],
  'paddles' => [
    'left' => [
      'x' => $redis->get('left_paddle_x'),
      'y' => $redis->get('left_paddle_y'),
      'score' => $redis->get('left_paddle_score')
    ],
    'right' => [
      'x' => $redis->get('right_paddle_x'),
      'y' => $redis->get('right_paddle_y'),
      'score' => $redis->get('right_paddle_score')
    ]
  ]
]);
