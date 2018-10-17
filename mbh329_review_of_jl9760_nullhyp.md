### N0(null) hypothesis is formatted correctly 
### N1 (alternative) hypothesis is formatted is correctly

*I think it would be helpful to add some definitions of what data you will be analyzing in your hypthesis testing. Define the time period you will be studying and define user type for the reader, needs a benchmark to base analysis off of (day/month/year). I would stay consistent with "birth year" in your hypothesis, so instead of 30 years old state the year that would determine if they are over or under 30. In further testing, it would be interesting to extract customer vs subscriber data to tripduration and see what correlation you can find, if any. "IF x THAN y"

--------------------------------------------------------------------------------------------------------
The dataframe (df_age_tripduration_2) jl9760 used was narrowed down appropriately to focus on the null hypothesis they were trying to reject. They correctly extracted birth year of the users and tripduration from the orignal dataset which were the key elements spoken about in the N0 and N1.

The scatterplots he used to visualize the data were helpful to make a conclusion from the data and I thought were a good use of data visualization. Some small adjustments I would make to the scatterplot would be to label the unit on the y axis (seconds).

### As for some suggestions to improve the experiment:

-I think it is important to find out the ratio in riders that are over and under 30 years old. The data might suggest that "Users that are younger than 30 years old are more likely have a longer trip duration" but if there are a lot more users who are 30 years old what does this alternative hypothesis give us? Is it giving us a true description of the population? Would be cool to see if we can extract that.

-State the p value and the significance level.

-Filter outliers (i.e. from the scatter plot it says that there are people born in 1890 that are riding citibike but I doubt that anyone that old is still alive, let alone riding a bike)

I would suggest using the Mann-Whitney U test which "is a nonparametric test of the null hypothesis that it is equally likely that a randomly selected value from one sample will be less than or greater than a randomly selected value from a second sample" (wikipedia). jl9760 null hypothesis test is unpaired (not related to other values), unparametric, and is comparing two numerical data sets. The way the hypothesis is set up would be best tested with the Mann-Whitney U test.

All together a good example of a null hypothesis test. Great job!