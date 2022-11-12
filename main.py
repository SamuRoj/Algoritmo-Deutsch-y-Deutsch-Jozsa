import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Ejercicios de QiskitWorkshop
# Ejercicio No 1 a) |01>
print("Ejercicio Ket |01>")
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Ejercicio No 2 b) |100>

print("Ejercicio Ket |100>")
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(3, 3)
circuit.x(0)
circuit.barrier()
circuit.measure([0, 1, 2], [2, 1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Ejercicio No 3 c) (H Tensor I) |00>

print("Ejercicio (H Tensor I) |00>")
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.i(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()
