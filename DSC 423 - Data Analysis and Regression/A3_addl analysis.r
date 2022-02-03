library(ggplot2)

df$readingScore_Z <- (df$readingScore-mean(df$readingScore))/sd(df$readingScore)
plot(df$readingScore_Z)

plot(df$readingScore_Z, col = "steelblue2", pch = 18)

max_z <- round(max(df$readingScore_Z),3)
min_z <- round(min(df$readingScore_Z),3)
mean_z <- round(mean(df$readingScore_Z),3)
median_z <- round(median(df$readingScore_Z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)

# ===
colnames(df2)[18]
colnames(df2)[19]
colnames(df2)[23]


df2$minutesPerWeekEnglish_z <- (df2$minutesPerWeekEnglish-mean(df2$minutesPerWeekEnglish))/sd(df2$minutesPerWeekEnglish)

plot(df2$minutesPerWeekEnglish_z, col = "steelblue2", pch = 18)

max_z <- round(max(df2$minutesPerWeekEnglish_z),3)
min_z <- round(min(df2$minutesPerWeekEnglish_z),3)
mean_z <- round(mean(df2$minutesPerWeekEnglish_z),3)
median_z <- round(median(df2$minutesPerWeekEnglish_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)

# ===

df2$studentsInEnglish_z <- (df2$studentsInEnglish-mean(df2$studentsInEnglish))/sd(df2$studentsInEnglish)

plot(df2$studentsInEnglish_z, col = "steelblue2", pch = 18)

max_z <- round(max(df2$studentsInEnglish_z),3)
min_z <- round(min(df2$studentsInEnglish_z),3)
mean_z <- round(mean(df2$studentsInEnglish_z),3)
median_z <- round(median(df2$studentsInEnglish_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)

# ===
df2$schoolSize_z <- (df2$schoolSize-mean(df2$schoolSize))/sd(df2$schoolSize)

plot(df2$schoolSize_z, col = "steelblue2", pch = 18)

max_z <- round(max(df2$schoolSize_z),3)
min_z <- round(min(df2$schoolSize_z),3)
mean_z <- round(mean(df2$schoolSize_z),3)
median_z <- round(median(df2$schoolSize_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)









# ===


df$minutesPerWeekEnglish_z <- (df$minutesPerWeekEnglish_sqrt-mean(df$minutesPerWeekEnglish_sqrt))/sd(df$minutesPerWeekEnglish_sqrt)

plot(df$minutesPerWeekEnglish_z, col = "steelblue2", pch = 18)

max_z <- round(max(df$minutesPerWeekEnglish_z),3)
min_z <- round(min(df$minutesPerWeekEnglish_z),3)
mean_z <- round(mean(df$minutesPerWeekEnglish_z),3)
median_z <- round(median(df$minutesPerWeekEnglish_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)

# ===

df$studentsInEnglish_z <- (df$studentsInEnglish_bc-mean(df$studentsInEnglish_bc))/sd(df$studentsInEnglish_bc)

plot(df$studentsInEnglish_z, col = "steelblue2", pch = 18)

max_z <- round(max(df$studentsInEnglish_z),3)
min_z <- round(min(df$studentsInEnglish_z),3)
mean_z <- round(mean(df$studentsInEnglish_z),3)
median_z <- round(median(df$studentsInEnglish_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)

# ===
df$schoolSize_z <- (df$schoolSize_sq-mean(df$schoolSize_sq))/sd(df$schoolSize_sq)

plot(df$schoolSize_z, col = "steelblue2", pch = 18)

max_z <- round(max(df$schoolSize_z),3)
min_z <- round(min(df$schoolSize_z),3)
mean_z <- round(mean(df$schoolSize_z),3)
median_z <- round(median(df$schoolSize_z), 3)

mtext(paste("Max Z-Score: ", max_z), side = 3, line = 1, adj = 0, cex = 1)
mtext(paste("Min Z-Score: ", min_z), side = 3, line = 0, adj = 0, cex = 1)
mtext(paste("Mean Z-Score: ", mean_z), side = 3, line = 1, adj = 1, cex = 1)
mtext(paste("Median Z-Score: ", median_z), side = 3, line = 0, adj = 1, cex = 1)



df[df$schoolSize_z > 3,]

model <- lm(df$readingScore ~ df$schoolSize_sq)
summary(model)
