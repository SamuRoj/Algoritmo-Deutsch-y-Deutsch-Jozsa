import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def DecToBinary(n):
    string = ""
    while n != 0:
        string += str(n % 2)
        n = n // 2
    string = string[::-1]
    while len(string) < 5:
        string = "0" + string
    return string
def BinarytoDec(string):
    n = 0
    for i in range(len(string)):
        if string[i] == "1":
            n += 2 ** int(i)
    return n

def buildMatrix1():
    matrix = [["1" if i == j else "0" for i in range(32)] for j in range(32)]
    return matrix
def buildMatrix2():
    matrix = [["1" if (DecToBinary(i)[0] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if DecToBinary(i)[0] == "1" and DecToBinary(i)[4] == "0" and i == j:
                matrix[i + 1][j] = "1"
            elif DecToBinary(i)[0] == "1" and DecToBinary(i)[4] == "1" and i == j:
                matrix[i - 1][j] = "1"
    return matrix
def buildMatrix3():
    matrix = [["1" if (DecToBinary(i)[1] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if DecToBinary(i)[1] == "1" and DecToBinary(i)[4] == "0" and i == j:
                matrix[i + 1][j] = "1"
            elif DecToBinary(i)[1] == "1" and DecToBinary(i)[4] == "1" and i == j:
                matrix[i - 1][j] = "1"
    return matrix

def buildMatrix4():
    matrix = [["1" if (DecToBinary(i)[2] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if DecToBinary(i)[2] == "1" and DecToBinary(i)[4] == "0" and i == j:
                matrix[i + 1][j] = "1"
            elif DecToBinary(i)[2] == "1" and DecToBinary(i)[4] == "1" and i == j:
                matrix[i - 1][j] = "1"
    return matrix
def printMatrix(matrix):
    for i in matrix:
        print(" ".join(i))
def balanced_constant(counts):
    if '0' in counts.keys():
        print("La función es constante")
    else:
        print("La función es balanceada")

print("Función constante todos los qubits a 0")
print()
print("Matriz")
printMatrix(buildMatrix1())
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.i(2)
circuit.i(3)
circuit.i(4)
circuit.barrier()
circuit.measure([0,1,2,3], [3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
balanced_constant(counts)
print(circuit)
plot_histogram(counts)
plt.show()

print("Función Balanceada No 1 Cambia si el bit No 1 es 1")
print()
print("Matriz")
printMatrix(buildMatrix2())
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.x(0)
circuit.barrier()
circuit.cx(0, 3)
circuit.barrier()
circuit.measure([0,1,2,3], [3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
balanced_constant(counts)
print(circuit)
plot_histogram(counts)
plt.show()

print("Función Balanceada No 2 Cambia si el bit No 2 es 1")
print()
print("Matriz")
printMatrix(buildMatrix3())
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.barrier()
circuit.cx(1, 3)
circuit.barrier()
circuit.measure([0,1,2,3], [3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
balanced_constant(counts)
print(circuit)
plot_histogram(counts)
plt.show()

print("Función Balanceada No 3 Cambia si el bit No 3 es 1")
print()
print("Matriz")
printMatrix(buildMatrix4())
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(5, 5)
circuit.barrier()
circuit.cx(2, 3)
circuit.barrier()
circuit.measure([0,1,2,3], [3,2,1,0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
balanced_constant(counts)
print(circuit)
plot_histogram(counts)
plt.show()