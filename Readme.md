{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Data Science Housing Project\
* Scraped over 8000 listings from primelocation.co.uk with scrapy for rental properties in England\
* Cleaned raw data and performed data analysis\
* Analysed a feature using nltk\
* Extracted a feature from property descriptions\
* Built a LinearRegression model using pipelines\
\
## Web Scraping With Scrapy:\
Scraped the following data from each listing:\
* price\
* n.o. bathrooms\
* n.o. bedrooms\
* n.o. living rooms\
* town/city\
* outward code\
* type of property (flat, detached house, etc)\
* description\
\
## Data Cleaning\
Much of the data cleaning was done in scrapy, which was then passed over into pandas for further cleaning. \
* removed html tags from text\
* converted price to float value\
* removed punctuation and special characters from multiple features\
* removed outliers\
\
## NLTK and Feature Engineering \
Goal was to convert corpus of description data into usable \'91tags\'92 which would then be encoded.\
* created a bag of words model to remove stop words\
* filtered non relevant words\
* lemmatised words in the resulting corpus\
* retrieved the 20 most important words according to the model \
I aimed to only include words which were property-amenities such as \'91garden\'92 or \'91kitchen\'92 and exclude adjectives as those are not as objective.\
* calculated the sum of tf_idf values for each description in the corpus, determining which descriptions were \
Ultimately this new feature didn\'92t appear to be correlated with the price so  it was dropped, but the insight gained lead to a much simpler \'91tags\'92 feature which was implemented into the final model.\
* created a \'91tag\'92 feature based on key words in the description\
\
## Data Analysis\
* Compared features with the target variable, price\
* Created count plots of categorical variables \
* Created contingency tables for each pair of categorical features and performed chi squared relationship tests between these features\
Highlights:\
![](/Desktop/DS/house_price_proj/property_price_dist.png)\
![](/Desktop/DS/house_price_proj/property_tags_vs_price.png)\
![](/Desktop/DS/house_price_proj/property_type_dist.png)\
Format: ![Alt Text](url)\
\
## Feature Importance\
As an aside to general data analysis, I explored the importance of each feature by using a decision tree and ranked them accordingly.\
\
## Model Building\
I transformed all of the categorical variables into dummy variables. What was left was a very wide data frame with lots of new features. To reduce the number of features I applied two steps to each model pipeline:\
* A feature selector, SelectFromModel which selects the most important features\
I trained three different models using cross validation:\
* Linear Regression: baseline model\
* XGB Regression\
* Lasso Regression\
The XGBRegressor model had the lowest MAE overall:\
* Linear Regressor average MAE: 2260.44\
* Lasso Regressor average MAE: 2255.49\
* XGB Regressor average MAE: 1935.71\
I chose the XGBRegressor model to test on, and got the following result:\
* XGB Regressor test MAE: 1960.96\
When taking into account the median price, \'a35742, this is a poor result. This is probably as a result of the features having a poor correlation with the price. I attribute this to a poor sample of the overall population. One way of dealing with this might have been to collect data from the website over a period of time. Another option would have been to find websites which allowed users to scrape their data, which very few do. Of these, it was hard to find websites with enough data. }