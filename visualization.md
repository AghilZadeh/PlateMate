# Visualization

## Overview

Visualizing training data before diving into modeling helps identify patterns, trends, and potential outliers that might impact the model's performance. It also gives a clearer understanding of the data's structure and relationships between variables, which can guide the selection of appropriate techniques and preprocessing steps for better results. One of the main benefits of visualizations is that they can serve as a sanity check for data, helping to identify outliers, null values, and other anomalies. It is important to carefully review visualizations to ensure that they accurately represent the underlying data. When creating visualizations there are a few best practices to keep in mind:

Labeling - Labels are a key element of effective visualizations. Column names should not be used as labels, as they often contain special characters and formatting that can make them difficult to read. Instead, labels should be clear and human-readable representations of the underlying feature. Visualizations should also include a header and subheader to provide context and help readers quickly understand the information presented.

 Color Scheme - When it comes to choosing colors for visualizations, it is important to use intuitive colors that help convey the information effectively. For example, light colors can be used for low values, while dark colors can be used for high values. When using categorical values, high contrast can help make the information more easily distinguishable. It is also important to include a clear and concise legend that explains the colors and categories used in the visualization.

 Digestibility - The faster a reader can understand a visualization, the better the visualization. Therefore, it is important to create visualizations that are easy to read and understand. Avoid clutter and unnecessary elements, and focus on presenting the key insights and trends in a clear and concise manner.

[Here](https://www.tableau.com/learn/articles/data-visualization-tips) is a list of more best practices

## How we do this:

To render plots in Python we will use Matplotlib, which is the most popular plotting library for the language.  Matplotlib includes methods that generate different types of charts (scatter plot, pie charts, bar chart, etc.) and methods to configure those charts by changing colors, axis names, window size, legend, etc. Check out this basic tutorial on matplotlib.


## Assumptions/Considerations

- Multiple ways to plot something. Consider which representation is the most intuitive.
- We can measure the quality of a plot in the amount of time it takes a reader to understand. We want readers to look at a plot and immediately understand what they are looking at.

## Variations/Alternatives

There are many different ways we can source data other than Web Scraping:

- [Plotly](https://plotly.com/python/)
- [Seaborn](https://seaborn.pydata.org/)
- [Altair](https://altair-viz.github.io/getting_started/overview.html)
