# Implementación del algoritmo de Deustch y Deutsch-Jozsa

Archivo de Python que contiene las implementaciones de los algoritmos de Deutsch y Deutsch-Jozsa.

## Para Empezar

### Prerequisitos

Lenguaje de programación Python, Idle o ejecución del programa desde terminal, además es necesario contar con las librerías de Qiskit, Qiskit.visualization y matplotlib.

### Instalación y Ejecución

Descarga de los archivos Functions.py, FunctionsJozsa.py, Deutsch.py, DeutschJozsa.py y Tests.py en un mismo directorio.

## Ejecución de Pruebas

### Archivo Deutsch.py


El archivo se divide en dos partes: 


Primero ejecuta el archivo Functions.py y realiza las pruebas de cada una de las funciones que se utilizan para el algoritmo de Deutsch, para este caso son funciones de la forma f: {0,1} -> {0,1}, entre ellas se encuentran 4 posibilidades y se hacen pruebas con cada una de estas.


Lo segundo que ejecuta es el algoritmo de Deutsch usando las funciones mencionadas anteriormente para determinar si la función usada en el circuito es balanceada o constante. La respuesta a esta pregunta se da antes de la impresión de cada uno de los circuitos que aplican el algoritmo de Deutsch.


### Archivo Deutsch-Jozsa


Este archivo se divide igual que el archivo Deutsch.py, solo que en este caso hay un cambio en las funciones que se implementan, las funciones son f: {0,1}^n -> {0,1}, con n = 4, el dominio de la función son las cadenas de bits de longitud 4 y su rango es el conjunto {0,1}, al igual que el algoritmo de Deutsch se debe determinar si las funciones dadas son constantes o balanceadas.


Primero se realizaron pruebas con algunos bits de longitud 4 para observar la funcionalidad de cada una de las funciones que se aplicaron al ejecutar el archivo FunctionsJozsa.py y luego se determina con ayuda del algoritmo de Deutsch-Jozsa si la función es balanceada o constante.


En el archivo FunctionsJozsa.py se encuentran funciones auxiliares como `DecToBinary` que se encarga de convertir un número decimal a binario, `buildMatrix` que se encarga de construir la matriz de acuerdo a la función que se solicite y por último `printMatrix` que imprime una matriz con formato.


### Archivo Tests.py


Este archivo se ejecutan los archivos Deutsch.py y DeutschJozsa.py, este se encarga de realizar las pruebas unitarias y verifica si las respuestas que retornan los programas son correctas o no, si las respuestas son correctas se debe obtener el siguiente resultado.


```
Ran 1 test in 45.336s
OK
```

**Nota:** Puede salir este "error" durante la ejecución:

```
PendingDeprecationWarning: The qiskit.Aer entry point will be deprecated in a future release and subsequently removed. Instead you should use this directly from the root of the qiskit-aer package simulator = Aer.get_backend('qasm_simulator')
```

Es solo una advertencia para realizar un cambio en el código pero no afectará en ninguna parte los resultados que se obtengan del experimento.

### Explicación de resultados y ecuaciones

La explicación de los resultados y sus respectivas ecuaciones se encuentran en el archivo `Informe Deutsch y Deutsch-Jozsa Samuel Rojas.docx` que se debe descargar y abrir con un editor de texto.

## Realizado con

* [Pycharm] (https://www.jetbrains.com/pycharm/) The Python IDE for Professional Developers

## Autor

* **Samuel Rojas** [SamuRoj](https://github.com/SamuRoj)
