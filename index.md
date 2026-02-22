---
layout: default
title: Regional Game Preference
---
# Analysis of Game Preference by Region using Steam Reviews

### Introduction
I believe that using language data from steam reviews, we can answer some interesting questions regarding game sentiment in regions. 

1. Are there any games which dominate a region?

2. Are there games which are loved in one region but hated in another?

3. Are there specific game genres which are more well received in certain regions?

These questions can help game publishers and developers make better informed decisions about what regions to prioritize support for.

### Assumptions Made
A language roughly corresponds to a region. So I'm assuming chinese reviews are coming from China, and English reviews are coming from English speaking countries.

This assumption is not perfect. It is possible for a review to be written in English by a Chinese gamer. But, I believe this analysis is still valid regardless of the fact.

Games with less than 10000 total reviews are ignored

### Our Regions
[Map of Regions]

Note that because English is adopted across multiple regions, it spans multiple countries which could be considered as part of separate regions. For this analysis, I define an English-Speaking region knowing that this is a very broad definition.

### Region Review Distribution
![region_pie](/Users/david/Downloads/images/screenshot-000067-2026.png)

The majority (41.92%) of reviews come from English speaking countries. This is partially because of how broad this 'region' is. Other notable regions are China (17.29%), CIS (Ukraine + Russia) (13.39%), and Western Europe (10.94%). Note that because English is the primary language in the UK, it is included as part of the English-speaking region instead of Western Europe.

### Popularity and Sentiment
The two main values on which I am running my analysis are popularity and sentiment.

Popularity: How popular is this game in this region?
Sentiment: How well received is this game in this region?

#### Popularity
Popularity is taken by taking the proportion of reviews a game has for all of a regions reviews, over the proportion of reviews that game makes up globally.

(region_game_reviews / region_total_reviews) / (global_game_reviews / global_total_reviews)

To reduce right skew, I use Log(Popularity)

A postive value means the game is more popular in this region, negative means the game is less popular in this region, and a 0 value means its as popular as it should be.

So for example, Counter Strike has X reviews globally, with X reviews in Poland.
Polish Counter Strike reviews make up X% of Polands total reviews, and Counter Strike makes up X% of global reviews.

Taking the quotient of these values shows us that Poland has a far larger amount of reviews for this game compared to the rest of the world.


#### Sentiment
Sentiment is the percentage of reviews which are positive in a region.

(region_game_positive_reviews / region_game_total_reviews)

### Games that Dominate


### Genres

### Some Outliers

<div class='tableauPlaceholder' id='viz1771783617838' style='position: relative'>
<noscript>
<a href='#'>
<img alt='Popularity vs Sentiment Scatter ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;SteamReviewRegionalAnalysis&#47;PopularityvsSentimentScatter&#47;1_rss.png' style='border: none' />
</a></noscript>
<object class='tableauViz'  style='display:none;'>
<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
<param name='embed_code_version' value='3' /> 
<param name='site_root' value='' />
<param name='name' value='SteamReviewRegionalAnalysis&#47;PopularityvsSentimentScatter' />
<param name='tabs' value='no' /><param name='toolbar' value='yes' />
<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;SteamReviewRegionalAnalysis&#47;PopularityvsSentimentScatter&#47;1.png' />
<param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
<param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
<param name='display_count' value='yes' /><param name='language' value='en-US' />
<param name='filter' value='publish=yes' /></object></div>
<script type='text/javascript'>
var divElement = document.getElementById('viz1771783617838');
var vizElement = divElement.getElementsByTagName('object')[0];
vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


