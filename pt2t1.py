import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 0.006  # Growth rate
M = 10**13  # Carrying capacity
N0 = 10**9  # Initial tumor cell population
h = 0.001  # Step size
t_max = 1200  # Maximum time
time = np.arange(0, t_max, h)  # Time array

# Gompertz model implementation
def gompertz_growth(N, t, k, M):
    return k * N * np.log(M / N)

# Initialize variables
N = np.zeros_like(time)
N[0] = N0

# Simulate growth using Euler's method
for i in range(1, len(time)):
    N[i] = N[i - 1] + h * gompertz_growth(N[i - 1], time[i - 1], k, M)
    if abs(N[i] - M) < 1:  # Steady-state check
        break

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time[:i + 1], N[:i + 1], label="Tumor Growth")
plt.axhline(y=M, color='r', linestyle='--', label="Carrying Capacity (M)")
plt.xlabel("Time (t)")
plt.ylabel("Number of Cells (N)")
plt.title("Tumor Growth Simulation (Gompertz Model)")
plt.legend()
plt.grid()
plt.show()

# Time to reach steady state
time_to_steady_state = time[i]
N_final = N[i]
time_to_steady_state, N_final
