<html>
<body>
<?php
	$username = "user";
	$password = "user01";
	$database = "test1";
	mysql_connect(localhost, $username, $password);
	@mysql_select_db($database) or die ("Unable to select database");
	
	$query = "SELECT * FROM 'temp'";
	$result = mysql_query($query);
	//$num = mysql_numrows($result);
	mysql_close();
?>

<?php print $username?>
	<table border="1">
		<tr>
			<td>czas</td>
			<td>temperatura</td>
		</tr>
		
		<?php
		while($row = mysql_fetch_row($result)){
			print "<tr>";
				print "<td>" . $row[0] . "</td>";
				print "<td>" . $row[1] . "</td>";
				
			print "</tr>";
		}
		?>
	</table>
</body>
</html>
