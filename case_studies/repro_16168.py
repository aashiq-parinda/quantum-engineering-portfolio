import sys
sys.path.insert(0, "/Volumes/Exty/CrackingTheQuantum/qiskit")

from qiskit.circuit.library.arithmetic.multipliers.multiplier import MultiplierGate

print("Creating MultiplierGate(1, 1)...")
mg = MultiplierGate(num_state_qubits=1, num_result_qubits=1)
print(f"MultiplierGate(1, 1) num_qubits: {mg.num_qubits}")

try:
    dec = mg.decompose()
    print(f"Decomposed circuit num_qubits: {dec.num_qubits}")
    print("Decompose successful!")
except Exception as e:
    print(f"Decompose failed with error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
