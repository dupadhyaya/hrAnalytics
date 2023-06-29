#AR

pacman::p_load(arules, tidyr)

ardata = read.csv('./data/misc/ardata.csv')
head(ardata)
arData1 = as(ardata, 'transactions')
arData1
inspect(arData1)
image(arData1)

itemFrequencyPlot(arData1)

#arData2 = read.transactions('./data/misc/ardata.csv', format = "single", sep = ",")

inspect(arData1[1:3])

rules1 <- apriori(arData1, parameter = list(supp = 0.005, conf = 0.8), minlen=5)
inspect(rules1[1:5])

inspect(subset(rules1, subset = rhs %pin% 'attrition=Y'))
