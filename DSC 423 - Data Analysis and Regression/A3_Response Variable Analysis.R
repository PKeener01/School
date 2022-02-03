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
y_var_nicename <- "MPW English"   # This is used to label graphs

convert_binaries = TRUE # if false, the data set will skip automatic conversion



# =============================================================================
# ============================= Data Preparation ==============================
# =============================================================================

# -- initialize libraries
library(stringi)
library(dplyr)
library(rcompanion)
library(forecast)


# ---- Create file structure
filepath_plots <- file.path(fpath, 'Analysis_Out', 'Graphs', 'Plots')
filepath_hist <- file.path(fpath, 'Analysis_Out', 'Graphs', 'Histograms')

dir.create(file.path(fpath, 'Analysis_Out'))
dir.create(file.path(fpath, 'Analysis_Out', 'Graphs'))
dir.create(filepath_plots)
dir.create(filepath_hist)


# read in data
df <- read.csv(file.path(fpath, data_filename))

# get col name of y_var
y_var_colname <- colnames(df[y_var_index])

# move y var to front
df <- df%>%
  select(all_of(y_var_colname), everything())

y_var_index <- 1
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



# move y var to front
df <- df%>%
  select(y_var_index)

# include only data where the depedent variable has values
#df <- df[is.na(df[1])==FALSE,]

# get col name of y_var
y_var_colname <- colnames(df[1])




# ==== Convert binary variables to factors
# select 1000 random rows from DF and check the number of unique values
# if there are only 2 unique values then convert the column to factor


df <- df %>%
  mutate_if(is.numeric
            , list(r = function(x)(1/(x+1)-1),  # recipricol transform
                   l = log1p,  # log transform
                   sqrt = sqrt, # square root transform
                   sq = function(x)(x**2), #square transform
                   bc = function(x) (BoxCox(x, BoxCox.lambda(x))) #box-cox transform
            )
  )


counter <- 0

for (counter in 1:ncol(df))
  {
# === histograms
fname <- file.path(filepath_hist,
                   paste(counter, "_hist_", y_var_nicename, ".png", sep = ""))

skew <- paste("Skew:  ", round(skewness(df[,counter]),4))
kurt <- paste("Kurtosis:  ", round(kurtosis(df[,counter]),4))

png(fname)
plotNormalHistogram(df[,counter], xlab = colnames(df[counter])
                    , cex.lab = 1.5, cex.axis = 1.5)
mtext(skew, side=3, line=2, adj=0, cex = 1.5)
mtext(kurt, side=3, line=1, adj=0, cex = 1.5)

dev.off()

}