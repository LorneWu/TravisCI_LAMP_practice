<?php
  $servername = "localhost";
  $username = "root";
  $password = "new_password";

  // Create connection
  $conn = new mysqli($servername, $username, $password,"ntvel");

  // Check connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  } 
  echo "Connected successfully";
?>
