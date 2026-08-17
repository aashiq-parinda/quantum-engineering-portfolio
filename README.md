# ⚛️ Applied Quantum Computing, Hybrid Orchestration & HPC Simulation Portfolio

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests: 131/131 Passed](https://img.shields.io/badge/tests-131%2F131%20passing-brightgreen)](#-repository-index)

Welcome to the master portfolio repository consolidating 8 research-grade & Solutions Architecture repositories built from mathematical first principles. This suite covers the full spectrum of modern quantum engineering — from statevector gate propagators and open-system density matrix channels to Quantum Machine Learning, VQE Quantum Chemistry, Surface Code Error Correction, Shor's RSA Factoring Algorithm, HPC GPU-accelerated tensor contraction engines, and Enterprise Hybrid Quantum-Classical Pipeline Orchestration.

---

## 🗺️ Master Repository Index

| Stage | Domain | Repository | Status | Key Features & Math |
| :---: | :--- | :--- | :---: | :--- |
| **FDE** | **Hybrid Orchestration** | [`quantum-hybrid-orchestration`](https://github.com/aashiq-parinda/quantum-hybrid-orchestration) | ✅ `9/9 tests` | Solutions Architect / FDE Evidence: Preprocessing $\rightarrow$ Quantum Dispatch $\rightarrow$ Postprocessing loop, dual-backend smart router (Sim vs QPU), job queue state machine, cost/latency benchmarking, VQE & QAOA adaptability, Executive Translation Blog. |
| **01** | **Quantum Foundations** | [`quantum-computing-foundations`](https://github.com/aashiq-parinda/quantum-computing-foundations) | ✅ `28/28 tests` | Statevector $\mathbb{C}^{2^N}$, unitary gates, Grover's search $O(\sqrt{N})$, QFT, QPE, Deutsch-Jozsa, Teleportation. |
| **02** | **Open Systems & Noise** | [`quantum-simulation-noise`](https://github.com/aashiq-parinda/quantum-simulation-noise) | ✅ `12/12 tests` | Density matrices $\rho$, Kraus channels $\sum K_i \rho K_i^\dagger$, $T_1/T_2$ relaxation, Zero Noise Extrapolation (ZNE). |
| **03** | **Quantum Machine Learning** | [`quantum-machine-learning`](https://github.com/aashiq-parinda/quantum-machine-learning) | ✅ `9/9 tests` | Parameterized Quantum Circuits (PQC), exact Parameter-Shift gradients $\frac{\partial E}{\partial \theta_i}$, QNN, QSVC, Barren Plateaus. |
| **04** | **Quantum Chemistry** | [`quantum-chemistry-sim`](https://github.com/aashiq-parinda/quantum-chemistry-sim) | ✅ `14/14 tests` | Second Quantization $a_i^\dagger, a_i$, Jordan-Wigner transform, molecular $H_2$ & $LiH$ Hamiltonians, VQE & UCCSD. |
| **05** | **Quantum Error Correction** | [`quantum-error-correction`](https://github.com/aashiq-parinda/quantum-error-correction) | ✅ `20/20 tests` | Repetition code, 9-qubit Shor code, 7-qubit Steane CSS code, Distance-$d$ Surface Code, MWPM decoder. |
| **06** | **Shor's Factoring Algorithm** | [`quantum-shor-factoring`](https://github.com/aashiq-parinda/quantum-shor-factoring) | ✅ `20/20 tests` | Modular exponentiation $x^a \bmod N$, QFT period finding, continued fractions rational approximation, RSA factoring. |
| **07** | **HPC & GPU Acceleration** | [`quantum-hpc-acceleration`](https://github.com/aashiq-parinda/quantum-hpc-acceleration) | ✅ `19/19 tests` | Tensor-sliced $O(2^N)$ statevector contraction, memory profiling up to 30 qubits, vectorized NumPy `einsum` batching. |

---

## 🧬 Curriculum & Architecture Roadmap

```mermaid
flowchart TD
    subgraph Core ["Stage 1: Core Quantum Mechanics"]
        A["Statevectors C^(2^N) & Gates"] --> B["Quantum Oracles & Grover Search"]
        B --> C["QFT & Quantum Phase Estimation"]
    end

    subgraph Noise ["Stage 2: Real Hardware Physics"]
        C --> D["Density Matrices & Kraus Operators"]
        D --> E["T1/T2 Decoherence & ZNE Mitigation"]
    end

    subgraph Applications ["Stage 3: Applied Quantum Software"]
        E --> F["Quantum Machine Learning (PQC, QNN, QSVC)"]
        E --> G["Quantum Chemistry (VQE, Jordan-Wigner, UCCSD)"]
    end

    subgraph Architecture ["Stage 4: Solutions Architecture & Production FDE"]
        F --> H["Quantum Hybrid Orchestration (Smart Router, Queueing, Benchmarks)"]
        G --> H
        H --> I["Multi-Workload Pipeline Adaptability (VQE Chemistry + QAOA Max-Cut)"]
        I --> J["Executive Translation Whitepaper (Cost & Latency ROI)"]
    end

    subgraph FaultTolerance ["Stage 5: Scale & Fault Tolerance"]
        J --> K["Quantum Error Correction & Surface Codes"]
        J --> L["Shor's RSA Factoring & Order Finding"]
        K --> M["HPC Statevector & Tensor-Sliced Engine O(2^N)"]
        L --> M
    end

    style Core fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff
    style Noise fill:#1f2937,stroke:#10b981,stroke-width:2px,color:#fff
    style Applications fill:#1f2937,stroke:#8b5cf6,stroke-width:2px,color:#fff
    style Architecture fill:#1f2937,stroke:#ec4899,stroke-width:2px,color:#fff
    style FaultTolerance fill:#1f2937,stroke:#f59e0b,stroke-width:2px,color:#fff
```

---

## 📊 Comprehensive Algorithmic Purpose Matrix

| Category | Algorithm / Feature | Real-World Application & Benefit |
| :--- | :--- | :--- |
| **Hybrid Orchestration** | **Smart Backend Router** | Automatically routes jobs to Simulators vs Cloud QPUs based on depth, cost, & queue latency. |
| **Hybrid Orchestration** | **Pipeline Adaptability (VQE + QAOA)** | Solves both molecular chemistry and graph optimization through a single unified pipeline interface. |
| **Executive Translation** | **Quantum ROI & Cost Analysis** | Proves 99.78% cloud cost reduction by running inner variational loops on local simulators. |
| **Foundations** | **Grover's Search** | Quadratic speedup $O(\sqrt{N})$ for database search & SAT solving. |
| **Foundations** | **Quantum Phase Estimation (QPE)** | Subroutine for Shor's algorithm, energy estimation, & eigenvalue computation. |
| **Noise & Mitigation** | **Zero Noise Extrapolation (ZNE)** | Error mitigation on noisy NISQ hardware without additional physical qubits. |
| **Quantum ML** | **Parameter-Shift Rule** | Computes exact analytical gradients on real quantum hardware without backprop. |
| **Quantum ML** | **Quantum Support Vector Classifier (QSVC)** | Non-linear classification by mapping data into $2^N$-dimensional Hilbert space. |
| **Quantum Chemistry** | **Variational Quantum Eigensolver (VQE)** | Computes molecular ground-state energy for EV battery design & catalysts. |
| **Error Correction** | **Distance-$d$ Surface Code** | Leading 2D lattice candidate for fault-tolerant, million-qubit quantum computers. |
| **Cryptography** | **Shor's Factoring Algorithm** | Polynomial time factoring of RSA integers via QFT period finding. |
| **HPC Simulator** | **Tensor-Sliced Contraction** | Reduces gate application time from $O(4^N)$ to $O(2^N)$ using index slicing. |

---

## ⚡ Quickstart & Local Verification

Clone any repository directly to inspect the source, run unit tests, or execute interactive console demonstrations:

```bash
# Example: Clone and run Quantum Hybrid Orchestration
git clone https://github.com/aashiq-parinda/quantum-hybrid-orchestration.git
cd quantum-hybrid-orchestration
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Run full pytest test suite
pytest tests/ -v

# Run interactive system demonstration
python example.py
```

---

## 📄 License

All repositories in this portfolio are open-source under the [MIT License](LICENSE).
