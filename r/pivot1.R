# pivot longer

library(tidyr)

dfsales <- data.frame(
  subjectid = c("a","b","c","d","e","f","g","h","i","j","k"),
  location = c("NY","NC","WA","WA","OR","CA","AR","KS","AZ","VT","MA"),
  month1 = c(NA,NA,1,0,0,2,1,1,0,0,0),
  month2 = c(NA,NA,0,0,0,0,NA,0,0,0,NA),
  month3 = c(NA,1,0,1,0,0,0,1,NA,NA,NA),
  month4 = c(0,0,0,0,0,1,2,0,1,NA,0),
  goods1 = c(1,2,1,2,0,0,1,2,2,1,0),
  goods2 = c(0,0,1,2,1,1,2,2,1,0,0),
  goods3 = c(0,1,2,1,1,NA,2,1,2,1,NA),
  goods4 = c(0,1,2,1,1,1,2,2,NA,NA,NA))
dfsales
names(dfsales)

dfsales %>% pivot_longer(!(c(subjectid,location)), values_drop_na = TRUE   )

long <- pivot_longer(data = dfsales,cols = month1:goods4, names_pattern = "([^\\d]+)(\\d)", names_to = c("type","month"))
long
wide <- pivot_wider(data = long ,names_from = "type",values_from = "value",  names_prefix = "value_")
wide

pivot_longer(data = dfsales,cols = month1:goods4,   names_pattern = "([^\\d]+)(\\d)", names_to = c(".value","monthNo"))
#[^\\d] means not a numeric digit, plus sign means one or more of the preceding, so [^\\d]+ means one or more characters that are not numeric digits.  (\\d) is simple. It means a numeric digit.
#The expression as a whole will match some non-digits followed by a digit 

df <- data.frame(jan_2023 = c(1,1),   feb_2023 = c(2,2),     mar_2023 = c(3,3))
df

df2 <- df %>% pivot_longer(cols =everything(), names_to ='date', values_to='n')
df2
df %>% pivot_longer(cols=everything(), names_to = c('month','year'), names_sep='_')
df %>% pivot_longer(cols=everything(), names_to = c('month','year'), names_sep='_', values_to ='sales', names_transform = list(year = as.numeric))
df %>% pivot_longer(cols=everything(), names_to = c('month','year'), names_pattern = '([A-Za-z]+)_([0-9]+)', values_to ='sales', names_transform = list(year = as.numeric))

