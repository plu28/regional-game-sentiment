## Addressing Feedback

#### 1. Professor Feedback

Feedback #1: Artifacts and missing visualizations.  
Resolution: Discussed over slack. No artifacts on Github Pages where the analysis is hosted.

---

#### 2. Jazzy's Feedback

Feedback #2: Breadth of English speaking countries being too wide.  
Resolution: I can't really do anything about this one. The dataset doesn't tie a region to a review so the only way I can correlate a review to a region is through its language. And unfortunately, 17th century British colonialism has resulted in many disconnected regions being primarily English.

Feedback #3: Visualizations are too congested  
Resolution: Modified heatmaps to have games as rows so the full game name is readable. Also divided them into Regions/Country/Language.

Feedback #4: Review count not shown which could affect credibility of analysis  
Resolution: Added review count tooltip to visualizations.

Feedback #5: No sentiment over time visualization to justify claims of review bombing  
Resolution: I can't make a visualization that could provide any meaningful insight with this data. Overwatch 2 was only listed on steam August 10, 2023. It immediately had negative reviews from Chinese players. I have no data on previous Chinese ratings to compare to. Regardless, this still shows an interesting story where Chinese players immediately review bombed the game in protest of Blizzard exiting the Chinese market.

---

#### Connor's Feedback

Feedback #6: No introduction for visual aids  
Resolution:

Feedback #7: Adding a background section  
Resolution:

Feedback #8: No link to data source  
Resolution:

Feedback #9: "Games so popular that they've had a cultural impact on a country"  
Resolution:

Feedback #10: Elaborate more on the language assumption  
Resolution:

Feedback #11: No explanation for the amount of missing regions  
Resolution:

Feedback #12: Pie chart being a bad way to represent regions  
Resolution: We can use a histogram instead

Feedback #13: Rendering popularity/sentiment formulas in latex instead of in plaintext  
Resolution:

Feedback #14: Not using playtime to determine popularity/sentiment.  
Resolution: This is a fair point but I don't think playtime is a perfect signal of sentiment/popularity. Sentiment changes overtime. A hardcore player might have 3000 hours on Overwatch, but hate the game and write a negative review after a recent update removed his favorite character or something. Just because he has 3000 hours doesn't mean I should evaluate that review as having positive sentiment. Also for popularity, I'm worried about the potential of 'hardcore' players to skew results. Someone might love a game and leave a positive review with 3000 hours. Another person might play the game for 5 hours, realize they don't like it, and leave a negative review. Should the negative review be weighed as less valuable for sentiment/popularity in this case? I do think playtime could be an interesting metric for answering other questions outside my hypothesis, but for the sake of keeping my report concise, I've decided to leave it out.

> Again, you make this claim while assuming that the reader knows what Counter Strike is. Although a popular game, I would suggest giving some context to it before your visual. This context should include what type of game it is, why it is popular, and some history of the game to back this up.  

Feedback #15: No background on Counter Strike  
Resolution:

> You mention that this results aligns with your expectations, but do not provide proof that many of the world's top Counter Strike players originate from these regions. When you say this are you specifically talking about pro players in leagues such ESL/PGL, or does this statement include players from the Counter Strike premier leaderboards or Faceit leaderboards? There are a lot of possibilities here, and some further insight would significantly improve this conclusion.  

Feedback #16: Didn't explain why results align with my expectations.  
Resolution:

> You mention an esports ecosystem that exists only in Asian countries, but what exactly do you mean by this? Are you referring to the shear amount of money in esports in Asian countries?  
Feedback #17: Not clear on how NARAKA only has an esports ecosystem in Asia  

Resolution:

> While this is an interesting conclusion, this could be more interesting if you could match the timeline of these events with reviews that back this claim. Maybe a visual showing how your sentiment calculation changes over time both before and after this period where Overwatch was taken offline in China. Or perhaps just simply how the proportion of positive and negative reviews change over time in China.  

Feedback #18: No sentiment over time visualization to justify claims of review bombing (duplicate of feedback #5) 
Resolution:

> Is there anything in particular about these games that may indicate why Asian countries have such strong standards? Are there perhaps any signs that these "standards" could have been a result of review bombing?

Feedback #19: Explain why Asian countries have strong standards. Are they just review bombing a bunch of games? Go deeper on this section
Resolution: I should've been more clear about how I reached my conclusion in this section and tried. Also, with how consistent 

Feedback #20: Add comparisons to global logPopularity values in conclusion

> Adding something like this to your graph might bring some interesting conclusions
Feedback #21: Adding more detail the extra scatter plot
Resolution: 

#### 3. Hunter's Feedback

Feedback #22: No explanation for the amount of missing regions (duplicate of feedback #11)
Resolution:

> For your popularity and sentiment calculations, you forget to mention that you use a log transformation. So your descriptions of what 0 means don't match up with the formula; it only matches after your log calculation which you used in your heatmap plots. 
Feedback #23: Didn't mention the log transformation and descriptions didn't match. 
Resolution

> Also might be nitpicky of me, but it could be nice if the game titles could be turned 45 or 90 deg just so someone looking for a specific game doesn't need to hover over the truncated titles to see if its the correct one. Fullscreen on my laptop I only see a single character (A.., A.., A.., B..., etc). The plots look great though I think it could just be a nice QOL touch. 
Feedback #24: Rotate titles 90deg so they aren't truncated to their first letter
Resolution: 

> For your results section, it would be nice to see some possible reasonings for why you believe CS is so popular in Eastern Europe. You did a really good job of this in the following Nakara section, so I think giving this the same treatment would help answer the question a reader may have as to why thats the case. 
Feedback #25: Didn't explain why results align with my expectations (duplicate of feedback #16)
Resolution:

Feedback #26: Embed visualization for Overwatch 2 in China 
Resolution:

Feedback #27: Duplicate apex legends in Taiwan in conclusion
Resolution:1

>In your last section you provide a scatterplot. Even though you're deeming this an extra, I think it would still benefit to explain what might be some possible take aways from the plot, and maybe explain how someone should go about interpreting it. 
Feedback #28: Add more to the extra scatter plot
Resolution: 

>At the start of the analysis, you hypothesize (for part 2.) that there may be games that are generally considered good, but may have reasons such as discriminating another region. In your conclusion however you don't really seem to connect it back to that specific initial hypothesis, only that there are games which are liked everywhere but here. Other than your reasonings for Overwatch2 and Rocket League. I think even giving a brief explanation of the others, and possibly linking to your hypothesis to see if any of those were results of discrimination somehow.
Feedback #29: Elaborate more on the results for the second hypothesis
Resolution: 

#### 4. Theo's Feedback

> There is a grammatical error in the first hypothesis: “Games so popular that they’ve had a cultural impact on a country.” I think it is better worded as “Some games are so popular that they’ve had a cultural impact on countries.”
Feedback #29: "Games so popular that they've had a cultural impact on a country" (duplicate of feedback #9) 

>  I realized later that all the English speaking countries have the same values, which means that there's a bunch of duplicate information in your heatmaps. I know you were able to get to country level granularity for other countries so I would either just condense all english speaking countries into one column in your heatmaps or have a disclaimer because I think its misleading as is.
Feedback #30: Confusing duplicate data 

>I am also curious why you lumped all countries with different languages such as Western Europe into regions but chose not to for Japan, Korea and China. Is it market size? I think you should explain your reasoning or go with one or the other for consistency.
Feedback #31: Regions are broken

> Next, when reading through your whitepaper, I was wondering how you differentiated between Portuguese reviews and Brazilian Reviews or Mexican reviews versus Spanish reviews. Since those country pairs have the same dominant language I expected a similar feedback to english-speaking countries but I see that the dataset actually differentiates between them so I would consider calling those out to avoid confusion to the reader.
Feedback #32: Spanish regions and overlap between disparate countries
Resolution:

> It also seems like the 2nd assumption of “Games with less than 10000 total reviews are ignored” cuts down the list of games to a pretty small number (I’m assuming this is all the games that are in the heatmap) so just giving the number of games being analyzed after filtering out those under 10,000 total reviews would be helpful to the reader.
Feedback #33: Number of games after filtering out would be good

> Lastly, I think you should have also noted that some country game combinations had no data associated with them ex: Mirror 2: Project X and most European countries as in the heatmaps Its hard to tell since missing data just shows a white cell and I didn’t figure it out until I looked closely at one of your maps.
Feedback #34: Need to do a better job filtering out games.

> The first problem I found is that you switch your analysis over to countries, but refer to them as regions. This is confusing as you spent your last section talking about grouping countries into regions.
Feedback #35: Lack of consistency with regions

>I found the heatmaps to be a really cool visualization, but difficult to read. In the heatmap, only the first letter of a game is possible to be read so we can’t see what game each column corresponds to without hovering over the top. I would recommend swapping games to be the row and country to be the column and then instead of country level heatmaps, aggregate so its region level heatmaps from the regions you defined in the beginning. This would make the heatmaps much easier to read since there is less data without fully flattening data.
Feedback #36: Rotate titles 90deg so they aren't truncated to their first letter (similar to feedback #24)

> Lastly, in your heatmaps the countries are ordered alphabetically, when it would make more sense for them to be grouped by region. You say “The first thing to note is the lack of variance in sentiment across regions.” Looking for this pattern in the heatmap is easier if the regions are already grouped rather than having to jump across looking for Finland, then Norway, then Sweden for the Nordic countries as an example.
Feedback #37: Add better visualization for making conclusions between regions

> I would provide a source of some kind showing that CS:GO pros tend to be from eastern europe just so that the reader doesn’t have to just take your word for it.
Feedback #38: Didn't explain why results align with my expectations (duplicate of feedback #16)

> I would include a visual to make what happened easier to follow.
Feedback #39: Embed visualization for Overwatch 2 in China (duplicate of feedback #26)
Resolution:

> I would say East Asian Countries instead of Asian since you also have SEA as a region where all those countries are still considered Asian countries.
Feedback #40: Separate east asian from south east asian
Resolution:

> It would have been interesting to do some comparison between your two measurements. For example, are popular games in a certain region more likely to be well liked as well?
Feedback #41: Compare popularity to sentiment and try to draw conclusions
Resolution:

> You accidentally repeated “Apex Legends in Taiwan (Global 79% positive, Taiwan 48% positive)” twice.
Feedback #42: Duplicate apex legends in Taiwan in conclusion (duplicate of feedback #27)
Resolution:


