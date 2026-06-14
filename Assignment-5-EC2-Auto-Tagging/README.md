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

 <br>
<img width="602" height="392" alt="image" src="https://github.com/user-attachments/assets/7de3b7d6-45a4-40c3-ac18-91ee21feaf10" />
 <br><br>

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 
    <br>
   <img width="602" height="342" alt="image" src="https://github.com/user-attachments/assets/5916c714-a55c-4d5c-bae9-22fd438c9cd6" />
    <br><br>
 
   - Write the Boto3 Python script to:
     1. Initialize a boto3 EC2 client.
     2. Retrieve the instance ID from the event.
     3. Tag the new instance with the current date and another tag of your choice.
     4. Print a confirmation message for logging purposes.
    
   <br>
   <img width="486" height="306" alt="image" src="https://github.com/user-attachments/assets/835c9471-f79d-43fb-b3a8-655d0f58ac05" />
   <br><br>
 
4. CloudWatch Events:
   - Set up a CloudWatch Event Rule to trigger the EC2 instance launch event.
  
     Note: Amazon EventBridge (formerly CloudWatch Events) was used to trigger the Lambda function when an EC2 instance entered the Running state.

   <br>
   <img width="602" height="255" alt="image" src="https://github.com/user-attachments/assets/e3378099-880f-41b9-ae78-ae04f99922d7" />
   <br><br>

   - Attach the Lambda function as the target.
    <br>
   <img width="602" height="214" alt="image" src="https://github.com/user-attachments/assets/26e40248-0d14-4685-9b74-84e4dc000e1b" />
   
   <img width="602" height="282" alt="image" src="https://github.com/user-attachments/assets/4741319d-8102-4a5f-8d7d-ba44663f16a6" />
   
    <br><br>
 
5. Testing:
   - Launch a new EC2 instance.
 
    <br>
   <img width="602" height="94" alt="image" src="https://github.com/user-attachments/assets/dfef899f-27fa-488f-80b0-1f47721960b5" />
    <br><br>
   
   - After a short delay, confirm that the instance is automatically tagged as specified.
   <br>
   <img width="602" height="200" alt="image" src="https://github.com/user-attachments/assets/6388c774-680b-4d5a-8516-f84b44d88a71" />
   <br><br>
 
   - CloudeWatch logs:
   <br>
   <img width="602" height="157" alt="image" src="https://github.com/user-attachments/assets/e8f50dd1-dc0b-42c9-9908-e0d4f76c39f2" />
   <br><br>
 
Amazon EventBridge (formerly CloudWatch Events) was configured to monitor EC2 state changes. When a new EC2 instance entered the Running state, EventBridge triggered the Lambda function, which automatically added the LaunchDate and Environment tags.

<br><br>

