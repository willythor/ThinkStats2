#Do Midwestern colleges have better ACT scores?
### by David Papp

Corresponding jupyter notebook:
https://github.com/davpapp/ThinkStats2/blob/master/code/report1.ipynb


#### Introduction
The merits of the ACT and SAT are widely debated by students and college admissions alike. Many students seek to gain an edge by taking one or the other. There are a number of rules of thumb regarding each, with one of the main ones being that colleges in the Midwest prefer ACT scores. The goal of this article is to explore the differences in ACT and SAT scores between students in the Midwest and other areas. 

#### Methodology
To study this relationship, I downloaded data from the US Department of Education's College Scorecard for the 2014-2015 academic year. This data is collected annualy and contains hundreds of variables for all acredited colleges in the US. The full documentation can be read here https://collegescorecard.ed.gov/assets/FullDataDocumentation.pdf. The variables of interest in my study were ACT Scores ('ACTCMMID'), SAT Scores ('SAT_AVG'), and region ('REGION'). I dropped all schools that were missing data from any of these three categories.

To get an initial sense of how ACT scores and SAT scores compare, I first plotted both SAT and ACT scores for all regions combined using KDE for smoothing. Both distributions appear roughly normal, with longer right tails.

![ACT Scores by Region](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/pmf.png?raw=true)

![ACT/SAT Score Ratios by Region](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/kde.png?raw=true)

Next, we can combine the ACT scores between Midwestern and other colleges. The first thing that stands out is that schools in the Midwest appear to have ACT scores that have are on average higher. Midwestern schools seemed to be skewed to the right more than non-Midwestern schools. We cannot draw many conclusions from this graph. However, it does seem to suggest that Midwestern schools score higher on the ACT. It might be interesting to compare the ratio of ACT / SAT scores in the two regions.

#### Analysis
A few things stand out from this graph. Schools in the "other" category have a wider distribution of scores, which makes sense considering there are about 7 times as many schools in this category. Second, it appears that Midwest areas have a slightly higher ratio (0.9694 compared to 0.9600). We are not yet sure whether this is statistically significant. However, from the model it appears that the non-midwest schools' ratios are skewed left.

Finally, we can use Cohen's effect to get a more quantitative answer as to what the differences in ACT/SAT score ratios are like across Midwestern and other regions.

The ratio is 0.298, which is clearly positive and slight but noticeable. Although we can't determine any causation effects from this, we can draw inferences on what causes such distributions in the models. It could be that students applying to Midwestern schools (which might be Midwestern students) spend more time studying for the ACT than for the SAT. (It's also worth noting that our model only includes schools that accept both the ACT and SAT). The longer left tail of non-Midwestern schools might be explained by the fact that many students outside the Midwest primarily study for the SAT and only take the ACT out of curiosity, whim, or hope.

#### Interpretation
What does this all mean for students trying to gain an edge in admissions? If you are applying to a Midwestern school, it might be slightly easier to stand out by studying for the SAT. Conversely, if you are not in the Midwest, studying for the ACT might give you an upper edge. This hypothesis of course makes a variety of assumptions, such as the fact that studying for either tests will have an equal advantage.
