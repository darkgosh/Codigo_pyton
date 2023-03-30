# Python leer archivo JSON – Cómo cargar JSON desde un archivo y procesar dumps

Aprenderás:

* La importancia del formato JSON.
* Su estructura y tipos de datos.
* Cómo JSON y los diccionarios funcionan juntos en Python.
* Cómo trabajar con el módulo incorporado json de Python.
* Cómo convertir cadenas de caracteres en formato JSON a objetos de Python y viceversa.
* Cómo usar loads() y dumps().
* Cómo indentar cadenas de caracteres en formato JSON automáticamente.
* Cómo leer archivos JSON en Python con load().
* Cómo escribir archivos JSON en Python con dump().
* ¡Y más!


 Introducción: ¿Qué es JSON?

JSON = Java Script Object Notation

El formato JSON fue inspirado por la sintaxis de JavaScript (un lenguaje de programación usado para desarrollo web). Pero desde entonces se ha convertido en un formato de datos independiente del lenguaje de programación. La mayoría de los lenguajes de programación que usamos hoy en día pueden generar y leer JSON.

## Importancia y usos de JSON
JSON es un formato usado para almacenar o representar datos. Sus usos más frecuentes incluyen desarrollo web y creación de archivos de configuración.

Veamos por qué:

* Desarrollo web: JSON se usa comúnmente en aplicaciones web para enviar información desde el servidor al cliente o desde el cliente al servidor.
image-65 <image src="/Imagenes/image-65.png" alt="imagen">
Archivos de configuración: el formato JSON también es usado para almacenar configuraciones y ajustes. Por ejemplo, para crear una aplicación para Chrome, debes incluir un archivo JSON llamado manifest.json para especificar el nombre de la aplicación, su descripción, versión actual y otras propiedades.
image-99
🔸 Estructura y formato JSON
Ahora que ya sabes cómo se usa el formato JSON, veamos su estructura básica con un ejemplo que representa una orden de pizza:

'''javascript
{ 
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": null,
		"correo": "janedoe@email.com"
	}
}
'''
Ejemplo de archivo JSON
💡 Dato: no se incluyen acentos en los ejemplos para evitar cualquier incompatibilidad entre JSON y caracteres especiales.

Estas son las características principales del formato JSON:

Posee una secuencia de pares clave-valor rodeados por un par de llaves {}.
Cada clave se asocia a un valor con este formato:
"clave": <valor> 
💡 Dato: Los valores que incluyen comillas simples deben estar rodeados por comillas dobles.

Los pares clave-valor deben estar separados por una coma. Solo el último par no debe estar seguido de una coma.
{
	"tamano": "mediana", # ¡Coma!
	"precio": 15.67
}
💡 Dato: Generalmente estructuramos los archivos JSON con distintos niveles de indentación para que la información sea más fácil de leer. En este artículo, aprenderás cómo agregar la indentación de forma automática con Python.

Tipos de datos JSON: claves y valores
Los archivos JSON tienen reglas específicas que determinan los tipos de datos que son válidos para las claves y para los valores.

Las claves deben ser cadenas de caracteres.
Los valores pueden ser cadenas de caracteres, números, arreglos, valores Booleanos (true/ false), null, o un objeto JSON.
Según la documentación de Python:

Las claves en los pares clave/valor de JSON siempre son de tipo str. Cuando se convierte un diccionario a JSON, todas las claves del diccionario se convierten a cadenas de caracteres.
Texto original en inglés:

Keys in key/value pairs of JSON are always of the type str. When a dictionary is converted into JSON, all the keys of the dictionary are coerced to strings.
Guía de estilo
Según la guía de estilo de Google para el formato JSON:

Siempre debes escoger nombre descriptivos.
Los arreglos (arrays) deberían tener claves escritas en plural. Otras claves deberían ser escritas en singular. Por ejemplo: usar  "ordenes" en lugar de "orden" si su valor correspondiente es un arreglo (array).
No debería haber comentarios en objetos JSON.
🔹 JSON vs. diccionarios de Python
JSON y los diccionarios pueden parecer muy similares inicialmente (visualmente) pero en realidad son muy diferentes. Veamos cómo están relacionados y cómo se complementan para lograr que Python sea una herramienta poderosa para trabajar con archivos JSON.
JSON es un formato de archivo usado para representar y almacenar información mientras que un diccionario de Python es una estructura de datos (objeto) que se almacena en la memoria del dispositivo mientras se ejecuta el programa de Python.
Cómo JSON y los diccionarios de Python funcionan juntos
image-11
Cuando trabajamos con archivos JSON en Python, no podemos simplemente leerlos y usar la información en nuestro programa directamente.

Esto se debe a que el archivo completo estaría representado como una sola cadena de caracteres y no podríamos acceder a los pares clave-valor de forma individual.

A menos que...

Usemos los pares clave-valor del archivo JSON para crear un diccionario de Python que podamos usar en nuestro programa para leer, usar y modificar la información si es necesario.

Esta es la relación principal entre JSON y los diccionarios de Python. JSON es la representación en forma de cadena de caracteres de la información y los diccionarios son las estructuras de datos en memoria que se crean cuando se ejecuta el programa.

Genial. Ahora que ya sabes más sobre JSON, comencemos a ver los aspectos prácticos de cómo puedes trabajar con JSON en Python.

🔸 El módulo JSON
Afortunadamente para nosotros, Python tiene un módulo incorporado llamado json. Se instala automáticamente cuando instalas Python e incluye funciones que te ayudarán a trabajar con archivos y cadenas de caracteres JSON.

Usaremos este módulo en los siguientes ejemplos.

Cómo importar el módulo JSON
Para usar json en nuestro programa, solo necesitamos escribir una sentencia de importación al inicio del archivo.

De esta forma:

image-73
Con esta línea podrás tener acceso a las funciones definidas en el módulo. Usaremos varias de ellas en los ejemplos.

💡 Dato: si escribes esta sentencia de importación necesitarás usar la siguiente sintaxis para llamar a la función definida en el módulo json:

image-13
🔹 Python y cadenas de caracteres JSON
Para mostrarte cómo funcionan algunas de las funciones más importantes del módulo json, usaremos una cadena de caracteres con varias líneas en formato JSON.

Cadena de caracteres JSON
Usaremos la siguiente cadena de caracteres en los ejemplos. Es una cadena de caracteres de varias líneas en Python que cumple las reglas del formato JSON.

datos_JSON =  """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""
JSON String
Para definir una cadena de caracteres de varias líneas en Python, usamos tres comillas dobles.
Luego, asignamos la cadena de caracteres a la variable datos_JSON.
💡 Dato: la Guía de Estilo de Python recomienda usar comillas dobles para definir  cadenas de caracteres con tres comillas.

De una cadena de caracteres JSON a un diccionario de Python
Usaremos una cadena de caracteres con el formato JSON para crear un diccionario de Python al cual podemos tener acceso para usarlo y modificarlo en nuestro programa.

Para hacerlo, usaremos la función loads() del módulo json, pasando la cadena de caracteres como argumento.

Esta es la sintaxis básica:

image-14
Este es el código:

# Importar el módulo
import json

# Cadena de caracteres en el formato JSON
datos_JSON =  """
{
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": "455-344-234",
		"correo": "janedoe@email.com"
	}
}
"""

# Convertir cadena de caracteres JSON a un diccionario
datos_diccionario = json.loads(datos_JSON)
Veamos esta línea:

datos_diccionario = json.loads(datos_JSON)
json.loads(datos_JSON) crea un diccionario con los pares clave-valor de la cadena de caracteres JSON y retorna este diccionario nuevo.
Luego, el diccionario retornado se asigna a la variable datos_diccionario.
¡Genial! Si mostramos el diccionario, vemos el siguiente resultado:

{'tamano': 'mediana', 'precio': 15.67, 'toppings': ['champinones', 'queso extra', 'pepperoni', 'albahaca'], 'cliente': {'nombre': 'Jane Doe', 'telefono': '455-344-234', 'correo': 'janedoe@email.com'}}
El diccionario contiene la información de la cadena de caracteres en formato JSON. Cada par clave-valor fue añadido exitosamente.

Ahora veamos lo que sucede cuando intentamos acceder a los valores de los pares clave-valor con la misma sintaxis que usaríamos para acceder a los valores de un diccionario de Python:

print(data_dict["tamano"])
print(data_dict["precio"])
print(data_dict["toppings"])
print(data_dict["cliente"])
El resultado es:

mediana
15.67
['champinones', 'queso extra', 'pepperoni', 'albahaca']
{'nombre': 'Jane Doe', 'telefono': '455-344-234', 'correo': 'janedoe@email.com'}
Exactamente lo que esperábamos. Cada clave puede ser usada para acceder a su valor correspondiente.

💡 Dato: podemos trabajar con este diccionario de la misma forma que trabajamos con cualquier diccionario de Python. Por ejemplo, podemos llamar a métodos de diccionarios, agregar, actualizar y eliminar pares clave-valor y mucho más. Incluso podemos usarlo en un ciclo for.

JSON a Python: conversión de tipos de datos
Cuando uses loads() para crear un diccionario en Python a partir de una cadena de caracteres JSON, notarás que algunos valores serán convertidos a sus valores y tipos de datos correspondientes en Python.

Esta tabla presentada en la documentación de Python para el módulo json resume la correspondencia entre los tipos de datos y valores JSON y los tipos de datos y valores en Python:

image-6
Tabla presentada en la documentación oficial del módulo json
💡 Dato: la misma tabla de conversión aplica cuando trabajamos archivos JSON en lugar de cadenas de caracteres JSON.

Diccionario de Python a cadena de caracteres JSON
Ahora ya sabes cómo crear un diccionario de Python a partir de una cadena de caracteres en formato JSON.

Pero a veces necesitarás hacer exactamente lo opuesto, crear una cadena de caracteres en formato JSON a partir de un objeto (por ejemplo, un diccionario) para mostrarla, guardarla, o usarla como una cadena de caracteres en el programa.

Para hacerlo, puedes usar la función dumps del módulo json, pasando el objeto como argumento:

image-15
💡 Dato: esta función retorna una cadena de caracteres.

Este es un ejemplo en el cual convertimos un diccionario de Python cliente a una cadena de caracteres en formato JSON y lo asignamos a una variable:

# Diccionario Python
cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

# Obtener una cadena de caracteres JSON
cliente_JSON = json.dumps(cliente)
Veamos esta línea:

cliente_JSON = json.dumps(cliente)
json.dumps(cliente) crea y retorna una cadena de caracteres con todos los pares clave-valor del diccionario en formato JSON.
Luego, esta cadena de caracteres se asigna a la variable cliente_JSON.
Si mostramos esta cadena de caracteres, vemos el siguiente resultado:

{"nombre": "Nora", "edad": 56, "id": "45355", "color_ojos": "verdes", "usa_lentes": false}
💡 Dato: Nota que el último valor (false) cambió. En el diccionario de Python, este valor era False pero en JSON, el valor equivalente es false. Esto nos ayuda a confirmar que el diccionario original se representa como una cadena de caracteres en el formato JSON.

Si verificamos el tipo de dato de esta variable, vemos:

<class 'str'>
Así que el valor retornado por esta función definitivamente es una cadena de caracteres.

Python a JSON: conversión de tipo de datos
Cuando convertimos un diccionario a una cadena de caracteres JSON, también ocurre un proceso de conversión de tipo de datos. Esta tabla de la documentación de Python describe los valores correspondientes:

image-10
Tabla de la documentación oficial del módulo JSON
Cómo mostrar JSON con indentación
Si usamos la función dumps y luego mostramos la cadena de caracteres que obtuvimos en el ejemplo anterior, veremos lo siguiente:

{"nombre": "Nora", "edad": 56, "id": "45355", "color_ojos": "verdes", "usa_lentes": false}
Pero esta presentación no es muy fácil de leer, ¿cierto?

Podemos lograr que sea más fácil de leer si añadimos indentación.

Para hacerlo manualmente, solo necesitamos pasar un segundo argumento para especificar el número de espacios que queremos usar para indentar la cadena de caracteres JSON:

image-16
💡 Dato: el segundo argumento debe ser un número entero no negativo (el número de espacios) o una cadena de caracteres. Si es una cadena de caracteres (como "\t"), esa cadena de caracteres se usará para indentar cada nivel (fuente).

Ahora, si llamamos a dumps con este segundo argumento:

cliente_JSON = json.dumps(cliente, indent=4)
El resultado de mostrar cliente_JSON es:

{
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": false
}
¡Es genial! ¿no? Ahora nuestra cadena de caracteres se presenta en un formato fácil de leer. Esto es muy útil cuando comenzamos a trabajar con archivos para almacenar información.

Cómo ordenar las claves
También puedes ordenar las claves en orden alfabético si lo necesitas. Para hacerlo, solo debes escribir el nombre del parámetro sort_keys y pasar el valor True:

image-17
💡 Dato: el valor de sort_keys es False por defecto si no se pasa un valor como argumento.

Por ejemplo:

cliente_JSON = json.dumps(cliente, sort_keys=True)
Retorna esta cadena de caracteres con las claves ordenadas en orden alfabético:

{"color_ojos": "verdes", "edad": 56, "id": "45355", "nombre": "Nora", "usa_lentes": false}
Cómo ordenar las claves alfabéticamente e indentar (simultáneamente)
Para generar una cadena de caracteres JSON que esté ordenada alfabéticamente e indentada, solo necesitamos pasar los dos argumentos:

image-104
En este caso, el resultado es:

{
    "color_ojos": "verdes", 
    "edad": 56, 
    "id": "45355", 
    "nombre": "Nora", 
    "usa_lentes": false
}
💡 Dato: puedes pasar los dos últimos argumentos en cualquier orden pero el objeto debe ser el primer argumento de la lista.

Genial. Ahora sabes cómo trabajar con cadenas de caracteres JSON, así que veamos cómo puedes trabajar con archivos JSON en tus programas de Python.

🔸 JSON y archivos
Generalmente, el formato JSON se usa para almacenar información en archivos, así que Python nos da las herramientas que necesitamos para leer este tipo de archivos en nuestro programa, trabajar con sus datos y agregar nueva información.

💡 Dato: un archivo JSON tiene la extensión .json:

image-18
Veamos cómo puedes trabajar con archivos .json en Python.

Cómo leer archivos JSON en Python
Digamos que creamos un archivo ordenes.json con esta información que representa dos órdenes de una tienda de pizzas:

{
	"ordenes": [ 
		{
			"tamano": "mediana",
			"precio": 15.67,
			"toppings": ["champinones", "pepperoni", "albahaca"],
			"queso_extra": false,
			"delivery": true,
			"cliente": {
				"nombre": "Jane Doe",
				"telefono": null,
				"correo": "janedoe@email.com"
			}
		},
		{
			"tamano": "pequena",
			"precio": 6.54,
			"toppings": null,
			"queso_extra": true,
			"delivery": false,
			"cliente": {
				"nombre": "Foo Jones",
				"telefono": "556-342-452",
				"correo": null
			}
		}
	]
}
ordenes.json
Por favor toma unos segundos para analizar la estructura de este archivo JSON.

Aquí tenemos algunos datos importante:

Nota los tipos de datos de los valores, la indentación y la estructura general del archivo.
El valor de la clave principal "ordenes" es un arreglo de objetos JSON (es arreglo será representado como una lista en Python). Cada objeto JSON contiene la información de una órden de pizza.
Si quieremos leer este archivo en Python, solo debemos usar un administrador de contexto (una sentencia with):

image-19
💡 Dato: en la sintaxis anterior, puedes asignar cualquier nombre a archivo. Esta es una variable que podemos usar dentro de la sentencia with para referirnos al objeto archivo.

La línea de código clave en esta sintaxis es:

datos = json.load(archivo)
json.load(archivo) crea y retorna un diccionario nuevo de Python con los pares clave-valor del archivo JSON.
Luego, este diccionario se asigna a la variable datos.
💡 Dato: Nota que estamos usando load() en lugar de loads(). Esta es una función diferente del módulo json. Aprenderás más sobre sus diferencias al final de este artículo.

Una vez que tenemos el contenido del archivo JSON almacenado en la variable datos como un diccionario, podemos usarlo como lo necesitemos.

Ejemplos
Por ejemplo, si escribimos:

print(len(datos["ordenes"]))
El resultado es 2 porque el valor de la clave principal "orders" es una lista con dos elementos.

También podemos usar las claves para acceder a sus valores correspondientes. Esto es lo generalmente hacemos cuando trabajamos con archivos JSON.

Por ejemplo, para acceder a los toppings de la primera orden, escribiríamos:

datos["ordenes"][0]["toppings"]
Primero seleccionamos la clave principal "ordenes".
Luego, seleccionamos el primer elemento de la lista (índice 0).
Finalmente, seleccionamos el valor que corresponde a la clave "toppings".
Puedes ver este "camino" de forma gráfica en el siguiente diagrama:

image-20
Si mostramos este valor, el resultado es:

['champinones', 'pepperoni', 'albahaca']
Exactamente lo que esperábamos. Solo debes adentrarte en la estructura del diccionario usando las claves y los índices necesarios. Puedes usar el archivo JSON original o la cadena de caracteres JSON original como referencia visual. De esta forma, puedes acceder, modificar o eliminar cualquier valor.

💡 Dato: Recuerda que estamos trabajando con un diccionario nuevo. Los cambios que hagamos a este diccionario no afectarán al archivo JSON. Para actualizar el contenido del archivo, debemos escribir al archivo.

Cómo escribir a un archivo JSON
Ahora veamos cómo puedes escribir a un archivo JSON.

La primera línea de la sentencia with es muy similar. El único cambio es que ahora debemos abrir el archivo JSON en modo de escritura 'w' (write) para poder modificar el archivo.

image-22
💡 Dato: si el archivo no existe en el directorio de trabajo actual (en la carpeta), se creará automáticamente. Al usar el modo 'w', se reemplazará todo el contenido del archivo si ya existe.

Hay dos formas alternativas de escribir a un archivo JSON en el cuerpo de la sentencia with:

dump
dumps
Veámos estas alternativas en detalle.

Primera alternativa: dump

Esta es una función que toma dos argumentos:

El objeto que será almacenado en formato JSON (por ejemplo, un diccionario).
El archivo en el cual será almacenado (un objeto archivo).
image-23
Digamos que una tienda de pizza quiere eliminar "cliente" de cada orden en el archivo JSON y crear un nuevo archivo JSON llamado ordenes_nuevo.json con esta nueva versión.

Podemos hacerlo con el siguiente código:

# Abrir el archivo ordenes.json
with open("ordenes.json") as archivo:
    # Cargar su contenido y crear un diccionario
    datos = json.load(archivo)

    # Eliminar el par clave-valor "cliente" de cada orden
    for orden in datos["ordenes"]:
        del orden["cliente"]

# Abir (o crear) un archivo ordenes_nuevo.json 
# y guardar la nueva versión de la información
with open("ordenes_nuevo.json", 'w') as archivo_nuevo:
    json.dump(datos, archivo_nuevo)
Esta era la versión original de la información en el archivo ordenes.json. Nota que hay un par clave-valor para "cliente" en cada orden:

{
	"ordenes": [ 
		{
			"tamano": "mediana",
			"precio": 15.67,
			"toppings": ["champinones", "pepperoni", "albahaca"],
			"queso_extra": false,
			"delivery": true,
			"cliente": {
				"nombre": "Jane Doe",
				"telefono": null,
				"correo": "janedoe@email.com"
			}
		},
		{
			"tamano": "pequena",
			"precio": 6.54,
			"toppings": null,
			"queso_extra": true,
			"delivery": false,
			"cliente": {
				"nombre": "Foo Jones",
				"telefono": "556-342-452",
				"correo": null
			}
		}
	]
}
Esta es la nueva versión del archivo ordenes_nuevo.json:

{"ordenes": [{"tamano": "mediana", "precio": 15.67, "toppings": ["champinones", "pepperoni", "albahaca"], "queso_extra": false, "delivery": true}, {"tamano": "pequena", "precio": 6.54, "toppings": null, "queso_extra": true, "delivery": false}]}
ordenes_nuevo.json
Si analizas este resultado en detalle, notarás que el par clave-valor que corresponde a "clients" fue eliminado de todas las órdenes.

Sin embargo, falta algo en este archivo, ¿cierto?

Por favor, tómate un momento para pensar... ¿Qué puede ser?

¡Por supuesto! Indentación.

El archivo no se parece a un archivo JSON porque no tiene indentación, pero podemos arreglar esto rápidamente si pasamos el argumento indentation=4 a dump().

image-24
Ahora este es el contenido del archivo:

{
	"ordenes": [ 
		{
			"tamano": "mediana",
			"precio": 15.67,
			"toppings": ["champinones", "pepperoni", "albahaca"],
			"queso_extra": false,
			"delivery": true,
		},
		{
			"tamano": "pequena",
			"precio": 6.54,
			"toppings": null,
			"queso_extra": true,
			"delivery": false,
		}
	]
}
ordenes_nuevo.json
¡Qué diferencia! Así es exactamente cómo esperaríamos que se presentara un archivo JSON.

Ahora sabes cómo leer y escribir a un archivo JSON con load() y dump(). Veamos las diferencias entre estas funciones y las funciones que usamos para trabajar con las cadenas de caracteres en formato JSON.

🔹 load() vs. loads()
Esta table resume las diferencias claves entre estas dos funciones:

image-25
💡 Dato: Piensa en loads() como "load string" (cargar cadena de caracteres). Esto te ayudará a identificar la función que se usa para cada propósito.

🔸 dump() vs. dumps()
Aquí tenemos una tabla que resume las diferencias claves entre estas dos funciones:

image-26
💡 Dato: Piensa en dumps() como "dump string" (dump cadena de caracteres) y esto te ayudará a identificar la función que se usa para cada propósito.

🔹 Terminología importante en JSON
Finalmente, hay dos términos importantes que debes conocer para trabajar con JSON:

Serialización: el proceso de convertir un objeto a una cadena de caracteres en formato JSON.
Deserialización: convertir una cadena de caracteres JSON a un objeto.
🔸 En resumen
JSON (JavaScript Object Notation) es un formato usado para representar y almacenar información.
Se usa comúnmente para transferir información a través de la web y para almacenar ajustes y configuración.
Los archivos JSON tienen una extensión .json.
Puedes convertir cadenas de caracteres en formato JSON a objetos de Python y viceversa.
Puedes leer archivos JSON y crear objetos de Python a partir de sus pares clave-valor.
Puedes agregar información a archivos JSON para almacenar el contenido de objetos de Python en formato JSON.




