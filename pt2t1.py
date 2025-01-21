import numpy as np
import matplotlib.pyplot as plt
import math

# Gompertz model implementation
def gompertz_growth(N, k, M):
    return k * N * np.log(M / N)

def simulate_graph(M):
    # time_gradient_decrease = None

    steady_state = M * 0.99

    # Parameters
    k = 0.006  # Growth rate
    N0 = 10**9  # Initial tumor cell population
    h = 0.001  # Step size
    t_max = 1200  # Maximum time
    time = np.arange(0, t_max, h)  # Time array

    # Initialize variables
    N = np.zeros_like(time)
    N[0] = N0
    N_steady = None
    T_steady = None
    state_reach=False

    N_steady6 = None
    T_steady6 = None
    state_reach6=False

    # Simulate growth using Euler's method
    for i in range(1, len(time)):
        dN_dt =  gompertz_growth(N[i - 1], k, M)
        N[i] = N[i - 1] + h * dN_dt

        if N[i] > steady_state * (1 - math.exp(-1)) and not state_reach6:
            T_steady6 = time[i]
            N_steady6 = N[i]
            state_reach6 = True
        
        if N[i] > steady_state and not state_reach:  
            T_steady = time[i]
            N_steady = N[i]
            state_reach = True


        if i == len(time) and N_steady == None:
            print("Warning: Maximum time reached without full convergence.")
            N_steady = 0
            T_steady = 0
            N_steady6 = 0
            T_steady6 = 0

    return N_steady, T_steady, time, N, N_steady6, T_steady6, i


M_vals = [10**12, 10**13, 10**14]

for M in M_vals:
    N_steady, T_steady, time, N, N_steady6, T_steady6, i = simulate_graph(M)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(time[:i + 1], N[:i + 1], label="Tumor Growth")
    
    plt.axhline(y=M, color='y', linestyle='--', label="Carrying Capacity (M)")
    plt.axhline(y=N_steady, color='r', linestyle='-', label="99% of Carrying Capacity")
    plt.axvline(x=T_steady, color='b', linestyle=":", label="Steady State")
    plt.text(
        T_steady, 
        plt.ylim()[1] * 0.8,  # Position slightly below the top of the plot
        f"{T_steady:.2f}", 
        color='b', 
        fontsize=10, 
        ha='right', 
        va='center'
    )

    plt.axvline(x=T_steady6, color='m', linestyle=":", label="Inflection Point (63.21%)")
    plt.text(
        T_steady6, 
        plt.ylim()[1] * 0.4,  # Position slightly below the top of the plot
        f"{T_steady6:.2f}", 
        color='m', 
        fontsize=10, 
        ha='right', 
        va='center'
    )

    plt.xlabel("Time (t)")
    plt.ylabel("Number of Cells (N)")
    plt.title("Tumor Growth Simulation (Gompertz Model)")
    plt.legend()
    plt.grid()
    plt.show()
