# AWS Serverless Architecture & Cloud Automation 
Assignment On AWS Serverless Architecture

## Region
ap-south-1

## AWS Services used
This repository contains solutions for AWS Serverless Architecture assignments using:

* AWS Lambda
* Amazon EC2
* Amazon S3
* Amazon SNS
* Amazon EventBridge
* AWS Cost Explorer
* IAM
* Python (Boto3)

## Assignments Completed

### Assignment 1

   Automated EC2 start/stop based on tags.

### Assignment 3

   S3 encryption monitoring using Lambda.

### Assignment 5

   Automatic EC2 tagging on instance launch.

### Assignment 6

   AWS billing monitoring with SNS notifications.

## Technologies Used

* Python 3.x
* Boto3
* AWS Lambda
* EventBridge
* SNS
* Cost Explorer


<br><br>

---

<br><br>

## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

### Objective

Automate EC2 instance start and stop operations based on tags.

### Steps Performed

1. Created two EC2 instances.
2. Added tags:

   * Action=Auto-Stop
   * Action=Auto-Start
3. Created IAM Role for Lambda.
4. Attached AmazonEC2FullAccess and AWSLambdaBasicExecutionRole.
5. Created Lambda function.
6. Implemented Boto3 automation.
7. Invoked Lambda manually.
8. Verified EC2 state changes.
9. Verified CloudWatch logs.

### Result

Lambda successfully stopped instances tagged Auto-Stop and started instances tagged Auto-Start.

---

## Assignment 3: Monitor Unencrypted S3 Buckets

### Objective

Detect S3 buckets without server-side encryption.

### Steps Performed

1. Created test S3 buckets.
2. Created IAM Role for Lambda.
3. Attached AmazonS3ReadOnlyAccess.
4. Developed Lambda function using Boto3.
5. Invoked Lambda manually.
6. Verified CloudWatch logs.

### Observation

AWS currently enables SSE-S3 encryption by default on newly created buckets. All test buckets were detected as encrypted.

### Result

Lambda successfully inspected bucket encryption status.

---

## Assignment 5: Auto Tagging EC2 Instances

### Objective

Automatically tag newly launched EC2 instances.

### Steps Performed

1. Created IAM Role for Lambda.
2. Developed Lambda function.
3. Configured EventBridge rule.
4. Launched a new EC2 instance.
5. Verified automatic tagging.

### Tags Added

* LaunchDate
* Environment=Test

### Result

New EC2 instances were automatically tagged upon launch.

---

## Assignment 6: Billing Alert Automation

### Objective

Send alerts when AWS spending exceeds a threshold.

### Steps Performed

1. Created SNS Topic.
2. Added email subscription.
3. Created Lambda function.
4. Used AWS Cost Explorer API.
5. Configured SNS notifications.
6. Created EventBridge daily schedule.
7. Tested alert functionality.

### Result

Billing information was retrieved successfully and SNS email alerts were generated when threshold conditions were met.

---

## Conclusion

Successfully implemented serverless automation solutions using AWS Lambda, Boto3, EventBridge, SNS, Cost Explorer, S3, IAM and EC2 services.
