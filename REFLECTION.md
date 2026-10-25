
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
