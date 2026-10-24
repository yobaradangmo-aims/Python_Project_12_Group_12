


First of all ,we created a new empty list named sim_list=[]:    in which the results are stored .
And then we use a loop for  that will iterate through each day , calculates the values for each day and returns d, S, I and R   :      for d in range(day+1):
For the second task, we have created a new function that takes the output of the first ‘simulate’ function as a parameter.
In R, we uses the max function to find the maximum I  we also pass it the parameters days, S and I. When it finds the maximum I, it returns the day and the I.
For the third task, we used a for loop to iterate through the various values of beta,
we defined two variables, day_peak (the day on which we have most  infections) and patient_of_peak (the total number of patients infected on the peak day), to which we assigned the function peak_day, which takes as a parameter the simulate function with a fixed number of days and a fixed gamma value. 

For the fourth task, we want to see what happens  when  the immunity threshold is set at 700; we note that it is on day 0 that  the number of infected people reaches its lowest point.
We use a ‘for’ loop that varies the number of immune people across different values, bearing in mind that the number of days is 300.
By observing the number of infected people for each value of I, we notice that when the number of immune people is 700, the number of infected people is at its lowest.
