art.d <- data.frame(y = c(87, 90, 103, 83, 99, 94, 79, 87, 87),
Columns= as.factor(c(1:tt)),
Rows=as.factor(rep(1:tt,each=tt)),
Treatment= c("A","B","C","B","C","A","C","A","B"))
ybars <- tapply(art.d$y,art.d$Treatment,mean) ## ybars
ybars[-1]-ybars[1] ## tau_{k.}-\tau_{1.}
## B C
## -2.666667 4.333333
m1 <- lm(y ~ Rows+Columns+Treatment,data=art.d)
coef(m1)