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
	
	$query_hour_table = "SELECT * FROM `temp2`";
	$result_hour_table = mysql_query($query_hour_table);
	
	$query_day_table = "SELECT * FROM `temp_daily`";
	$result_day_table = mysql_query($query_day_table);
	
	//$num = mysql_numrows($result);
?>

	<b><h1>TABELA DZIENNA</h1></b>
	<table border="1">
		<tr>
			<td>data</td>
			<td>godzina</td>
			<td>temperatura</td>
		</tr>
		
		<?php
		while($row = mysql_fetch_row($result_hour_table)){
			print "<tr>";
				print "<td>" . $row[0] . "</td>";
				print "<td>" . $row[1] . "</td>";
				print "<td>" . $row[2] . "</td>";
			print "</tr>";
		}
		?>
	</table>
	
	<b><h1>TABELA MIESIĘCZNA</h1><b>
	<table border="1">
		<tr>
			<td>data</td>
			<td>temperatura</td>
		</tr>
		<?php
		while($row = mysql_fetch_row($result_day_table)){
			print "<tr>";
				print "<td>" . $row[0] . "</td>";
				print "<td>" . $row[1] . "</td>";
			print "</tr>";
		}
		if(!mysql_close()){
			echo "Nie moge zakonczyc polaczenia z baza danych";
			exit(0);
		}
		?>
	</table>
</body>
</html>
