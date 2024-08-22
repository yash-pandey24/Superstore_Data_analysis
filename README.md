# Superstore_Data_analysis
Comprehensive Sales Data Analysis using Power BI, Python (pandas, numpy, plotly), and DAX for interactive visualizations and deep insights.

## Overview

This project involves the development of a comprehensive Sales Data Analysis Dashboard using a combination of Python, Power BI, and DAX. The goal of this project is to analyze sales data, uncover insights into product performance, sales trends, and customer behavior, and create interactive visualizations to present these findings effectively.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [DAX Calculations](#dax-calculations)
- [Visualizations](#visualizations)
- [License](#license)

## Project Structure

```
sales-data-analysis/
│
├── data/
│   └── Processed_Superstore_Sales.csv
│
├── scripts/
│   └── sales_data_analysis.py
│
├── README.md
└── Sales_Data_Analysis_Dashboard.pbit
```

## Features

- **Data Preprocessing**: Cleaned and prepared the data using pandas and numpy.
- **Feature Engineering**: Created new columns for `Total Sales` and `Profit Margin` to enhance analysis.
- **DAX Calculations**: Developed custom DAX queries for advanced metrics like `Total Profit` and `Average Discount`.
- **Interactive Visualizations**: Utilized plotly and Power BI for dynamic charts and graphs.
- **Power BI Dashboard**: Created a comprehensive dashboard for visualizing sales trends, product performance, and regional analysis.

## Technologies Used

- **Python**: Data preprocessing, feature engineering, and basic analysis.
- **pandas & numpy**: For data cleaning and manipulation.
- **plotly**: Interactive visualizations.
- **Power BI**: Dashboard creation and DAX calculations.
- **DAX (Data Analysis Expressions)**: Custom calculations within Power BI.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sales-data-analysis.git
   cd sales-data-analysis
   ```

2. **Install Python Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install pandas numpy plotly
   ```

3. **Run the Python Script**:
   ```bash
   python scripts/sales_data_analysis.py
   ```

4. **Load Data into Power BI**:
   - Open Power BI Desktop.
   - Load the `Processed_Superstore_Sales.csv` file from the `data/` folder.

5. **Explore the Power BI Dashboard**:
   - If using the provided template (optional), load the `Sales_Data_Analysis_Dashboard.pbit` file in Power BI.

## Usage

- Run the Python script to preprocess the data and generate visualizations.
- Open the Power BI file to explore the dashboard, interact with filters, and view different data insights.

## DAX Calculations

This project includes several DAX calculations for enhanced analysis:

- **Total Profit**:
  ```DAX
  Total Profit = SUM('Processed_Superstore_Sales'[Profit])
  ```
- **Average Discount**:
  ```DAX
  Average Discount = AVERAGE('Processed_Superstore_Sales'[Discount])
  ```
- **Year-Month**:
  ```DAX
  YearMonth = FORMAT('Processed_Superstore_Sales'[Order Date], "YYYY-MM")
  ```

## Visualizations

- **Sales Trend Over Time**: Line chart to track how sales have changed over time.
- **Sales by Product Category**: Bar chart comparing sales across different product categories.
- **Discount vs. Sales**: Scatter plot to analyze the relationship between discount and sales.
- **Profit Margin by Region**: Bar chart showing average profit margin across different regions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
