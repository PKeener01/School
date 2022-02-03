# ---- This script is meant to be generalizable to provide initial analysis for
# ---- model building projects


# =============================================================================
# ============================= Configuration =================================
# =============================================================================

# ---- Analysis Selection

# Produce graphs for each dependent vs independent variable.  
# Includes the regression equation, adj. R^2, model p-value
#    , and Correlation (if applicable)
univariate_graphs <- TRUE


# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.

directory <- file.path("c:", "Users", "smpat",'desktop','school'
                        , "CSC 323 - Data Analysis and Regression"
                       , "Assignments", "Assignment 3")


# ---- Assign data set
dir_data_in <- file.path(directory,"pisa2009_noX.csv")

# === Note: file read from directory + data_filename

# ---- Assign dependent/response variable
y_var_index <- 24 # This is used to identify the variable
y_var_nicename <- "Reading Score"   # This is used to label graphs

x_var_index <- 23
x_as_factor <- FALSE
x_var_colname <- 'MPW English'

convert_binaries = TRUE # if false, the data set will skip automatic conversion

# =============================================================================
# ============================= Data Preparation ==============================
# =============================================================================

# -- initialize libraries
#
library(stringi)
library(dplyr)
library(forecast)
library(rcompanion)
library(moments)


# ---- Create file structure
filepath_plots <- file.path(directory, 'Analysis_Out', 'Graphs', 'Transformation Analysis')
filepath_hist <- filepath_plots

dir.create(file.path(directory, 'Analysis_Out'))
dir.create(file.path(directory, 'Analysis_Out', 'Graphs'))
dir.create(filepath_plots)


# read in data
df <- read.csv(dir_data_in)

# ***********  include only data where the depedent variable has values

# get col name of y_var
y_var_colname <- colnames(df[y_var_index])

x_var_colname <- colnames(df[x_var_index])

# move y var to front
df <- df%>%
  select(y_var_index, x_var_index)

# ==== Convert binary variables to factors
# select 1000 random rows from DF and check the number of unique values
# if there are only 2 unique values then convert the column to factor

if(x_as_factor == TRUE){df[,2] <- as.factor(df[,2])}


df1 <- as.data.frame(df[,y_var_colname])
df1[y_var_colname] <- as.data.frame(df[,y_var_colname])

df2 <- as.data.frame(df[,2])
# ==== Perform data transformations

df2 <- df2 %>%
  mutate_if(is.numeric
            , list(r = function(x)(1/(x+1)-1),  # recipricol transform
                   l = log1p,  # log transform
                   sqrt = sqrt, # square root transform
                   sq = function(x)(x**2), #square transform
                   bc = function(x) (BoxCox(x, BoxCox.lambda(x))) #box-cox transform
            )
  )

df2[x_var_colname] <- as.data.frame(df[,x_var_colname])
df2 <- df2[,2:7]
df2 <- tibble::rowid_to_column(df2, "ID")
df1 <- tibble::rowid_to_column(df1, "ID")
df1 <- df1[,-c(2)]
df <- merge(df1, df2, "ID")
df <- df%>%
  select(y_var_colname, x_var_colname, everything())
df <- subset(df, select=-c(ID))


remove(df1)
remove(df2)
# =

# -- log scale GDP per capita

# df$GDP_PC_L <- log1p(df$GDP.per.capita..current.US..)
# df <- df[,-1]
# 
# df <- df%>%
#   select(GDP_PC_L, everything())
# 
# y_var_colname <- colnames(df)[1]
# y_var_index <- 1


# =============================================================================
# ============================= Analysis ======================================
# =============================================================================



# -- Create additional datasets
y_var_data <- df[,y_var_colname]
x_var_data <- dplyr::select(df, -one_of(c(y_var_colname)))


# ================== First Order & Transformation Graphs ======================


 
  


if(univariate_graphs==TRUE)
{
  counter = 0
  
  first_order_investigation <- function(dependent_variable, independent_variables, counter)
  {
    
    # - need to decide how to handle non-binary factors
    
    df <- independent_variables[counter] 
    df[y_var_colname] <- dependent_variable
    
    # Additional cleaning
    df <- df[complete.cases(df),]
    if(is.numeric(df[1,1])==TRUE){df <- df[!is.infinite(rowSums(df)),]}
    #-- 
    
    fname <- file.path(filepath_plots,
                       paste(counter, "_", colnames(df[1]), ".png", sep = ""))
    
    model <- lm(df[,2] ~ df[,1])
    
    png(fname)
    
    plot(df, pch = 18, cex.lab = 1.5, cex.axis = 1.5, col = "blue"
         ,ylab = y_var_nicename)
    
    if(is.factor(df[,1])==FALSE)
    {
      lines(df[,1], fitted(model), col="red", lwd = 2)
    }
    
    
    
    model_p <- round(pf(summary(model)$fstatistic[1], summary(model)$fstatistic[2]
                        , summary(model)$fstatistic[3], lower.tail = FALSE),6)
    
    model_summary <- paste("Adj.R^2:   ", round(summary(model)$adj.r.squared, 4)
                           ,"   Model p-value: ", model_p, sep = "" )
    
    
    equation <- paste("Equation:   ", round(summary(model)$coefficients[1], 4)
                      , " + ", round(summary(model)$coefficients[2], 4), "x"
                      , sep = "")
    
    
    
    if(is.numeric(df[,1])==TRUE)
    {
      # browser()
      
      cur_corr <- cor(df)
      
      var_cor <- paste("Correlation:  ", round(cor(df)[2],4), sep="")
      mtext(var_cor, side = 3, line = 2, adj = 0, cex = 1)
      
      # === histograms
      fname <- file.path(filepath_hist,
                         paste(counter, "_hist_", colnames(df[1]), ".png", sep = ""))
      
      png(fname)
      plotNormalHistogram(df[,1], xlab = colnames(df[1]))
      skew <- paste("Skew:  ", round(skewness(df[,1]),4))
      kurt <- paste("Kurtosis:  ", round(kurtosis(df[,1]),4))
      
      mtext(skew, side=3, line=2, adj=0)
      mtext(kurt, side=3, line=1, adj=0)
      
      dev.off()
    }
    
    
    mtext(equation, side = 3, line = 1, adj = 0, cex = 1)
    mtext(model_summary, side = 3, line = 0, adj = 0, cex = 1)
    
    dev.off()
  }
  
  
  
  for(counter in 1:ncol(x_var_data))
  {
    first_order_investigation(y_var_data, x_var_data, counter)  
  }
}
