import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the model
def malware_spread(y, t, beta, N):
    I = y[0]
    dI_dt = beta * I * (N - I)
    return [dI_dt]

# Parameters
N = 1000 # total number of computers
beta = 0.01 # transmission rate
I0 = 1 # initial number of infected computers
t = np.linspace(0, 100, 1000) # time points

# Solve the differential equation
y0 = [I0]
sol = odeint(malware_spread, y0, t, args=(beta, N))

# Extract the number of infected computers over time
I = sol[:, 0]

# Plot the results
plt.plot(t, I)
plt.xlabel('Time')
plt.ylabel('Number of Infected Computers')
plt.title('Malware Spread Simulation')
plt.show()
