# Interactive dashboard to visualize and predict customer churn

## Problem Description
Customer Churn is when customers stop using a business’s product or service and switch to products or services offered by the business’s competitors. This is a challenging issue for many businesses since it costs more to acquire new customers than to retain existing customers. Thus, it is useful for businesses to analyze customer churn and find ways to reduce it. 

Customer churn is a prominent problem in the telecommunication industry due to the low switching costs and the abundance of alternative service providers. The telecommunication industry has access to a large amount of customer data compared to many other industries. This data can be used to derive massive insights relevant to customer churn and measures can be taken to reduce it.

This project develops a web-based interactive dashboard for a given dataset for Chatterbox Telco Pvt Ltd in the Banana Republic to derive valuable insights from customer data to make decisions to reduce customer churn. Interactive dashboards provide real-time data visualizations in a manner that’s easy for stakeholders to comprehend and make decisions.

## Approach followed 

In the approach to be followed, a machine learning pipeline was created to accurately predict the customer churn. First the data was cleaned to remove erroneous and duplicate values since they will interfere with the proper analysis of data. Next, data was manipulated and analyzed. Thereafter, different machine learning models were used to predict the customer churn. The model with the highest accuracy was then be chosen using different evaluation metrics. Power BI was then used to derive insights from the data and produce the interactive dashboard containing the analytics most useful for the telecommunication company to make decisions.

# Implementation

The intial dataset was preprocessed using python. Python pandas, numpy libraries were used. The preprocessing code can be found in the 'Data Preprocessing' folder.

The preprocessed train dataset used to derive visualisations and thePowerBI file containing visualisation are contained in the 'Dashboard-PowerBI' folder.

The preprocessed train dataset was used to train the model and the preprocessed test dataset was used to test the accuracy of the model. The model seletion process was done separately and is not included in this repository. 

The selected model and the model training can be found in the model.py file. The app is built using Flask and can be found in the app.py file.

This dashboard created in PowerBI was published and the embedded HTML code was incorporated into the app. The dashboard.html file in the 'templates' folder contains the full HTML code for the dashboard and the form to fill in the input fields for churn prediction. Upon filling the form, the user is directed to the result.html page, where the prediction output will appear.
