<!-- HEADINGS -->

# my tittle h1
## my tittle h2
### my tittle h3
#### my tittle h4
##### my tittle h5
###### my tittle h6

<!-- Italic -->
This is a *italic* Text

<!-- Strong -->
this is an **Strong** text


<!-- StrikeTrough -->
<!-- (para poner tilde ALT+ 126) '~' -->
Este es un ~~TEXTO~~ tachado

<!-- Listas -->
* apple
* Orange
* etc.

<!-- Listas Numeradas -->
1.
2.
3.


<!-- URLs -->
[youtube.com](www.youtube.com "Custom Title")


<!-- Citas -->
> this a quote

<!-- linea divisoria  -->
---


___

<!-- Linea de codigo -->

`
 print("Hello World")
`


<!-- Varias lineas de codigo de codigo -->

```javascript
<script>
		function actualizarBarra() {
			var total = document.querySelectorAll('input[type="checkbox"]').length;
			var completadas = document.querySelectorAll('input[type="checkbox"]:checked').length;
			var porcentaje = (completadas / total) * 100;
			document.getElementById("barra").style.width = porcentaje + "%";
			document.getElementById("porcentaje").innerHTML = Math.round(porcentaje) + "%";
		}
	</script>
```

```HTML
<h1>hello world</h1>
```
<!-- tablas -->

|Titulo 1|Titulo 2  |Titulo 3 |
|  ----- | :-----:  |--------:|
| Col 1  | col 2    |  col 3  |
|dato 1  |dato 2    |dato 3   |


<!-- vinvular imagen desde URL -->
![Visual estudio code logo](data:image/png;base64,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)




<!-- vinvular imagen desde local  -->
![Visual estudio code logo](imagenes/VSC_ico.png)


<!-- Tagear usuarios  -->
 @revidana :thumbsup: :cloud:

<!-- insertar emogis -->

[Lista de Emogis para Github y Gist](https://gist.github.com/rxaviers/7360908)

|:thumbsup: |:cloud: |:smile: |
|-----------|--------|--------|
|:sunny:    |:cat:   |:tiger: |
|-----------|--------|--------|



<!-- Github Markdown cheat sheet -->
[Github Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet "Custom Title")




[Markdown, Curso Práctico para principiantes y desarrolladores](https://www.youtube.com/watch?v=oxaH9CFpeEE)