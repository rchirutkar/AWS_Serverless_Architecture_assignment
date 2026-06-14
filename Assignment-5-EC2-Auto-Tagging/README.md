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

