# ---- This script is meant to be generalizable to provide initial analysis for
# ---- model building projects


# =============================================================================
# ============================= Configuration =================================
# =============================================================================

# ---- Analysis Selection

# Produce graphs for each dependent vs independent variable.  
# Includes the regression equation, adj. R^2, model p-value
#    , and Correlation (if applicable)
univariate_graphs <- FALSE

# Generate correlation matrix of all numeric variables
correlation_matrix <- FALSE


# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.
fpath_base <- file.path("c:", "Users", "smpat",'desktop','school'
                        , "CSC 323 - Data Analysis and Regression")
fpath <- file.path(fpath_base, "Assignments", "Assignment 3")  



# ---- Assign data set
data_filename = "pisa2009_noX.csv"

# ---- Assign dependent/response variable
y_var_index <- 24 # This is used to identify the variable
y_var_nicename <- "Reading_Score"   # This is used to label graphs

convert_binaries = TRUE # if false, the data set will skip automatic conversion



# =============================================================================
# ============================= Data Preparation ==============================
# =============================================================================


# ---- Create file structure
filepath_plots <- file.path(fpath, 'Analysis_Out', 'Graphs', 'Plots')
filepath_hist <- file.path(fpath, 'Analysis_Out', 'Graphs', 'Histograms')

dir.create(file.path(fpath, 'Analysis_Out'))
dir.create(file.path(fpath, 'Analysis_Out', 'Graphs'))
dir.create(filepath_plots)
dir.create(filepath_hist)

  
# -- initialize libraries
library(stringi)
library(dplyr)
library(rcompanion)
library(forecast)

# library(ggplot2)
# library(olsrr)
# library(mosaic)
# --

# read in data
df <- read.csv(file.path(fpath, data_filename))

# get col name of y_var
y_var_colname <- colnames(df[y_var_index])

# move y var to front
df <- df%>%
  select(all_of(y_var_colname), everything())

# ==== Convert binary variables to factors
# select 1000 random rows from DF and check the number of unique values
# if there are only 2 unique values then convert the column to factor

# -- Create new Columns

df$mothersEducation <- as.factor(df$motherBachelors + df$motherHS)
df$fathersEducation <- as.factor(df$fatherBachelors + df$fatherHS)
df$familyEducation <- as.factor(df$motherBachelors + df$motherHS
                                + df$fatherBachelors + df$fatherHS)
df$numParentBachelors <- as.factor(df$motherBachelors + df$fatherBachelors)
df$parentBachelors <- df$motherBachelors + df$fatherBachelors
df$parentBachelors[df$parentBachelors > 0] <- 1

df$parentHS <- df$motherHS + df$fatherHS
df$parentHS[df$parentHS > 0] <- 1

df$parentHighestEdu <- df$parentBachelors + df$parentHS
df$parentHighestEdu <- as.factor(df$parentHighestEdu)

df$numParentsBornUS <- as.factor(df$motherBornUS + df$fatherBornUS)
df$numParentsWork <- as.factor(df$motherWork + df$fatherWork)
df$yrsInSchool <- as.factor(df$grade + df$preschool)



# ==== Convert variables to factors
if(convert_binaries==TRUE)
{
  binary_to_factors <- 
    df[sample(nrow(df),min(1000,nrow(df))),] %>%    
    sapply(.,function(col) length(unique(col)) == 2)
  
  df[,binary_to_factors] <- lapply(df[,binary_to_factors], factor)
}

df$grade <- as.factor(df$grade)  # Convert "grades" to factor


# ==== Perform data transformations

df <- df %>% 
  mutate_if(is.numeric
            , list(r = function(x)(1/(x+1)-1),  # recipricol transform
                   l = log1p,  # log transform
                   sqrt = sqrt, # square root transform
                   sq = function(x)(x**2), #square transform
                   z = function(x)((x-mean(x))/sd(x)), # z-normalize
                   bc = function(x) (BoxCox(x, BoxCox.lambda(x))) #box-cox transform
                   )
            )

# =




# ===== End Data Prep




# =============================================================================
# ============================= Analysis ======================================
# =============================================================================

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
    fname <- file.path(filepath_plots,
                       paste(colnames(df[1]), "_", counter, ".png", sep = ""))
    
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
      var_cor <- paste("Correlation:  ", round(cor(df)[2],4), sep="")
      mtext(var_cor, side = 3, line = 2, adj = 0, cex = 1)
      
      # === histograms
      
      
      fname <- file.path(filepath_hist, 
                         paste(colnames(df[1]), "_hist_", counter, ".png", sep = ""))
      
      png(fname)
      plotNormalHistogram(df[,1])
      dev.off()
      
    }
    
    
    mtext(equation, side = 3, line = 1, adj = 0, cex = 1)
    mtext(model_summary, side = 3, line = 0, adj = 0, cex = 1)
    
    dev.off()
    
    
    
  }
  
  
  
  for(counter in 2:ncol(x_var_data))
  {
    first_order_investigation(y_var_data, x_var_data, counter)  
  }
}

# ====== Correlation Matrix

if(correlation_matrix == TRUE)
{
  numeric_df <- select_if(df[,-c(1)], is.numeric)
  correlation_matrix <- cor(numeric_df, use = "complete.obs")
  
  corr_matrix_out_file <- "Correlation_Matrix.csv"
  
  write.csv(correlation_matrix, file = file.path(fpath, 'Analysis_Out'
                                                 ,corr_matrix_out_file))
}