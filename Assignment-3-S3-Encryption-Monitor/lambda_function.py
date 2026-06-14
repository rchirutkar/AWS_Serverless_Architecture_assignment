import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def lambda_handler(event, context):

    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:

        bucket_name = bucket['Name']

        try:
            s3.get_bucket_encryption(
                Bucket=bucket_name
            )

            print(f"{bucket_name} -> ENCRYPTED")

        except ClientError as e:

            error_code = e.response['Error']['Code']

            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"{bucket_name} -> NOT ENCRYPTED")
            else:
                print(f"{bucket_name} -> ERROR: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'S3 Encryption Check Complete'
    }