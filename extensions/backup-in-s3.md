# Backup data in S3

## Overview

Backing up training data to Amazon S3 is an important protocol in order to safeguard it against unexpected events like data corruption, hardware issues, or human errors. This ensures the integrity and availability of the data for future analysis. Additionally, you can easily share large files on S3, as well as providing a centralized location for data management and version control.

## How we do this:

Refer to the [AWS Cloud Guide](https://github.com/CodesmithLLC/aws-cloud-guides) for using S3. For your initially dataset you can upload it manually to S3. For future datasets you should automate the process of uploading to S3 with [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

## Assumptions/Considerations

- We need to consider who has permissions to our AWS bucket
- It is OK to make the bucket public, but consider if there is any sensitive information that needs to be private
- AWS now sets S3 objects as [private by default](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-s3-automatically-enable-block-public-access-disable-access-control-lists-buckets-april-2023/) so you need change the permissions to make them public 

## Variations/Alternatives

- Git / Github - not recommended for large datasets, github [limits file size to 50MB](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
- Network Files System (NFS) drive (e.g [AWS EFS](https://aws.amazon.com/efs/))
- Multiple S3 [storage classes](https://aws.amazon.com/s3/storage-classes/) for cost savings
- Google Drive
