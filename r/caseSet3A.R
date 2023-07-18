# HR Analytics 
# dataset - set3

pacman::p_load(tidyverse)
#https://www.tidyverse.org/ #https://www.tidyverse.org/packages/

folder3 = './data/set3/'
list.files(folder3)
(file3a = paste0(folder3, 'WA_Fn-UseC_-HR-Employee-Attrition.csv'))
                                
df3a = read.csv(file3a)
head(df3a)

names(df3a)
sort(names(df3a))
selCols1 = c('Age','Education','EducationField', 'Gender', 'MaritalStatus', 'Over18', "NumCompaniesWorked" )
setCols2 = c('EmployeeNumber', 'Attrition', 'Department', 'DistanceFromHome', 'BusinessTravel', "WorkLifeBalance")
selCols3 = c('JobLevel', 'JobRole', 'JobSatisfication', "PerformanceRating", "RelationshipSatisfaction", "YearsAtCompany", "YearsInCurrentRole" , "YearsSinceLastPromotion", "YearsWithCurrManager", "EnvironmentSatisfaction")
selCols4 = c('Overtime', "HourlyRate", "DailyRate" , "MonthlyRate", "PercentSalaryHike" , "StandardHours" )
dim(df3a)

df3a %>% select(all_of(selCols1)) %>% head()
df3a %>% filter(Over18 == 'N')  #none < 18

(df3a1 <- df3a %>% select('EmployeeNumber', all_of(selCols1)))
head(df3a1)                         

library(sjmisc)
to_long(df3a1, keys='EmployeeNumber', values =c('Gender'))

df3a1 %>% select(c('Gender','MaritalStatus')) %>% pivot_longer(everything(), names_to = c('.value', 'set'),  names_pattern = "(.......)(.......)")

descr(df3a1)

frq(df3a1)

df3a1 %>% as_tibble()  %>% tidyr::uncount(n) %>% mutate_all(as.factor)

df3a1 %>% ggplot(., aes(x=Gender, fill=Gender)) + geom_bar(stat='count')
names(df3a)
str(df3a)
head(df3a1)

df3a1a <- df3a1 %>% pivot_longer(cols=c("Gender", 'MaritalStatus', 'EducationField','Over18','Education'), names_to = 'cat1', values_to = 'value1', names_transform = list(cat1 = as.character), values_transform = list(value1 = as.character))  %>% pivot_longer(cols=c('Age','NumCompaniesWorked'), names_to = 'cat2', values_to = 'value2')

df3a1a %>% group_by(cat1, value1)  %>% summarise(n=n())  %>% ggplot(., aes(x=value1, y=n, fill=value1)) + geom_bar(stat='identity') + facet_wrap(cat1 ~. , scale='free')  + geom_text(aes(label=n)) + guides(fill='none')
