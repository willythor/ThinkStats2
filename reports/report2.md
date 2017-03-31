# The Association Between Drug Usage and Depression
### by David Papp and Willem Thorbecke

Corresponding jupyter notebook: https://github.com/davpapp/ThinkStats2/blob/master/code/Report%202.ipynb

#### Introduction
The goal of this article is to explore the association between drug usage and depression. Intuitively, many would argue that those who use drugs are more likely to be depressed. To explore this relationship, we took data from the National Drug Usage and Health Survey from 2014. 

#### Methodology
To answer our question, we used logistical regression. Our dependent variable was DEPRSLIF, which is a binary variable representing whether a person has ever been diagnosed with depression by a professional. This second half is very important because being diagnosed with depression by a medical or other health professional might be very different from being self-diagnosed with depression.

First, to visualize the effect of at least one variable, we plotted the age at which respondents first drank alcohol versus whether they've been diagnosed with depression. 

![Plot](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/scr.png?raw=true)

This doesn't tell us a whole lot visually, so we need to do some regression.

First, we tested for correlation between depression and typical demographic variables. Since almost everything, including drug usage, is likely correlated with basic demographics such as income and age, including these demographics in our regression allowed us to control for some variables. Had we not included them, the drug usage variables might have just been reporting the hidden effect of some demographic variable. The variables we decided to use were age, sex, income, and race. We had to create separate, binary variables for each reach in order to include them in our regression model. The results are as shown:

![Demographics](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/demo.png?raw=true)

The variables in the chart above have the following relations (if the variable dictates a yes or no question, then (0==yes,1==no): 
⋅⋅⋅c_white == respondants race is white
⋅⋅⋅c_black == respondants race is black
⋅⋅⋅c_hispanic == respondants race is hispance
⋅⋅⋅INCOME == respondants income bracket
⋅⋅⋅CATAG7 == respondants age bracket 
⋅⋅⋅IRSEX == respondants sex (0==male, 1==female)

Analyzing each of the coefficients: 
- Race: We recoded race into binary dummy variables in order to be able to sensibly include them in our regression (otherwise, they would have been on a scale of 1-7). Surprisingly, being white is positively correlated with having been diagnosed with depression, whereas being black and Hispanic are negatively correlated. 
- Age: Income is a categorical variable where each unit increase corresponds to an increase in the age group of the person. There is a positive correlation, suggesting that older people are more likely to have been diagnosed with depression. This makes sense, considering that people who have been alive for longer have a higher likelihood of having been depressed at some point. 
- Income: Income is negatively correlated with having been depressed. This is interesting because one would both expect wealthier people to have a higher quality of life, but also receive better medical coverage and thus be more likely to be depressed. The first one seems to be stronger in effect size. 
- Sex: Women are more likely to be diagnosed as depressed. This aligns with other studies that show that women are more likely than men to be diagnosed with depression.

Next, we used data mining to find the variables included in the study that are most correlated with depression. Interestingly, of the thousands of variables, the top fifteen were each a health condition or disease. We took a few of the top ones and did a separate regression of these:

![Health](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/health.png?raw=true)

The variables in the chart above have the following relations (0==no,1==yes):
⋅⋅⋅LIFANXD == has been diagnosed with anxiety by a doctor
⋅⋅⋅LIFULCER == has had an ulcer
⋅⋅⋅LIFPANCR == has had pancreatitis
⋅⋅⋅LIFTINN == has had tinnitus
⋅⋅⋅LIFSTDS == has had an STD
⋅⋅⋅LIFCIRR == has had cirrhosis
⋅⋅⋅LIFSINUS == has had sinusitis
⋅⋅⋅LIFHIV == has had HIV 

When we ran the regression, we underestimated the scope of the data we're dealing with. We did not expect these variables to relate to health conditions or diseases as opposed to drug usage. However, we realized that even if we are not interested in these variables, they provide a relative metric for effect size. 

These results also surprised us. One would expect diseases to cause a decrease in life quality and thus a higher likelihood of being depressed. However, most of the listed diseases or conditions are negatively correlated with being diagnosed with depression (except cirrhosis and HIV). One possible explanation for this is that those who are diagnosed with these diseases are likely wealthy, which we earlier saw was negatively correlated with depression. It'll be interesting to see what happens when we combine the demographic and disease regressions.


Next, we did a regression with four of the more common street drugs. At first, we did not include any of the demographic variables. The results are as shown:

![Drug Usage](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/drugs.png?raw=true)

The variables in the chart above have the following relations (0==no,1==yes):
⋅⋅⋅MJEVER == has ever tried marijuana 
⋅⋅⋅COCEVER == has ever tried cocaine 
⋅⋅⋅ALCEVER == has ever tried alcohol
⋅⋅⋅HEREVER == has ever tried heroin

Again, the results go against our intuition that drug usage is correlated with depression. Cocaine is the only drug that is positively associated with being diagnosed with depression. It'll be interesting to see how including the demographic variables changes this because it could be that the drug usage variables are absorbing the effect of some demographic variable. The pseudo R^2 value is once again very low.

Finally, we did a regression of all of the variables mentioned above. The idea behind this was to remove the effect of possible confounding variables. We expected some of the signs of correlation to change. For example, we suspected that white people are only more likely to be diagnosed as depressed because they are wealthier and thus have better access to healthcare.

![All](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/all.png?raw=true)

One important thing to note is that NONE of the signs of correlation flipped. For example, being white is still correlated with being more likely to be diagnosed with depression and having tried marijuana is still correlated with lower rates of depression, even when income is controlled for. This is surprising. We are now left wondering why having certain diseases and conditions such as ulcers and anxiety are negatively correlated with depression.

As we added demographic controls, the coefficients of the variables having to do with diseases and health conditions all decreased, while coefficients remained roughly the same for drug usage. This suggests that drug usage is not as correlated with income and other demographics as health conditions. The greatest odds ratios (coefficients) came from being black (-.55), being female (.69), and, surprisingly, having tried marijuana and heroin (-.4 each). In the case of sex, the coefficient can be interpreted to mean that a unit change in gender (i.e., switching from male to female) results in a .69 unit change in the log of the odds of being diagnosed with depression. 

One potential source of error in our analysis is the categorization of variables. We treated some of our variables as continuous although they were more discrete in nature. For example, rather than using the actual ages of respondents, the ages were lumped into 7 equally sized categories. We do not think this should affect the results too much.
