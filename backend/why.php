<?php
  $response = $_POST['response'] ?? "";
  $db = new SQLite3('responses.db');

  $date = time();

  $root = realpath($_SERVER["DOCUMENT_ROOT"]);

  $program_path = $root . "/neuralnet/program.py";

  $filename = uniqid("input_");

  $path = $root . "/neuralnet/" . $filename;

  file_put_contents($path, trim($response));
  system("cd neuralnet && python3 $program_path $path", $retval);
  $output = trim(file_get_contents($path . ".out"));

  unlink($path);
  unlink($path . '.out');

  $cmd = "insert into why (date, response, nnval) values ($date, '$response', $output)";
  $db->exec($cmd);
  print($output);
