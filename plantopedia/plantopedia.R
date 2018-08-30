# retrieve plant names (scientific name and used name)
#install.packages('rvest')
require('rvest')
url <- 'http://pflanzen-lexikon.com/index.php?c=wissenschaftlich-z&l=de'
webpage <- read_html(url)
names_data_html <- html_nodes(webpage,'strong')
name_data <- html_text(names_data_html)
name_data_all <- rbind(name_data_all, name_data)

# cleaning names
name_data_all <- as.data.frame(name_data_all)
name_data_all <- unlist(name_data_all[], use.names = FALSE)
name_data_all <- subset(name_data_all, name_data_all != "Hinweis:")
plants <- data.frame(id = c(1:length(name_data_all)), full_name = name_data_all)
delim <- data.frame(do.call('rbind', strsplit(as.character(plants$full_name),'(',fixed=TRUE)))
plants$name <- gsub(")", "", delim$X2)
plants$name_scientific <- delim$X1
plants$name_lang <- ifelse(grepl("en: ", plants$name)== T,"en","de")
plants$name <- gsub("en: ", "", plants$name)
require(dplyr)
plants <- select(plants, "full_name", "name", "name_scientific", "name_lang")
plants <- unique(plants)
plants$id <- c(1 : nrow(plants))

write.csv(plants, "plants_pflanzen-lexikon.com.csv")

# retrieve plant care information 
url <- 'https://www.compo.de/de/de/pflanzenratgeber/pflanzen/efeu.html'
webpage <- read_html(url)
caretext_html <- html_nodes(webpage,'p')
caretext_data <- html_text(caretext_html)
caretext_data <- subset(caretext_data, caretext_data != "")
caretext_data <- caretext_data[!caretext_data %in% caretext_data[1:4]]
caretext_data <- caretext_data[caretext_data %in% caretext_data[1:6]]
care_header_html <- html_nodes(webpage,'h2')
care_header_data <- html_text(care_header_html)
care_header_data <- care_header_data[!care_header_data %in% care_header_data[1:2]]
care_header_data <- care_header_data[!care_header_data %in% care_header_data[3]]
care_header_data <- care_header_data[!care_header_data %in% care_header_data[4]]
care_header_data <- care_header_data[!care_header_data %in% care_header_data[6:9]]
care_header_data <- append(care_header_data, "Warnhinweis")
care <- data_frame( category = care_header_data, text = caretext_data)
require(data.table)
tcare <- setNames(data.table(t(care[,-1])), care[["category"]])
tcare$name <- gsub("https://www.compo.de/de/de/pflanzenratgeber/pflanzen/", "", url)
tcare$name <- gsub(".html", "", tcare$name)

# create final dataset
PlantCare <- data.frame(tcare)
plants$name <- tolower(plants$name)
PlantsAndCare <- merge( x = plants, y = PlantCare, by = "name", all.x = T)

# ask user what plant he's interested in
userInput <- function(){
  my.plant <- readline(prompt="Welche Pflanze suchst du? ")
  myPlantInfo <- subset(PlantsAndCare, tolower(PlantsAndCare$name) == tolower(my.plant))
  myPlantOutput <- paste(
    "Deine Pflanze ist ", myPlantInfo$full_name, 
  ". Wo steht er am liebsten? " ,myPlantInfo$Standort,
  " Wann pflanzt man ihn ? " ,myPlantInfo$Pflanzen,
  " Wie gießt man ihn ? " ,myPlantInfo$Bewässerung,
  " Wie beschneidet man ihn ? " ,myPlantInfo$Schnittmaßnahmen,
  " Ist er winterhart ? " ,myPlantInfo$Überwinterung,
  " Warnhinweis: ",myPlantInfo$Warnhinweis)
  
  if (tolower(my.plant) %in% tolower(PlantsAndCare$name)) {
    return(myPlantOutput)} 
  else {
    return("Entschuldige, von dieser Pflanze habe ich noch nicht gehört...")
  }
}

userInput()

