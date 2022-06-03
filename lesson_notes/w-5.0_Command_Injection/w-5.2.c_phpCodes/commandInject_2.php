<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Code Injection</title>
</head>
<body>
	<form name="ping" action="#" method="post">
			<p>
				Enter an IP address:
				<input type="text" name="ip" size="30">
				<input type="submit" name="Submit" value="Submit">
			</p>

		</form>

</body>
</html>



<?php 
$target = $_POST['ip'];
$target = $_REQUEST['ip'];

$cmd = shell_exec("ping -c 4 ".$target);
echo "<br>{$cmd}<br>";


 ?>