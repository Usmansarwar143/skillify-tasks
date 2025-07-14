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
To run the analysis notebook, ensure you have the following installed:
- **Python 3.6+**
- Required Python libraries:
  ```bash
  pip install pandas matplotlib seaborn jupyter
  ```
- The Superstore Sales Dataset CSV file (named `Superstore.csv`).

## Installation
1. **Download the Dataset**:
   - Obtain the Superstore Sales Dataset from the [Kaggle link](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).
   - Save the CSV file as `Superstore.csv` in the `Week1` directory.

2. **Set Up the Environment**:
   - Install Python if not already installed (download from [python.org](https://www.python.org/downloads/)).
   - Install the required libraries by running:
     ```bash
     pip install pandas matplotlib seaborn jupyter
     ```

3. **Download the Analysis Notebook**:
   - Save the provided `Data_Understanding&Visualization.ipynb` notebook in the `Week1` directory.

## Usage
The `Data_Understanding&Visualization.ipynb` notebook performs the entire analysis pipeline, including data cleaning, exploratory analysis, visualization, and insight generation. Follow these steps to use it:

1. **Prepare the Dataset**:
   - Ensure `Superstore.csv` is in the `Week1` directory alongside `Data_Understanding&Visualization.ipynb`.
   - If the dataset has a different name or location, update the `pd.read_csv` line in the notebook to point to the correct file path (e.g., `pd.read_csv('Week1/Superstore.csv')`).

2. **Run the Notebook**:
   - Open a terminal or command prompt and navigate to the `Week1` directory.
   - Start Jupyter Notebook by running:
     ```bash
     jupyter notebook
     ```
   - In the Jupyter interface, open `Data_Understanding&Visualization.ipynb` and run all cells (or use the "Run All" option).

3. **Outputs**:
   - **Console Output (in Notebook)**: The notebook displays:
     - Dataset information (data types, missing values)
     - Key insights (e.g., best-selling category, top region, sales trends)
   - **Visualizations**: The following PNG files are generated in the `Week1/Outputs` directory:
     - `category_sales.png`: Bar chart of total sales by category
     - `region_sales.png`: Bar chart of total sales by region
     - `monthly_sales_trend.png`: Line graph of monthly sales trends
     - `correlation_heatmap.png`: Heatmap of correlations between Sales, Profit, Quantity, and Discount
     - `profit_by_category_region.png`: Grouped bar chart of profit by category and region
   - **Cleaned Dataset**: A cleaned version of the dataset is saved as `cleaned_superstore_sales.csv` in the `Week1` directory.

4. **Interpreting Results**:
   - Review the notebook output for key insights, such as the top-selling category and region.
   - Check the `Week1/Outputs` directory for visualization PNG files that support the insights.
   - Use `cleaned_superstore_sales.csv` for further analysis if needed.

## Project Structure
```
Week1/
├── Data_Understanding&Visualization.ipynb  # Main Jupyter Notebook for analysis
├── Superstore.csv                         # Input dataset
├── cleaned_superstore_sales.csv           # Output cleaned dataset
├── Outputs/                               # Directory for visualization outputs
│   ├── category_sales.png
│   ├── region_sales.png
│   ├── monthly_sales_trend.png
│   ├── correlation_heatmap.png
│   └── profit_by_category_region.png
```

## Learning Outcomes
This project addresses the following learning objectives:
- **Data Types & Null Handling**: The notebook inspects data types, handles missing values (numerical with median, categorical with mode), and parses dates.
- **Grouping, Filtering, Aggregation**: Uses pandas `groupby` and `pivot_table` to analyze sales and profit by category, region, and sub-category.
- **Basic Plots & Visual Storytelling**: Generates bar charts, line graphs, and heatmaps with clear labels to communicate insights effectively.

## Troubleshooting
- **FileNotFoundError**: Ensure `Superstore.csv` is in the `Week1` directory or update the file path in the notebook.
- **Missing Dependencies**: Verify that `pandas`, `matplotlib`, `seaborn`, and `jupyter` are installed using `pip install`.
- **Date Parsing Issues**: If `Order Date` or `Ship Date` fail to parse, check the date format in the dataset and adjust the `pd.to_datetime` format parameter in the notebook if needed.
- **Output Directory**: Ensure the `Outputs` folder exists in the `Week1` directory, or create it manually before running the notebook to store visualization files.

## Contact
For questions, issues, or feedback about this project, please contact:
- **Email**: muhammadusman.becsef22@iba-suk.edu.pk
- **GitHub**: [https://www.github.com/Usmansarwar143](https://www.github.com/Usmansarwar143)
- **LinkedIn**: [https://www.linkedin.com/in/muhammad-usman-018535253](https://www.linkedin.com/in/muhammad-usman-018535253)

If you need assistance with the notebook or dataset, feel free to reach out!

## License
This project is for educational purposes and uses the Superstore Sales Dataset, which is publicly available on Kaggle. Ensure you comply with the dataset's terms of use.
