# Global Sales Performance Analysis

## Project Overview
A comprehensive statistical analysis of global sales data to extract actionable business insights. This project demonstrates various data analysis techniques using Python, from basic descriptive statistics to advanced hypothesis testing and visualization.

## Dataset Description
The dataset (`large_sales_data.csv`) contains 1000 sales records with the following attributes:
- **Region**: Geographic sales regions (East, West, North, South)
- **Salesperson**: Sales representative names
- **Revenue**: Total revenue generated
- **Profit**: Profit earned
- **Units_Sold**: Number of units sold
- **Customer_Satisfaction**: Rating from 1-5
- **Marketing_Spend**: Amount spent on marketing
- **Discount_Percentage**: Discount offered
- **Product_Category**: Type of product (Furniture, Automobile, Electronics, Clothing, Grocery)
- **Sales_Channel**: Distribution channel (Retail, Wholesale, Online)
- **Order_Processing_Time**: Time taken to process orders

## Analysis Performed

### 1. Exploratory Data Analysis
- Summary statistics for key metrics (Revenue, Profit, Units Sold)
- Distribution analysis with histograms and Q-Q plots
- Box plots for Customer Satisfaction

### 2. Statistical Analysis
- Correlation analysis between Marketing Spend and Revenue
- Probability calculations for Customer Satisfaction and Discount rates
- Confidence interval estimation

### 3. Hypothesis Testing
- T-tests comparing revenue across different sales channels
- Chi-Square test examining association between Product Category and Sales Channel
- ANOVA test evaluating revenue differences across sales channels

### 4. Regression Analysis
- Linear regression to examine relationship between Revenue and Profit

## Key Findings
1. **Marketing Impact**: Surprisingly, there is almost no correlation (-0.015) between Marketing Spend and Revenue
2. **Channel Distribution**: Online is the most common sales channel
3. **Customer Satisfaction**: 11.1% probability of Customer Satisfaction exceeding 4.5
4. **Product-Channel Association**: Statistically significant association exists between Product Category and Sales Channel (p-value = 0.041)
5. **Revenue Consistency**: No significant difference in revenue across different sales channels

## Technical Implementation
- **Language**: Python 3.10
- **Libraries**: pandas, numpy, matplotlib, seaborn, scipy.stats, statsmodels
- **Environment**: Jupyter Notebook

## How to Run
1. Clone this repository
2. Install required packages: `pip install -r requirements.txt`
3. Open and run the Jupyter notebook: `jupyter notebook statistics-in-python.ipynb`

## Future Work
- Time series analysis of sales trends
- Customer segmentation using clustering techniques
- Predictive modeling for future sales forecasting
- Advanced visualization with interactive dashboards

## Author
Shohinur Pervez Shohan  
Data Analyst  
[LinkedIn](https://www.linkedin.com/in/shohinur-pervez-shohan/)

## License
This project is licensed under the CC0-1.0 License - see the LICENSE file for details.