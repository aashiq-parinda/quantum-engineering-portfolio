# 🔬 Open Source Case Study: Mitiq Zero-Noise Extrapolation (ZNE) & Richardson Inference

## 📌 Overview & Ecosystem Context

* **Target Ecosystem**: [Mitiq (Unitary Fund)](https://github.com/unitaryfund/mitiq)
* **Core Modules**: `mitiq.zne.inference.RichardsonFactory` & `mitiq.zne.scaling.folding`
* **Direct Repository Mapping**: [`quantum-zne-reproduction`](https://github.com/aashiq-parinda/quantum-zne-reproduction) & [`quantum-simulation-noise`](https://github.com/aashiq-parinda/quantum-simulation-noise)

---

## 🔍 Technical Analysis: Vandermonde Polynomial vs Analytical Lagrange Extrapolation

### 1. The Core Problem in ZNE
Zero-Noise Extrapolation mitigates expectation value degradation by artificially scaling the physical noise parameter $\lambda \to c_j \lambda$ (e.g., via unitary gate folding $U \to U (U^\dagger U)^n$) and evaluating $\langle O \rangle_{c_j}$. 

The goal is to infer $\langle O \rangle_0 = \lim_{c \to 0} \langle O \rangle_c$.

### 2. Implementation Differences & Comparative Study
* **Mitiq's Approach (`PolyFactory`)**:
  Fits an $n-1$ degree polynomial across noise scale factors $\{c_1, \dots, c_n\}$ using least-squares or Vandermonde matrix inversion.
  $$\mathbf{V} \mathbf{a} = \mathbf{E} \implies E(0) = a_0$$
* **Temme et al. 2017 Approach (Lagrange Multipliers)**:
  Uses exact analytical weights $\gamma_j$ derived from the Lagrange interpolating polynomial evaluated at $c=0$:
  $$\gamma_j = \prod_{l \neq j} \frac{c_l}{c_l - c_j}, \quad \sum_{j=1}^n \gamma_j = 1$$
  $$\langle O \rangle_{\text{mitigated}} = \sum_{j=1}^n \gamma_j \langle O \rangle_{c_j} = \langle O \rangle_0 + \mathcal{O}(c^{n})$$

### 3. Numerical Stability Insights
* For standard scale factors ($n \le 5$, e.g., $c \in \{1, 1.5, 2.0, 2.5, 3.0\}$), both methods agree to machine precision ($\approx 10^{-16}$).
* For high-order extrapolation ($n > 8$), Vandermonde condition numbers $\kappa(\mathbf{V})$ grow exponentially ($\sim \mathcal{O}(e^n)$). The explicit Lagrange formulation avoids matrix inversion singularities.

---

## 🛠️ Verification Script

Executable verification available in [`verify_zne_extrapolation.py`](./verify_zne_extrapolation.py):
```bash
python3 verify_zne_extrapolation.py
```
Output:
```
=================================================================
🔬 Mitiq ZNE & Temme 2017 Richardson Extrapolation Benchmark
=================================================================
Target Ground Truth E(0): 0.850000
Noise Scale factors (c):  [1.0, 1.5, 2.0, 2.5, 3.0]
Noisy Expectation values: [0.744, 0.700375, 0.662, 0.628125, 0.598]

Analytical Lagrange Weights (sum=1.000000):
  c = 1.0 -> gamma = +15.000000
  c = 1.5 -> gamma = -40.000000
  c = 2.0 -> gamma = +45.000000
  c = 2.5 -> gamma = -24.000000
  c = 3.0 -> gamma = +5.000000

[Result] Lagrange Richardson Extrapolated E(0): 0.850000 (error: 9.99e-16)
[Result] Polynomial Fit Extrapolated E(0):     0.850000 (error: 7.77e-16)
✅ Verification Successful: Both methods achieve high-precision error mitigation.
```

---

## 🚀 Impact & Cross-Portfolio Value
This case study benchmarks Mitiq's industry-standard open-source error mitigation library against the foundational peer-reviewed derivations from Temme et al. (PRL 2017), linking software engineering practices with physical error modeling.
