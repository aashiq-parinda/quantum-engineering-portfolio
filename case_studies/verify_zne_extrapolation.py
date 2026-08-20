"""
Pure Python & NumPy Verification and Benchmark of Zero-Noise Extrapolation (ZNE)
Comparing Mitiq's Polynomial-based RichardsonFactory and Temme et al. 2017 exact Lagrange weights.
Zero external dependencies required (runs in pure standard library Python or NumPy).
"""
import math

def analytical_richardson_weights(scale_factors):
    """Computes exact analytical Lagrange extrapolation coefficients for Richardson ZNE.
    
    gamma_j = prod_{l != j} (c_l / (c_l - c_j))
    """
    n = len(scale_factors)
    gammas = []
    for j in range(n):
        prod = 1.0
        for l in range(n):
            if l != j:
                prod *= scale_factors[l] / (scale_factors[l] - scale_factors[j])
        gammas.append(prod)
    return gammas

def solve_linear_system(matrix, vector):
    """Gaussian elimination to solve M * x = v in pure Python."""
    n = len(vector)
    # Augment matrix
    aug = [matrix[i][:] + [vector[i]] for i in range(n)]
    
    for i in range(n):
        # Pivot
        max_row = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[max_row] = aug[max_row], aug[i]
        pivot = aug[i][i]
        if abs(pivot) < 1e-14:
            raise ValueError("Matrix is singular")
        
        for j in range(i + 1, n + 1):
            aug[i][j] /= pivot
        aug[i][i] = 1.0
        
        for r in range(n):
            if r != i:
                factor = aug[r][i]
                for c in range(i, n + 1):
                    aug[r][c] -= factor * aug[i][c]
                    
    return [aug[i][-1] for i in range(n)]

def polyfit_and_eval_zero(x_vals, y_vals):
    """Fits polynomial of degree (len(x)-1) and returns y-intercept (E(0)) in pure Python."""
    n = len(x_vals)
    # Vandermonde matrix: V[i][j] = x_vals[i] ** j
    v_mat = [[(x_vals[i] ** j) for j in range(n)] for i in range(n)]
    coeffs = solve_linear_system(v_mat, y_vals)
    # coeffs[0] is the constant term E(0)
    return coeffs[0]

def run_benchmarks():
    print("=" * 65)
    print("🔬 Mitiq ZNE & Temme 2017 Richardson Extrapolation Benchmark")
    print("=" * 65)
    
    # Ground truth unmitigated zero-noise value
    E_true = 0.8500
    
    # Noise model: E(c) = E_0 + a1*c + a2*c^2 + a3*c^3
    c_vals = [1.0, 1.5, 2.0, 2.5, 3.0]
    a1, a2, a3 = -0.12, 0.015, -0.001
    
    simulated_expectations = [
        E_true + a1 * c + a2 * (c**2) + a3 * (c**3) for c in c_vals
    ]
    
    print(f"Target Ground Truth E(0): {E_true:.6f}")
    print(f"Noise Scale factors (c):  {c_vals}")
    print(f"Noisy Expectation values: {[round(x, 6) for x in simulated_expectations]}")
    
    # 1. Analytical Lagrange Richardson
    gammas = analytical_richardson_weights(c_vals)
    print(f"\nAnalytical Lagrange Weights (sum={sum(gammas):.6f}):")
    for c, g in zip(c_vals, gammas):
        print(f"  c = {c:.1f} -> gamma = {g:+.6f}")
    
    E_mitigated_lagrange = sum(g * y for g, y in zip(gammas, simulated_expectations))
    print(f"\n[Result] Lagrange Richardson Extrapolated E(0): {E_mitigated_lagrange:.6f}")
    print(f"Error vs Ground Truth: {abs(E_mitigated_lagrange - E_true):.2e}")
    
    # 2. Vandermonde / Polynomial Inversion (Mitiq method)
    E_mitigated_poly = polyfit_and_eval_zero(c_vals, simulated_expectations)
    print(f"[Result] Polynomial Fit Extrapolated E(0):     {E_mitigated_poly:.6f}")
    print(f"Error vs Ground Truth: {abs(E_mitigated_poly - E_true):.2e}")
    
    assert abs(E_mitigated_lagrange - E_true) < 1e-5, "Lagrange Richardson verification failed!"
    assert abs(E_mitigated_poly - E_true) < 1e-5, "Polynomial fit verification failed!"
    print("\n✅ Verification Successful: Both methods achieve high-precision error mitigation.")

if __name__ == "__main__":
    run_benchmarks()
