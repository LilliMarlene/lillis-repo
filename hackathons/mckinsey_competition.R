#install.packages("randomForest")
require(randomForest)

#import datasets
train = read.csv("/Users/lilli-marlenelaudahn/Downloads/train_ZoGVYWq.csv",sep = ",", header = T)
test= read.csv("/Users/lilli-marlenelaudahn/Downloads/test_66516Ee.csv",sep = ",", header = T)

#remove id variable in train dataset
train$id <- NULL

#remove missing values in train dataset
train <- na.omit(train)

#fit random forest model
fit <- randomForest(train$renewal ~ .,
                    data=train, 
                    importance=T, 
                    ntree=100)

# replace missing values in underwriting score variable with median value
test[is.na(test$application_underwriting_score),"application_underwriting_score"]<-99.21
test[is.na(test$Count_3.6_months_late),"Count_3.6_months_late"]<-0
test[is.na(test$Count_6.12_months_late),"Count_6.12_months_late"]<-0
test[is.na(test$Count_more_than_12_months_late),"Count_more_than_12_months_late"]<-0

#predict on test dataset
test$renewal <- predict(fit, test)

# finding the optimal incentive

# prämissen
# effort = 10*(1 - exp(-incentive/400))
# improvement = 20*(1 - exp(-effort/5))
# revenue = (test$renewal + improvement) * (test$premium - incentive)

#abbruch bedingungen: 
# 1: improvement + renewal >= 1 (?)
# 2: premium - incentive <= 0
# 3: revenue < previous_revenue

# custom function 
optimal_incentive <- function(renewal_probability, premium, incentive, previous_revenue){
  effort = 10*(1 - exp(-incentive/400))
  improvement = 20*(1 - exp(-effort/5))
  revenue = (renewal_probability + improvement) * (premium - incentive)
  if
  (improvement + renewal_probability >= 1) {
    return(incentive)
    } 
   else if 
  (premium - incentive <= 0) {
    return(incentive)
  }
  else if (is.na(revenue)) {
    return(NA)
  }
  else if (revenue < previous_revenue) {
    return(incentive)
  }
  else {
    return (optimal_incentive(renewal_probability, premium, incentive + 1 , revenue))
  }
}

# apply custom function on test dataset
test$incentives <- mapply(optimal_incentive, 
                          renewal_probability = test$renewal, 
                          premium = test$premium , 
                          incentive = 0,
                          previous_revenue = 0)

require(dplyr)
submission <- select(test, "id", "renewal", "incentives")

write.csv(submission, "/Users/lilli-marlenelaudahn/Downloads/submission (2).csv",row.names = F )


