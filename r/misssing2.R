# summarise by dates
library(tidyr)
library(dplyr)
(d1 = seq.Date(from = Sys.Date(), Sys.Date() + 10, 2))
(v1 = sample.int(100,length(d1)))
v1
df = data.frame(d1, v1)
df

df %>% group_by(d1)  %>% summarise(n = sum(v1, na.rm=T))

df %>% group_by(d1)  %>% summarise(n = sum(v1, na.rm=T))  %>% complete(d1 = seq.Date( from = Sys.Date(),  to = Sys.Date() + 10, by = "days"
  ),fill = list(n = 0)) 

knitr::kable(df)
DT::datatable(df)
DT::datatable(df, options = list(scrollX = TRUE))
knitr::kable(df) %>%  kableExtra::scroll_box(height = "300px", width = "50%")


continuous_stats <- function(var) {
  df %>% 
    summarise(
      n_miss = sum(is.na({{ var }})),
      mean   = mean({{ var }}, na.rm = TRUE),
      median = median({{ var }}, na.rm = TRUE),
      min    = min({{ var }}, na.rm = TRUE),
      max    = max({{ var }}, na.rm = TRUE)
    )
}
continuous_stats(df$v1)
