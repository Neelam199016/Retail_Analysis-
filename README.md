# Retail_Analysis-
Retail Data Analysis
Exploratory Data Analysis of Retail Transaction Data

This project performs Exploratory Data Analysis (EDA) on a large-scale retail transaction dataset containing 100,000 records.

The analysis focuses on understanding customer behavior, product pricing, quantities, discounts, final prices, delivery times, and relationships between important numerical variables.

📊 Project Overview

The project uses Python-based data analysis and visualization techniques to explore a retail transaction dataset.

Dataset Information
Records: 100,000
Original Variables: 18
Missing Values: 0
Duplicate Records: 0
Data Type: Retail transaction data

The dataset contains information about:

Customers
Orders
Products
Product prices
Quantity purchased
Discounts
Final prices
Payment methods
Shipping methods
Delivery days
Return status
🎯 Project Objectives

The main objectives of this project are:

Perform data loading and initial inspection
Check and validate data quality
Analyze numerical variables using descriptive statistics
Understand data distributions using visualizations
Identify relationships between variables
Perform univariate analysis
Perform bivariate analysis
Perform multivariate analysis
Calculate correlations between numerical variables
Perform statistical significance testing
Extract meaningful business insights from the data
🛠️ Technologies and Tools

The project was developed using:

Python
Pandas
NumPy
Matplotlib
Seaborn
SciPy
Jupyter Notebook
Visual Studio Code
Git & GitHub
🔍 Analysis Performed
1. Data Quality Analysis

The dataset was checked for:

Missing values
Duplicate records
Invalid ages
Invalid quantities
Invalid discount percentages
Invalid product prices
Invalid delivery days

The analysis found 0 missing values and 0 duplicate records.

2. Statistical Analysis

The project includes:

Descriptive statistics
Mean and median analysis
Standard deviation
Quartiles
Interquartile Range (IQR)
Outlier analysis
Skewness
Kurtosis
95% confidence interval estimation
Pearson correlation analysis
Statistical significance testing
3. Univariate Analysis

Univariate analysis was performed to understand individual variables.

The analysis includes:

Customer Age
Product Price
Quantity
Discount Percentage
Final Price
Delivery Days

Histograms, count plots, and boxplots were used to understand distributions and identify patterns.

4. Bivariate Analysis

Relationships between pairs of variables were analyzed using visualizations and correlation analysis.

Important relationships examined include:

Product Price vs Final Price
Age vs Final Price
Quantity vs Final Price
Discount Percentage vs Final Price
5. Multivariate Analysis

Multivariate analysis was performed to examine relationships among multiple numerical variables simultaneously.

A correlation matrix and heatmap were created using:

Age
Product Price
Quantity
Discount Percentage
Final Price
Delivery Days

A multivariate scatter plot was also created to examine Product Price vs Final Price by Quantity.

📈 Key Findings

Some important findings from the analysis include:

The average customer age is approximately 41.56 years.
Product Price ranges from ₹500 to ₹59,998.
The average Product Price is approximately ₹30,164.53.
Quantity purchased ranges from 1 to 4 units.
The average Final Price is approximately ₹64,165.72.
Product Price and Final Price have a correlation of approximately 0.731, indicating a strong positive linear association.
Quantity and Final Price have a correlation of approximately 0.575, indicating a moderate positive linear association.
Discount Percentage and Final Price have a correlation of approximately -0.137, indicating a weak negative linear association.
Age and Final Price have a correlation of approximately -0.001, indicating almost no linear relationship.
Delivery Days and Final Price have a correlation of approximately 0.004, indicating almost no linear relationship.
💡 Business Insights

The analysis provides several useful observations:

Higher product prices are generally associated with higher final prices.
Transactions with higher quantities tend to have higher final prices.
Discount percentage has a relatively weak relationship with final price.
Customer age shows very little linear association with final price.
Delivery days show very little linear association with final price.

These findings demonstrate how statistical analysis can be used to understand patterns in retail transaction data.

📂 Project Files

The repository contains:

Retail_Analysis/
│
├── retail_analysis.ipynb
├── retail_analysis.py
└── .vscode/
retail_analysis.ipynb

Contains the complete interactive analysis, including:

Data preparation
Statistical analysis
Visualizations
Interpretations
Key findings
Conclusion
retail_analysis.py

Contains the Python script used to perform the retail data analysis.

📊 Project Structure
Data Loading
      ↓
Data Quality Checks
      ↓
Statistical Analysis
      ↓
Univariate Analysis
      ↓
Bivariate Analysis
      ↓
Multivariate Analysis
      ↓
Correlation Analysis
      ↓
Business Insights
      ↓
Conclusion
🏁 Conclusion

This project demonstrates an end-to-end Exploratory Data Analysis workflow using Python.

The analysis combines statistical techniques and data visualization to understand a large-scale retail transaction dataset.

It demonstrates practical use of Pandas, NumPy, Matplotlib, Seaborn, and SciPy for data cleaning, statistical analysis, visualization, and interpretation.

The project also demonstrates how exploratory analysis can help identify relationships between product pricing, quantity, discounts, and final transaction prices.

👩‍💻 Author

Neelam

Aspiring Data Analyst

Skills demonstrated:

Python | Pandas | NumPy | Matplotlib | Seaborn | SciPy | Exploratory Data Analysis | Data Visualization | Statistics
