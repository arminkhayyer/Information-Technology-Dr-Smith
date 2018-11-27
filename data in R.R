MyData <- read.csv(file="C:/Users/oguzt/Documents/GitHub/Information-Technology-Dr-Smith/ALLDATA.csv", header=TRUE, sep=",")
head(MyData, n = 20, addrownums = FALSE)
tail(MyData, n = 20, addrownums = FALSE)
agg = aggregate(MyData$AMOUNT, by = list(MyData$YEAR),FUN = sum)
agg
sum(MyData$AMOUNT)
