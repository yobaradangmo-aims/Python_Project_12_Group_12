
I was responsible for Task 2: finding the peak of the epidemic with beta = 0.3
and gamma = 0.1.

I wrote a function `peak_day(results)` that finds the day with the
most sick people. It uses `max` with `key=lambda row: row[2]`, because each row of
the simulation is a tuple (day, S, I, R) and the number of sick people I is at
index 2. The function returns the peak day and the number of sick people on that
day. Then I ran `simulate(300, 0.3, 0.1)` and displayed the results:
the peak is on day 41 with about 312.73 sick people, and the final value of R is
about 946.74 (read from the last row, `results[-1][3]`).
I learned to use `max` with a `key`, to unpack a tuple into
several variables, and to put code in a function so that it can be reused. Without
`key`, `max` would compare the days instead of the sick people.








Task 4: Herd Immunity
What I did
First, I simulated the spread of a disease in a population of 300 people, 
with a transmission rate of 0.3 and a recovery rate of 0.1. I started with 700 
immune people to observe the peak number of infected individuals.
Then, I tested different numbers of immune people: 300, 400, 500, 600, 
and 700. I used a loop to compare the results and determine whether the
disease continued to spread or stopped.
Finally, I used another loop to find the smallest number of 
immune people needed to stop the disease. The program stops 
when the peak number of infected people is less than or equal to 1.
Difficulties I encountered :One difficulty was understanding how to find the minimum number 
of immune people needed to stop the disease. I also had to understand
how to use loops and conditions to test different values automatically.
How I overcame the difficulties:I overcame these difficulties by breaking the problem into 
smaller steps. I first tested different values of immunity, then used an 
if condition to check whether the disease stopped. Finally, I used break to stop the loop as
soon as the smallest value was found.



Task 3:In this code, I have used a 'for' loop that varies the beta parameter between 
0.05 and 0.3, while keeping gamma constant at 0.1. For each value, it simulates 300 days, identifies
the point in time when the number of infected individuals is at its highest, and then checks whether
this peak exceeds 1. For each case, it displays the beta value, R0, the peak, and the corresponding day.

