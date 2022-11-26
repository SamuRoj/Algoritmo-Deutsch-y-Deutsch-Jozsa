import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Función que se encarga de convertir un número decimal a binario
def DecToBinary(n):
    string = ""
    while n != 0:
        string += str(n % 2)
        n = n // 2
    string = string[::-1]
    while len(string) < 5:
        string = "0" + string
    return string

# Función que construye las matrices de acuerdo a la función que se está implementando
def buildMatrix(cond0 = False, cond1 = False, cond2 = False, cond3 = False):
    matrix = []
    if cond0:
        matrix = [["1" if i == j else "0" for i in range(32)] for j in range(32)]
    elif cond1:
        matrix = [["1" if (DecToBinary(i)[0] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if DecToBinary(i)[0] == "1" and DecToBinary(i)[4] == "0" and i == j:
                    matrix[i + 1][j] = "1"
                elif DecToBinary(i)[0] == "1" and DecToBinary(i)[4] == "1" and i == j:
                    matrix[i - 1][j] = "1"
    elif cond2:
        matrix = [["1" if (DecToBinary(i)[1] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if DecToBinary(i)[1] == "1" and DecToBinary(i)[4] == "0" and i == j:
                    matrix[i + 1][j] = "1"
                elif DecToBinary(i)[1] == "1" and DecToBinary(i)[4] == "1" and i == j:
                    matrix[i - 1][j] = "1"
    elif cond3:
        matrix = [["1" if (DecToBinary(i)[2] != "1" and i == j) else "0" for i in range(32)] for j in range(32)]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if DecToBinary(i)[2] == "1" and DecToBinary(i)[4] == "0" and i == j:
                    matrix[i + 1][j] = "1"
                elif DecToBinary(i)[2] == "1" and DecToBinary(i)[4] == "1" and i == j:
                    matrix[i - 1][j] = "1"
    return matrix

# Función que imprime con formato a una matriz
def printMatrix(matrix):
    for i in matrix:
        print(" ".join(i))
    print()

# Ejecución del programa principal realizando pruebas con algunos qubits para verificar que la función no es constante
def main():
    # Primera Función
    print("Función constante todos los qubits a 0")
    print()
    print("Matriz")
    printMatrix(buildMatrix(True))
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)
    circuit.barrier()
    circuit.i(0)
    circuit.i(1)
    circuit.i(2)
    circuit.i(3)
    circuit.i(4)
    circuit.barrier()
    circuit.measure([0,1,2,3,4], [4,3,2,1,0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    # Segunda Función
    print("Función Balanceada No 1 Cambia si el bit No 1 es 1")
    print()
    print("Matriz")
    printMatrix(buildMatrix(False, True))
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)
    circuit.x(0)
    circuit.barrier()
    circuit.cx(0, 4)
    circuit.barrier()
    circuit.measure([0,1,2,3,4], [4,3,2,1,0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    # Tercera Función
    print("Función Balanceada No 2 Cambia si el bit No 2 es 1")
    print()
    print("Matriz")
    printMatrix(buildMatrix(False, False, True))
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)
    circuit.x(1)
    circuit.barrier()
    circuit.cx(1, 4)
    circuit.barrier()
    circuit.measure([0,1,2,3,4], [4,3,2,1,0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    # Cuarta Función
    print("Función Balanceada No 3 Cambia si el bit No 3 es 1")
    print()
    print("Matriz")
    printMatrix(buildMatrix(False, False, False, True))
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(5, 5)
    circuit.x(2)
    circuit.barrier()
    circuit.cx(2, 4)
    circuit.barrier()
    circuit.measure([0,1,2,3,4], [4,3,2,1,0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    print(circuit)
    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    main()
