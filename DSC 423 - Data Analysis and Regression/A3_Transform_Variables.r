library(forecast)
library(dplyr)

directory <- file.path("c:", "Users", "smpat",'desktop','school',
                       "CSC 323 - Data Analysis and Regression", 
                       "Assignments", "Assignment 4", "Remission")


# ---- Assign data set
dir_data_in <- file.path(directory, "Raw Data", "cleaned_data.csv")

y_var_index <- 24 # This is used to identify the variable

# ---- load data
df <- read.csv(file.path(dir_data_in, data_filename))

# get col name of y_var
y_var_colname <- colnames(df[y_var_index])

# move y var to front
df <- df%>%
  select(all_of(y_var_colname), everything())

# ===================

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

# --- Convert variables to factors
binary_to_factors <- 
  df[sample(nrow(df),min(1000,nrow(df))),] %>%    
  sapply(.,function(col) length(unique(col)) == 2)

df[,binary_to_factors] <- lapply(df[,binary_to_factors], factor)

df$grade <- as.factor(df$grade)  # Convert "grades" to factor



# ===========  Transformations =============


idcols <- c("readingScore","studentsInEnglish", "minutesPerWeekEnglish","schoolSize")
cols <- c(idcols, names(df)[-which(names(df)%in%idcols)])
df <- df[,cols]


df[,2] <- BoxCox(df[,2], BoxCox.lambda(df[,2]))
df[,3] <- df[,3]**.5 #sqrt transform
df[,4] <- df[,4]**.5 #sqrt transform

names(df)[2] <- paste(colnames(df)[2],"_bc", sep = "")
names(df)[3] <- paste(colnames(df)[3],"_sqrt", sep = "")
names(df)[4] <- paste(colnames(df)[4],"_sqrt", sep = "")

write.csv(df, file.path(directory,"Raw Data", "pisa2009_transformed.csv"), row.names=FALSE)
