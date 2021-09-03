# Using Twitter to Detect for Disaster Resources
by Dan Chen, Ramiro Ramirez, Hitha Yeccaluri

## Problem Statement

In recent years, social media has been a major platform for sharing information and staying up-to-date on world events. During natural disasters and other crises, those networking and content-sharing capabilites can be very helpful for victims. They can post updates from their area, see updates from other people, potentially connect with resources they need and figure out their next steps. However, in the wake of tragedies like this, people likely do not have the bandwidth to determine what information is genuinely helpful and what is not. In desperate times, they just want help.<br >

Projects like Ushahidi and Twitcident have been making efforts to a) keep people updated during disaster events and b) connect with local governments for protection/prevention efforts. Ushahidi's open-source technology crowdsources information from texts, tweets, emails, etc. and has been pivotal in a number of political, social and public health challenges. Twitcident monitors tweets for preventative purposes; they aim to identify warning signs of increased risk for dangerous/criminal incidents. However, Ushahidi is a platform often reserved for organizations to use and Twitcident was created with the goal of helping law enforcement.<br >

Social media has been used to help people in disasters, but the process has not always been streamlined or open to the public. In 2012, Hurricane Sandy's response teams used social media to gain a better understanding of the impact and where to concentrate their aid. What if the people themselves had known how to use social media in a way that would direct them to resources and help? It can be difficult to spread helpful information with older methods (word-of-mouth, TV, radio, newspaper), maybe more people would have accessed the help they needed.<br >

Twitter is a popular platform for information dissemination and receives nearly 10,000 posts per second. During the 2020 California wildfires, it was used to send alerts, give updates about fire spread, warn people about potential evacuations, abd share updates about power outages, among other things. The information was there, but it was a nightmare to sort through it. How can we make finding information via Twitter more convenient for victims of natural fires?

## Contents

| File/Folder | Description |
| --- | --- |
| [datasets](https://git.generalassemb.ly/yeccaluh/project_5/tree/master/datasets) | Data folder; [Jul/Aug](https://git.generalassemb.ly/yeccaluh/project_5/tree/master/datasets/tweets_78), [Sept/Oct](https://git.generalassemb.ly/yeccaluh/project_5/tree/master/datasets/tweets_910), [Nov/Dec](https://git.generalassemb.ly/yeccaluh/project_5/tree/master/datasets/tweets_1112), [cleaned and labeled](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/datasets/finaldata_label.csv) |
| [Data Collection and Cleaning](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/collection_cleaning.ipynb) | Collecting and cleaning data, feature engineering, prepping dataset for use |
| [Preprocessing, EDA, Modeling](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/processing_modeling_1.ipynb) | EDA and visualizations to understand feature relationships, modeling to answer problem statement |
| [More Processing, EDA, Modeling](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/processing_modeling_2.ipynb) | More of the above, different models |
| [Scraping Script](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/scraper_script.py) | Python script to scrape tweets using snscrape and save as a .csv file |
| [Presentation visuals](https://git.generalassemb.ly/yeccaluh/project_5/blob/master/project_presentation.pdf) | PDF of presentation slides |

## Workflow

**1. Data Collection and Cleaning**<br >
Scraped 108,000+ tweets from July 1, 2020 to December 31, 2020 within 160km around Napa, California using snscrape. Dropped columns not needed for EDA or modeling, engineered four columns, labeled tweets, merged individual datasets, saved as a new CSV file.

**2. EDA**<br >
No strong relationships between features; we had engineered features that we thought would provide some insight and nothing seemed to be particularly correlated.

**3. Modeling**<br >
Used both CountVectorizer and TF-IDF to process the data. Compared seven models (logistic regression, KNN classifier, decision tree, random forest, support vector classifier, linear support vector classifier and multinomial naive-bayes), ran each with the two types of vectorized data for a total of 14 models.

**4. Evaluations**<br >
Compared test/train scores to check model fits. Calculated accuracy, precision and recall scores; each could be optimized based on the situation at hand. Visualized AUC for two top-performing models.

## Executive Summary

After some trial and error, we chose snscrape to gather our data. Other scraping methods that go through the official Twitter API only allow standard users to access tweets from the last week. Since we needed to access archival tweets, we went with snscrape. We scraped tweets from July 1, 2020 to December 31, 2020 because fires were rampant during the second half of the year. Our search area was confined to a 160km radius around 38.502500, -122.265400 (Napa, California) because the largest California fire of 2020 occured across Napa. Using a list of keywords (‘wildfire’, ‘fire’, ‘forest fire’, ‘smoke’, ‘burn’, ‘blaze’, ‘california’, and ‘warning’), we created a dataset of 108,000+ tweets. Our scrape provided us with quite a bit of metadata, but we were interested in five columns: 'date', 'user', 'content', 'user_location', 'id'. We then created a column for the keyword that produced the tweet, a column indicating whether or not the tweet appears more than once in the data (this would indicate that it was associated with more than one keyword), a column with the user's verification status, and our label column.<br >

For our label column, we used two methods to choose which tweets would be "relevant" and which would not be. Due to the size of the dataset, hand-labeling was out of the question, so we turned to some academic articles for inspiration. Researchers at the National Institute of Technology in Tamil Nadu, India performed a similar study on tweets from a 2016 Italy earthquake. Using a base dataset, they mined words that were important and relevant to victims of the earthquake. They were then able to use those words on a new dataset, again about earthquakes, to classify which tweets were important and which were not. A second article by Endsley et al. did something very similar about prescribed fires. First, we went through a few thousand of the tweets and identified which ones were relevant to our goal and which were not, and noted the words that appeared frequently in those "relevant" tweets. Then, we looked at a wordcloud created by the authors of the second article and used some of those words that we had not included in our original words. After putting all those "important" words in a list, we wrote a function to check each tweet against the list and tweets classified as "1" (relevant) included at least one of those important words, while tweets classified with "0" did not. This function labeled about 23.1% of tweets as relevant, which makes sense.<br >

Labeling was our biggest hurdle, and after clearing that, we were able to run a number of classifying models on the dataset. We chose to use both CountVectorizer and TF-IDF Vectorizer in our models because we had not compared their performances in binary classification and were curious if one had the upper hand. Of our 14 models, a Random Forest classifier with CountVectorizer and Multinomial Naive-Bayes with either vectorizer had the least amounts of overfitting. When comparing our accuracy, precision and recall metrics, though, our Decision Tree model performed the best across the board. Our Decision Tree with a TF-IDF Vectorizer scored highest in accuracy and recall, 98.91% and 96.44% respectively, and our Decision Tree with a CountVectorizer had the highest precision at 99.96%. Each metric has its own importance and can be optimized depending on situational context, but, regardless of chosen metric, a Decision Tree classifier seems like the way to go.<br >

## Conclusions

With a precision score of 99.96%, our Decision Tree model is successful in identifying relevant tweets about wildfires. If we were able to create a landing page, a website or app of some kind, that passed a livestream of tweets through this model to sort in real time, that would be . Viewers would then be able to see only the informative tweets without having to manually sort through every tweet vaguely related to their situaton.<br >

Of course, for this model to be useful to the public, it needs to be accessible. Ideally, this page would be able to be reached quickly and easily, even in areas with low connection.

## References

- [Napa, CA coordinates](https://www.latlong.net/place/napa-ca-usa-6661.html)
- [2020 CA fire information](https://www.fire.ca.gov/incidents/2020/)
- [Intro to snscrape](https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721)
- [Scraping Tweets by Location with snscrape](https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25)
- [snscrape GitHub page](https://github.com/JustAnotherArchivist/snscrape)
- [Map of SCU, CZU and LNU fire complexes](https://abc7news.com/cal-fire-california-fires-map-in/6380949/)
- [Social media uses in disasters](https://preparecenter.org/topic/social-media-disasters/)
- [Social media saving lives in disasters](https://phys.org/news/2018-08-social-media-bad-disaster-zones.html)
- [Twitter is relevant and convenient](https://www.buzzfeednews.com/article/nishitajha/afghanistan-woman-hiding-taliban-blacklist)
- [Ushahidi](https://www.ushahidi.com/about)
- [Twitcident Workshop PDF](https://irgc.org/wp-content/uploads/2018/09/Twitcident-OECD-IRGC-Expert-Workshop.pdf)
- [Hala Systems](https://halasystems.com/)
- [Tweets per second](https://www.internetlivestats.com/one-second/#tweets-band)
- [CountVectorizer vs. TF-IDF Vectorizer](https://www.linkedin.com/pulse/count-vectorizers-vs-tfidf-natural-language-processing-sheel-saket/)
- Ghosh, A., Pal, R., & Prasath, R. (2017). Mining Intelligence and Knowledge Exploration: 5th International Conference, p348–358. SPRINGER. 
- Endsley, K. & McCarty, Jessica. (2013). Mapping prescribed burns and wildfires from Twitter with natural language processing and information retrieval techniques. 
