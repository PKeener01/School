library(dplyr)
library(glmnet)
library(caret)
library(rcompanion)
library(moments)
# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.
directory <- file.path("c:", "Users", "smpat",'desktop','school',
                       "CSC 323 - Data Analysis and Regression", 
                       "Assignments", "Assignment 4", 'PISA')


# ---- Assign data set
dir_data_in <- file.path(directory, "Raw Data", "PISA2009_noX.csv")

df <- read.csv(dir_data_in)

# ====================== Prep Data Sets =======================================


df <- df %>%
  select(24,everything())

df$grade <- as.factor(df$grade)

df$familyEducation <- as.factor(df$motherBachelors + df$motherHS
                                + df$fatherBachelors + df$fatherHS)


y <- df[,1]
ybar <- mean(y)
x <- df[,-c(2, 4, 25)]
factors <- df[,c(2, 4, 25)]

# ====================== Basic OLD ===========================================

OLS <- lm(readingScore ~ read30MinsADay + male + raceeth + computerForSchoolwork
          + familyEducation + expectBachelors + grade + publicSchool
          + sqrt(minutesPerWeekEnglish) + sqrt(schoolSize) 
          + familyEducation * expectBachelors + grade*publicSchool
            ,data = df)


summary(OLS)

y_predict <- predict(OLS, data = x)

SSE.OLS <- sum((y_predict-y)**2)
MSE.OLS <- mean((y_predict-y)**2)
RMSE.OLS <- sqrt(MSE.OLS)



plot(y_predict, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Predicted Reading Score'
     , main = 'OLS Regression')
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE : ', round(SSE.OLS,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE : ', round(MSE.OLS,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE : ', round(RMSE.OLS,4)),side = 3, line = 2, adj = 0)


# ============== Prep data for Ridge & LASSO

dummies <- dummyVars(~., data = factors, fullRank = TRUE)
dvals <- predict(dummies, factors)
x <- cbind(x,dvals)

remove(dvals, dummies, factors)

# ============== Ridge Regression

set.seed(123)
ridge <- cv.glmnet(as.matrix(x), as.double(y), alpha = 0, nfolds = 10)
y_predict <- predict(ridge, newx = as.matrix(x))


residuals <- y_predict - y

SSE.Ridge <- sum((residuals)**2)
MSE.Ridge <- mean((residuals)**2)
RMSE.Ridge <- sqrt(MSE.Ridge)

plot(residuals, pch = 18, col = 'steelblue2')
abline(2*sd(residuals),0, col = 'red', lty = 2)
abline(sd(residuals),0, col = 'red')
abline(0,0)
abline(-sd(residuals),0, col = 'red')
abline(-2*sd(residuals),0, col = 'red', lty = 2)
mtext(paste('Standard Deviation: ', round(sd(residuals),2)), side = 3, line = 0, adj = 0)




# ===== plot

SSE <- sum((y_predict-y)**2)
MSE <- mean((y_predict-y)**2)
RMSE <- sqrt(MSE)

plot(y_predict, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Predicted Reading Score'
     , main = 'Ridge Regression - No Adjustments')  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE : ', round(SSE,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE : ', round(MSE,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE : ', round(RMSE,4)),side = 3, line = 2, adj = 0)


plotNormalHistogram(residuals, xlab = 'Residuals', col = 'steelblue2')
skew <- paste("Skew:  ", round(skewness(residuals),4))
kurt <- paste("Kurtosis:  ", round(kurtosis(residuals),4))

mtext(skew, side=3, line=2, adj=0)
mtext(kurt, side=3, line=1, adj=0)

