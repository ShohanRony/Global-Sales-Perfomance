# Global Sales Data Description

## Overview
This dataset contains 1000 records of global sales data across different regions, product categories, and sales channels. It's designed for statistical analysis and business intelligence exercises.

## Column Descriptions

| Column Name | Data Type | Description | Example Values |
|-------------|-----------|-------------|----------------|
| Region | Categorical | Geographic sales region | East, West, North, South |
| Salesperson | Categorical | Name of the sales representative | Alice, Bob, Charlie, David, Eve |
| Revenue | Numeric | Total revenue generated from the sale | 137118, 78577, 19078 |
| Profit | Numeric | Profit earned from the sale | 10067, 38481, 28037 |
| Units_Sold | Numeric | Number of units sold | 219, 750, 406 |
| Customer_Satisfaction | Numeric | Customer satisfaction rating | 1.0 to 5.0 scale |
| Marketing_Spend | Numeric | Amount spent on marketing for this sale | 14666, 8254, 14746 |
| Discount_Percentage | Numeric | Percentage discount offered | 13.40, 3.70, 6.18 |
| Product_Category | Categorical | Type of product sold | Furniture, Automobile, Electronics, Clothing, Grocery |
| Sales_Channel | Categorical | Distribution channel used | Retail, Wholesale, Online |
| Order_Processing_Time | Numeric | Time taken to process the order (in days) | 1, 3, 5 |

## Statistical Summary

| Variable | Mean | Std Dev | Min | Max |
|----------|------|---------|-----|-----|
| Revenue | 107,316 | 55,015 | 10,163 | 199,784 |
| Profit | 23,973 | 14,067 | 1,097 | 49,980 |
| Units_Sold | 499 | 282 | 10 | 999 |
| Customer_Satisfaction | 2.87 | 1.13 | 1.00 | 5.00 |
| Marketing_Spend | 10,181 | 5,754 | 501 | 19,965 |
| Discount_Percentage | 15.42 | 8.77 | 0.03 | 29.98 |
| Order_Processing_Time | 5.02 | 2.58 | 1 | 9 |

## Category Distributions

### Region Distribution
- East: 28.7%
- West: 27.3%
- North: 25.1%
- South: 18.9%

### Product Category Distribution
- Furniture: 21.6%
- Automobile: 20.8%
- Electronics: 20.5%
- Clothing: 19.7%
- Grocery: 17.4%

### Sales Channel Distribution
- Online: 37.2%
- Retail: 33.5%
- Wholesale: 29.3%

## Data Quality Notes
- No missing values in the dataset
- All numeric variables have appropriate ranges
- Customer Satisfaction follows a relatively normal distribution
- Revenue shows slight positive skewness