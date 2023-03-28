<script>
	let inp = "";
	let elements = [];
	let open = '';
	
	function add(){
		if(isNaN(inp)) {
			elements.push(inp);
		} else {
			elements.push(parseFloat(inp));
		}
		
		elements = elements;
		inp = "";
	}
	
	function del(id){
		elements.splice(id,1);
		elements = elements;
	}
	
	function checkEnter(e){
		if(e.key === "Enter"){
			add();
		}
	}
	
	function inport(){
		elements = JSON.parse(open);
		open = '';
	}
	
</script>

<h1>
	Array Editor
</h1>
	<h2>Importar Array:</h2>
	<input bind:value={open} type="text"><button on:click={inport}>Abrir</button>
	
<div class="flex">
	<div>
	<h2>Adicionar Item:</h2>
	<input bind:value={inp} on:keyup={checkEnter} type="text"><button on:click={add}>ADD</button>

	<h2>Itens do Array:</h2>
{#if elements.length === 0}
	<div>nenhum!</div>
{:else}
	<ol start="0">

	{#each elements as el, i}
		{#if isNaN(el)}
		<li><input type="text" bind:value={el}> <button on:click={() => del(i)} >X</button></li>
		{:else}
		<li><input type="number" bind:value={el}> <button on:click={() => del(i)} >X</button></li>
		{/if}
	{/each}
		
	</ol>
{/if}
</div>
<div>


	<h2>Array:</h2>
{#if elements.length === 0}
	<p>array vazio!</p>
{:else}
	<p>{JSON.stringify(elements, null, 1)}</p>
{/if}
</div>
	



</div>

<style>
	div{box-sizing:border-box; padding:20px}
	.flex{display:flex}
	.flex div{flex:1}
	p{background:#eee; padding:20px;border:1px solid #ccc;}
</style>
