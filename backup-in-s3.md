# Backup data in S3

## Overview

Backing up training data to Amazon S3 is an important protocol in order to safeguard it against unexpected events like data corruption, hardware issues, or human errors. This ensures the integrity and availability of the data for future analysis. Additionally, using S3's scalable and secure cloud storage enables efficient collaboration among team members, as well as providing a centralized location for data management and version control.

## How we do this:

Refer to the [AWS Cloud Guide](https://github.com/CodesmithLLC/aws-cloud-guides) for using S3. 

## Assumptions/Considerations

- We need to consider who has permissions to our AWS bucket
- It is OK to make the bucket public, but consider if there is any sensitive information that needs to be private


## Variations/Alternatives

- Can backup in NFS drive (EFS)
- Bunch of S3 storage tiers
