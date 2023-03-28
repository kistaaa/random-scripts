<script>
	import { afterUpdate } from 'svelte';
	let svgData = {width: 700, height:300};
	let pointsData = {number: 10, xRandom:false, yRandom:true};
	let points = [];
	let linePoints = stringPoints();
	let mouseX = 0;
	let mouseY = 0;

	function stringPoints() {
		let str = '';
		for(let i=0; i<points.length; i++) {
			str += points[i].x + ',' + points[i].y + ' ';
		}
		console.log(str)
		return str
	}
	
	function map(val, low1, high1, low2, high2) {
    return Math.floor(low2 + (high2 - low2) * (val - low1) / (high1 - low1));
}
	
	function rand(min, max) {
		min = Math.ceil(min);
		max = Math.floor(max);
		return Math.floor(Math.random() * (max - min)) + min;
	}
	
	function generate(){
		if(points.length > pointsData.number) points.length = pointsData.number;
			
		for(let i=0; i<=pointsData.number; i++) {
			let x = i, y = i, xmax = pointsData.number, ymax = pointsData.number;
			if(pointsData.xRandom) {x = rand(0, 100); xmax = 100}
			if(pointsData.yRandom) {y = rand(0, 100); ymax = 100}
			x = map(x, 0, xmax, 0, svgData.width);
			y = map(y, ymax, 0, 0, svgData.height);
			
			if(!points[i])
				{ points.push( {x: x, y: y} )
				}
			else
				{ points[i].x = x; points[i].y = y; 
				
				}
		}
		
		points = points;
		linePoints = stringPoints();
	}
	
	afterUpdate(() => {
		generate()
	});

	
</script>
<h1>Svg Graph</h1>
<h2>
	Svg:
</h2>
Width: <input type="number" bind:value={svgData.width}>
Height: <input type="number" bind:value={svgData.height}>
<h2>
	Points:
</h2>
Number of Points: <input type="number" bind:value={pointsData.number}>
<label for="rx">Random X: </label><input type="checkbox" id="rx" bind:checked={pointsData.xRandom}>
<label for="ry">Random Y: </label><input type="checkbox" id="ry" bind:checked={pointsData.yRandom}>
<button on:click={generate}>Regenerate</button>

<svg width="{svgData.width}" height="{svgData.height}" >
	<polyline points={linePoints} />
	{#each points as point, i}
		<circle cx={points[i].x} cy={points[i].y} r="10" id={i}/>
	{/each}
</svg>

<style>
	svg {display:block; border:1px solid #ccc}
	label {display:inline}
	polyline {stroke:black; stroke-width:2; fill:none}
	circle:hover {fill:orange; r:14}
</style>
