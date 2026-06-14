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