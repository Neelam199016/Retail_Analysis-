# Retail_Analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. LOAD DATA
df = pd.read_excel(
    r"C:\Users\Neela\Desktop\retail_large_dataset.csv.xlsx"
)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("\nFirst 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print("\nColumn Names:")
print(df.columns.tolist())

# 2. BASIC DATA INFORMATION
print("\nData Information:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nUnique Customers:", df["customer_id"].nunique())
print("Unique Orders:", df["order_id"].nunique())
print("\nDescriptive Statistics:")
print(df.describe())

# 3. NUMERIC COLUMNS
numeric_columns = [
    "age",
    "product_price",
    "quantity",
    "discount_percentage",
    "final_price",
    "delivery_days"
]
print("\nNumeric Column Statistics:")
print(df[numeric_columns].describe().T)

# 4. DATA VALIDATION
print("\n--- Checking Invalid Values ---")
print(
    "Invalid age values:",
    ((df["age"] < 18) | (df["age"] > 100)).sum()
)
print(
    "Invalid quantity values:",
    (df["quantity"] <= 0).sum()
)
print(
    "Invalid discount values:",
    (
        (df["discount_percentage"] < 0) |
        (df["discount_percentage"] > 100)
    ).sum()
)
print(
    "Invalid product prices:",
    (df["product_price"] <= 0).sum()
)

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])
print(
    "\nOrder Date Data Type:",
    df["order_date"].dtype
)
print(
    "Invalid delivery days:",
    (df["delivery_days"] <= 0).sum()
)

# 5. REVENUE COLUMN
df["revenue"] = df["final_price"]

print("\nRevenue Check:")
print(
    df[
        [
            "product_price",
            "quantity",
            "discount_percentage",
            "final_price",
            "revenue"
        ]
    ].head()
)

# 6. FINAL DATA CHECK
print("\n--- Final Data Checking ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\nData Types:")
print(df.dtypes)

#                    UNIVARIATE ANALYSIS

# 7. AGE ANALYSIS
print(df["age"].describe())

mean_age = df["age"].mean()
median_age = df["age"].median()
min_age = df["age"].min()
max_age = df["age"].max()
std_age = df["age"].std()

print(f"\nAverage Customer Age: {mean_age:.2f} years")
print(f"Median Customer Age: {median_age:.2f} years")
print("Minimum Age:", min_age)
print("Maximum Age:", max_age)
print(f"Standard Deviation of Age: {std_age:.2f}")

# Age Summary Table
age_summary = pd.DataFrame({
    "Statistic": [
        "Count",
        "Mean",
        "Median",
        "Minimum",
        "Maximum",
        "Standard Deviation"
    ],
    "Value": [
        df["age"].count(),
        df["age"].mean(),
        df["age"].median(),
        df["age"].min(),
        df["age"].max(),
        df["age"].std()
    ]
})

print("\nAge Summary:")
print(age_summary)

# Age Histogram
plt.figure(figsize=(10, 6))
plt.hist(df["age"], bins=18)
plt.title(
    "Distribution of Customer Age",
    fontsize=16,
    fontweight="bold"
)
plt.xlabel(
    "Age",
    fontstyle="italic"
)
plt.ylabel(
    "Number of Customers",
    fontsize=12
)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Age Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df["age"])
plt.title(
    "Boxplot of Customer Age",
    fontsize=20,
    fontweight="bold"
)
plt.ylabel(
    "Age",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# 8. AGE GROUP ANALYSIS
bins = [17, 25, 35, 45, 55, 65]
labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65"
]
df["age_group"] = pd.cut(
    df["age"],
    bins=bins,
    labels=labels,
    right=True
)
age_group_counts = (
    df["age_group"]
    .value_counts()
    .sort_index()
)
print("\nCustomer Count by Age Group:")
print(age_group_counts)
age_group_percentage = (
    df["age_group"]
    .value_counts(normalize=True)
    .sort_index() * 100
)
print("\nCustomer Percentage by Age Group:")
print(age_group_percentage.round(2))

# Age Group Bar Chart
plt.figure(figsize=(10, 6))
age_group_counts.plot(kind="bar")
plt.title(
    "Customer Distribution by Age Group",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Age Group",
    fontstyle="italic"
)
plt.ylabel(
    "Number of Customers",
    fontsize=14
)
plt.xticks(
    rotation=0,
    fontsize=12
)
plt.yticks(fontsize=12)
plt.show()

# 9. PRODUCT PRICE ANALYSIS
print("\nProduct Price Statistics:")
print(df["product_price"].describe())

mean_price = df["product_price"].mean()
median_price = df["product_price"].median()
min_price = df["product_price"].min()
max_price = df["product_price"].max()
std_price = df["product_price"].std()

print(f"\nAverage Product Price: ₹{mean_price:,.2f}")
print(f"Median Product Price: ₹{median_price:,.2f}")
print(f"Minimum Product Price: ₹{min_price:,.2f}")
print(f"Maximum Product Price: ₹{max_price:,.2f}")
print(f"Standard Deviation: ₹{std_price:,.2f}")

# Product Price Summary
price_summary = pd.DataFrame({
    "Statistic": [
        "Count",
        "Mean",
        "Median",
        "Standard Deviation",
        "Minimum",
        "25th Percentile",
        "75th Percentile",
        "Maximum"
    ],
    "Value": [
        df["product_price"].count(),
        df["product_price"].mean(),
        df["product_price"].median(),
        df["product_price"].std(),
        df["product_price"].min(),
        df["product_price"].quantile(0.25),
        df["product_price"].quantile(0.75),
        df["product_price"].max()
    ]
})
print("\nProduct Price Summary:")
print(price_summary)

# Product Price Histogram
plt.figure(figsize=(10, 6))
plt.hist(
    df["product_price"],
    bins=30,
    edgecolor="black"
)
plt.title(
    "Distribution of Product Price",
    fontsize=18,
    fontweight="bold"
)
plt.xlabel(
    "Product Price (₹)",
    fontstyle="italic"
)
plt.ylabel(
    "Number of Products",
    fontsize=12
)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# Product Price Boxplot

plt.figure(figsize=(10, 4))
plt.boxplot(
    df["product_price"],
    orientation="horizontal"
)
plt.title(
    "Boxplot of Product Price",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Product Price (₹)",
    fontstyle="italic"
)
plt.xticks(fontsize=12)
plt.show()

# Product Price IQR
Q1 = df["product_price"].quantile(0.25)
Q3 = df["product_price"].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
product_price_outliers = df[
    (df["product_price"] < lower_bound) |
    (df["product_price"] > upper_bound)
]
print("\nProduct Price IQR Analysis:")
print(f"Q1: ₹{Q1:,.2f}")
print(f"Q3: ₹{Q3:,.2f}")
print(f"IQR: ₹{IQR:,.2f}")
print(f"Lower Bound: ₹{lower_bound:,.2f}")
print(f"Upper Bound: ₹{upper_bound:,.2f}")
print("Number of Outliers:", len(product_price_outliers))

# 10. QUANTITY ANALYSIS
print(df["quantity"].describe())
quantity_counts = (
    df["quantity"]
    .value_counts()
    .sort_index()
)
print("\nQuantity Counts:")
print(quantity_counts)
quantity_percentage = (
    df["quantity"]
    .value_counts(normalize=True)
    .sort_index() * 100
)
print("\nQuantity Percentage:")
print(quantity_percentage.round(2))

# Quantity Bar Chart
plt.figure(figsize=(8, 5))
quantity_counts.plot(kind="bar")
plt.title(
    "Distribution of Quantity Purchased",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Quantity Purchased",
    fontstyle="italic"
)
plt.ylabel(
    "Number of Transactions",
    fontsize=14
)
plt.xticks(
    rotation=0,
    fontsize=12
)
plt.yticks(fontsize=12)
plt.show()

# 11. DISCOUNT PERCENTAGE ANALYSIS
# Discount Histogram
plt.figure(figsize=(10, 6))
plt.hist(
    df["discount_percentage"],
    bins=31,
    edgecolor="black"
)
plt.title(
    "Distribution of Discount Percentage",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Discount Percentage",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Frequency",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Discount Boxplot
plt.figure(figsize=(10, 5))
plt.boxplot(df["discount_percentage"])
plt.title(
    "Boxplot of Discount Percentage",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Discount Percentage",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Discount Percentage",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# 12. FINAL PRICE ANALYSIS

print("\nFinal Price Statistics:")
print(df["final_price"].describe())

# Final Price Histogram
plt.figure(figsize=(10, 6))
plt.hist(
    df["final_price"],
    bins=30,
    edgecolor="black"
)
plt.title(
    "Distribution of Final Price",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Final Price (₹)",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Frequency",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Final Price Boxplot

plt.figure(figsize=(10, 5))
plt.boxplot(df["final_price"])
plt.title(
    "Boxplot of Final Price",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Final Price (₹)",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Final Price (₹)",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# Final Price IQR

Q1 = df["final_price"].quantile(0.25)
Q3 = df["final_price"].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
final_price_outliers = df[
    (df["final_price"] < lower_bound) |
    (df["final_price"] > upper_bound)
]
print("\nFinal Price IQR Analysis:")
print(f"Q1: ₹{Q1:,.2f}")
print(f"Q3: ₹{Q3:,.2f}")
print(f"IQR: ₹{IQR:,.2f}")
print(f"Lower Bound: ₹{lower_bound:,.2f}")
print(f"Upper Bound: ₹{upper_bound:,.2f}")
print("Number of Outliers:", len(final_price_outliers))

#                    BIVARIATE ANALYSIS
# 13. AGE VS FINAL PRICE
print("\n--- Bivariate Analysis: Age vs Final Price ---")
age_price_correlation = (
    df["age"].corr(df["final_price"])
)
print(
    f"Correlation between Age and Final Price: "
    f"{age_price_correlation:.3f}"
)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["age"],
    y=df["final_price"],
    alpha=0.5
)
plt.title(
    "Age vs Final Price",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Customer Age",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Final Price (₹)",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# 14. PRODUCT PRICE VS FINAL PRICE
print("\n--- Bivariate Analysis: Product Price vs Final Price ---")
price_correlation = (
    df["product_price"].corr(df["final_price"])
)
print(
    f"Correlation between Product Price and Final Price: "
    f"{price_correlation:.3f}"
)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df["product_price"],
    y=df["final_price"],
    alpha=0.5
)
plt.title(
    "Product Price vs Final Price",
    fontsize=20,
    fontweight="bold"
)
plt.xlabel(
    "Product Price (₹)",
    fontsize=14,
    fontstyle="italic"
)
plt.ylabel(
    "Final Price (₹)",
    fontsize=14
)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

# MULTIVARIATE ANALYSIS
print("\n" + "=" * 60)
print("              MULTIVARIATE ANALYSIS")
print("=" * 60)
# Correlation Matrix
correlation_matrix = df[
    ["age", "product_price", "quantity",
     "discount_percentage", "final_price", "delivery_days"]
].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix.round(3))

# Heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.show()
plt.close()

# Multivariate Scatter Plot
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="product_price",
    y="final_price",
    hue="quantity",
    alpha=0.6
)

plt.title("Product Price vs Final Price by Quantity")
plt.xlabel("Product Price (₹)")
plt.ylabel("Final Price (₹)")
plt.tight_layout()
plt.show()
plt.close()

# END OF CURRENT ANALYSIS
print("\n\n====================================================")
print("          ANALYSIS COMPLETED SUCCESSFULLY")
print("====================================================")
