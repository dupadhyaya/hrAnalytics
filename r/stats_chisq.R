#Stats - Chi Square

#is data is as expected; if Ho is true, observed values ~ expected values
#Goodness Test : 1 variable, Does variable come from a given distribution, eg. if candy bags have same no of pieces of each flavour or not
#Ho = Proprotion of flavours of candy are same ; Ha = Proportions of flavours are not the same (sample not from the same distribution)
#Independence : 2 variables, Check if 2 variables are related. eg if movie goers decision to buy snacks depends on type of move they watch
#Ho = Prop of people who buy snacks is idenpendent of movie type ; Ha = proportion of people snacks is different for different types of movies (Snacks related to Movie Type)
# 5% risk of concluding the two variables are independent when in reality they are not.

#significant correlation between the types of car sold and the type of Air bags it has. If correlation is observed we can estimate which types of cars can sell better with what types of air bags.
pacman::p_load(tidyr, dplyr, ggplot2)
library(MASS)
names(Cars93)
head(Cars93)
str(Cars93)
Cars93 %>% select(c('AirBags', 'Type')) 

(T1= table(Cars93$AirBags, Cars93$Type))

prop.table(T1, margin=1)
prop.table(T1, margin=2)

chisq.test(T1)
#p-value of less than 0.05 which indicates a strong correlation.
#https://www.tutorialspoint.com/r/r_chi_square_tests.htm
#visually check-----

Cars93 %>% group_by(AirBags, Type) %>% summarise(n=n()) %>% ggplot(., aes(x=AirBags, y=n, fill=Type)) + geom_bar(stat='identity', position=position_stack()) + geom_text(aes(label=n), position=position_stack(vjust=.5))

Cars93 %>% group_by(AirBags, Type) %>% summarise(n=n()) %>% ggplot(., aes(x=AirBags, y=n, fill=Type)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))

Cars93 %>% group_by(AirBags, Type) %>% summarise(n=n()) %>% ggplot(., aes(fill=AirBags, y=n, x=Type)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))



#eg2------
#chi-squared test on the treatment (X) and improvement (Y) columns in treatment.csv
dfT <- read.csv("https://goo.gl/j6lRXD")  #Reading CSV
head(dfT)
table(dfT$treatment, dfT$improvement)
dfT %>% group_by(treatment, improvement) %>% summarise(n=n()) %>% ggplot(., aes(fill=treatment, y=n, x=improvement)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))

#is it observation or simulated, if actual , correct=F
chisq.test(dfT$treatment, dfT$improvement, correct=FALSE)
             
#pvalue < .05, reject Ho (not independent); Accept Ha : dependent yes   
#improvement after treatment is true


#eg3 : mtcars
#are no of carb and no of cyl related
chisq.test(mtcars$cyl, mtcars$carb)
#p-value of less than 0.05 significance level. So we reject the null hypothesis and conclude that carb and cyl have a significant relationship.
mtcars %>% group_by(carb = factor(carb), cyl = factor(cyl)) %>% summarise(n=n()) %>% ggplot(., aes(fill=carb, y=n, x=cyl)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))

#investigate whether distributions of categorical variables differ from one another. Chi-square test is also useful while comparing the tallies or counts of categorical responses between two(or more) independent groups.
head(survey)
chisq.test(survey$Smoke,survey$Exer)
#p-value 0.4828 is greater than the .05, we conclude that the smoking habit is independent of the exercise level of the student and hence there is a weak or no correlation between the two variable
prop.table(table(survey$Smoke,survey$Exer), margin=2)
#Within each Exer cat, never smoking is highest
prop.table(table(survey$Smoke,survey$Exer), margin=1)
#Withing each Smoking cat, Never Freq is highest 
survey %>% group_by(Smoke = factor(Smoke), Exer = factor(Exer)) %>% summarise(n=n()) %>% ggplot(., aes(fill=Smoke, y=n, x=Exer)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))


#eg-----
(M = matrix(c(762,327, 468, 484, 239, 477), byrow=T, nrow=2))
dimnames(M) = list(gender=c('M','F'), party=c('BJP','Congress','Others'))
M
class(M)
chisq.test(M)
#relation between gender and party they vote
prop.table(M,1)  #proportions(M,1)
prop.table(M,2)

M %>% group_by(Smoke = factor(Smoke), Exer = factor(Exer)) %>% summarise(n=n()) %>% ggplot(., aes(fill=Smoke, y=n, x=Exer)) + geom_bar(stat='identity', position=position_fill()) + geom_text(aes(label=n), position=position_fill(vjust=.5))
Xsq <- chisq.test(M)
Xsq
Xsq$observed   # observed counts (same as M)
Xsq$expected   # expected counts under the null
Xsq$residuals  # Pearson residuals
Xsq$stdres     # standardized residuals

