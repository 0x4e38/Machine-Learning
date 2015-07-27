library(dtw)

walk <- read.table("event6.txt", header=T)
fall_1 <- read.table("event40.txt", header=T) 
fall_2 <- read.table("event47.txt", header=T)

fall_3 <- rev(fall_1[,3])

#rms_walk <- sqrt((walk[,1]^2+walk[,2]^2+walk[,3]^2)/3)
#rms_fall_1 <- sqrt((fall_1[,1]^2+fall_1[,2]^2+fall_1[,3]^2)/3)
#rms_fall_2 <- sqrt((fall_2[,1]^2+fall_2[,2]^2+fall_2[,3]^2)/3)

## Find the best match with the canonical recursion formula
alignment1<-dtw(fall_1[,3],fall_2[,3],keep=TRUE);
print(alignment1$distance)

alignment2<-dtw(fall_1[,3],walk[,3],keep=TRUE);
print(alignment2$distance)

alignment3<-dtw(fall_1[,3],fall_3,keep=TRUE, window="sakoechiba");
print(alignment3$distance)

alignment4<-dtw(fall_1[,3],fall_1[,3],keep=TRUE);
print(alignment4$distance)

## Display the warping curve, i.e. the alignment curve
dtwPlot(alignment1,type="threeway",xlab="Fall 1",ylab="Fall 2")
dtwPlot(alignment2,type="threeway",xlab="Fall 1",ylab="Walk")
dtwPlot(alignment3,type="threeway",xlab="Fall 1",ylab="Rev. Fall 1")
dtwPlot(alignment4,type="threeway",xlab="Fall 1",ylab="Fall 1")

dtwPlot(alignment1,type="twoway",offset=-2,xlab="Fall 1",ylab="Fall 2")
dtwPlot(alignment2,type="twoway",offset=0,xlab="Fall 1",ylab="Walk")
dtwPlot(alignment3,type="twoway",offset=0,xlab="Fall 1",ylab="Walk")

dtwPlotDensity(alignment3,xlab="Fall 1",ylab="Walk")
