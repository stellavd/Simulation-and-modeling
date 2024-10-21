import numpy as np
import matplotlib.pyplot as plt 
import random

def simulate_malware_spread_with_immunity(N, beta, time_steps, immunity_time):
    states = [0] * N  # all pc healthy
    states[random.randint(0, N-1)] = 1  # ιnfect one random or start
    infection_time = [0] * N  # track how long for 1 to be infected

    infected_count = [1]  # initial number of infected
    immune_count = [0]  # initial number of immune

    for t in range(1, time_steps):
        # attempt to infect others
        for i in range(N):
            if states[i] == 1:  # if computer infected infect others
                for _ in range(int(beta * N)):  
                    target = random.randint(0, N-1)
                    if states[target] == 0:  # only infect healthy 
                        states[target] = 1
                        infection_time[target] = 0  # reset infection timer
        
        # update infection times and manage immunity
        for i in range(N):
            if states[i] == 1:
                infection_time[i] += 1
                if infection_time[i] >= immunity_time:  # time to become immune
                    states[i] = 2

        # record current infected and immune counts
        infected_count.append(states.count(1))
        immune_count.append(states.count(2))

    return infected_count, immune_count

# param
N = 1000
beta = 0.001
time_steps = 100
immunity_time = 10

# run cyberpunk (nope dont the laptop will explode)
infected_count, immune_count = simulate_malware_spread_with_immunity(N, beta, time_steps, immunity_time)

# za plot rezults
plt.plot(range(len(infected_count)), infected_count, label='Infected')  # Use len() to match the data length
plt.plot(range(len(immune_count)), immune_count, label='Immune')
plt.xlabel('Time Steps')
plt.ylabel('Number of Computers')
plt.title('Malware Spread with Immunity')
plt.legend()
plt.show()
