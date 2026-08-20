# 🔬 Open Source Case Study: Qiskit Issue #16168 & PR #16394

## 📌 Overview & Problem Statement

* **Target Ecosystem**: [Qiskit SDK](https://github.com/Qiskit/qiskit)
* **Component**: `qiskit.circuit.library.arithmetic.multipliers.multiplier.MultiplierGate`
* **Issue Tracked**: [Issue #16168](https://github.com/Qiskit/qiskit/issues/16168)
* **Upstream Resolution**: [PR #16394](https://github.com/Qiskit/qiskit/pull/16394) (`commit d89a84bd74`)

---

## 🔍 Bug Analysis & Root Cause

### 1. Expected Behavior
`MultiplierGate(num_state_qubits, num_result_qubits)` allows defining a quantum arithmetic multiplier circuit on two input state registers of size $n$ (`num_state_qubits`) with an output register of size $r$ (`num_result_qubits`, where $r \le 2n$).
When decomposing the gate (`.decompose()`), the resulting sub-circuit should respect the user-defined `num_result_qubits` dimension:

$$\text{Total Qubits} = 2 \times n + r$$

### 2. Actual Behavior / Root Cause
In `qiskit/circuit/library/arithmetic/multipliers/multiplier.py`:
```python
# Before Fix:
self.definition = multiplier_qft_r17(self.num_state_qubits)
```
The constructor called `multiplier_qft_r17` with only the `num_state_qubits` parameter, causing `multiplier_qft_r17` to default to $r = 2n$ result qubits. 
Consequently, whenever a user specified a truncated result register ($r < 2n$), the gate definition allocated $4n$ qubits instead of $2n + r$, causing dimension mismatches and errors during decomposition.

---

## 🛠️ Reproduction & Test Scripts

### Minimal Reproduction (`repro_16168.py`)
```python
from qiskit.circuit.library.arithmetic.multipliers.multiplier import MultiplierGate

# Create multiplier with 1 state qubit and 1 result qubit (Total expected: 2*1 + 1 = 3 qubits)
mg = MultiplierGate(num_state_qubits=1, num_result_qubits=1)
print(f"MultiplierGate(1, 1) num_qubits: {mg.num_qubits}")

# Decompose gate definition
dec = mg.decompose()
print(f"Decomposed circuit num_qubits: {dec.num_qubits}")
assert dec.num_qubits == mg.num_qubits, "Decomposition qubit count mismatch!"
```

---

## 💡 The Upstream Fix

The fix passed the explicit `num_result_qubits` through to the synthesis constructor:

```diff
--- a/qiskit/circuit/library/arithmetic/multipliers/multiplier.py
+++ b/qiskit/circuit/library/arithmetic/multipliers/multiplier.py
@@ -198,4 +198,4 @@ class MultiplierGate(Gate):
         # This particular decomposition does not use any ancilla qubits.
         # Note that the transpiler may choose a different decomposition
         # based on the number of ancilla qubits available.
-        self.definition = multiplier_qft_r17(self.num_state_qubits)
+        self.definition = multiplier_qft_r17(self.num_state_qubits, self.num_result_qubits)
```

Added comprehensive test matrix in `test/python/circuit/library/test_multipliers.py`:
```python
def test_multiplier_gate_decompose_with_custom_result_qubits(self):
    """Test MultiplierGate.decompose() with non-default num_result_qubits."""
    cases = ((1, 1), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5))
    for num_state_qubits, num_result_qubits in cases:
        gate = MultiplierGate(num_state_qubits, num_result_qubits)
        self.assertEqual(gate.num_qubits, 2 * num_state_qubits + num_result_qubits)
        self.assertEqual(gate.definition.num_qubits, gate.num_qubits)
```

---

## 📈 Impact
* Restored compatibility for truncated modular arithmetic in quantum algorithms (e.g., Shor's modular exponentiation and resource-constrained arithmetic circuits).
* Ensured high-level synthesis (HLS) passes correctly propagate custom register widths through transpiler passes.
