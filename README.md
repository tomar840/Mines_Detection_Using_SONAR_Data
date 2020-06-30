# Mines_Detection_Using_SONAR_Data
Detection of Mines/Rock using SONAR Data. Accuracy has been compared among various classification models 

* This project aims to classify the obstacle under sea water as either **Rock** *OR* **Mines**.
![image](https://user-images.githubusercontent.com/37335834/86133518-05d0f680-bb06-11ea-86d4-9256323974d3.png)

During the **Russo-Japanese War of 1904–1905**, two mines blew up when the Petropavlovsk struck them near Port Arthur, sending the holed vessel to the bottom and killing most of his crew in the process. This show us that why detecting mines under sea water, with good accuracy, is crucial to Navy of any country.

## 1. Data 
* I have used SONAR data available [publicly](http://networkrepository.com/sonar.php). This dataset contains 60 numerical features. 

### 1.1 Data Pre-Processing 
* This dataset does not contains any missing value and has all the features in numeric form. So, we just only need to find the relevant features. I have used principal component analysis [**(pca)**](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) for removing correlation among the features and reducing the dimension.

Below plot shows the variation of **explained variance** with the **number of componets** of *pca*

![image](https://user-images.githubusercontent.com/37335834/86135787-e7202f00-bb08-11ea-918f-3dbd1f0d285a.png)


## 2. Model Selection 
I have compared the *accuracy* with the *number of pca components* for **LinearRegression**, **LogisticRegression** and **RandomForestClassifier** model. 

### 2.1 LinearRegression 
Below plot shows the variation of *accuracy of test data* with *number of pca components* for LinearRegression model. 
![image](https://user-images.githubusercontent.com/37335834/86136007-2b133400-bb09-11ea-91f8-cdb06daced7a.png)

### 2.2 LogisticRegression  
Below plot shows the variation of *accuracy of test data* with *number of pca components* for LogisticRegression model. 
![image](https://user-images.githubusercontent.com/37335834/86136214-6e6da280-bb09-11ea-838b-36ea800bf1ff.png)

### 2.3 RandomForestClassifier  
Below plot shows the variation of *accuracy of test data* with *number of pca components* for RandomForestClassifier model. 
![image](https://user-images.githubusercontent.com/37335834/86136356-9f4dd780-bb09-11ea-99ab-c04c2fe25e73.png)

## 3. Conclusion 
* LinearRegression has the worst performance among the above models. 

* There is one intresting observayion from the above *accuracy* Vs *number of pca features* graph, RandomForestClassifier (an *ensemble* model) outperform LogisticRegrssion when the *number of pca components* are low. However, both these models have nearly the same performance when *number of pca components* are increased. 

* When *number of pca components* are in range 30 - 40, all the models failed miserably to perform on generalized data. 

* Taking **8-12** *pca features* on *RandomForestClassifier* will give the best performance on generalised data.


