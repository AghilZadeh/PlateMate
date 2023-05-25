# Sanitize Data with Pandas

## Overview

Because data is often collected from multiple sources, it is common to encounter inconsistencies, missing values, and other issues that can negatively impact the performance of machine learning models.

Sanitizing data before visualization, such as removing duplicate entries, filling missing values, or correcting data entry errors, leads to more accurate and meaningful representations. This process helps uncover genuine trends and relationships, such as correlations or clusters, facilitating informed decision-making and analysis.

## How we do this:

Some basic steps to sanitize data include:
- Removing duplicate entries
- Filling missing values
- Correcting data entry errors

See [guide](https://github.com/CodesmithLLC/dsml-modeling-guide/tree/main/preprocessing) for more info.

## Assumptions/Considerations

- Preprocessing steps are model dependent. We want are processed data to meet the assumptions of our model
- There are multiple ways to perform preprocessing. We want to represent our data in the most optimal way for our model
- It is important to keep detailed documentation of preprocessing steps. This is important so that other users of our model can preprocess there data similarly in order to make our model usable

## Variations/Alternatives

- Polars Excel
- Dask
- Excel
