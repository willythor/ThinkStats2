# The Association Between Drug Usage and Depression
### by David Papp and Willem Thorbecke

Corresponding jupyter notebook:


#### Introduction
The goal of this article is to explore the association between drug usage and depression. Intutively, many would argue that those who use drugs are more likely to be depressed. To explore this relationship, we took data from the National Drug Usage and Health Survey from 2014. 

#### Methodology
To answer our question, we used logistical regression. Our dependent variable was DEPRSLIF, which is a binary variable representing whether a person has ever been diagnosed with depression by a professional. This second half is very important, because being diagnosed with depression by a medical or other health professional might be very different from being self-diagnosed with depression.

First, we tested for correlation between depression and typical demographics. Since almost everything, including drug usage, is likely correlated with basic demographics, including these demographics in our regression allowed us to control for some variables. Had we not included them, the drug usage variables might have just been reporting the hidden effect of some demographic variable. The variables we decided to use were AGE, SEX, INCOME, and race. We had to create separate, binary variables for each reach in order to include them in our regression model. The results are as shown:

![Demographics](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/demo.png?raw=true)

Next, we used data mining to find the variables included in the study that are most correlated with depression. Interestingly, of the thousands of variables, the top fifteen were each a health condition or disease. We took a few of the top ones and did a separate regression of these:

![Demographics](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/health.png?raw=true)


Next, we did a regression with four of the more common street drugs. At first, we did not include any of the demographic variables. The results are as shown:

![Demographics](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/drugs.png?raw=true)

Finally, we did a regression of all of the variables mentioned above. The idea behind this was to remove the effect of possible confounding variables. We expected some of the signs of correlation to change. For example, we suspected that white people are only more likely to be diagnosed as depressed because they are wealthier and thus have better access to healthcare.

![Demographics](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/all.png?raw=true)


#### Analysis
Some interesting takeaways from these results includes that fact that someone having used drugs at some point in their life was negatively associated with having been depressed. Albeit the pseudo r-squared value was very small compared to the other cases of regression that we calculated. The number of days in a month that someone engaged in any of the aforementioned drugs had a statistically insignificant association with depression.

As mentioned before, we included demographic variables as a method of control for the other variables we looked at. However, in comparing the logistic regression we ran on just the top 8 factors associated with depression (all health issues), and the logistic regression we ran on those same factors, but also demographics, we found that the effect size of the original variables changed significantly. 

As expected, factors such as race and sex played a huge role in the chance of someone being depressed. In comparing the effect size of race being black versus white, it's interesting to note that the r-squared value when white is almost .3, compared to -.58 when black.

In the final logistic we ran, the largest effect sizes came from being black (-.55), sex (.69), and surprisingly having tried marijuana and heroin had an effect size of (-.4) each.

#### Interpretation
One thing to note was that income had very little impact on the odds of being depressed. The fact that being black had to largest effect size could have been a result of the NSDUH having interviewed a disproportionately small amount of black people. Sex being a contributing factor aligns with research claiming depression to be twice as common in women than in men. As for factors such as someone having tried heroin or marijuana decreasing the odds of that person also being depressed are harder to fathom, and are open to speculation.
