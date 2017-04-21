# NBA Shot Distribution
### by Willem Thorbecke and David Papp

https://github.com/davpapp/ThinkStats2/blob/master/code/report3nba.ipynb


#### Introduction
Despite playing specific positions and zones, NBA players take shots from all over the court. The location of the shot is important in determining the efficiency of the shot and the chance of being blocked. We took data from the 2016-2017 NBA year from Stephen Curry and used clustering to divide his shots into clusters based on region. Our goal was to see which clustering algorithm produces clusters most consistent with NBA positions.

#### Methodology
We used a third-party API to download official data from the NBA. The API fetched relevant information from the NBA's website, including the IDs of players and the location of their shots. We chose to study perhaps the most famous shooter, Stephen Curry. First, we plotted the location of his shots to get a sense of our raw data.

![Curry Shots](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/curry_shots.png?raw=true)

Applying a K-means cluster model with a varied number of clusters, we obtained reasonable clusters. 

![K-means ward](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/kmeansward.png?raw=true)

Using only 4 clusters with no connectivity, when linkage was set to ward, the plot started to resemble typical NBA positions.

Finally, with 5 clusters, connectivity, and ward linkage, we got the most consistent plot. 

![5 cluster ward](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/5clusterward.png?raw=true)

We also created a side-by-side visualization tool to help us choose the most fitting model. This tool could be generalized for other purposes.

![Visualization](https://github.com/davpapp/ThinkStats2/blob/master/Reports/Images/visualization.png?raw=true)

#### Analysis
Although splitting one player's shots into clusters by position provides relatively little value, there is much to learn from the process. Using the same cluster algorithm, if we have information regarding the accuracy of each zone from which shots are taken, we could estimate the likelihood of making future shots. Similarly, if we know the location of defenders, we could calculate how a defender affects Curry's shot. Furthermore, using our visualization tool for different clustering algorithms, we could easily find the appropriate the model for different purposes.
