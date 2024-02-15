# My Portfolios

## Contents
- Thesis at Master's Degree (Image Enhancement and Hybrid CNN to Improve COVID-19 Classification Performance on Chest X-Ray Images)
- Python Projects
- Kaggle Competitions
- PowerBI Dashboards
- SQL

# Thesis at Master's Degree (Image Enhancement and Hybrid CNN to Improve COVID-19 Classification Performance on Chest X-Ray Images)

The COVID-19 pandemic has claimed many lives and is predicted to continue. The classification process using CXR images has been widely carried out and uses various methods, one of which is using a hybrid CNN model. To improve classification performance using a hybrid CNN model, image enhancement techniques can be applied to CXR images. This research proposes the CLAHE image enhancement technique which is applied to CXR images which are then classified using a hybrid CNN model. The experimental results show that there is an increase in classification performance as evidenced by the highest AUC value of 0.821. Testing results also show a significant increase in classification performance between the proposed hybrid CNN model and the existing hybrid CNN models.

# Python Projects
### Predict prices of airline tickets

[Python Code](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/airlines/Predict_pres_of_airline_tickets.ipynb)

I did a data science case by analysing and validating the ticket price of multiple airlines in India. I built a model using Random Forest Regressor to validate the of airline ticket's price. My first step began with loading the data which was in excel format, it has about 10,500 rows of records. Then, I cleaned the data by deleting the missing values which was happened on one row only. Next step, I started to do a little feature engineering from existing features (ex. extracting time, date, month, year).

Next, I explore the modified data to get some insights. Here, I found that most flights happened at early morning (4 AM to 8 AM) followed by evening (16 PM to 20 PM) (**Figure 1**).

The process of feature engineering and finding insights had been done couple times alternately. After couple of process, I found new insight that as the duration of flight increases, the price also increases (**Figure 2**). Other insights I found as well such as most flights flew to Cochin (**Figure 3**), Jet Airways Business has the most expensive ticket price among other airlines (**Figure 4**).

Figure 1             |  Figure 2
:-------------------------:|:-------------------------:
<img width="333" alt="image" src="https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/python-projects/airlines/img/most_time.png">  |  <img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/airlines/img/most_destination.png?raw=true">
Figure 3             |  Figure 4
<img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/airlines/img/price_duration.png?raw=true"> |  <img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/airlines/img/airlines_price.png?raw=true">

After several feature encoding, the two last thing I did was handling the outliers of the price and showing the feature importance. 

Now the final step which was building the model using Random Forest Regressor and applied it to the splitted data (train and validation). By using this model, I got 95.1% of training result and 83.0% of test result.

This data science project is for experimental and study purpose only. And yes, there are still a lot of other things that could improve this whole step.

### Predict status of chronic kidney disease

[Python Code](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/Predict_status_of_chronic_kidney_disease.ipynb) 

Using only small amount of CSV data (400 rows and 26 columns), I predicted the status of chronic kidney disease (CKD or not CKD) which resulted in 92% of validation accuracy. I did several feature engineering by modifying column names, handling couple of redundat values but have same meaning.

Exploratory data analysis was done by using multiple visualization. Several features such as age, blood glucose, blood urea were skewed (**Figure 1**). Then, I showed distribution of categorical data whose distributions were not balanced, even the class was not balanced as well (**Figure 2**). 

Other insights I discoverd such as when red blood count is 5 or more and packed cell volume is 40 or more, the class more likely to be not CKD rather than CKD (**Figure 3**). Albumin levels also affect the CKD status (**Figure 4**). The same thing happed with packed cell volume, it's observed that not CKD status are detected when packed cell volume is 40 or more (**Figure 5**).
The specific gravity is 1.02 or more also affects CKD status (**Figure 6**).

Figure 1             |  Figure 2
:-------------------------:|:-------------------------:
<img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/skewed_histogram.png">  |  <img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/class_distribution.png">
Figure 3             |  Figure 4
<img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/pcv_bu.png?raw=true"> |  <img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/rbcc_alb.png">
Figure 5             |  Figure 6
<img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/rbcc_pcv.png"> |  <img width="333" alt="image" src="https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/kidney/img/specific_gravity.png">

Next step is feature encoding and feature selection that 10 most important features were selected for model training using XGBoost Classifier. Finally, RandomizedSearchCV was used to select the best hyperparameter for the trained model.


### Other Python Projects
| Projects Title | Description | 
|---|---|
| [Predict the cancellation of hotel bookings](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/hotel/Predict_the_cancellation_of_hotel_bookings.ipynb) | Used multiple classification algorithms such as Naive Bayes, KNN, Logistic Regression, Random Forest and Decision Tree to predict the cancellations whether it is yes or no. |

# Kaggle Competitions

| Link | Description | 
|---|---|
| [Spaceship Titanic](https://www.kaggle.com/code/yeehawww/titanic-spaceship-competition/notebook) | This competition gives me 80.0% of accuracy The algorithm VotingClassifier between CatBoost and GaussianNB was used. |
| [Digit Recognizer](https://www.kaggle.com/yeehawww/digit-recognizer-using-neural-network) | 96.4% of score was achieved using simple Neural Network algorithm. |
| [Titanic - Machine Learning from Disaster](https://www.kaggle.com/code/yeehawww/titanic-competition/notebook?scriptVersionId=128118357) | By using VotingClassifier between CatBoost and GaussianNB, I got 78.2% of accuracy. |
| [Binary Prediction of Smoker Status using Bio-Signals](https://www.kaggle.com/code/yeehawww/binary-prediction-of-smoker) | I applied Light Gradient Boosting Machine Classifier on this binary prediction and it gave me 79.0% of AUC score. |
| [Binary Classification with a Bank Churn Dataset](https://www.kaggle.com/code/yeehawww/binary-classification-with-a-bank-churn-dataset) | A Kaggle competition which I joined to classify bank churn dataset. I used CatBoost classifer and it gave me 88.6% of AUC score. |
| [House Prices - Advanced Regression Techniques](https://www.kaggle.com/code/yeehawww/house-prices) | Here, I predict the price of houses from its available features. This regression competition I solved using CatBoost Regressor and resulted in 0.172 of Root Mean Squared Error (RMSE) metrics. |

# PowerBI Dashboards
## Experience Recap
- Developed multiple dashboards such as campus registration reports and major’s acceptance rate year by year.
- Combined annual data from 2020-2023 which happened to have different data structures.
- Cleaned redundant data which recorded more than one.
- Published dashboards to make them accessible.
  
### Campus' Registration Dashboard
<img width="577" alt="image" src="https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Registration%20Dashboard.png">
This dashboard shows the summary of new students who successfully registered to the campus in 2023. It has multiple visualizations and its has multiple kind of interactions such as direct click to a visual, search bar, and selection.

### Campus' Acceptance Rate
Bar Chart             |  Line Chart
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Acceptance%20Rate_Page_1.png)  |  ![](https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Acceptance%20Rate_Page_2.png)

This dashboard shows how each major has different acceptance rate from 2019 to 2022. Bar chart and line chart are used to visualize the rates.

Note: These dashboards above have been modified for privacy reason. They do not represent true data.

# SQL
| Link | Description |
|---|---|
| [Airport Database Analysis](https://github.com/tengkumuazabs/my-portfolio/blob/main/sql/Airport_database_analysis.md) | Applying some SQL queries to answer couple of questions regarding aviation use case. Multiple tables are involved here with their uniqe relation each other. Here, couple entities has been analysed such as airplane info, passengers info, and airport info. |
| [Supermart Database Analysis](https://github.com/tengkumuazabs/my-portfolio/blob/main/sql/Supermart_database_analysis.md) | Doing analysis by answering couple of questions in market business like who did the order the most, what is the top 5 most ordered product, who ordered product X, etc. |

