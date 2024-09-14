# Alpha Care Insurance Analysis

## Overview

This project focuses on optimizing car insurance marketing strategies for AlphaCare Insurance Solutions (ACIS) by
analyzing historical claim data. The current focus is on performing Exploratory Data Analysis (EDA) to gain actionable
insights and implementing Data Version Control (DVC) to efficiently manage dataset versions.

## Project Structure

- **Branch Management**:
    - `main`: Contains the finalized code.
    - `task-1`: Branch for performing EDA and statistical analysis.
    - `task-2`: Branch for setting up Data Version Control (DVC) and data tracking.

## Task 1: Exploratory Data Analysis (EDA)

### Key Objectives:

- **Data Summarization**:
    - Perform descriptive statistics on key features like `TotalPremium`, `TotalClaim`.
    - Check and ensure correct data types for categorical variables and dates.

- **Data Quality Assessment**:
    - Identify missing values and handle them appropriately.

- **Univariate Analysis**:
    - Visualize distributions of numerical columns (histograms) and categorical columns (bar charts).

- **Bivariate/Multivariate Analysis**:
    - Explore correlations between `TotalPremium` and `TotalClaim` as a function of `ZipCode`.

- **Outlier Detection**:
    - Identify outliers using box plots for numerical data.

- **Visualization**:
    - Create insightful and visually appealing plots to summarize the EDA findings.

## Task 2: Data Version Control (DVC)

### Key Objectives:

- **Install and Initialize DVC**:
    - Set up DVC in the project directory (`dvc init`).

- **Set Up Local Remote Storage**:
    - Configure local storage as a DVC remote to track datasets.

- **Track and Version Data**:
    - Use DVC to add datasets (`dvc add <data.csv>`) and commit version information to Git.

- **Push Data**:
    - Ensure data versions are stored remotely using `dvc push`.


