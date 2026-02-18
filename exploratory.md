# Exploratory Analysis of Steam Review Data


### Questions
1. **What dates the data spans (approximate)**
Early 2011 to Late 2023

2. **What regions the data has reviews from**
Review's dont specify specific regions wherethe review was made, but you can associate a review to a region via the language the review was written in.

List of languages:
Brazilian
Bulgarian
Czech
Danish
English
Finnish
French
German
Greek
Hungarian
Italian
Japanese
Korean
Latam
Norwegian
Polish
Portuguese
Romaninan
Russian
Simplified Chinese
Spanish
Swedish
Traditional Chinese
Thai
Turkish
Ukrainian
Vietnamese

Region Representation in Dataset
Looks like its mostly English (~45%) with a good amount of Chinese (~15%) and Russian (~11%)

Positive to negative reviews
About 85% are positive reviews, 15% negative reviews.

Amount of games
Around 3000 games

### Quality Issues
Looks like review time is given as time since epoch. Will have to convert to datetime if I end up needing this field.

The same language might span different regions. Say a review written in English but by a reviewer in Russia.

Dataset is extremely large. Compressed to parquet and only included the columns that I'll need for my analysis (~43GB --> 80MB) in data_cleaning.py

Otherwise, for the columns that I need for my analysis (game, language, voted_up), this data is perfectly clean. 


