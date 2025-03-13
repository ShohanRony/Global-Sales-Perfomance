#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualization script for Global Sales Performance data
Author: Shohinur Pervez Shohan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(file_path='large_sales_data.csv'):
    """Load the sales dataset"""
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_revenue_by_region(df):
    """Plot average revenue by region"""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Region', y='Revenue', data=df, estimator=np.mean, ci=None)
    plt.title('Average Revenue by Region', fontsize=16)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Average Revenue', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig('revenue_by_region.png', dpi=300)
    plt.close()
    
def plot_revenue_by_category(df):
    """Plot average revenue by product category"""
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Product_Category', y='Revenue', data=df, estimator=np.mean, ci=None)
    plt.title('Average Revenue by Product Category', fontsize=16)
    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Average Revenue', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig('revenue_by_category.png', dpi=300)
    plt.close()

def plot_satisfaction_distribution(df):
    """Plot distribution of customer satisfaction"""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Customer_Satisfaction'], kde=True, bins=20)
    plt.title('Distribution of Customer Satisfaction', fontsize=16)
    plt.xlabel('Customer Satisfaction', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.savefig('satisfaction_distribution.png', dpi=300)
    plt.close()

def plot_channel_comparison(df):
    """Compare sales channels by revenue and profit"""
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Sales_Channel', y='Revenue', data=df)
    plt.title('Revenue by Sales Channel', fontsize=14)
    plt.xlabel('Sales Channel', fontsize=12)
    plt.ylabel('Revenue', fontsize=12)
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='Sales_Channel', y='Profit', data=df)
    plt.title('Profit by Sales Channel', fontsize=14)
    plt.xlabel('Sales Channel', fontsize=12)
    plt.ylabel('Profit', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('channel_comparison.png', dpi=300)
    plt.close()

def plot_correlation_heatmap(df):
    """Plot correlation heatmap of numeric variables"""
    numeric_cols = ['Revenue', 'Profit', 'Units_Sold', 'Customer_Satisfaction', 
                    'Marketing_Spend', 'Discount_Percentage', 'Order_Processing_Time']
    
    plt.figure(figsize=(12, 10))
    correlation = df[numeric_cols].corr()
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', 
                mask=mask, vmin=-1, vmax=1, center=0,
                square=True, linewidths=.5)
    
    plt.title('Correlation Heatmap of Numeric Variables', fontsize=16)
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300)
    plt.close()

def main():
    """Main function to run all visualizations"""
    print("Starting sales data visualization...")
    df = load_data()
    
    if df is not None:
        print("Generating visualizations...")
        plot_revenue_by_region(df)
        plot_revenue_by_category(df)
        plot_satisfaction_distribution(df)
        plot_channel_comparison(df)
        plot_correlation_heatmap(df)
        print("All visualizations have been saved!")
    else:
        print("Visualization process aborted due to data loading error.")

if __name__ == "__main__":
    main()