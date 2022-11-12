# Implementación del algoritmo de Deustch y Deutsch-Jozsa

Archivo de Python que contiene las implementaciones de los algoritmos de Deutsch y Deutsch-Jozsa.

## Para Empezar

### Prerequisitos

Lenguaje de programación Python, Idle o ejecución del programa desde terminal, además es necesario contar con las librerías de Qiskit, Qiskit.visualization y mathplotlib.

### Instalación y Ejecución

Descarga de los archivos Functions.py, Deutsch.py y DeutschJozsa.py.

## Ejecución de Pruebas

### Archivo Functions

El archivo contiene la ejecución de cada una de las funciones {0,1} -> {0,1}.

En este se puede encontrar primeramente una función `printMatrix` que permite imprimir la matriz correspondiente a cada función.

La prueba de cada una de las funciones se realizó con el siguiente formato, primeramente se señala cuál es la función que se está modelando,
luego se imprime la matriz que modela su funcionamiento y por último se imprime el circuito que la implementa y se realiza una prueba con los qubits que pertenecen al espacio (C^4).

Se realiza lo mismo con cada una de las 4 funciones. Al ejecutar el archivo se pueder ver cada uno de sus resultados, se mostrará también una gráfica con el qubit o qubits resultados al finalizar cada uno de los circuitos y realizar la medición.
Además se agrega la implementación de este circuito dentro del computador cuántico de IBM.

`Imágenes`

### Archivo Deutsch

El archivo contiene la ejecución del algoritmo de Deutsch.

En este se realizan las pruebas con las funciones modeladas anteriormente y se determina si la función que se prueba es balanceada o constante para verificar su validez. Al ejecutar el archivo se pueden ver cada uno de sus resultados.

### Archivo Deutsch-Jozsa

El archivo contiene la ejecución las funciones n = 2 que permiten probar el algoritmo de Deutsch-Jozsa.

### Explicación de resultados y ecuaciones

Pendiente

## Realizado con

* [Pycharm] (https://www.jetbrains.com/pycharm/) The Python IDE for Professional Developers

## Autor

* **Samuel Rojas** [SamuRoj](https://github.com/SamuRoj)
