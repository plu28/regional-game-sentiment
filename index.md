---
layout: default
title: Steam Games Regional Sentiment 
---
# Analysis of Game Preference by Region using Steam Reviews

## Introduction and Hypothesis
I believe that using language data from steam reviews, we can answer some interesting questions regarding game sentiment in regions. 

1. What games are beloved by a country?
    - Games so popular that they've had a cultural impact on a country.
    - For example, Counter Strike has had a cultural impact in Eastern European countries, and I know Rocket League is also very strong in the french community.

2. Are there games which are liked in one region but hated in another?
    - I think there will be good games that might've done something to discriminate a particular region. 

# How the Analysis Was Done

## Assumptions
1. A language roughly corresponds to a region. So I'm assuming chinese reviews are coming from China, and English reviews are coming from English speaking countries.
    - *This assumption is not perfect. It is possible for a review to be written in English by a Chinese gamer. Regardless, I believe this analysis can still yield some interesting results.*

2. Games with less than 10000 total reviews are ignored

## Regions
<div class="tableauPlaceholder" 
     id="viz1771784930728" 
     style="position: relative">

  <noscript>
    <a href="#">
      <img alt="Region Map"
           src="https://public.tableau.com/static/images/St/SteamReviewRegions/RegionMap/1_rss.png"
           style="border: none" />
    </a>
  </noscript>

  <object class="tableauViz" style="display:none;">
    <param name="host_url" value="https://public.tableau.com/" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />
    <param name="name" value="SteamReviewRegions/RegionMap" />
    <param name="tabs" value="no" />
    <param name="toolbar" value="yes" />
    <param name="static_image"
           value="https://public.tableau.com/static/images/St/SteamReviewRegions/RegionMap/1.png" />
    <param name="animate_transition" value="yes" />
    <param name="display_static_image" value="yes" />
    <param name="display_spinner" value="yes" />
    <param name="display_overlay" value="yes" />
    <param name="display_count" value="yes" />
    <param name="language" value="en-US" />
    <param name="filter" value="publish=yes" />
  </object>
</div>

<script type="text/javascript">
  var divElement = document.getElementById("viz1771784930728");
  var vizElement = divElement.getElementsByTagName("object")[0];

  vizElement.style.width = "100%";
  vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

  var scriptElement = document.createElement("script");
  scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";

  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

Note that because English is adopted across multiple regions, it spans multiple countries which could be considered as part of separate regions. For this analysis, I define an English-Speaking region knowing that this is a very broad definition.

## Region Review Distribution
<div class="tableauPlaceholder"
     id="viz1771785040592"
     style="position: relative">

  <noscript>
    <a href="#">
      <img alt="Region Review Distribution"
           src="https://public.tableau.com/static/images/St/SteamReviewPie/RegionReviewDistribution/1_rss.png"
           style="border: none" />
    </a>
  </noscript>

  <object class="tableauViz" style="display:none;">
    <param name="host_url" value="https://public.tableau.com/" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />
    <param name="name" value="SteamReviewPie/RegionReviewDistribution" />
    <param name="tabs" value="no" />
    <param name="toolbar" value="yes" />
    <param name="static_image"
           value="https://public.tableau.com/static/images/St/SteamReviewPie/RegionReviewDistribution/1.png" />
    <param name="animate_transition" value="yes" />
    <param name="display_static_image" value="yes" />
    <param name="display_spinner" value="yes" />
    <param name="display_overlay" value="yes" />
    <param name="display_count" value="yes" />
    <param name="language" value="en-US" />
    <param name="filter" value="publish=yes" />
  </object>
</div>

<script type="text/javascript">
  var divElement = document.getElementById("viz1771785040592");
  var vizElement = divElement.getElementsByTagName("object")[0];

  vizElement.style.width = "100%";
  vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

  var scriptElement = document.createElement("script");
  scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";

  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

The majority (41.92%) of reviews come from English speaking countries. This is partially because of how broad this 'region' is. Other notable regions are China (17.29%), CIS (Ukraine + Russia) (13.39%), and Western Europe (10.94%). Note that because English is the primary language in the UK, it is included as part of the English-speaking region instead of Western Europe.

## Popularity and Sentiment
The two main values on which I am running my analysis are popularity and sentiment.

Popularity: How popular is this game in this region?
Sentiment: How well received is this game in this region?

#### Popularity
Popularity is taken by taking the proportion of reviews a game has for all of a regions reviews, over the proportion of reviews that game makes up globally.

This tells us how much a games popularity deviates from the norm for a region. 

(region_game_reviews / region_total_reviews) / (global_game_reviews / global_total_reviews)

A postive value means the game is more popular in this region, negative means the game is less popular in this region, and a 0 value means its as popular as it should be.

<div class="tableauPlaceholder" id="viz1771885401652" style="position: relative">
    <noscript>
        <a href="#">
            <img 
                alt="Popularity Heatmap"
                src="https://public.tableau.com/static/images/St/SteamReviewPopHeatmap/PopularityHeatmap/1_rss.png"
                style="border: none;" 
            />
        </a>
    </noscript>
    <object class="tableauViz" style="display:none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="SteamReviewPopHeatmap/PopularityHeatmap" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/St/SteamReviewPopHeatmap/PopularityHeatmap/1.png" />
        <param name="animate_transition" value="yes" />
        <param name="display_static_image" value="yes" />
        <param name="display_spinner" value="yes" />
        <param name="display_overlay" value="yes" />
        <param name="display_count" value="yes" />
        <param name="language" value="en-US" />
        <param name="filter" value="publish=yes" />
    </object>
</div>

<script type="text/javascript">
    var divElement = document.getElementById("viz1771885401652");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

Visualizing popularity on a heatmap. The more red the tile, the less popular the game is than usual and vice versa for green tiles.

Rows are countries, columns are games.

The more varied a column is in its color, the more varied its popularity is region wide.

The first thing to note is how varied the popularity is across regions. If games were equally popular in most regions, then the heatmap would be mostly white. 

Counter Strike is a good example of this where the game is extremely popular in Eastern Europe (Romania especially) compared to other countries.

#### Relative Sentiment
Sentiment is calculated similarly to popularity, but using the positive review percent metric instead.

This tells us if the amount of positive reviews for a game deviate from the norm for a region.

(region_game_positive_reviews / region_game_total_reviews) / (global_game_positive_reviews / global_game_reviews)

A positive value means the game has more positive reviews in this region than normal, negative means the game has more positive reviews than normal, and a 0 means its positive reviews are normal. 

<div class="tableauPlaceholder" id="viz1771885508101" style="position: relative;">
    <noscript>
        <a href="#">
            <img
                alt="Sentiment Heatmap"
                src="https://public.tableau.com/static/images/St/SteamReviewSentHeatmap/SentimentHeatmap/1_rss.png"
                style="border: none;"
            />
        </a>
    </noscript>
    <object class="tableauViz" style="display: none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="SteamReviewSentHeatmap/SentimentHeatmap" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/St/SteamReviewSentHeatmap/SentimentHeatmap/1.png" />
        <param name="animate_transition" value="yes" />
        <param name="display_static_image" value="yes" />
        <param name="display_spinner" value="yes" />
        <param name="display_overlay" value="yes" />
        <param name="display_count" value="yes" />
        <param name="language" value="en-US" />
        <param name="filter" value="publish=yes" />
    </object>
</div>

<script type="text/javascript">
    var divElement = document.getElementById("viz1771885508101");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

The more red the tile, the more that country deviates towards negative from the games positive percentage globally, and vice versa for green tiles.

Rows are countries, columns are games.

The first thing to note is the lack of variance in sentiment across regions. This implies that a games sentiment does not vary much across region.

# Results

## Counter Strike is Very Popular in Eastern Europe
<div class="tableauPlaceholder" id="viz1771885639870" style="position: relative;">
    <noscript>
        <a href="#">
            <img
                alt="Counter Strike Popularity Global Heatmap"
                src="https://public.tableau.com/static/images/CS/CSPopHeat/CounterStrikePopularityGlobalHeatmap/1_rss.png"
                style="border: none;"
            />
        </a>
    </noscript>
    <object class="tableauViz" style="display: none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="CSPopHeat/CounterStrikePopularityGlobalHeatmap" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/CS/CSPopHeat/CounterStrikePopularityGlobalHeatmap/1.png" />
        <param name="animate_transition" value="yes" />
        <param name="display_static_image" value="yes" />
        <param name="display_spinner" value="yes" />
        <param name="display_overlay" value="yes" />
        <param name="display_count" value="yes" />
        <param name="language" value="en-US" />
        <param name="filter" value="publish=yes" />
    </object>
</div>

<script type="text/javascript">
    var divElement = document.getElementById("viz1771885639870");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

This aligns with expectations considering how many of the worlds top players originate from these regions. 

## NARAKA: Bladepoint dominant in Asia Due to Asian Aesthetic

We see the opposite popularity for NARAKA: Bladepoint where the game isn't popular in any countries except for Asian ones.

This is a battle royale game developed by a Chiense studio which takes centers its aesthetic around Chinese mythology and martial arts. Developers also invest heavily into an esports ecosystem which exists solely in Asian countries. 

So the focus on Asian mythology and esports investment solely in the Asian region, has made the game popular in Asian countries but not in others.

Games popularity who is less skewed like Cities: Skylines provide a gameplay style which is more neutral and global language support. 
The game revolves around city building which is a niche that isn't specific to a culture like chinese mythology is for Bladepoint. 


## What happened with Overwatch 2 in China?
There is an interesting outlier though with Overwatch 2. The game got delisted from mainland China when parent company Blizzard lapsed their contract with Chinese company NetEase. Since China required foreign games to be published through a local partner, this meant that all Blizzard titles (including Overwatch 2) were taken offline in mainland China. Looking at the popularity for China (LogPopularity=0.57), the game is more popular in China than other regions by a considerable amount. Therefore, when all players lost all of their progress and access to the game, the game was review bombed by Chinese players when Overwatch 2 released (3.5% positive reviews in China).

## Asians seem to have higher standards
<div class="tableauPlaceholder" id="viz1771885731599" style="position: relative;">
    <noscript>
        <a href="#">
            <img
                alt="Sentiment Heatmap (Asian Countries)"
                src="https://public.tableau.com/static/images/As/AsianSentiment/SentimentHeatmapAsianCountries/1_rss.png"
                style="border: none;"
            />
        </a>
    </noscript>
    <object class="tableauViz" style="display: none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="AsianSentiment/SentimentHeatmapAsianCountries" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/As/AsianSentiment/SentimentHeatmapAsianCountries/1.png" />
        <param name="animate_transition" value="yes" />
        <param name="display_static_image" value="yes" />
        <param name="display_spinner" value="yes" />
        <param name="display_overlay" value="yes" />
        <param name="display_count" value="yes" />
        <param name="language" value="en-US" />
        <param name="filter" value="publish=yes" />
    </object>
</div>

<script type="text/javascript">
    var divElement = document.getElementById("viz1771885731599");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

Also, if you look at Asian countries (Japan, Taiwan, China, South Korea), they seem to generally skew negative for their reviews for nearly all games. I believe these players have higher standards for games compared to other regions. 




## Returning to the Hypothesis and Conclusion
1. What games are beloved by a country?

    My hypothesis is mostly true. Counter Strike in Eastern Europe is extremely popular compared to other games in Eastern Europe.  
    Rocket league is also popular in France, but not that much so compared to other European countries like Portugal.

    Games especially more popular in these regions than others:
    - Scrap Mechanic in Sweden (LogPopularity = 0.92)
    - Euro Truck Simulator 2 in Romania (LogPopularity = 0.93)
    - World of Tanks Blitz in Ukraine (LogPopularity = 0.79)
    - World of Tanks Blitz in Russia (LogPopularity = 0.72)
    - 鬼谷八荒 Tale of Immortal in China (LogPopularity = 0.79)

    Games especially more liked than in other regions:
    - Battlefield 2042 in Portugal (Global 40% positive, Portugal 60% positive)
    - Call of Duty in Romania (Global 59% positive, Romania 87% positive)



2. Are there games which are liked in one region but hated in another?
    Yes, there are actually a significant amount. 

    Games especially more hated than in other regions:
    - Overwatch 2 in China (Global 11% positive, China 3% positive) 
        - China lost support
    - Apex Legends in Taiwan (Global 79% positive, Taiwan 48% positive)
    - Apex Legends in Taiwan (Global 79% positive, Taiwan 48% positive)
    - EA Sports FIFA 23 in Japan (Global 55% positive, Japan 26% positive)
    - Rocket League in China (Global 89% Positive, China, 57% Positive)
        - China lost support


## Extra: Popularity vs Sentiment Scatter
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


