# AWS_Serverless_Architecture_assignment
Assignment On AWS Serverless Architecture ( Lambda )


## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
### Goal: Create a Lambda function that will automatically manage EC2 instances based on their tags. 
### Task: Automate the stopping and starting of EC2 instances based on tags.

1. Setup:
   - Create two EC2 instances.

   <br><br>
   <img width="533" height="47" alt="image" src="https://github.com/user-attachments/assets/65243025-4ae0-4ac8-8b16-26d064ba19bb" />
   <br><br>
   
   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.
     
   <br><br>
   <img width="554" height="237" alt="image" src="https://github.com/user-attachments/assets/4524f210-eff9-419a-bb4e-4aa7c559faad" />

   <img width="552" height="222" alt="image" src="https://github.com/user-attachments/assets/3d134369-d998-42be-b73c-e7e95970c175" />
   <br><br>
   
2. Lambda Function Creation:
   - Set up an AWS Lambda function.
  
   <br><br>
   <img width="602" height="330" alt="image" src="https://github.com/user-attachments/assets/b601b628-5981-4380-ac66-3bb33e9b5331" />
   <br><br>
   
   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.
     
   <br><br> 
   <img width="602" height="26" alt="image" src="https://github.com/user-attachments/assets/236872e6-b39c-4110-b186-1ac1c69940cb" />

   <img width="519" height="382" alt="image" src="https://github.com/user-attachments/assets/21c6cc5b-517c-4ced-a807-29c6cbcddf63" />
   <br><br>

3. Coding:
   - Using Boto3 in the Lambda function:
   - Detect all EC2 instances with the `Auto-Stop` tag and stop them.
   - Detect all EC2 instances with the `Auto-Start` tag and start them.

    ```
        import boto3
    
        ec2 = boto3.client('ec2')
        
        def lambda_handler(event, context):
    
        # Find Auto-Stop instances
        stop_instances = ec2.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Action',
                    'Values': ['Auto-Stop']
                }
            ]
        )
    
        stop_ids = []
    
        for reservation in stop_instances['Reservations']:
            for instance in reservation['Instances']:
                stop_ids.append(instance['InstanceId'])
    
        if stop_ids:
            ec2.stop_instances(InstanceIds=stop_ids)
            print(f"Stopped instances: {stop_ids}")
    
        # Find Auto-Start instances
        start_instances = ec2.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Action',
                    'Values': ['Auto-Start']
                }
            ]
        )
    
        start_ids = []
    
        for reservation in start_instances['Reservations']:
            for instance in reservation['Instances']:
                start_ids.append(instance['InstanceId'])
    
        if start_ids:
            ec2.start_instances(InstanceIds=start_ids)
            print(f"Started instances: {start_ids}")
    
        return {
            'statusCode': 200,
            'body': 'EC2 actions completed'
        }
        
    ```

   <br><br>
   <img width="556" height="545" alt="image" src="https://github.com/user-attachments/assets/d1fc7f9c-16af-440c-afc5-dafb10188abd" />
<br><br>

4. Testing:

   - Manually invoke the Lambda function.
    <br><br>
    
   <img width="602" height="79" alt="image" src="https://github.com/user-attachments/assets/c4a51b76-e83d-40c1-b8db-99c4d039a617" />
<br><br>

   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.
     <br><br>
 
   <img width="602" height="61" alt="image" src="https://github.com/user-attachments/assets/9e538e6d-4685-41e4-a9c2-e2354ed3b2f4" />

   <img width="602" height="93" alt="image" src="https://github.com/user-attachments/assets/492ba316-a94a-40ca-9e4a-e1fdc6307931" />

   <img width="602" height="297" alt="image" src="https://github.com/user-attachments/assets/52f5f856-29cd-4b21-946a-315bae3341c7" />
<br><br>

## Assignment 3: Monitor Unencrypted S3 Buckets Using Lambda
### Goal: Create a Lambda function that identifies S3 buckets without server-side encryption enabled. 
### Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.

1. S3 Setup:
   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.
Note:
AWS now automatically applies Server-Side Encryption (SSE-S3) to newly created S3 buckets. Therefore, all test buckets were found to be encrypted by default.
 
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.
 
 
3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 

   - Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

During testing, all buckets were reported as encrypted. AWS currently enables SSE-S3 encryption by default on newly created S3 buckets, so no unencrypted buckets were found.
 
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Review the Lambda logs to identify the buckets without server-side encryption.

 <br><br>
 
## Assignment 5: Auto-Tagging EC2 Instances on Launch
### Goal: Whenever a new EC2 instance is launched:
•	Lambda is triggered automatically 
•	Lambda adds tags: 
   o	LaunchDate = current date 
   o	Environment = Test (or any custom value)
### Task: Automatically tag any newly launched EC2 instance with the current date and a custom tag.

1. EC2 Setup:
   - Ensure you have the capability to launch EC2 instances.

2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonEC2FullAccess` policy to this role.
 

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.
 
4. CloudWatch Events:
   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
Note: Amazon EventBridge (formerly CloudWatch Events) was used to trigger the Lambda function when an EC2 instance entered the Running state.
 
   - Attach the Lambda function as the target.
 
 
5. Testing:
   - Launch a new EC2 instance.
 
   
   - After a short delay, confirm that the instance is automatically tagged as specified.

 
    -CloudeWatch logs:
 
Amazon EventBridge (formerly CloudWatch Events) was configured to monitor EC2 state changes. When a new EC2 instance entered the Running state, EventBridge triggered the Lambda function, which automatically added the LaunchDate and Environment tags.

<br><br>
 
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
 
