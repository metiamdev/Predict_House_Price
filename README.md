# Predict_House_Price

# House Price Prediction Using Multiple Linear Regression 

# 1.Introduction 
The goal of this project is to predict house prices based on multiple features such as square footage, number of bedrooms, number of bathrooms, year built, lot size, garage size, and neighborhood quality.
<br>
We use Multiple Linear Regression (MLR) to model the relationship between these independent features and the dependent variable (House_Price).

# 2.Dataset
The dataset used in this project is stored in a CSV file named house_price_regression_dataset.csv.
It contains the following columns : 

<br>
◉ Square_Footage → Total area of the house.
<br>
◉ Num_Bedrooms → Number of bedrooms
<br>
◉ Num_Bathrooms → Number of bathrooms
<br>
◉ Year_Built → Year when the house was built
<br>
◉ Lot_Size → Size of the lot.
<br>
◉ Garage_Size → Size of the garage
<br>
◉ Neighborhood_Quality → A score representing the quality of the neighborhood
<br>
◉ House_Price → Target variable (price of the house)


# 3.Model : Multiple Linear Regression 
We use Linear Regression from scikit-learn 
The model learns the relationship between the features and house prices by minimizing the Mean Squared Error (MSE).
Coefficients represent the impact of each feature on house price.
Intercept represents the base price when all features are zero.
R² Score measures the accuracy of the model, indicating how much variance in house price is explained by the features.

# 4.Correlation Analysis
To measure the strength of relationship between each feature and house price, we calculate the Pearson correlation coefficient.
The program computes the correlation of each feature with House_Price and identifies the maximum correlated feature. This helps us understand which variable has the greatest influence on price.
