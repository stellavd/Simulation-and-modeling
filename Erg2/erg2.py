import numpy as np
import matplotlib.pyplot as plt

def simulate_malware_spread(N, beta, time_steps):
    I = 1  # Initial number of infected computers
    I_values = [I]  # Track the num of infected over time
    
    for t in range(1, time_steps):
        dI = beta * I * (N - I)  # Differential equation
        I += dI  # Update the number of infected
        I_values.append(I)
    
    return I_values

# Parameters
N = 1000
beta = 0.001  # Example transmission rate
time_steps = 100

# Run simulation
I_values = simulate_malware_spread(N, beta, time_steps)

# Plot results
plt.plot(range(time_steps), I_values, label=f'β={beta}')
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Computers')
plt.title('Malware Spread Simulation')
plt.legend()
plt.show()
