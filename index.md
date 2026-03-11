---
layout: default
title: Steam Games Regional Sentiment 
---
# Analysis of Game Preference by Region using Steam Reviews

## Introduction and Hypothesis
Steam is the largest PC game distributor worldwide with about a ~70% market share [^1] in the space. Using available steam reviews data [^2], this analysis hopes to answer questions regarding game sentiment in differnt regions.

1. What games are beloved by a country?
    - Hypothesis:
        - I believe games that are so popular that they've had a cultural impact on a country will appear clearly as beloved.
        - For example, Counter Strike has had a cultural impact in Eastern European countries, and I know Rocket League is also very strong in the french community.

2. Are there games which are liked in one region but hated in another?
    - Hypothesis:
        - I think there will be good games that might've done something to discriminate a particular region. 

# How the Analysis Was Done

## Assumptions
1. A language roughly corresponds to a region. So I'm assuming chinese reviews are coming from China, and English reviews are coming from English speaking countries. Languages in similar regions (i.e. ukrainian and russian) are grouped together under a region. 
    - *This assumption is not perfect. It is possible for a review to be written in English by a Chinese gamer. Regardless, I believe this analysis can still yield some interesting results.*
    - *The dataset actually does have some region labeling under language. For example, 'brazilian' and 'LATAM' map perfectly to regions and not languages. This isn't an issue and actually enhances the analysis.*

2. For this analysis, games with less than 100,000 total reviews globally and less than 100 reviews in a region are ignored. This cuts down the amount of distinct games analyzed from 105,208 to only 170.

## Regions
The following is a map of the regions represented in this data set. This isn't a perfect mapping since again, languages don't map perfectly to regions. Notably, certain large regions like Africa or India are excluded. This is simply because the language did not exist in the data. If only the Steam data recorded the region as well and not just language.

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
The following pie chart shows the proportion of the dataset each region represents.

<div class="tableauPlaceholder" id="viz1773103257473" style="position: relative">

  <noscript>
    <a href="#">
      <img 
        alt="Region Map"
        src="https://public.tableau.com/static/images/NA/NARAKAGlobal/RegionMap/1_rss.png"
        style="border: none"
      />
    </a>
  </noscript>

  <object class="tableauViz" style="display:none;">
    <param name="host_url" value="https://public.tableau.com/" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />
    <param name="name" value="NARAKAGlobal/RegionMap" />
    <param name="tabs" value="no" />
    <param name="toolbar" value="yes" />
    <param name="static_image" value="https://public.tableau.com/static/images/NA/NARAKAGlobal/RegionMap/1.png" />
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
  var divElement = document.getElementById("viz1773103257473");
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

- Popularity: How popular is this game in this region?
- Sentiment: How well received is this game in this region?

#### Popularity
Popularity is taken by taking the proportion of reviews a game has for all of a regions reviews, over the proportion of reviews that the game makes up globally.

This tells us how much a games popularity deviates from the norm for a region. 

$$
\log{\left(\frac{\text{region\ review\ proportion}}{\text{global\ review\ proportion}}\right)}
$$

A positive value means the game is more popular in this region, negative means the game is less popular in this region, and a 0 value means its as popular as it should be. 

Using this data, I was able to produce the following heatmap. The more red the tile, the less popular the game is than usual and vice versa for green tiles.

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

The more varied a column is in its color, the more varied its popularity is across regions.

The first thing to note is how varied the popularity is across regions. If games were equally popular in most regions, then the heatmap would be mostly white. 

Counter Strike is a good example of this where the game is extremely popular in Eastern Europe (Romania especially) compared to other countries.

#### Relative Sentiment
Sentiment is calculated similar to popularity, but using the positive review percent metric instead.

This tells us if the amount of positive reviews for a game deviate from the norm for a region.

$$
\log{\left(\frac{\text{region \%positive}}{\text{global \%positive}}\right)}
$$

A positive value means the game has more positive reviews in this region than normal, negative means the game has more positive reviews than normal, and a 0 means its positive reviews match the global average. 

Using this data, I was able to produce the following heatmap. The more red the tile, the more that country deviates towards negative from the games positive percentage globally, and vice versa for green tiles.

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



The first thing to note is the lack of variance in sentiment across regions. This implies that a games sentiment does not vary much across regions.

# Results
## Popularity vs Positive % Scatter
The following scatter plot graphs a games popularity in a region against the percentage of reviews which are positive in that region. Most games cluster around baseline popularity (the zero line) with mostly positive reviews. This isn't surprising considering games with <100,000 reviews were filtered out. One can assume if you aren't already a good game, you're unlikely to get >=100,000 reviews.

Nevertheless, the quadrants can be interpreted as so:
- Top right: Popular in a region & positively reviewed
- Bottom right: Not popular in a region, but positively reviewed (hidden gems for that region)
- Top left: Popular but poorly reviewed  (interesting)
- Bottom left: Poorly reviewed and unpopular (bad)

<div class="tableauPlaceholder" id="viz1773248916632" style="position: relative">

    <noscript>
        <a href="#">
            <img 
                alt="Popularity vs Positive % Scatter"
                src="https://public.tableau.com/static/images/OW/OW2Heat/PopularityvsPositiveScatter/1_rss.png"
                style="border: none"
            />
        </a>
    </noscript>

    <object class="tableauViz" style="display:none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="OW2Heat/PopularityvsPositiveScatter" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param 
            name="static_image"
            value="https://public.tableau.com/static/images/OW/OW2Heat/PopularityvsPositiveScatter/1.png"
        />
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
    var divElement = document.getElementById("viz1773248916632");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";

    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

From this scatterplot, I was able to notice some interesting outliers. Counterstrike in Eastern Europe, NARAKA: Bladepoint in China, and Overwatch 2 in China.

## Counter Strike is Very Popular in Eastern Europe
Counter Strike is a first person tactical shooter first released in 1999 by Valve. As of March 2026, it tops the Steam concurrent user charts and averages about 1.5M concurrent users daily [^3].

The following map shows the LogPopularity for Counter Strike as a heatmap across a world map.

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

This aligns with expectations. Many of the worlds top CS players have historically originated from Eastern European countries and the region alone makes up for 42% of the current top players [^4]. 

## NARAKA: Bladepoint only dominant in East Asia
We observe the opposite popularity for NARAKA: Bladepoint where the game isn't popular in any countries except for Asian ones.

NARAKA: Bladepoint is a battle royale game developed by a Chinese studio which centers its aesthetic around Chinese mythology and martial arts. The developers also invest heavily into an esports ecosystem which exists **only** in Asian countries. 

The folowing map shows the LogPopularity for NARAKA: Bladepoint as a heatmap across a world map.
<div class="tableauPlaceholder" id="viz1771886045112" style="position: relative;">
    <noscript>
        <a href="#">
            <img
                alt="NARAKA: Bladepoint Popularity Global Heatmap"
                src="https://public.tableau.com/static/images/NA/NARAKAGlobal/NARAKABladepointPopularityGlobalHeatmap/1_rss.png"
                style="border: none;"
            />
        </a>
    </noscript>
    <object class="tableauViz" style="display: none;">
        <param name="host_url" value="https://public.tableau.com/" />
        <param name="embed_code_version" value="3" />
        <param name="site_root" value="" />
        <param name="name" value="NARAKAGlobal/NARAKABladepointPopularityGlobalHeatmap" />
        <param name="tabs" value="no" />
        <param name="toolbar" value="yes" />
        <param name="static_image" value="https://public.tableau.com/static/images/NA/NARAKAGlobal/NARAKABladepointPopularityGlobalHeatmap/1.png" />
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
    var divElement = document.getElementById("viz1771886045112");
    var vizElement = divElement.getElementsByTagName("object")[0];

    vizElement.style.width = "100%";
    vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

    var scriptElement = document.createElement("script");
    scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

This highly concentrated popularity can be attributed to the games focus on East Asian mythology and martial arts which tie the game closer to Asian regions culture and distance it from other regions cultures. Developers also prioritize esports growth to Asian regions where nearly all of their events are hosted [^5]. 

## What happened with Overwatch 2 in China?
The following heatmap is a subset of sentiment heatmap filtered to only show Overwatch 2 sentiment.
<div class="tableauPlaceholder" id="viz1773245017043" style="position: relative">

  <noscript>
    <a href="#">
      <img
        alt="Sentiment Heatmap"
        src="https://public.tableau.com/static/images/OW/OW2Heat/SentimentHeatmap/1_rss.png"
        style="border: none"
      />
    </a>
  </noscript>

  <object class="tableauViz" style="display:none;">

    <param name="host_url" value="https://public.tableau.com/" />
    <param name="embed_code_version" value="3" />
    <param name="site_root" value="" />

    <param name="name" value="OW2Heat/SentimentHeatmap" />

    <param name="tabs" value="no" />
    <param name="toolbar" value="yes" />

    <param
      name="static_image"
      value="https://public.tableau.com/static/images/OW/OW2Heat/SentimentHeatmap/1.png"
    />

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
  var divElement = document.getElementById("viz1773245017043");
  var vizElement = divElement.getElementsByTagName("object")[0];

  vizElement.style.width = "100%";
  vizElement.style.height = (divElement.offsetWidth * 0.75) + "px";

  var scriptElement = document.createElement("script");
  scriptElement.src = "https://public.tableau.com/javascripts/api/viz_v1.js";

  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

Notably, sentiment is skewed very heavily by Chinese players.

The game got delisted from mainland China when parent company Blizzard lapsed their contract with Chinese company NetEase. Since China required foreign games to be published through a local partner, this meant that all Blizzard titles (including Overwatch 2) were taken offline in mainland China. Looking at the popularity for China (LogPopularity=0.57), the game is more popular in China than other regions by a considerable amount. Therefore, when all players lost all of their progress and access to the game, the game was review bombed by Chinese players when Overwatch 2 released (3.5% positive reviews in China).

## East Asian Reviews Skew Negative
If you look at East Asian countries relative game sentiment (Japan, Taiwan, China, South Korea), they seem to generally skew negative for their reviews for nearly all games. The following heatmap is a subset of the previous sentiment heatmap, but filtered to only show East Asian countries.

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

This observation brings up more questions than answers. But some plausible explanations:

- East asian players having higher standards for games.
- Games which are often developed in English having localization issues in these regions.
- Review bombing being generally more common.


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
    Yes, with two notable examples NARAKA: Bladepoint being beloved only in China and Counter Strike being loved everywhere aside from China.

    Other examples include:

    Games especially more hated than in other regions:
    - Overwatch 2 in China (Global 11% positive, China 3% positive) 
        - Overwatch 2 lost support in China and got review bombed 
    - Apex Legends in Taiwan (Global 79% positive, Taiwan 48% positive)
    - EA Sports FIFA 23 in Japan (Global 55% positive, Japan 26% positive)
    - Rocket League in China (Global 89% Positive, China, 57% Positive)
        - Rocket League lost support in China and got review bombed 


[^1]: https://en.wikipedia.org/wiki/Steam_(service)
[^2]: https://www.kaggle.com/datasets/kieranpoc/steam-reviews/data
[^3]: https://steamcharts.com/
[^4]: https://www.hltv.org/stats/players?rankingFilter=Top50
[^5]: https://liquipedia.net/naraka/S-Tier_Tournaments
