<script>
	let rows = 3;
	let cols = 3;
	let arr = [["A0","B0","C0"],["A1","B1","C1"],["A2","B2","C2"]];
	let obj = [{"A0":"A1","B0":"B1","C0":"C1"},{"A0":"A2","B0":"B2","C0":"C2"}];
	
	function fill(){
		arr = [];
		
		for(var x=0; x<rows; x++){
			arr.push([]);
			for(var y=0; y<cols; y++){
				arr[x].push(String.fromCharCode(65+y) + x);
			}
			
		}
		fillObj();
	}
	
	function fillObj(){
		obj = [];
		for(var x=1; x<arr.length; x++){
			let item = {};
			for(var y=0; y<arr[x].length; y++){
				item[arr[0][y]] = arr[x][y];
			}
			obj.push(item);
		}
	}
</script>

<h2>Table to Arrays</h2>
Cols: <input type="number" bind:value={cols} on:input={fill}>
Rows: <input type="number" bind:value={rows} on:input={fill}>

<h3>
	Table:
</h3>

<table>
	
	{#each arr as row}
  	<tr>
			{#each row as col}
			
  				<td>
						<input bind:value={col} on:input={fillObj}>
					</td>
			
			{/each}
		</tr>
	{/each}
	
</table>
<h3>
	2 dimensional array:
</h3>
<code>{JSON.stringify(arr)}</code>
<h3>
	Array of objects:
</h3>
<code>{JSON.stringify(obj)}</code>
