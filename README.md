# My Portfolios

## Contents
- Thesis at Master's Degree (Image Enhancement and Hybrid CNN to Improve COVID-19 Classification Performance on Chest X-Ray Images)
- Python Projects
- Kaggle Competitions
- PowerBI Dashboards
- SQL

# Thesis at Master's Degree (Image Enhancement and Hybrid CNN to Improve COVID-19 Classification Performance on Chest X-Ray Images)
The COVID-19 pandemic has claimed many lives and is predicted to continue. The classification process using CXR images has been widely carried out and uses various methods, one of which is using a hybrid CNN model. To improve classification performance using a hybrid CNN model, image enhancement techniques can be applied to CXR images. This research proposes the CLAHE image enhancement technique which is applied to CXR images which are then classified using a hybrid CNN model. The experimental results show that there is an increase in classification performance as evidenced by the highest AUC value of 0.821. Testing results also show a significant increase in classification performance between the proposed hybrid CNN model and the existing hybrid CNN models.

[Thesis summary](https://drive.google.com/file/d/1ERZ1nT4senbCwTnfA8rvYDTc6ldcQWUH/view?usp=sharing)

# Python Projects
### Predict prices of airline tickets
I did a data science case by analysing and validating the ticket price of multiple airlines in India. I built a model using Random Forest Regressor to validate the of airline ticket's price. My first step began with loading the data which was in excel format, it has about 10500 rows of records. Then I cleaned the data by deleting the missing values which was happened on one row only. Next step, I started to do a little feature engineering from existing features (ex. extracting time, date, month, year).

Next, I explore the modified data to get some insights. Here, I found that most flights happened at early morning (4 AM to 8 AM) followed by evening (16 PM to 20 PM).

The process of feature engineering and finding insights had been done couple times alternately. After couple of process, I found new insight that as the duration of flight increases, the price also increases. Other insights I found as well such as most flights flew to Cochin, Jet Airways Business has the most expensive ticket price among other airlines.

After several feature encoding, the two last thing I did was handling the outliers of the price and showing the feature importance. 

Now the final step which was building the model using Random Forest Regressor and applied it to the splitted data (train and validation). By using this model, I got 95.1% of training result and 83.0% of test result.

This data science case is just for experiment only, they are not for business purpose, and yes, there are still a lot of other things that could improve this whole step.

[Python Code](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/Predict_prices_of_airline_tickets.ipynb)

### Predict status of chronic kidney disease
Address the chronic kindney disease classification problem by applying XGBoost and then Randomized Search which resulted in best parameter for the classifier.

[Python Code](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/Predict_status_of_chronic_kidney_disease.ipynb) 

### Predict the cancellation of hotel bookings
Using multiple classification algorithms such as Naive Bayes, KNN, Logistic Regression, Random Forest and Decision Tree to predict the cancellations in binary format.

[Python Code](https://github.com/tengkumuazabs/my-portfolio/blob/main/python-projects/Predict_the_cancellation_of_hotel_bookings.ipynb) 

# Kaggle Competitions

| Link | Tools | Description | 
|---|---|---|
| [Titanic Spaceship Data Competition](https://www.kaggle.com/code/yeehawww/titanic-spaceship-competition/notebook) | Python | This competition gives me 80.0% of accuracy The algorithm VotingClassifier between CatBoost and GaussianNB was used. |
| [Digit Recognizer Competition](https://www.kaggle.com/yeehawww/digit-recognizer-using-neural-network) | Python | 96.4% of score was achieved using simple Neural Network algorithm. |
| [Titanic Spaceship Data Competition](https://www.kaggle.com/code/yeehawww/titanic-competition/notebook?scriptVersionId=128118357) | Python | Again, by using VotingClassifier between CatBoost and GaussianNB, I got 78.2% of accuracy. |

# PowerBI Dashboards
### Campus' Registration Dashboard
<img width="577" alt="image" src="https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Registration%20Dashboard.png">

### Campus' Acceptance Rate
Bar Chart             |  Line Chart
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Acceptance%20Rate_Page_1.png)  |  ![](https://raw.githubusercontent.com/tengkumuazabs/my-portfolio/main/powerbi/Acceptance%20Rate_Page_2.png)

Note: These dashboards above have been modified for privacy reason. They do not represent true data.

# SQL
| Link | Description |
|---|---|
| [Airport Database Analysis](https://github.com/tengkumuazabs/my-portfolio/blob/main/sql/Airport_database_analysis.md) | Applying some SQL queries to answer couple of questions regarding aviation use case. Multiple tables are involved here with their uniqe relation each other. Here, couple entities has been analysed such as airplane info, passengers info, and airport info. |
| [Supermart Database Analysis](https://github.com/tengkumuazabs/my-portfolio/blob/main/sql/Supermart_database_analysis.md) | Doing analysis by answering couple of questions in market business like who did the order the most, what is the top 5 most ordered product, who ordered product X, etc. |

