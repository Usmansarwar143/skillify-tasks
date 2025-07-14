# Superstore Sales Trends Analysis

## Project Overview
This project analyzes the Superstore Sales Dataset to uncover sales trends and insights as part of a Week 1 task for learning data understanding and visualization. The goal is to clean, explore, and visualize the dataset to answer key business questions, such as which category sells best and which region earns the most. The project focuses on:
- Data cleaning (handling missing values, date parsing)
- Exploratory data analysis (grouping, filtering, aggregation)
- Visualization (bar charts, line graphs, heatmaps)
- Presenting 3–5 key insights with visual evidence

## Dataset
The dataset used is the **Superstore Sales Dataset**, which contains sales data for a retail superstore. It includes the following columns:
- `Order ID`: Unique identifier for each order
- `Order Date`: Date the order was placed
- `Ship Date`: Date the order was shipped
- `Ship Mode`: Shipping method (e.g., Standard, First Class)
- `Customer ID`: Unique identifier for each customer
- `Customer Name`: Name of the customer
- `Segment`: Customer segment (e.g., Consumer, Corporate)
- `Country`: Country of the sale
- `City`: City of the sale
- `State`: State of the sale
- `Postal Code`: Postal code of the sale location
- `Region`: Region of the sale (e.g., West, East)
- `Product ID`: Unique identifier for each product
- `Category`: Product category (e.g., Furniture, Technology)
- `Sub-Category`: Product sub-category (e.g., Chairs, Phones)
- `Product Name`: Name of the product
- `Sales`: Total sales amount (in USD)
- `Quantity`: Number of items sold
- `Discount`: Discount applied to the order
- `Profit`: Profit earned from the order

**Source**: The dataset can be downloaded from [Kaggle: Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).

## Prerequisites
To run the analysis script, ensure you have the following installed:
- **Python 3.6+**
- Required Python libraries:
  ```bash
  pip install pandas matplotlib seaborn
  ```
- The Superstore Sales Dataset CSV file (named `superstore_sales.csv`).

## Installation
1. **Download the Dataset**:
   - Obtain the Superstore Sales Dataset from the [Kaggle link](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).
   - Save the CSV file as `superstore_sales.csv` in the same directory as the analysis script.

2. **Set Up the Environment**:
   - Install Python if not already installed (download from [python.org](https://www.python.org/downloads/)).
   - Install the required libraries by running:
     ```bash
     pip install pandas matplotlib seaborn
     ```

3. **Download the Analysis Script**:
   - Save the provided `superstore_analysis.py` script in the same directory as the dataset.

## Usage
The `superstore_analysis.py` script performs the entire analysis pipeline, including data cleaning, exploratory analysis, visualization, and insight generation. Follow these steps to use it:

1. **Prepare the Dataset**:
   - Ensure `superstore_sales.csv` is in the same directory as `superstore_analysis.py`.
   - If the dataset has a different name or location, update the `pd.read_csv` line in the script to point to the correct file path.

2. **Run the Script**:
   - Open a terminal or command prompt in the directory containing the script and dataset.
   - Execute the script using:
     ```bash
     python superstore_analysis.py
     ```

3. **Outputs**:
   - **Console Output**: The script prints:
     - Dataset information (data types, missing values)
     - Key insights (e.g., best-selling category, top region, sales trends)
   - **Visualizations**: The following PNG files are generated in the same directory:
     - `category_sales.png`: Bar chart of total sales by category
     - `region_sales.png`: Bar chart of total sales by region
     - `monthly_sales_trend.png`: Line graph of monthly sales trends
     - `correlation_heatmap.png`: Heatmap of correlations between Sales, Profit, Quantity, and Discount
     - `profit_by_category_region.png`: Grouped bar chart of profit by category and region
   - **Cleaned Dataset**: A cleaned version of the dataset is saved as `cleaned_superstore_sales.csv`.

4. **Interpreting Results**:
   - Review the console output for key insights, such as the top-selling category and region.
   - Open the PNG files to view visualizations that support the insights.
   - Use `cleaned_superstore_sales.csv` for further analysis if needed.

## Project Structure
- `superstore_sales.csv`: Input dataset (must be provided by the user).
- `superstore_analysis.py`: Python script for data cleaning, analysis, and visualization.
- `cleaned_superstore_sales.csv`: Output cleaned dataset.
- Visualization files:
  - `category_sales.png`
  - `region_sales.png`
  - `monthly_sales_trend.png`
  - `correlation_heatmap.png`
  - `profit_by_category_region.png`

## Learning Outcomes
This project addresses the following learning objectives:
- **Data Types & Null Handling**: The script inspects data types, handles missing values (numerical with median, categorical with mode), and parses dates.
- **Grouping, Filtering, Aggregation**: Uses pandas `groupby` and `pivot_table` to analyze sales and profit by category, region, and sub-category.
- **Basic Plots & Visual Storytelling**: Generates bar charts, line graphs, and heatmaps with clear labels to communicate insights effectively.

## Troubleshooting
- **FileNotFoundError**: Ensure `superstore_sales.csv` is in the same directory as the script or update the file path in the script.
- **Missing Dependencies**: Verify that `pandas`, `matplotlib`, and `seaborn` are installed using `pip install`.
- **Date Parsing Issues**: If `Order Date` or `Ship Date` fail to parse, check the date format in the dataset and adjust the `pd.to_datetime` format parameter if needed.

## Contact
For questions, issues, or feedback about this project, please contact:
- **Email**: [muhammadusman.becsef22@iba-suk.edu.pk]
- **GitHub**: [https://www.github.com/Usmansarwar143]
- **LinkedIn**: [https://www.linkedin.com/in/muhammad-usman-018535253]

If you need assistance with the script or dataset, feel free to reach out!

## License
This project is for educational purposes and uses the Superstore Sales Dataset, which is publicly available on Kaggle. Ensure you comply with the dataset's terms of use.
