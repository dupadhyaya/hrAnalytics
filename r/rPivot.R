# pivot in R

pacman::p_load(tidyverse)

mtcars

mtcars %>% pivot_longer(., cols='mpg')

mtcars %>% select(wt, cyl, mpg) %>% pivot_longer(., cols='mpg', names_to='feature', values_to='MPG_value')

mtcars %>% select(wt, cyl, mpg) %>% pivot_longer(., cols=c('mpg','wt'), names_to='feature', values_to='Value')

mtcars %>% select(wt, cyl, mpg) %>% pivot_longer(., cols=c('mpg','wt'), names_pattern='.value')

head(who)

head(anscombe)

anscombe %>% pivot_longer(cols=everything())
anscombe %>% pivot_longer(cols=everything(), names_to=c('.value','set'), names_pattern='(.)(.)')

head(billboard)

billboard %>% select(c(artist, track, wk1, wk2, wk3))
billboard %>% select(c(artist, track, wk1, wk2, wk3)) %>% pivot_longer(cols=starts_with('wk'))
billboard %>% select(c(artist, track, wk1, wk2, wk3)) %>% pivot_longer(cols=starts_with('wk'), names_to = 'week', names_prefix='wk', values_to = 'rank')

head(who)

names(who)
who1 <- who %>% select(c(country, new_sp_m014, new_sp_m65, newrel_m4554, newrel_f5564))
who1
who1 %>% pivot_longer(  cols = new_sp_m014:newrel_f5564, names_to = c("diagnosis", "gender", "age"),  names_pattern = "new_?(.*)_(.)(.*)", values_to = "count")

library(nycflights13)
#githubinstall::githubinstall("dcl-docs/dcldata")
#remotes::install_github("dcl-docs/dcldata")
#library(dcldata)

?pivot_wider

