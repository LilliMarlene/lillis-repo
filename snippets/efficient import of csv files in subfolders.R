#load libraries to efficiently import all csv files from folder
require(tidyverse)
require(dplyr)

#specify directory that contains the files to be imported
# requirement is that all files have to be in one folder with no sub-directories
read_plus <- function(flnm) {
  read_csv(flnm) %>% 
    mutate(filename = flnm)
}

#read all csv files and append filenames
marketing_data <-
  list.files(path, pattern = "*.csv", 
             recursive = T,
             full.names = T) %>% 
  map_df(~read_plus(.))