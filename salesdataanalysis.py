# ==========================================
# Sales Data Analysis Project Using Pandas
# ==========================================

# Import the Pandas library for data analysis
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file and store it in a DataFrame
df = pd.read_excel("Book1.xlsx")

# Display the first 5 rows of the dataset
print(df.head())

# Show information about the dataset
# (column names, data types, non-null values, memory usage)
print(df.info())

# Display statistical summary of numerical columns
print(df.describe())

# Create a new column named Total_Sales
# Formula: Price × Quantity
df["Total_Sales"] = df["Price"] * df["Quantity"]

# Display the first 5 rows after adding the new column
print(df.head())

# Calculate the total revenue generated from all orders
total_revenue = df["Total_Sales"].sum()
print("Total Revenue =", total_revenue)

# Calculate total sales for each product
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Display product-wise sales in descending order
print(product_sales.sort_values(ascending=False))

# Calculate total sales for each city
city_sales = df.groupby("City")["Total_Sales"].sum()

# Display city-wise sales in descending order
print(city_sales.sort_values(ascending=False))

# Calculate total sales for each category
category_sales = df.groupby("Category")["Total_Sales"].sum()

# Display category-wise sales in descending order
print(category_sales.sort_values(ascending=False))

# Filter and display only the records from Deesa city
deesa_sales = df[df["City"] == "Deesa"]
print(deesa_sales)

# Find the highest value in the Total_Sales column
print(df["Total_Sales"].max())

# Display the complete row having the highest Total_Sales
highest_sale = df[df["Total_Sales"] == df["Total_Sales"].max()]
print(highest_sale)

# Sort all records alphabetically by Product name (A-Z)
product_name = df.sort_values(by="Product", ascending=True)
print(product_name)

# Sort records by Price (Low to High)
print(df.sort_values(by="Price"))

# Sort records by Price (High to Low)
print(df.sort_values(by="Price", ascending=False))

# Sort records by Total_Sales (Highest to Lowest)
print(df.sort_values(by="Total_Sales", ascending=False))

# Sort records first by City and then by Product
print(df.sort_values(by=["City", "Product"]))

# Sort records by Category and within each category by Total_Sales
print(df.sort_values(by=["Category", "Total_Sales"], ascending=[True, False]))

# Display the Top 3 highest sales records
print(df.sort_values(by="Total_Sales", ascending=False).head(3))

# Display the Bottom 3 lowest sales records
print(df.sort_values(by="Total_Sales").head(3))

# Display all unique product names
print(df["Product"].unique())

# Display the total number of unique products
print(df["Product"].nunique())

# Count how many times each product appears
print(df["Product"].value_counts())

# Calculate the average sale amount
print("Average Sale =", df["Total_Sales"].mean())

# Display the row containing the highest priced product
print(df.loc[df["Price"].idxmax()])

# Display all orders where Total_Sales is greater than 50,000
highest_sales = df[df["Total_Sales"] > 50000]
print(highest_sales)

# Display the complete details of the order with the maximum Total_Sales
highest_order = df.loc[df["Total_Sales"].idxmax()]
print(highest_order)
#checking missing value
print(df.isnull().sum())
#duplicates values
print(df.duplicated().sum())
plt.figure(figsize=(12,6))
plt.bar(product_sales.index, product_sales.values)
plt.title("Product wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

