\# SIR model of a disease



\## Where the ideas come from: Kermack and McKendrick



Before writing any code, we read about the work of \*\*W. O. Kermack and A. G. McKendrick\*\*.

In 1927 they published \*"A contribution to the mathematical theory of epidemics"\*, which is the

origin of the SIR model. Without their work, we would not have known how to start this project.

Their ideas helped us in four ways:



1\. \*\*Splitting the town into three groups.\*\* Kermack and McKendrick put each person in one group:

&#x20;  can catch the disease (S), sick (I), or recovered (R). The 2-equation version of their model is

&#x20;  the one we use. Our program is a day-by-day (discrete) version of it.



2\. \*\*The threshold.\*\* Their most important result is that there is a \*\*threshold\*\*: below it, the

&#x20;  disease dies out; above it, there is an epidemic. In our project, this threshold is

&#x20;  `R0 \* S / N = 1`. This idea told us what to look for in Task 3 (which values of `beta` make the

&#x20;  disease grow) and in Task 4 (how many immune people are needed to stop it).



3\. \*\*An epidemic stops before everyone is sick.\*\* They also showed that an epidemic ends

&#x20;  \*\*without infecting the whole population\*\*. Our simulation shows the same thing: in Task 2,

&#x20;  the final value of `R` is about 947, not 1000. About 53 people never get sick, because the

&#x20;  disease runs out of people to infect.



4\. \*\*Quarantine and lockdown.\*\* Brauer (2005) explains that after the SARS epidemic (2002–2003),

&#x20;  researchers added quarantine and isolation to the Kermack–McKendrick model, and that the threshold

&#x20;  and the "epidemic stops before everyone is sick" results are still true. This gave us the idea

&#x20;  for the lockdown in the Extra task: a lockdown simply makes `beta` smaller.



\### Sources



\- F. Brauer, \*The Kermack–McKendrick epidemic model revisited\*, Mathematical Biosciences 198(2),

&#x20; 119–131, 2005. https://www.sciencedirect.com/science/article/abs/pii/S0025556405001331

\- \*SIR Model\* (course notes, MATH 5000, Auburn University).

&#x20; http://webhome.auburn.edu/\~smith01/math5000Fa22/SIRModel01.pdf

\- Video: https://youtu.be/eAHDiT40fkU

\- Video: https://youtu.be/LLjQxWVJwdk

\- W. O. Kermack and A. G. McKendrick, \*A contribution to the mathematical theory of epidemics\*,

&#x20; Proceedings of the Royal Society A, 115, 700–721, 1927.



\## What the program does



The program simulates a disease in a town of `N = 1000` people with the SIR model.

Each person is in one group: \*\*S\*\* (can catch the disease), \*\*I\*\* (sick) or \*\*R\*\* (recovered and safe).



\*\*Task 1.\*\* The function `simulate(days, beta, gamma, N=1000, I0=1, immune=0)` first sets the

values of day 0: `S = N - I0 - immune`, `I = I0`, `R = immune`. It stores them in a list named

`results`. Then a `for` loop goes through each day (`for day in range(1, days + 1)`). For each day,

it calculates `new\_infected` and `new\_recovered` with today's values, updates S, I and R at the

same time, and adds the tuple `(day, S, I, R)` to the list. At the end, the function returns the list.



\*\*Task 2.\*\* We created a second function, `peak\_day`, which takes the output of `simulate` as a

parameter. It uses the `max` function on the list, comparing the rows by their value of `I`. When

it finds the maximum of `I`, it returns the day and the number of sick people on that day.

We use it with `beta = 0.3`, `gamma = 0.1` and 300 days, and we print the final value of `R`.



\*\*Task 3.\*\* We used a `for` loop to go through the different values of `beta`. For each one, we

defined two variables: `day\_peak` (the day with the most sick people) and `patient\_of\_peak` (the

number of sick people on that day). We get them with `peak\_day`, which takes as a parameter

`simulate` with a fixed number of days (300) and a fixed `gamma` (0.1). If the peak stays at 1

(the first sick person), the disease does not grow.



\*\*Task 4.\*\* First we set `immune = 700`. The peak of sick people is on day 0: the disease never

grows and dies out. Then we used a `for` loop to try other values of `immune` (300, 400, 500, 600,

700), always with 300 days. The more immune people there are, the lower the peak. To find the

\*\*smallest\*\* value that stops the disease, we used a second loop that tries every value from 0 to

999 and stops at the first one where the peak stays at 1. The answer is \*\*666\*\*, not 700:

700 stops the disease, but it is not the smallest value.



\*\*Extra.\*\* The function `simulate\_lockdown` is the same as `simulate`, but from day 20 it uses a

smaller `beta` (`beta \* 0.5`). We compare its peak with the peak without lockdown.



\## Think and explain



The number of sick people changes each day by:



```

new\_infected - new\_recovered = gamma \* I \* (R0 \* S / N - 1)

```



So `I` grows only when `R0 \* S / N > 1`. To stop the disease from the start, we need

`R0 \* S / N < 1`, so `S < N / R0 = 1000 / 3 = 333.33`.



At day 0, `S = 1000 - 1 - immune = 999 - immune`, so:



```

999 - immune < 333.33   =>   immune > 665.67   =>   immune = 666

```



The simulation gives the same answer: \*\*666 immune people\*\* is the smallest value that stops the disease.



The formula `N \* (1 - 1 / R0) = 1000 \* (1 - 1/3) = 666.67` gives almost the same number.

The small difference comes from the one sick person at day 0: the formula supposes that everyone

who is not immune is in S, but here one person is already in I.

With `R0 = 3`, about \*\*2/3 of the town must be immune\*\* to stop the disease.



\## Example results



\*\*1. Normal epidemic\*\* (`beta = 0.3`, `gamma = 0.1`, 300 days)



```

Peak day: 41, sick people: 312.73, final R: 946.74

```



About 95% of the town gets sick.



\*\*2. Different values of beta\*\* (`gamma = 0.1`)



| beta | R0 | Peak of I |

|---|---|---|

| 0.05 | 0.5 | 1.00 (does not grow) |

| 0.1 | 1.0 | 1.00 (does not grow) |

| 0.2 | 2.0 | 157.66 |

| 0.3 | 3.0 | 312.73 |



The disease stops growing when `beta <= 0.1`, that is when `R0 <= 1`.



\*\*3. Lockdown from day 20\*\* (`beta` divided by 2)



| | Peak of I | Peak day | Final R |

|---|---|---|---|

| No lockdown | 312.73 | 41 | 946.74 |

| Lockdown | 83.10 | 57 | 615.31 |



The peak is 73% lower and 16 days later, and about 330 fewer people get sick.

