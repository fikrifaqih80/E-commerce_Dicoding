# E-Commerce Data Analysis and Visualization Project

[Interactive E-Commerce Dashboard](https://e-commerce_data_analyst.streamlit.app/)

## Table of Contents
- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Installation Guide](#installation-guide)
- [How to Use](#how-to-use)
- [Dataset Information](#dataset-information)

## Introduction
This project is designed to analyze and visualize public data related to e-commerce. It includes scripts for data cleaning, exploratory data analysis (EDA), and an interactive dashboard built using Streamlit to allow users to explore the data dynamically. The main goal is to uncover insights from the E-Commerce Public Dataset.

## Directory Structure
- `dashboard/`: Contains `dashboard.py`, the script responsible for generating the interactive dashboard.
- `data/`: Directory that stores the raw CSV datasets used for analysis.
- `notebook.ipynb`: Jupyter notebook file containing code for data wrangling and EDA.
- `notebook_ID.ipynb`: Indonesian version of the analysis notebook.
- `README.md`: Documentation file for the project.

## Installation Guide
1. Clone this repository onto your local machine:
```bash
git clone https://github.com/mhdhfzz/data-analyst-dicoding.git
```
2. Navigate to the project directory:
```bash
cd data_analyst_dicoding
```
3. Install the necessary dependencies by running:
```bash
pip install -r requirements.txt
```

## How to Use
1. **Data Wrangling**: Use the provided Jupyter notebook (`notebook.ipynb`) to clean and transform the raw data for analysis.

2. **Perform EDA**: Analyze the dataset using the scripts included in the notebook to gain insights into the e-commerce trends and patterns.

3. **Visualize the Data**: Launch the Streamlit app for interactive data exploration:
```bash
cd data_analyst_dicoding/dashboard
streamlit run dashboard.py
```
Once the app is running, open your web browser and go to `http://localhost:8501` to explore the data.

## Dataset Information
This project utilizes an E-Commerce dataset provided as part of the [Python Data Analysis Course](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view) from [Dicoding](https://www.dicoding.com/).