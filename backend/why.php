<?php
  $stars = $_POST['star'] ?? 0;
  $response = $_POST['text'] ?? "";
  $whyid = $_POST['whyid'] ?? 0;
  $db = new SQLite3('responses.db');
  $date = time();
  $rand = mt_rand() / mt_getrandmax();
  $cmd = "insert into why values ($date, '$response', $rand)";
  $db->exec($cmd);
  print($stars);
  print($response);