#The Association Between Drug Usage and Depression
### by David Papp and Willem Thorbecke

Corresponding jupyter notebook:


#### Introduction
The goal of this article is to explore the association between drug usage and depression. Intutively, many would argue that those who use drugs are more likely to be depressed. To explore this relationship, we took data from the National Drug Usage and Health Survey from 2014. 

#### Methodology
To answer our question, we used logistical regression. Our dependent variable was DEPRSLIF, which is a binary variable representing whether a person has ever been diagnosed with depression by a professional. This second half is very important, because being diagnosed with depression by a medical or other health professional might be very different from being self-diagnosed with depression.

First, we tested for correlation between depression and typical demographics. Since almost everything, including drug usage, is likely correlated with basic demographics, including these demographics in our regression allowed us to control for some variables. Had we not included them, the drug usage variables might have just been reporting the hidden effect of some demographic variable. The variables we decided to use were AGE, SEX, INCOME, and race. We had to create separate, binary variables for each reach in order to include them in our regression model. The results are as shown:

!(insert pic of demographics here)

Next, we used data mining to find the variables included in the study that are most correlated with depression. Interestingly, of the thousands of variables, the top fifteen were each a health condition or disease. We took a few of the top ones and did a separate regression of these:

!(insert pic here)




Next, we did a regression with four of the more common street drugs. At first, we did not include any of the demographic variables. The results are as shown:

!(insert pic of drug results here)

Finally, we did a regression of all of the variables mentioned above. The idea behind this was to remove the effect of possible confounding variables. We expected some of the signs of correlation to change. For example, we suspected that white people are only more likely to be diagnosed as depressed because 

#### Analysis

#### Interpretation


