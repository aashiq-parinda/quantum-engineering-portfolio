import sys
sys.path.insert(0, "/Volumes/Exty/CrackingTheQuantum/qiskit")

from qiskit.synthesis.arithmetic.multipliers.rg_qft_multiplier import multiplier_qft_r17

print("Testing multiplier_qft_r17(1, 1)...")
try:
    qc = multiplier_qft_r17(1, 1)
    print(f"qc.num_qubits = {qc.num_qubits}")
    print(f"qubits: {qc.qubits}")
except Exception as e:
    print(f"Error: {e}")
