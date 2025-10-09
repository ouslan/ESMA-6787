library("ggplot2")
# Define parameters
k <- length(nk)
df1 <- k - 1 # Numerator degrees of freedom
df2 <- sum(nk) - k # Denominator degrees of freedom
lambda2_values <- c(0, lambda2) # Non-centrality parameters
x <- seq(0, 14, by = 0.1)
fvalues <- data.frame(
  x = rep(x, times = length(lambda2_values)),
  density = unlist(lapply(lambda2_values, function(lambda2) {
    df(x, df1, df2, ncp = lambda2)
  })), lambda2 = factor(rep(lambda2_values, each = length(x)))
)
ggplot(fvalues, aes(x = x, y = density, color = lambda2, linetype = lambda2)) +
  geom_line(linewidth = 1) +
  labs(
    x = NULL,
    y = NULL,
    color = expression(lambda^2),
    linetype = expression(lambda^2)
  ) +
  theme_bw()
