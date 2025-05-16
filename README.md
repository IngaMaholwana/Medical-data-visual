# Medical Data Visualizer

## Description
Medical Data Visualizer is a Python-based project that visualizes and analyzes medical data to provide insights into patients' health. The project generates plots such as categorical bar plots and heatmaps to help analyze key health metrics like cholesterol levels, glucose levels, and weight.

---

## Installation Instructions
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/IngaMaholwana/Medical-data-visual
   cd Medical-data-visual

Install the required dependencies:
pip install -r requirements.txt

## Usage
Run the main script to generate visualizations:
The generated plots will be saved in the project directory as:
catplot.png: A categorical bar plot.
heatmap.png: A heatmap showing correlations between health metrics.

## Features
Cholesterol and Glucose Normalization: Automatically normalizes cholesterol and glucose levels for better analysis.
Overweight Indicator: Adds a calculated column to indicate whether a patient is overweight.
Categorical Plot: Visualizes the distribution of health metrics across different categories.
Heatmap: Displays correlations between various health metrics.
Configuration Options
Replace the dataset medical_examination.csv with your own CSV file if needed. Ensure it has the required columns.
Customize the visualizations by editing the draw_cat_plot and draw_heat_map functions in medical_data_visualizer.py.
