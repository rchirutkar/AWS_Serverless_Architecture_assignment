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
