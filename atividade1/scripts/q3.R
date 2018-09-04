require(ggplot2)

dataframe = read.csv(file = "q3_rss.csv", sep = ";")
ggplot(dataframe, aes(x=Iteracao, y=RSS)) + geom_point()
