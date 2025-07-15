# Customer Segmentation for Retail Business

## Project Overview
This project implements an unsupervised machine learning approach to segment customers of a retail business based on their behavioral and demographic characteristics. Utilizing the K-Means clustering algorithm, the project analyzes the Mall Customers dataset to identify distinct customer groups, enabling targeted marketing strategies and personalized customer experiences. The analysis focuses on three key features: Annual Income, Spending Score, and Age. This project serves as an educational exercise in unsupervised learning, clustering evaluation, and pattern recognition.

### Objectives
- **Unsupervised Learning**: Apply and understand the principles of unsupervised machine learning using K-Means clustering.
- **Clustering and Evaluation**: Determine the optimal number of clusters using the Elbow method and Silhouette scores.
- **Pattern Recognition**: Identify meaningful customer segments based on behavioral and demographic patterns.
- **Data Visualization**: Visualize high-dimensional data in a 2D space using Principal Component Analysis (PCA).

## Dataset
The analysis leverages the [Mall Customers dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python) available on Kaggle. This dataset contains customer information for a retail business, with the following relevant features:
- **Annual Income (k$)**: Customer's annual income in thousands of dollars.
- **Spending Score (1-100)**: A score assigned based on customer purchasing behavior and spending patterns.
- **Age**: Customer's age in years.

The dataset is publicly available under Kaggle's licensing terms, and users must ensure compliance with these terms when downloading and using the data.

## Prerequisites
To execute the project, the following Python libraries are required:
- pandas
- numpy
- matplotlib
- scikit-learn

Install the dependencies using pip:
```bash
pip install pandas numpy matplotlib scikit-learn
```

Ensure Python 3.6 or higher is installed on your system.

## Repository Structure
- **`customer_segmentation.py`**: The primary Python script that performs data preprocessing, feature scaling, K-Means clustering, cluster evaluation, and visualization.
- **`Mall_Customers.csv`**: The input dataset (not included; must be downloaded from Kaggle).
- **`elbow_silhouette.png`**: Generated plot displaying the Elbow method and Silhouette scores for cluster evaluation.
- **`customer_clusters.png`**: Generated plot visualizing the customer segments in a 2D PCA projection.

## Installation and Setup
1. **Download the Dataset**:
   - Obtain the Mall Customers dataset from [Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python).
   - Place the `Mall_Customers.csv` file in the same directory as the `customer_segmentation.py` script.

2. **Install Dependencies**:
   - Run the pip command listed above to install required libraries.
   - Verify that all libraries are correctly installed by running `pip list`.

3. **Run the Script**:
   - Execute the Python script from the command line:
     ```bash
     python customer_segmentation.py
     ```
   - Ensure the working directory contains both the script and the dataset file.

## Workflow
The `customer_segmentation.py` script performs the following tasks:
1. **Data Loading and Preprocessing**:
   - Loads the Mall Customers dataset using pandas.
   - Selects the features: Annual Income, Spending Score, and Age.

2. **Feature Scaling**:
   - Applies `StandardScaler` from scikit-learn to standardize the features, ensuring equal contribution to the clustering process.

3. **Cluster Evaluation**:
   - Implements the Elbow method to compute Within-Cluster Sum of Squares (WCSS) for 2 to 6 clusters.
   - Calculates Silhouette scores to assess cluster cohesion and separation.
   - Generates a plot (`elbow_silhouette.png`) to visualize WCSS and Silhouette scores.

4. **K-Means Clustering**:
   - Applies K-Means clustering with 4 clusters, determined as optimal based on the Elbow method and Silhouette scores.
   - Assigns cluster labels to each customer in the dataset.

5. **Visualization**:
   - Uses PCA to reduce the dimensionality of the scaled features to 2D for visualization.
   - Generates a scatter plot (`customer_clusters.png`) showing the customer segments in the PCA space.

6. **Cluster Analysis**:
   - Computes average feature values (Annual Income, Spending Score, Age) for each cluster.
   - Provides descriptive interpretations of each customer segment based on these statistics.

## Outputs
- **Console Output**:
  - Displays average Annual Income, Spending Score, and Age for each cluster.
  - Provides detailed descriptions of the customer segments, such as:
    - **Cluster 0**: Young, high-income, high-spending customers, likely trendy spenders who purchase premium products.
    - **Cluster 1**: Older, moderate-income, low-spending customers, potentially budget-conscious or conservative shoppers.
    - **Cluster 2**: Young, low-income, high-spending customers, possibly impulse buyers focusing on trendy or affordable items.
    - **Cluster 3**: Middle-aged, high-income, moderate-spending customers, characterized as balanced and selective shoppers.

- **Visual Outputs**:
  - `elbow_silhouette.png`: A dual plot showing the Elbow curve (WCSS vs. number of clusters) and Silhouette scores to justify the choice of 4 clusters.
  - `customer_clusters.png`: A 2D scatter plot visualizing the customer segments in PCA space, with clusters differentiated by color.

## Results and Insights
The analysis identifies four distinct customer segments, enabling the retail business to tailor marketing strategies:
- **Cluster 0**: Target with premium product promotions and loyalty programs to capitalize on their high spending.
- **Cluster 1**: Offer budget-friendly options or discounts to encourage spending among conservative shoppers.
- **Cluster 2**: Promote trendy, affordable products to appeal to young, impulsive buyers.
- **Cluster 3**: Focus on quality-driven promotions for selective, balanced shoppers.

The choice of 4 clusters was validated by analyzing the Elbow curve and Silhouette scores, ensuring optimal cluster separation and cohesion.

## Notes
- The script assumes the `Mall_Customers.csv` file is in the same directory. Update the file path in the script if necessary.
- The number of clusters (4) was selected based on empirical evaluation; users may experiment with different values by modifying the script.
- PCA is used solely for visualization purposes, preserving the original features for clustering.
- The visualizations are saved as PNG files in the working directory.

## License
This project is developed for educational purposes and uses the Mall Customers dataset, which is subject to Kaggle's licensing terms. Users are responsible for ensuring compliance with these terms when downloading and using the dataset. The code is provided under the MIT License.

## Contact
For questions or contributions, please contact the project maintainer via GitHub or email. This project was developed as part of a Week 3 assignment for a machine learning course focused on unsupervised learning.
