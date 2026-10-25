# Reflection

We all read about the Kermack–McKendrick model together before starting the code.
We all worked together on `README.md` and `REFLECTION.md`.

## Who did what

### YOBARA DANGMO AXEL JUNIOR — Task 1: the simulation

I was responsible for Task 1: writing the function
`simulate(days, beta, gamma, N=1000, I0=1, immune=0)`.

First, the function sets the values of day 0: `S = N - I0 - immune`, `I = I0` and
`R = immune`, and stores them in a list `results`. Then a `for` loop goes through each day,
from 1 to `days`. For each day, it calculates `new_infected = beta * S * I / N` and
`new_recovered = gamma * I` with today's values, then updates S, I and R in one line:
`S, I, R = S - new_infected, I + new_infected - new_recovered, R + new_recovered`.
It adds the tuple `(day, S, I, R)` to the list and returns the list at the end.
I checked it with the tests: `simulate(1, 0.3, 0.1)` gives
`[(0, 999, 1, 0), (1, 998.7003, 1.1997, 0.1)]` and `len(simulate(300, 0.3, 0.1))` gives 301.
I learned that the three values must be updated at the same time. If we update S first on its
own line, the formula for I uses the new S instead of today's S, and the result is wrong.

### [Name 2] — Task 2: the peak of the epidemic

I was responsible for Task 2: finding the peak of the epidemic with `beta = 0.3`
and `gamma = 0.1`.

I wrote a function `peak_day(results)` that finds the day with the
most sick people. It uses `max` with `key=lambda row: row[2]`, because each row of
the simulation is a tuple `(day, S, I, R)` and the number of sick people I is at
index 2. The function returns the peak day and the number of sick people on that
day. Then I ran `simulate(300, 0.3, 0.1)` and displayed the results:
the peak is on day 41 with about 312.73 sick people, and the final value of R is
about 946.74 (read from the last row, `results[-1][3]`).
I learned to use `max` with a `key`, to unpack a tuple into
several variables, and to put code in a function so that it can be reused. Without
`key`, `max` would compare the days instead of the sick people.

### [Name 3] — Task 3: different values of beta

I was responsible for Task 3: finding for which `beta` the number of sick people stops growing.

I used a `for` loop that goes through the values of `beta` 0.05, 0.08, 0.1, 0.15, 0.2 and 0.3,
while keeping `gamma` at 0.1. For each value, the program simulates 300 days and uses `peak_day`
to find the day when the number of sick people is the highest. Then it checks whether this peak
is bigger than 1 (the first sick person at day 0). For each case, it displays `beta`, `R0`, the
peak and the day of the peak. The result: the disease does not grow for `beta = 0.05`, `0.08` and
`0.1` (`R0 <= 1`), and it grows for `0.15`, `0.2` and `0.3`.
I learned to reuse functions written by the others (`simulate` and `peak_day`) inside a loop,
and to write a short condition with `"grows" if ... else "does NOT grow"`.
I also understood the Kermack–McKendrick threshold: the disease spreads only when `R0 > 1`.

### [Name 4] — Task 4: herd immunity

I was responsible for Task 4: finding how many immune people are needed to stop the disease.

**What I did.** First, I simulated the spread of the disease in the town of 1000 people
for 300 days, with a transmission rate of 0.3 and a recovery rate of 0.1. I started with 700
immune people to observe the peak number of sick people: the peak is on day 0, so the disease
never spreads. Then, I tested different numbers of immune people: 300, 400, 500, 600 and 700.
I used a loop to compare the results and see whether the disease continued to spread or stopped.
Finally, I used another loop to find the smallest number of immune people needed to stop the
disease. The loop stops when the peak number of sick people is less than or equal to 1.
The answer is 666.

**Difficulties I encountered.** One difficulty was understanding how to find the minimum
number of immune people needed to stop the disease: testing only 300, 400, 500… does not give
the exact value. I also had to understand how to use loops and conditions to test different
values automatically.

**How I overcame the difficulties.** I broke the problem into smaller steps. I first tested
different values of immunity, then used an `if` condition to check whether the disease stopped.
Finally, I tested every value from 0 to 999 and used `break` to stop the loop as soon as the
smallest value was found.

### BIENVENU — Think and explain

I was responsible for the *Think and explain* part: checking the result of Task 4 with the
formula.

I wrote a function `disease_grow()` that tests each number of immune people. For each one, it
calculates `S = N - I0 - im` and `R_eff = R0 * S / N`, and returns the first value where
`R_eff <= 1`. It returns 666, the same answer as the simulation. Then I compared it with the
formula `N * (1 - 1 / R0) = 666.67`. The difference of 0.67 comes from the one sick person at
day 0, who is not in S.
I learned that a simple formula can confirm the result of a simulation.

### ALL THE MUMBER OF GROUP — Extra: the lockdown

We were responsible for the Extra: adding a lockdown from day 20.

We wrote a separate function, `simulate_lockdown`, so that `simulate` and the tests of Tasks 1
to 4 do not change. It is the same as `simulate`, but each day it chooses the value of the
transmission rate: `b = beta` before day 20, and `b = beta * factor` after (`factor = 0.5`).
Then we compared the two simulations with `peak_day`: with the lockdown, the peak goes from
312.73 people on day 41 to 83.10 people on day 57 (73% lower and 16 days later), and the final R
goes from 946.74 to 615.31.
We learned how to change a parameter during a simulation with an `if` condition.

## One problem we had: adding the lockdown without breaking the other tasks

For the Extra, we needed a smaller `beta` from day 20. We had two problems:

1. **The other tasks could break.** If we changed the function `simulate` to add the lockdown,
   the results of Tasks 1 to 4 and the tests (`simulate(1, 0.3, 0.1)`, `len(...) == 301`)
   could change, because all these tasks use `simulate`.
2. **`beta` could be divided again and again.** If we write `beta = beta * 0.5` inside the loop,
   this line runs **every day** after day 20. So `beta` is divided by 2 on day 21, again on
   day 22, again on day 23… and becomes almost 0. The lockdown would get stronger every day,
   which is not what the task asks.

At first we did not know how to put a lockdown in the SIR model, so we used sources.

## How we fixed it

**We used sources to understand how to model a lockdown.** All of them do the same thing:
a lockdown means fewer contacts between people, so it **reduces the transmission rate `beta`**.

- **Law et al. (2020)** use an SIR model where the transmission rate changes over time. In their
  study of COVID-19 in Malaysia, transmission dropped as soon as the lockdown started. This gave
  us the idea: `beta` changes from a given day (day 20).
- **The UCLouvain Python course** simulates an SIR model in Python and says that a lockdown reduces
  the value of `beta`. Its code divides `beta` by 2 or by 4. This is why we used `factor = 0.5`.
- **Cadoni (2020)** shows that social distancing, which reduces the transmission rate, lowers the
  peak and the total number of sick people. We used it to check that our results make sense.

**Then we wrote the code in two steps:**

1. We created a **separate function**, `simulate_lockdown`. The function `simulate` does not
   change, so Tasks 1 to 4 and the tests still give the same results.
2. We **never change `beta` itself**. Each day, we use a new variable `b`:

```python
if day > lockdown_day:
    b = beta * factor      # lockdown: 0.3 * 0.5 = 0.15
else:
    b = beta               # before the lockdown: 0.3
new_infected = b * S * I / N
```

Now `b` is exactly 0.15 every day after day 20, so `R0 = 0.15 / 0.1 = 1.5`. The peak goes from
312.73 people on day 41 to 83.10 people on day 57, which agrees with the sources: the lockdown
lowers the peak and moves it later.

**What we learned:** before coding something new, it helps to look at how other people did it.
We also learned to add a new feature in a new function instead of changing code that already works.

## Sources

- W. O. Kermack and A. G. McKendrick, *A contribution to the mathematical theory of epidemics*,
  Proceedings of the Royal Society A, 115, 700–721, 1927.
- K. B. Law et al., *Tracking the early depleting transmission dynamics of COVID-19 with a
  time-varying SIR model*, Scientific Reports 10, 2020.
  https://doaj.org/article/7e4b66cf9c174a618a17437128f93686
- *Python for dummies : problème 6* (course, UCLouvain).
  https://perso.uclouvain.be/vincent.legat/documents/epl1104/python6/epidemic.pdf
- M. Cadoni, *How to reduce epidemic peaks keeping under control the time-span of the epidemic*,
  2020. https://arxiv.org/pdf/2004.02189