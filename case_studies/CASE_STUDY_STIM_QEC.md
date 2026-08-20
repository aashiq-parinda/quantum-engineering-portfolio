# 🛡️ Open Source Case Study: Stim, Surface Codes & High-Performance Stabilizer Simulation

## 📌 Overview & Ecosystem Context

* **Target Ecosystem**: [Stim (Google Quantum AI)](https://github.com/quantumlib/Stim) / [PyMatching](https://github.com/oscarhiggott/PyMatching)
* **Core Mechanisms**: Gottesman-Knill Stabilizer Tableau, Detector Error Models (`DEM`), Minimum-Weight Perfect Matching (`MWPM`)
* **Direct Repository Mapping**: [`quantum-error-correction`](https://github.com/aashiq-parinda/quantum-error-correction)

---

## 🔍 Technical Analysis: Surface Code Syndromes & Fault Tolerance

### 1. Quantum Error Correction with CSS Stabilizers
In Calderbank-Shor-Steane (CSS) surface codes, quantum information is encoded into non-local degrees of freedom defined by the simultaneous $+1$ eigenspace of commuting Pauli operators:

$$\mathcal{S} = \langle S_{X,1}, \dots, S_{X,m}, S_{Z,1}, \dots, S_{Z,k} \rangle, \quad [S_i, S_j] = 0$$

### 2. Error Detection via Commutation Relations
When a physical Pauli error $E \in \{X, Y, Z\}$ strikes a data qubit:
$$S_i (E |\psi\rangle) = (-1)^{\delta_{i}} E (S_i |\psi\rangle) = (-1)^{\delta_{i}} E |\psi\rangle$$
* If $S_i$ and $E$ commute: eigenvalue is $+1$ (no defect).
* If $S_i$ and $E$ anti-commute: eigenvalue is $-1$ (syndrome defect flag).

### 3. Decoding & Recovery
Syndrome defects form endpoints of error chains in the dual lattice graph. Stim extracts detector events across rounds, and graph matching decoders (e.g. MWPM in PyMatching or Union-Find) match pairs of defects with minimal physical path weight to apply recovery operations $R = E^\dagger$.

---

## 🛠️ Verification Script

Executable verification available in [`verify_surface_code_syndrome.py`](./verify_surface_code_syndrome.py):
```bash
python3 verify_surface_code_syndrome.py
```
Output:
```
=================================================================
🛡️ Stim / Fault-Tolerance: Surface Code Syndrome Extraction & Decoding
=================================================================

--- Case: Single Bit-Flip on Central Data Qubit (Q4) ---
  Injected Errors: {4: 'X'}
  Extracted Syndrome Defects: ['S_Z1', 'S_Z2']
  Decoder Recovery Operation:  {4: 'X'}
  Status: ✅ 100% Fidelity Recovery Verified

--- Case: Composite Error (X on Q0, Z on Q4) ---
  Injected Errors: {0: 'X', 4: 'Z'}
  Extracted Syndrome Defects: ['S_Z1', 'S_X1', 'S_X2']
  Decoder Recovery Operation:  {0: 'X', 4: 'Z'}
  Status: ✅ 100% Fidelity Recovery Verified
```

---

## 🚀 Impact & Cross-Portfolio Value
Provides a rigorous bridge between theoretical quantum fault-tolerance codes (Surface Codes, Steane, Shor [[9,1,3]]) and high-throughput production stabilizer engines used in experimental quantum hardware labs.
