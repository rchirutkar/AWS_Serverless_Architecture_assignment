## Assignment 6: Monitor and Alert High AWS Billing
### Goal: Check AWS billing daily and send an email alert if spending exceeds a threshold.
### Task: Set up a Lambda function to check your AWS billing amount daily, and if it exceeds a specified threshold, send an alert via SNS.

1. SNS Setup:
   - Navigate to the SNS dashboard and create a new topic.
 
   - Subscribe your email to this topic.
 

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
 

   - Attach policies that allow reading CloudWatch metrics and sending SNS notifications.
 
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 

   - Write the Boto3 Python script to:
     1. Initialize boto3 clients for CloudWatch and SNS.
     2. Retrieve the AWS billing metric from CloudWatch.
     3. Compare the billing amount with a threshold (e.g., $50).
     4. If the billing exceeds the threshold, send an SNS notification.
Note: AWS Cost Explorer API was used to retrieve current account spending, and Amazon SNS was used to send email notifications when the configured threshold was exceeded.
 
     5. Print messages for logging purposes.
 
4. Event Source (Bonus):
   - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function daily.

 

 
 
5. Testing:
   - Manually trigger the Lambda function or wait for the scheduled event.
 
   - If your billing is over the threshold, you should receive an email alert.
 
 

It is triggered second alert after setting the scheduler as below:
 
