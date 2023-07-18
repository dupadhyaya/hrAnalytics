# HR Analytics 
# dataset - set2

pacman::p_load(tidyrverse)
#https://www.tidyverse.org/ #https://www.tidyverse.org/packages/

folder2 = './data/set2/'
list.files(folder2)
(file2a = paste0(folder2, 'tbl_Action.csv'))
(file2b = paste0(folder2, 'tbl_Employee.csv'))
(file2c = paste0(folder2, 'tbl_Perf.csv'))
                                
df2a = read.csv(file2a)
head(df2a)

df2b = read.csv(file2b)
head(df2b)

df2c = read.csv(file2c)
head(df2c)

lapply(list(df2a, df2b, df2c), names)
