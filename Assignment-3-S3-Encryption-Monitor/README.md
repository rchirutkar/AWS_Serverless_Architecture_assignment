## Assignment 3: Monitor Unencrypted S3 Buckets Using Lambda
### Goal: Create a Lambda function that identifies S3 buckets without server-side encryption enabled. 
### Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.

1. S3 Setup:
   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.
     
Note:
AWS now automatically applies Server-Side Encryption (SSE-S3) to newly created S3 buckets. Therefore, all test buckets were found to be encrypted by default.

<br><br>
<img width="602" height="193" alt="image" src="https://github.com/user-attachments/assets/b28608f7-0c31-4f49-97b0-9df5733c2df3" />
<br><br>
 
2. Lambda IAM Role:
   - In the IAM dashboard, create a new role for Lambda.
   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.
 <br>
 <img width="495" height="452" alt="image" src="https://github.com/user-attachments/assets/bdf518e9-4508-4f46-9dcb-fb68c6701368" />
 <br><br>

3. Lambda Function:
   - Navigate to the Lambda dashboard and create a new function.
   - Choose Python 3.x as the runtime.
   - Assign the IAM role created in the previous step.
 <br>
<img width="602" height="401" alt="image" src="https://github.com/user-attachments/assets/fdb78c39-3812-441f-9c5e-d1b981527c33" />
 <br><br>

   - Write the Boto3 Python script to:
     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

During testing, all buckets were reported as encrypted. AWS currently enables SSE-S3 encryption by default on newly created S3 buckets, so no unencrypted buckets were found.
 
 <br>
 <img width="620" height="606" alt="image" src="https://github.com/user-attachments/assets/a9d9ed30-e1f1-4b79-8279-7aa083ebab53" />
 <br><br>
 
4. Manual Invocation:
   - After saving your function, manually trigger it.
   - Review the Lambda logs to identify the buckets without server-side encryption.
 <br>
 <img width="602" height="369" alt="image" src="https://github.com/user-attachments/assets/38fe3991-1eb8-49c5-92df-3b8735ea7bd4" />

 <img width="601" height="352" alt="image" src="https://github.com/user-attachments/assets/e08bd6ad-a83c-4805-bd8f-1d2b7d5f150c" />

 <br><br>
