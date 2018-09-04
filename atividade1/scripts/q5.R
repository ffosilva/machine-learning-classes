require(ggplot2)
require(dplyr)

dataframe = read.csv(file = "q5_grad.csv", sep = ";")
ggplot(filter(dataframe, Iteracao < 1000), aes(x=Iteracao, y=grad_m)) + geom_line()
ggplot(filter(dataframe, Iteracao < 1000), aes(x=Iteracao, y=grad_b)) + geom_line()
