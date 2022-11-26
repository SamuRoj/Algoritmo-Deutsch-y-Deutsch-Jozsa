import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


# Función que determina si la función ingresada es balanceada o constante
def balanced_constant(counts):
    if '0' in counts.keys():
        print("La función es constante")
    else:
        print("La función es balanceada")

# Ejecución de las pruebas con cada una de las funciones para determinar si es constante o balanceada
def main():
    print("Verificación de si la función dada es balanceada o constante")
    print()
    print("Pruebas con el algoritmo de Deutsch")
    print()

    # Primera Función
    print("Función No 1: 0 -> 0, 1 -> 0")
    print()
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)
    circuit.x(1)
    circuit.barrier()
    circuit.h(0)
    circuit.h(1)
    circuit.barrier()
    circuit.i(0)
    circuit.i(1)
    circuit.barrier()
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    balanced_constant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    # Segunda Función
    print("Función No 2: 0 -> 0, 1 -> 1")
    print()
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)
    circuit.x(1)
    circuit.barrier()
    circuit.h(0)
    circuit.h(1)
    circuit.barrier()
    circuit.cx(0, 1)
    circuit.barrier()
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    balanced_constant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    # Tercera Función
    print("Función No 3: 0 -> 1, 1 -> 0")
    print()
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)
    circuit.x(1)
    circuit.barrier()
    circuit.h(0)
    circuit.h(1)
    circuit.barrier()
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    circuit.barrier()
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    balanced_constant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()

    # Cuarta Función
    print("Función No 4: 0 -> 1, 1 -> 1")
    print()
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)
    circuit.x(1)
    circuit.barrier()
    circuit.h(0)
    circuit.h(1)
    circuit.barrier()
    circuit.x(1)
    circuit.barrier()
    circuit.h(0)
    circuit.barrier()
    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    balanced_constant(counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    main()
