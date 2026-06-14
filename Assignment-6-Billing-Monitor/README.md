## Assignment 6: Monitor and Alert High AWS Billing
### Goal: Check AWS billing daily and send an email alert if spending exceeds a threshold.
### Task: Set up a Lambda function to check your AWS billing amount daily, and if it exceeds a specified threshold, send an alert via SNS.

1. SNS Setup:
   - Navigate to the SNS dashboard and create a new topic.
    <br>
    <img width="602" height="129" alt="image" src="https://github.com/user-attachments/assets/e64da9f9-0612-4e0d-8055-1abc7925156b" />
    <br><br>
    
   - Subscribe your email to this topic.
    <br>
    <img width="602" height="157" alt="image" src="https://github.com/user-attachments/assets/f7cff2df-1371-4244-a1e1-d4d80eda07ef" />
    <br><br>

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
    <br>
    <img width="602" height="141" alt="image" src="https://github.com/user-attachments/assets/d50e5833-e24d-4ead-a319-198d495f7665" />
    <br><br>

   - Attach policies that allow reading CloudWatch metrics and sending SNS notifications.
    <br>
    <img width="602" height="228" alt="image" src="https://github.com/user-attachments/assets/081e1a19-a1ba-43cb-85c0-fbe560ab4151" />
    <br><br>
    
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
     
    <br>
    <img width="602" height="419" alt="image" src="https://github.com/user-attachments/assets/9f54db4e-4684-4d00-b698-519869b79667" />
    <br><br>

   - Write the Boto3 Python script to:
     1. Initialize boto3 clients for CloudWatch and SNS.
     2. Retrieve the AWS billing metric from CloudWatch.
     3. Compare the billing amount with a threshold (e.g., $50).
     4. If the billing exceeds the threshold, send an SNS notification.
   
      Note: AWS Cost Explorer API was used to retrieve current account spending, and Amazon SNS was used to send email notifications when the configured threshold was exceeded.
 
       <br>
       <img width="602" height="487" alt="image" src="https://github.com/user-attachments/assets/01ed9a4b-a157-4d48-8001-f47b16f95f5e" />
       <br><br>
    
     5. Print messages for logging purposes.
   
      <br>
      <img width="602" height="280" alt="image" src="https://github.com/user-attachments/assets/82bebc56-6c04-45a4-b9d0-c760646f3484" />
      <br><br>
   
4. Event Source (Bonus):
   - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function daily.
   <br>
   <img width="602" height="239" alt="image" src="https://github.com/user-attachments/assets/4a57d3ec-56a8-4a08-94dc-a507f0af0920" />
   <img width="602" height="205" alt="image" src="https://github.com/user-attachments/assets/25079928-3734-4c1a-9221-8cbb4542544c" />
   <img width="602" height="323" alt="image" src="https://github.com/user-attachments/assets/3ea97100-0961-4b34-89cc-8a86c30593f5" />
   <br><br>

5. Testing:
   - Manually trigger the Lambda function or wait for the scheduled event.
    <br>
    <img width="602" height="209" alt="image" src="https://github.com/user-attachments/assets/f9b89324-ec2c-44ac-aa7c-26d117fdaa49" />
    <br><br>
    
   - If your billing is over the threshold, you should receive an email alert.
 
    <br>
    <img width="593" height="197" alt="image" src="https://github.com/user-attachments/assets/3b31d0cb-ad9f-4bd7-b6c8-2d5ca9f0f57f" />
   <img width="602" height="273" alt="image" src="https://github.com/user-attachments/assets/af7f4edf-f4ac-4c25-9c42-678e1ce1b203" />
    <br><br>

It is triggered second alert after setting the scheduler as below:
<br>
 <img width="602" height="256" alt="image" src="https://github.com/user-attachments/assets/d86631e2-3fcd-4aaa-9459-2c35775d0613" />
<br><br>
