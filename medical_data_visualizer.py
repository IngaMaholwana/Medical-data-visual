import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2) > 25
df['overweight'] = df['overweight'].astype(int)

# Normalize cholesterol and glucose (0 is good, 1 is bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    # Convert data into long format
    df_cat = pd.melt(df, id_vars=["cardio"], 
                     value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Group and count occurrences
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).size()
    df_cat.rename(columns={"size": "total"}, inplace=True)

    # Create a categorical plot
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio",
                      data=df_cat, kind="bar", height=5, aspect=1)

    # Extract the figure
    fig = fig.fig

    # Save the figure
    fig.savefig("catplot.png")

    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5, ax=ax)

    # Save the figure
    fig.savefig("heatmap.png")

    return fig
