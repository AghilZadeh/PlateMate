# Web Scraping Data and Saving it to CSV

## Overview

Web scraping is the process of automating data collection from the internet, enabling the collection of vast amounts of diverse real-world data. Acquiring data through web scraping can help overcome limitations of traditional datasets, enhancing generalizability and ensuring models remain up-to-date with current trends and information.

## How we do this:

Refer to the  web scraping unit to download and parse the content of your target site.

## Assumptions/Considerations

Web Scraping is often IO bound, meaning a significant amount of time in executing the script comes from network IO
When initially requesting a site with Selenium, we must use the XPath to determine what portion of the HTML we want. Look at the difference between full XPath and relative XPath and consider the tradeoffs of using either.

## Variations/Alternatives

There are many different ways we can source data other than Web Scraping:

- APIs 
- Fixed Datasets
- Surveys
- Experiments
- Simulation
