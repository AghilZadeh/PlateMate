# Sanitize Data with Pandas

## Overview

Web scraping is the process of automating data collection from the internet, enabling the collection of vast amounts of diverse real-world data. Acquiring data through web scraping can help overcome limitations of traditional datasets, enhancing generalizability and ensuring models remain up-to-date with current trends and information.
Sanitizing data before visualization, such as removing duplicate entries, filling missing values, or correcting data entry errors, leads to more accurate and meaningful representations. This process helps uncover genuine trends and relationships, such as correlations or clusters, facilitating informed decision-making and analysis.

## How we do this:

See [guide](https://github.com/CodesmithLLC/dsml-modeling-guide/tree/main/preprocessing) for sanitizing and preprocessing data.

##Assumptions/Considerations

- Preprocessing steps are model dependent. We want are processed data to meet the assumptions of our model
- There are multiple ways to perform preprocessing. We want to represent our data in the most optimal way for our model
- It is important to keep detailed documentation of preprocessing steps. This is important so that other users of our model can preprocess there data similarly in order to make our model usable

##Variations/Alternatives

- Polars Excel
- Dask
- Excel
