library(olsrr)
library(MASS)
library(caret)
library(dplyr)
library(DAAG)
# library(DAAS)
# library(dplyr)
# library(rcompanion)
# library(stringi)
# library(forecast)
# library(rcompanion)
# library(moments)
# library(car)



# =============================================================================
# ============================= Configuration =================================
# =============================================================================

# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.
directory <- file.path("c:", "Users", "smpat",'desktop','school'
                       , "CSC 323 - Data Analysis and Regression"
                       , "Assignments", "Assignment 3")


# ---- Assign data set
dir_data_in <- file.path(directory,"pisa2009_transformed.csv")

# ----- load data
df <- read.csv(dir_data_in)

binary_to_factors <- 
  df[sample(nrow(df),min(1000,nrow(df))),] %>%    
  sapply(.,function(col) length(unique(col)) <= 10)

df[,binary_to_factors] <- lapply(df[,binary_to_factors], factor)

df2 <- df[complete.cases(df),]
# =============================================================================




graph_model_v_response <- function(model)
{
  model_frame <- model.frame.default(model)
  model_frame <- model_frame[complete.cases(model_frame),]
  
  plot(fitted(model)**2, model_frame$readingScore,
       pch = 18, cex.lab = 1.5, cex.axis = 1.5, col = "steelblue2",
       cex = 1.5, ylab = colnames(model_frame)[1]
       )
  
  abline(0,1, col= "red", lwd = 2)
  
  mtext(paste("Observations: ", nrow(model_frame)), 
        side = 3, line = 1, adj = 0, cex = 1.5
        )
  mtext(paste("Number of Variables: ", ncol(model_frame)-1),
        side = 3, line = 2, adj = 0, cex = 1.5)
  
  # Generate F Statistic
  model_p <- round(pf(summary(model)$fstatistic[1], summary(model)$fstatistic[2]
                      , summary(model)$fstatistic[3], lower.tail = FALSE),6)
  # Combine F statistic and Adj.R^2
  model_summary <- paste("Adj.R^2:   ", round(summary(model)$adj.r.squared, 4)
                         ,"   Model p-value: ", model_p, sep = "" )
  
  mtext(model_summary, side = 3, line = 0, adj = 0, cex = 1.5)

  summary(model)


}






empty_model <- lm(readingScore ~ 1, data = df2)
full_model <- lm(readingScore ~ ., data = df2)


step <- stepAIC(full_model, direction = "backward", na.action = na.omit)
graph_model_v_response(step)
summary(step)
ols_vif_tol(step)
graph_model_v_response(step)

step2 <- stepAIC(empty_model, direction = "forward", na.action = na.omit, 
                scope = list(upper = full_model, lower = empty_model))
graph_model_v_response(step2)
summary(step2)
ols_vif_tol(step2)

model <- lm(readingScore ~  englishAtHome + minutesPerWeekEnglish_sqrt + read30MinsADay 
            ,data = df)
summary(model)
ols_vif_tol(model)


model <- lm(sqrt(readingScore) ~ read30MinsADay
            + male  + raceeth + computerForSchoolwork +
              minutesPerWeekEnglish_sqrt + schoolSize_sqrt + 
              familyEducation*expectBachelors + grade*publicSchool
            , data = df2)
summary(model)
ols_vif_tol(model)
graph_model_v_response(model)

plot(df$schoolSize_sqrt, model$residuals)
plot(df$minutesPerWeekEnglish_sqrt, model$residuals, pch=18, col="steelblue2")
plot(df$raceeth, model$residuals)

plot(df$readingScore, fitted(model)**2)



# =====================
plot(fitted(model)**2, df$readingScore,
     pch = 18, cex.lab = 1.5, cex.axis = 1.5, col = "steelblue2",
     cex = 1.5, ylab = colnames(df)[1], xlab = "readingScore"
)
abline(0,1, col= "red", lwd = 2)

mtext(paste("Observations: ", nrow(df)), 
      side = 3, line = 1, adj = 0, cex = 1.5
)

mtext(paste("Number of Variables: ", ncol(df)-1),
      side = 3, line = 2, adj = 0, cex = 1.5)

# Generate F Statistic
model_p <- round(pf(summary(model)$fstatistic[1], summary(model)$fstatistic[2]
                    , summary(model)$fstatistic[3], lower.tail = FALSE),6)
# Combine F statistic and Adj.R^2
model_summary <- paste("Adj.R^2:   ", round(summary(model)$adj.r.squared, 4)
                       ,"   Model p-value: ", model_p, sep = "" )

mtext(model_summary, side = 3, line = 0, adj = 0, cex = 1.5)

summary(model)
# ===================






# ======================= Validation ===================

set.seed(123)
train.control <- trainControl(method =  "cv", number = 10)

model2 <- train(sqrt(readingScore) ~ read30MinsADay
                + male  + raceeth + computerForSchoolwork +
                  minutesPerWeekEnglish_sqrt + schoolSize_sqrt + 
                  familyEducation*expectBachelors + grade*publicSchool
                , data = df2, method = "lm",
                trControl = train.control)
print(model2)


out <- cv.lm(data = df, form.lm = model, plotit = "Observed", m=10) #10 fold
