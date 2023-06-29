# AR data for HR

n= 100 #employees
gender = sample(c('M','F'), size=n, replace=T, prob=c(.7,.3))
table(gender)
salary = sample(c('Low','Medium','Low'), replace=T,  size=n, prob=c(.3, .5, .2))
pL = c(.3, .225, .2, .175, .1)
sum(pL)
level = sample(c('L1','L2', 'L3', 'L4', 'L5'), replace=T, size=n,  prob=pL)
pT = c(.3, .4, .2, .1); sum(pT)
tenure = sample(c('<5Y','5-10Y', '10-20Y', '>20Y'), replace=T, size=n,  prob=pT)
attrition = sample(c('Y','N'), replace=T, size=n,  prob=c(.3,.7))
increment = sample(c('1LY','2LY'), size=n, replace=T, prob=c(.7,.3))

df = data.frame(gender, salary, level, tenure, attrition, increment)
df

write.csv(df, file='./data/misc/ardata.csv', row.names = F, na='')

