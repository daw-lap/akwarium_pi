<html>
<body>
<?php
	$username = "user";
	$password = "user01";
	$database = "test1";
	if( !mysql_connect(localhost, $username, $password)){
		print "Blad polaczenia z baza danych";
		exit(0);
	}
	if( !mysql_select_db($database)){
		print "Blad otwarcia bazy danych";
		exit(0);
	}
	
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
