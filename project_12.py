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



#task2
def peak_day(results):
    day, S, I, R = max(results, key=lambda row: row[2])
    return day, I

most_sick = simulate(300, 0.3, 0.1)
day_peak, patient_of_peak = peak_day(most_sick)
print(f"The day: {day_peak}, sick people: {patient_of_peak:.2f}, final R: {most_sick[-1][3]:.2f}")
    


#Tasks 3 Kermack and McKendrick threshold theorem
for beta in [0.05, 0.08, 0.1, 0.15, 0.2, 0.3]:
    day_peak, patient_of_peak = peak_day(simulate(300, beta, 0.1))
    grows = "grows" if patient_of_peak > 1 else "does NOT grow"
    print(f"beta={beta:<5} R0={beta / 0.1:.1f}  peak I={patient_of_peak:7.2f} (day {day_peak:3})  -> {grows}")
    

#Task 4: herd immunity
day, i = peak_day(simulate(300, 0.3, 0.1, immune=700))
print(f"immune=700 -> peak I={i:.2f} (day {day})")

for im in [300, 400, 500, 600,700]:
    day_peak, patient_of_peak = peak_day(simulate(300, 0.3, 0.1, immune=im))
    stops = "stops" if patient_of_peak <= 1 else "grows"
    print(f"immune={im:<4} peak I={patient_of_peak:7.2f} (day {day_peak:3})  -> {stops}")

# Find the smallest value that stops the disease
for im in range(0, 1000):
    day_peak, patient_of_peak = peak_day(simulate(300, 0.3, 0.1, immune=im))
    if patient_of_peak <= 1:
        print(f"Smallest immune that stops the disease: {im}")
        break

# Think and explain

beta = 0.3
gamma = 0.1
I0 = 1
N = 1000

R0 = beta / gamma

def disease_grow():
    for im in range(0, N - I0 + 1):
        S = N - I0 - im
        R_eff = R0 * S / N

        if R_eff <= 1:
            return im, R_eff

immune_min, R_eff = disease_grow()

print("Smallest immune:", immune_min)
print("Effective reproduction number:", R_eff)

# Compare with theoretical threshold
threshold = N * (1 - 1 / R0)

print("Theoretical threshold:", threshold)
print("Difference:", threshold - immune_min)
