#library labelled

library(labelled)

var_label(mtcars)

mtcars %>% look_for()
mtcars %>% look_for('s')
mtcars %>% look_for('s', details=T)
mtcars %>% look_for('m|w', details=T)

mtcars %>% set_value_labels(am = c('auto'=0, 'manual'=1)) %>% summary()

na_values(mtcars)

library(imputeTS)

ggplot_na_distribution(tsAirgap)
ggplot_na_gapsize(tsAirgap)
ggplot_na_distribution2(tsAirgap)
imp_locf <- na_locf(tsAirgap)
ggplot_na_imputations(x_with_na = tsAirgap, x_with_imputations = imp_locf,  x_with_truth = tsAirgapComplete)

library(gtsummary)
tbl_summary(mtcars)

mtcars %>% chop(c(mpg, wt))
mtcars %>% unchop(mpg)

full_seq(c(1,4,25,17),1)

cricket
purrr::pluck(cricket$teams)

mtcars %>% pack(mg = c(mpg, gear))
