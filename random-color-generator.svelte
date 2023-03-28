<script>
	const hex = (d) => Number(d).toString(16).padStart(2, '0')
	const rnd = () => Math.floor(Math.random() * 256)
	let color = hex(rnd()) + hex(rnd()) + hex(rnd())
	const gen = () =>	color = hex(rnd()) + hex(rnd()) + hex(rnd())
</script>

<style>
	.color{display:inline-block; padding:24px; border-radius:50px; vertical-align: middle;}
	.text{display:inline-block; font-size:24px; vertical-align: middle;}
	button{display:block; margin-top:24px}
</style>

<h1>Random Color Generator</h1>
<span class="color" style="background:#{color}"></span>
<span class="text" >#{color}</span>
<button on:click={gen}>Random!</button>
