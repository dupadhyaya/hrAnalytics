#missing data

#basic------
age = c(20,45,NA, 72, 18, 25, 64, 48, 19,27,NA)
smoke = c(T,T, NA, F, NA, NA, NA, T, F, F,NA)
uti = c('No', NA, 'No', NA, 'No', 'Yes', 'No', 'Yes','No','Yes',NA)
lapply(list(age, smoke, uti), length)
df = data.frame(age, smoke, uti)
df

#missing due to - random  or not
is.na(df)
rowSums(is.na(df))
colSums(is.na(df))

library(tidyr)

df %>% drop_na()
rowSums(is.na(df))
df
ncol(df)
nrow(df)
rowSums(is.na(df)) != ncol(df)
df[rowSums(is.na(df)) != ncol(df),]
df[rowSums(is.na(df)) == ncol(df),]

na.omit(df)
#no row with missing values
complete.cases(df)
df[complete.cases(df),]

df[rowSums(is.na(df)) == 0, ]

df %>% drop_na()
df[rowSums(is.na(df)) != ncol(df), ]
