  #Tasks 1 
def simulate(days, beta, gamma, N=1000, I0=1, immune=0):
 
    # return a list of tuples (day, S, I, R)
    S = N - I0 - immune
    I = I0
    R = immune
    #results=[(day,S,I,R)]
    results = [(0, S, I, R)]

    for day in range(1, days + 1):
        new_infected = beta * S * I / N
        new_recovered = gamma * I
        S, I, R = S - new_infected, I + new_infected - new_recovered, R + new_recovered
        results.append((day, S, I, R))
    return results
    
print(simulate(1, 0.3, 0.1))