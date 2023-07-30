#Tidyr

library(tidyr)

expand(mtcars, cyl, gear, carb)

complete(mtcars, cyl, gear, carb)

#missing
x <- tribble(  ~x1, ~x2, "A",   1,  "B",  NA, "C",  NA,  "D",   3, "E",  NA )
x

drop_na(x, x2)
#drop rows where data in x2 is missing

?fill(x)
fill(x, x2)
fill(data=x, x2, .direction = 'down')
replace_na(x, list(x2=2))

storms
str(storms)
dim(storms)
n_storms <- storms |> group_by(name)  |> nest()
n_storms
?nest
n_storms[1]
str(n_storms)
class(n_storms)

mtNest1a <- mtcars %>% group_by(gear) %>% nest()
mtNest1b <- mtcars %>% nest(.by='gear')
mtNest1a
mtNest1b
mtNest1a %>% unnest(cols='gear')
?unnest


pivot
?unpivot

mu1 <- mtcars %>% unite(gear, cyl, col='gearcyl', sep='_')

mu1 %>% separate_rows(., gearcyl)

mtcars %>% select(gear, mpg) %>% hoist(mpg)

starwars %>%  select(name, films) %>%  hoist(films, first_film = 1, second_film = 2)

starwars %>% select(name, films)  %>% head()

pool = c('A','B')
A1 = c('India','Australia', 'West Indies', 'Canada')
A2 = c('Pakistan','Sri Lanka', 'Bangladesh')
teams = list(A1, A2)
teams
teams[2]
cricket = data.frame(pool, I(teams))
str(cricket)
cricket
cricket$teams
cHoist <- cricket %>% select(pool, teams)  %>% hoist(teams, T1=1, T2=2, T3=3)
cHoist

cHoist %>% group_by(pool)  %>% mutate ( teamsAll = paste(T1, T2, teams, collapse=', '))

cHlist <- cHoist %>% group_by(pool)  %>% mutate ( teamsAll = list(list(T1, T2, T3)))  %>% select(pool, teamsAll)
cHlist

cHlist$teamsAll

#howmany teams in each
cricket %>% rowwise()  %>% mutate(nT = length(teams))

cHoist %>% rowwise() 5%>% group_by(pool) %>% mutate ( teamsAll = list(list(everything)))
?append


library(sets)

x1 = c('A','B','C','C')
x1
set_power(x1)
print(set(x1))
s1 = set('A','B','C','C')
s1
s2 = set('A','E','F','G')
set_union(s1, s2)
set_intersection(s1, s2)
set_complement(s1, s2)
setequal(s1,s2)
'B' %in% s1

choose(n=3, k=c(0,1,2,3))
set_power(x1)

## basic plots
plot(gset(1:3, 1:3/3))


t1 = tuple(1,3,4)
t1
t1[1] = 23
t1
#https://cran.r-project.org/web/packages/sets/sets.pdf
