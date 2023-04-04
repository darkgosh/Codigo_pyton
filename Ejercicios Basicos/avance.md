<!DOCTYPE html>
<html>
<head>
	<title>Barra de avance con checkbox</title>
	<script>
		function actualizarBarra() {
			var total = document.querySelectorAll('input[type="checkbox"]').length;
			var completadas = document.querySelectorAll('input[type="checkbox"]:checked').length;
			var porcentaje = (completadas / total) * 100;
			document.getElementById("barra").style.width = porcentaje + "%";
			document.getElementById("porcentaje").innerHTML = Math.round(porcentaje) + "%";
		}
	</script>
	<style>
		#barra {
			background-color: lightblue;
			height: 20px;
			width: 0%;
			transition: width 0.5s;
		}
	</style>
</head>
<body>
	<h1>Barra de avance con checkbox</h1>
	<p>Selecciona las tareas que has completado:</p>
	<input type="checkbox" id="tarea1" name="tarea1" onchange="actualizarBarra()">
	<label for="tarea1">Tarea 1</label><br>
	<input type="checkbox" id="tarea2" name="tarea2" onchange="actualizarBarra()">
	<label for="tarea2">Tarea 2</label><br>
	<input type="checkbox" id="tarea3" name="tarea3" onchange="actualizarBarra()">
	<label for="tarea3">Tarea 3</label><br>
	<input type="checkbox" id="tarea4" name="tarea4" onchange="actualizarBarra()">
	<label for="tarea4">Tarea 4</label><br>
	<input type="checkbox" id="tarea5" name="tarea5" onchange="actualizarBarra()">
	<label for="tarea5">Tarea 5</label><br>
	<br>
	<div id="barra"></div>
	<p>Completado: <span id="porcentaje">0%</span></p>
</body>
</html>
