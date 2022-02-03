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

# Generate correlation matrix of all numeric variables
correlation_matrix <- TRUE


# ---- User Filepath Inputs.  Automatically inserts the "/" between commas.
directory <- file.path("c:", "Users", "smpat",'desktop','school',
                       "CSC 323 - Data Analysis and Regression", 
                       "Group Project", "Analysis")


# ---- Assign data set
dir_data_in <- file.path(directory, "Raw Data", "cleaned_data.csv")

# === Note: file read from directory + data_filename

# ---- Assign dependent/response variable
y_var_index <- 8 # This is used to identify the variable
y_var_nicename <- "GDP Per Capita"   # This is used to label graphs

convert_binaries = TRUE # if false, the data set will skip automatic conversion

# =============================================================================
# ============================= Data Preparation ==============================
# =============================================================================


# ---- Create file structure
filepath_plots <- file.path(directory, 'Analysis_Out', 'Graphs', 'Plots')
filepath_hist <- file.path(directory, 'Analysis_Out', 'Graphs', 'Histograms')

dir.create(file.path(directory, 'Analysis_Out'))
dir.create(file.path(directory, 'Analysis_Out', 'Graphs'))
dir.create(filepath_plots)
dir.create(filepath_hist)


# -- initialize libraries
#
library(stringi)
library(plyr)
library(dplyr)
library(forecast)
library(rcompanion)
library(moments)

# if(!require(rcompanion)){install.packages("rcompanion")}
# library(ggplot2)
# library(olsrr)
# library(mosaic)
# --

# read in data
df_in <- read.csv(dir_data_in, row.names = 1)
y_var_index <- match('GDP.per.capita..current.US..', names(df_in))
# ***********  include only data where the depedent variable has values
df <- df_in[is.na(df_in$GDP.per.capita..current.US..)==FALSE,]



# get col name of y_var
y_var_colname <- colnames(df[y_var_index])


# move y var to front
df <- df%>%
  select(y_var_index, everything())

# ==== Convert binary variables to factors
# select 1000 random rows from DF and check the number of unique values
# if there are only 2 unique values then convert the column to factor

if(convert_binaries==TRUE)
{
  binary_to_factors <- 
    df[sample(nrow(df),min(1000,nrow(df))),] %>%    
    sapply(.,function(col) length(unique(col)) == 2)
  
  df[,binary_to_factors] <- lapply(df[,binary_to_factors], factor)
}


df$Region <- as.factor(df$Region)

# -- log scale GDP per capita

df$GDP_PC_L <- log1p(df$GDP.per.capita..current.US..)
df <- df[,-1]

df <- df%>%
  select(GDP_PC_L, everything())

y_var_colname <- colnames(df)[1]
y_var_index <- 1
y_var_nicename <- "Log GDP Per Capita"
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
      
      plot(df, pch = 18, cex.lab = 1.5, cex.axis = 1.5, col = "steelblue2"
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
        plotNormalHistogram(df[,1], xlab = colnames(df[1]), col = "steelblue2")
        skew <- paste("Skew:  ", round(skewness(df[,1]),4))
        kurt <- paste("Kurtosis:  ", round(kurtosis(df[,1]),4))
        
        mtext(skew, side=3, line=2, adj=0)
        mtext(kurt, side=3, line=1, adj=0)
        
        dev.off()
        
        # ===== binned data
        fname <- file.path(filepath_plots,
                           paste(counter, "_binned_", colnames(df[1]), ".png", sep = ""))
        
        png(fname)
        
        df$x_var_buckets <-round_any(df[,1], 5)
        df <- df[order(df[,3]),]
        df2 <- df %>%
          group_by(x_var_buckets) %>% summarize(count=n())
        
        plot(df[1:2], pch = 18, cex.lab = 1.5, cex.axis = 1.5, col = "steelblue2"
             ,ylab = y_var_nicename)
        par(new=TRUE)
        plot(df2, pch = 17, col = 'red', type = 'line', lwd = 2,
            axes = FALSE, xlab = "", ylab = "")
        
        axis(side = 4, at = pretty(range(df[,3])), cex=1.5)
        mtext("Count", side = 4, line = 3, cex = 1.5)
        
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

# ====== Correlation Matrix

if(correlation_matrix == TRUE)
  {
    numeric_df <- select_if(df[,-c(1)], is.numeric)
    correlation_matrix <- cor(numeric_df, use = "complete.obs")
    
    corr_matrix_out_file <- "Correlation_Matrix.csv"
    
    write.csv(correlation_matrix, file = file.path(directory, 'Analysis_Out'
                                                   ,corr_matrix_out_file))
 }