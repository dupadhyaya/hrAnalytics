# HR Analytics 
# dataset - set1

pacman::p_load(tidyverse)
#https://www.tidyverse.org/ #https://www.tidyverse.org/packages/


file1 ='./data/set1/HRDataset_v14.csv'
df = read.csv(file)
head(df)

names(df)
