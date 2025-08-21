#Assumption

Overall, I analyzed the data in more detail using various data visualization methods (including MAR, MCAR, and MNAR).

I noticed a large number of NAN values, which I consider a bad sign and suggests it might be more difficult to define the distribution (linear or normal) it follows, which is a bit troubling. However, since this is more like a study of age and income in a city, I think imputing missing values and deleting the row with almost 80% missing values would be more meaningful.

#Reflection

Through the course, I gained a general understanding of the pros and cons of these methods, as well as their usage scenarios. 

However, I'm not sure why MCAR/MNAR has so much missing data, but my own research has revealed that these two methods are ineffective, even negligible, for this data set. Furthermore, MAR only has four correlations between missing values and other variables (perhaps the dataset is too small?). Overall, to improve the visibility of the dataset, I used median imputation and removed the row with 80% missing data. This resulted in a more consistent and trended dataset.
