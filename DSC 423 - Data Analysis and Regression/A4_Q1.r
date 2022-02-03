library(dplyr)
library(glmnet)
library(caret)
library(rcompanion)
library(moments)
library(car)
# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.
directory <- file.path("c:", "Users", "smpat",'desktop','school',
                       "CSC 323 - Data Analysis and Regression", 
                       "Assignments", "Assignment 4", 'PISA')


# ---- Assign data set
dir_data_in <- file.path(directory, "Raw Data", "PISA2009_noX.csv") #PISA2009_noX.csv

df <- read.csv(dir_data_in)

# ====================== Prep Data Sets =======================================

# 
 df <- df %>%
   select(24,everything())

df$grade <- as.factor(df$grade)

 df$familyEducation <- as.factor(df$motherBachelors + df$motherHS
                                 + df$fatherBachelors + df$fatherHS)


y <- df[,1]
ybar <- mean(y)
x <- df[,-c(1, 2, 4, 25)]
factors <- df[,c(2, 4, 25)]

# factors[,3] <- as.factor(factors[,3])
# factors[,4] <- as.factor(factors[,4])
# factors[,5] <- as.factor(factors[,5])
# factors[,6] <- as.factor(factors[,6])
# factors[,7] <- as.factor(factors[,7])
# factors[,8] <- as.factor(factors[,8])
# factors[,9] <- as.factor(factors[,9])
# factors[,10] <- as.factor(factors[,10])
# factors[,11] <- as.factor(factors[,11])
# factors[,12] <- as.factor(factors[,12])

# ====================== Basic OLS ===========================================

OLS <- lm(readingScore ~ read30MinsADay + male + raceeth + computerForSchoolwork
          + familyEducation + expectBachelors + grade + publicSchool
          + minutesPerWeekEnglish_sqrt + schoolSize_sqrt 
          + familyEducation * expectBachelors + grade*publicSchool
            ,data = df)


summary(OLS)

y_predict <- predict(OLS, data = x)
residuals <- y_predict - y

SSE.OLS <- sum(residuals**2)
MSE.OLS <- mean(residuals**2)
RMSE.OLS <- sqrt(MSE.OLS)



# ===== plot
par(mfrow=c(1,1))  #1 chart in the picture
SSE <- sum(residuals**2)
MSE <- mean(residuals**2)
RMSE <- sqrt(MSE)

plot(y_predict, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Predicted Reading Score'
     , main = 'OLS Regression')  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE : ', round(SSE,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE : ', round(MSE,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE : ', round(RMSE,4)),side = 3, line = 2, adj = 0)

par(mfrow=c(1,2))  #1 chart in the picture
# ==== Residual Plot
plot(residuals, pch = 18, col = 'steelblue2')
abline(2*sd(residuals),0, col = 'red', lty = 2)
abline(sd(residuals),0, col = 'red')
abline(0,0)
abline(-sd(residuals),0, col = 'red')
abline(-2*sd(residuals),0, col = 'red', lty = 2)
mtext(paste('Standard Deviation: ', round(sd(residuals),2))
      , side = 3, line = 0, adj = 0)

# -- histogram
plotNormalHistogram(residuals, xlab = 'Residuals', col = 'steelblue2'
                    )
skew <- paste("Skew:  ", round(skewness(residuals),4))
kurt <- paste("Kurtosis:  ", round(kurtosis(residuals),4))

mtext(skew, side=3, line=2, adj=0)
mtext(kurt, side=3, line=1, adj=0)





# ================================================================================
# ================================================================================
# ================================================================================


# ============== Prep data for Ridge & LASSO

dummies <- dummyVars(~., data = factors, fullRank = TRUE)
dvals <- predict(dummies, factors)
x <- cbind(x,dvals)

remove(dvals, dummies, factors)

# ====================================================================
# ======================= Ridge Regression ===========================
# ====================================================================

set.seed(123)
ridge <- cv.glmnet(as.matrix(x), as.double(y), alpha = 0, nfolds = 10)
y_predict <- predict(ridge, newx = as.matrix(x))


residuals <- y_predict - y

SSE.Ridge <- sum((residuals)**2)
MSE.Ridge <- mean((residuals)**2)
RMSE.Ridge <- sqrt(MSE.Ridge)


par(mfrow=c(1,1))  #1 chart in the picture
plot(ridge)
log(ridge$lambda.min)

# ===== plot
SSE <- sum((y_predict-y)**2)
MSE <- mean((y_predict-y)**2)
RMSE <- sqrt(MSE)

plot(y_predict, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Predicted Reading Score'
     , main = 'Ridge Regression')  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE : ', round(SSE,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE : ', round(MSE,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE : ', round(RMSE,4)),side = 3, line = 2, adj = 0)

par(mfrow=c(1,2))  #set up for multiple graphs/chart
# ==== Residual Plot
plot(residuals, pch = 18, col = 'steelblue2')
abline(2*sd(residuals),0, col = 'red', lty = 2)
abline(sd(residuals),0, col = 'red')
abline(0,0)
abline(-sd(residuals),0, col = 'red')
abline(-2*sd(residuals),0, col = 'red', lty = 2)
mtext(paste('Standard Deviation: ', round(sd(residuals),2)), side = 3, line = 0, adj = 0)

# -- histogram
plotNormalHistogram(residuals, xlab = 'Residuals', col = 'steelblue2')
skew <- paste("Skew:  ", round(skewness(residuals),4))
kurt <- paste("Kurtosis:  ", round(kurtosis(residuals),4))

mtext(skew, side=3, line=0, adj=1)
mtext(kurt, side=3, line=0, adj=0)

# -- QQ Plot
par(mfrow=c(1,1))  #1 chart in the picture
qqPlot(y_predict, col = 'steelblue2', pch = 18, main = 'QQ Plot - Ridge Regression')



# ====================================================================
# ======================= LASSO Regression ===========================
# ====================================================================



y <- y

set.seed(123)
lasso <- cv.glmnet(as.matrix(x), as.double(y), alpha = 1, nfolds = 10)
y_predict_lasso <- predict(lasso, newx = as.matrix(x))


y_predict_lasso <- y_predict_lasso


residuals_lasso <- y_predict_lasso - y

SSE.lasso <- sum((residuals_lasso)**2)
MSE.lasso <- mean((residuals_lasso)**2)
RMSE.lasso <- sqrt(MSE.lasso)


par(mfrow=c(1,1))  #1 chart in the picture
plot(lasso)
log(lasso$lambda.min)

# ===== plot
SSE.lasso <- sum((y_predict_lasso-y)**2)
MSE.lasso <- mean((y_predict_lasso-y)**2)
RMSE.lasso <- sqrt(MSE.lasso)

plot(y_predict_lasso, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Predicted Reading Score'
     , main = 'LASSO Regression')  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE.lasso : ', round(SSE.lasso,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE.lasso : ', round(MSE.lasso,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE.lasso : ', round(RMSE.lasso,4)),side = 3, line = 2, adj = 0)

par(mfrow=c(1,2))  #set up for multiple graphs/chart
# ==== Residual Plot
plot(residuals_lasso, pch = 18, col = 'steelblue2')
abline(2*sd(residuals_lasso),0, col = 'red', lty = 2)
abline(sd(residuals_lasso),0, col = 'red')
abline(0,0)
abline(-sd(residuals_lasso),0, col = 'red')
abline(-2*sd(residuals_lasso),0, col = 'red', lty = 2)
mtext(paste('Standard Deviation: ', round(sd(residuals_lasso),2)), side = 3, line = 0, adj = 0)

# -- histogram
plotNormalHistogram(residuals_lasso, xlab = 'residuals_lasso', col = 'steelblue2')
skew <- paste("Skew:  ", round(skewness(residuals_lasso),4))
kurt <- paste("Kurtosis:  ", round(kurtosis(residuals_lasso),4))

mtext(skew, side=3, line=0, adj=1)
mtext(kurt, side=3, line=0, adj=0)

# -- QQ Plot
par(mfrow=c(1,1))  #1 chart in the picture
qqPlot(y_predict_lasso, col = 'steelblue2', pch = 18, main = 'QQ Plot - LASSO Regression')





# =======================================================

par(mfrow=c(1,2))  #set up for multiple graphs/chart

SSE <- sum((y_predict-y)**2)
MSE <- mean((y_predict-y)**2)
RMSE <- sqrt(MSE)

plot(y_predict, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'Ridge Regression - Predicted'
     )  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE : ', round(SSE,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE : ', round(MSE,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE : ', round(RMSE,4)),side = 3, line = 2, adj = 0)


# --

plot(y_predict_lasso, y, pch = 18, col = 'steelblue2'
     , ylab = 'Reading Score', xlab = 'LASSO Regression - Predicted'
     )  # update
abline(0,1, col = 'red', lwd = 2)

mtext(paste('SSE.lasso : ', round(SSE.lasso,4)),side = 3, line = 0, adj = 0)
mtext(paste('MSE.lasso : ', round(MSE.lasso,4)),side = 3, line = 1, adj = 0)
mtext(paste('RMSE.lasso : ', round(RMSE.lasso,4)),side = 3, line = 2, adj = 0)

# -- QQ Plot
par(mfrow=c(1,2))  #1 chart in the picture
qqPlot(y_predict, col = 'steelblue2', pch = 18, main = 'QQ Plot - Ridge Regression')
qqPlot(y_predict_lasso, col = 'steelblue2', pch = 18, main = 'QQ Plot - LASSO Regression')