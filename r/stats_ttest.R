# Stats t-test
#https://www.r-bloggers.com/2022/12/hypothesis-testing-in-r/

#T-test with one sample
#T-Test of two samples
#T-test for paired samples

# t.test(x, y = NULL,   alternative = c("two.sided", "less", "greater"),    mu = 0, paired = FALSE, var.equal = FALSE, conf.level = 0.95)
# x, y: The two samples of data.
# alternative: The alternative hypothesis of the test.
# mu: The true value of the mean.
# paired: whether or not to run a paired t-test.
# var.equal: Whether to assume that the variances between the samples are equal.
# conf.level: The confidence level to use.

#A one-sample t-test is used to determine whether the population’s mean is equal to a given value.

weights <- c(301, 305, 312, 315, 318, 319, 310, 318, 305, 313, 305, 305, 305)
t.test(x = weights, mu = 310)
#mean of turtle weights: 310.0769 We are unable to reject the null hypothesis since the test’s p-value of 0. 9647 is greater than or equal to.05. This means that we lack adequate evidence to conclude that this species of turtle’s mean weight is different from 310 pounds.


#TTest-2SI-----
#Two Sample t-test in R : To determine whether the means of two populations are equal,
#determine whether the mean weight of two different species of turtles is equal. We gather a straightforward random sample of turtles from each species with the following weights to test this.

sample1 <- c(310, 311, 310, 315, 311, 319, 310, 318, 315, 313, 315, 311, 313)
sample2 <- c(335, 339, 332, 331, 334, 339, 334, 318, 315, 331, 317, 330, 325)
t.test(x = sample1, y=sample2)
#We reject the null hypothesis because the test’s p-value (6.029e-06) is smaller than.05.
#Accordingly, we have enough data to conclude that the mean weight of the two species is not identical.

#TTest-2SP------
#Paired Samples t-test in R : When each observation in one sample can be paired with an observation in the other sample, a paired samples t-test is used to compare the means of the two samples.
#determine if a particular training program may help basketball players raise their maximum vertical jump (in inches).
#gather a small, random sample of 12 college basketball players to test this by measuring each player’s maximum vertical jump. Then, after each athlete has used the training regimen for a month, we might take another look at their max vertical leap
before <- c(122, 124, 120, 119, 119, 120, 122, 125, 124, 123, 122, 121)
after <- c(123, 125, 120, 124, 118, 122, 123, 128, 124, 125, 124, 120)
t.test(x = before, y=after, paired=T)
#We reject the null hypothesis since the test’s p-value (0. 02803) is smaller than.05.
#The mean jump height before and after implementing the training program is not equal, thus we have enough data to conclude so.