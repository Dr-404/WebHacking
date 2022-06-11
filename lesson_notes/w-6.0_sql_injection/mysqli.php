<?php


// To Show Errors

ini_set('display_errors',"1");

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

// To Create Connection

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "sqltest";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


$uid = $_GET['id'];
$sql = "SELECT * FROM users WHERE id='$uid'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "Greeting  : ", $row['status'];
    echo "<br>";
    echo "Department  : ", $row['work'];
    echo "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>