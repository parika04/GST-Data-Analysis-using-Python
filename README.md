# GST Data Analysis

This project analyzes Goods and Services Tax (GST) data to understand registration patterns, state-wise trends, and payer behavior. The analysis uses Python with libraries like Pandas, Matplotlib, Seaborn, and Scipy.

## Project Structure

* `finaldata.xlsx`: The dataset used for the analysis.
* `gst_data_analysis.ipynb`: (Optional) Jupyter Notebook containing the analysis code. You provided a python script, but a notebook is common.
* `README.md`: This file, providing an overview of the project.
* `eligible_payers_distribution.png`: (Optional) If the code generates this.
* `compliance_by_return_type.png`: (Optional) If the code generates this.
* `top_states_by_registered.png`: (Optional) If the code generates this.
* `state_compliance.png`: (Optional) If the code generates this.
* `jk_trends.png`: (Optional) If the code generates this.
* `time_trends.png`: (Optional) If the code generates this.
* `compliance_trend.png`: (Optional) If the code generates this.
* `high_value_states.png`: (Optional) If the code generates this.
* `correlation_matrix.png`: (Optional)
* `eligibility_vs_registrations.png`: (Optional)
* `state_registration_comparison.png`: (Optional)
* `payer_distribution_pie.png`: (Optional)
* `compliance_by_return_boxplot.png`: (Optional)
* `actual_vs_predicted.png`: (Optional)

## Data Description

The dataset (`finaldata.xlsx`) contains GST-related information, including:

* `srcStateName`: Name of the state.
* `srcYear`: Year of the data.
* `srcMonth`: Month of the data.
* `GST (Goods and Service Tax) Return Type`: Type of GST return.
* `Payer eligible for GST (Goods and Service Tax) registration`: Number of payers eligible for registration.
* `GST (Goods and Service Tax) Payers registered before due date`: Number of payers registered before the due date.
* `GST (Goods and Service Tax) Payers registered after due date`: Number of payers registered after the due date.
* `YearCode`: Numerical code for the year.
* `Year`: Year.
* `MonthCode`: Numerical code for the month.
* `Month`: Month name.

## Code Description

The provided Python script performs the following analysis:

1.  **Data Loading and Exploration:**
    * Loads the data from `finaldata.xlsx` using Pandas.
    * Displays the first few rows, dataset dimensions, column information, missing values, and a statistical summary.
    * Fills missing values with 0.
    * Calculates `Total_Registered` payers.

2.  **State-wise Analysis:**
    * Visualizes the top 10 states/UTs by the number of eligible GST payers.
    * Provides a summary of regional variations in payer eligibility.
    * **Interactive Question:** Which state do you think has the highest number of GST payers, and why might that be the case?

3.  **Time-based Trends:**
    * Visualizes GST payer eligibility and registrations over time.
    * Summarizes fluctuations and trends in payer activity.
    * **Interactive Question:** Can you identify any seasonal patterns or significant changes in GST activity over the observed period? What factors might explain these trends?

4.  **Return Type Analysis:**
    * Visualizes the total number of registered GST payers by return type.
    * Provides a table comparing eligible and registered payers for each return type.
    * Summarizes the contribution of different return types to overall registrations.
    * **Interactive Question**: What does the difference in GSTR-1 and GSTR-3 tell us about the filers?

5.  **Correlation Analysis:**
    * Calculates and visualizes the correlation between key GST metrics (eligible payers, registrations before/after due date, total registrations).
    * Summarizes the relationship between payer eligibility and registration numbers.
     * **Interactive Question**:  How does the strong correlation between eligible payers and total registered payers influence decision-making?

6.  **Registration Timing:**
    * Compares the number of GST payers registered before and after the due date.
    * Summarizes the timely compliance of GST payers.
    * **Interactive Question**: What are the possible reasons for the number of registrations after the due date?

## Key Findings

The analysis reveals the following key insights:

* **State-wise Variation:** States like Maharashtra and Uttar Pradesh have the highest number of eligible GST payers, indicating significant regional differences.
* **Time-based Trends:** GST payer eligibility and registrations show fluctuations over time, possibly influenced by seasonal or policy changes.
* **Return Type Contribution:** GSTR-3 filers contribute a larger share to total GST registrations compared to GSTR-1 filers.
* **Correlation:** A strong positive correlation exists between the number of eligible payers and the total number of registered payers.
* **Registration Timing:** Most GST payers register before the due date, indicating good compliance.
* The data is right skewed.

## Visualizations

The analysis includes the following visualizations:

* Bar plots showing the top 10 states/UTs by eligible GST payers.
* Line plots showing GST payer trends over time.
* Bar plots showing total registered payers by return type.
* Heatmaps visualizing the correlation between GST metrics.
* Bar plots comparing before and after due date registrations.

## Dependencies

The code requires the following Python libraries:

* Pandas
* Matplotlib
* Seaborn
* Scipy
* Statsmodels

## Further Exploration

* Explore the reasons behind the state-wise variations in GST payer registration.
* Investigate the factors influencing the time-based trends in GST activity.
* Analyze the characteristics of businesses that file GSTR-1 versus GSTR-3 returns.
* Build a predictive model for registration compliance.
* Examine the impact of policy changes on GST registration and compliance.
