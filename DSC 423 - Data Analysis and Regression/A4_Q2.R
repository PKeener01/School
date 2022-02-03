
# This will check to see whether the packages are installed and install if
# necessary, then load them

if (!require('ggplot2')) install.packages('ggplot2'); library('ggplot2')
if (!require('dplyr')) install.packages('dplyr'); library('dplyr')
if (!require('glmnet')) install.packages('glmnet'); library('glmnet')
if (!require('caret')) install.packages('caret'); library('caret')
if (!require('rcompanion')) install.packages('rcompanion'); library('rcompanion')
if (!require('AUC')) install.packages('AUC'); library('AUC')
if (!require('car')) install.packages('car'); library('car')

# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.  
# Make this the filepath to your input file
fpath <- file.path("c:", "Users", "smpat",'desktop','school',
                       "CSC 323 - Data Analysis and Regression", 
                       "Assignments", "Assignment 4", 'Remission',
                       'Raw Data', 'remission.csv')


# ---- Assign data set
df <- read.csv(fpath)


 plotNormalHistogram(df[,2], xlab = colnames(df)[2], col = 'steelblue2')
 plotNormalHistogram(df[,3], xlab = colnames(df)[3], col = 'steelblue2')
 plotNormalHistogram(df[,4], xlab = colnames(df)[4], col = 'steelblue2')
 plotNormalHistogram(df[,5], xlab = colnames(df)[5], col = 'steelblue2')
 plotNormalHistogram(df[,6], xlab = colnames(df)[6], col = 'steelblue2')
 plotNormalHistogram(df[,7], xlab = colnames(df)[7], col = 'steelblue2')


df$remiss <- as.factor(df$remiss)

y <- df[,1]
x <- df[,-1]


# This wants to be a normal distribution; can try transformations to get it there.  No strictly necessary.
plotNormalHistogram(df[,5], xlab = colnames(df)[5], col = 'steelblue2')



# ==================  LASSO =======================
x <- df[,c(2:7)]
y <- df[,1]
lasso <- glmnet(as.matrix(x),as.double(y), family = "binomial", alpha = 1, nfolds = 3)
coef(lasso)
plot(lasso)  # very unremarkable; lambda doen't properly optimize

lasso$lambda  # can look at the results for various lambdas here



# =========================================================
# ================== Logistic Regression ==================
# =========================================================

# give 'em their own variables
y <- df[,1]
x <- df[,-1]

# Build the GLM
model <- glm(remiss ~ blast + infil + smear + cell   + temp + li , data = df, family = 'binomial')



qqPlot(model$residuals)  # QQ plot to look at residuals.  Nicht so gut.


x <- predict(model, df)  # this will come in handy later
predictions <- exp(x)/(1+exp(x))  # change from log odds into probability



# AUROC - Area Under the Receiver Operator Characteristic Curve.  
# This is calculated as true positives/false positives and is used quite a bit in 
# risk analysis, so this is the one that I try to maximize.  The others are calculated
# as shown in the lecture.
#
# (Google ROC Curve and take a look at the wikipedia article.)

# make sure to download the "AUC" package  
auroc <- auc(roc(predictions, y))  
ausec <- auc(sensitivity(predictions, y))
auspc <- auc(specificity(predictions, y))
auacc <- auc(accuracy(predictions, y))



# Plot the ROC Curve. Anything above the diagnal grey line is positive predictive power.
plot(roc(predictions, y), lwd = 2)  

# mtext() lets you add words to a graph.  
# Side controls which side it's on (3 is top)
# Line controls the # of lines from the top of the plot space, 0 is on the line
# Adjustment tells it where on the line (0 is left side, .5 is center, 1 is right side)
# Can also us col = "blue" or whatever color you'd like if you want to spice it up a bit
#
# Make sure the graph is wide enough for all of the values.  Alternatively,
# Set adj. to .5 for all of them, then set the lines to 0, 1, 2, 3; this will center and stack them

mtext(paste('AUROC (ROC): ', round(auroc,4)), side = 3, line = 0, adj = 0)
mtext(paste('AUSEC (Sensitivity): ', round(ausec,4)), side = 3, line = 1, adj = 0)
mtext(paste('AUSPC (Specificity): ', round(auspc,4)), side = 3, line = 0, adj = 1)
mtext(paste('AUACC (Accuracy): ', round(ausec,4)), side = 3, line = 1, adj = 1)


# Summary
summary(model)
# Printing the terms to the console for easy copy/paste
print(paste('AIC:', round(summary(model)$aic,4), 'AUROC:', round(auroc,4), '  AUSEC:',round(ausec,4)  
            , '  AUSPC:', round(auspc,4), '  AUACC:',round(auacc,4)))