# Schedule Job

## Overview

Scheduling a job to run at a specific time is a common task in data science. This can be used to automate data collection, model training, or model deployment. In this guide we will use AWS Lambda to schedule a job to run at a specific time.

## How we do this:

1. Create a Lambda function that will run our job (see [guide](https://github.com/CodesmithLLC/aws-cloud-guides/lambda.md))

2. Configure Lambda to be triggered by [Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html)

## Assumptions/Considerations

Web Scraping is often IO bound, meaning a significant amount of time in executing the script comes from network IO
When initially requesting a site with Selenium, we must use the XPath to determine what portion of the HTML we want. Look at the difference between full XPath and relative XPath and consider the tradeoffs of using either.

## Variations/Alternatives

There are many ways you can schedule a job to run at a specific time:

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Airflow](https://airflow.apache.org/)
- [Local Cron Job](https://pypi.org/project/local-crontab/#:~:text=local%2Dcrontab%20is%20a%20Python,because%20of%20Daylight%20Saving%20Time.)