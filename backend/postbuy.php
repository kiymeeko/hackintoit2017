<?php
  $stars = $_POST['star'] ?? 0;
  $response = $_POST['text'] ?? "";
  $whyid = $_POST['whyid'] ?? 0;
  $db = new SQLite3('responses.db');
  $date = time();
  $cmd = "insert into postbuy values ($date, 4, '$response', $stars)";
  $db->exec($cmd);
  print($stars);
  print($response);
