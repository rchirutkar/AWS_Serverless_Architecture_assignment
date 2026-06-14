import boto3
from datetime import datetime, timedelta

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:488347380015:AWSBillingAlerts"

ce = boto3.client('ce')
sns = boto3.client('sns')

THRESHOLD = 10.0    
# THRESHOLD = 0.01    # Set low for testing


def lambda_handler(event, context):

    today = datetime.utcnow().date()
    first_day = today.replace(day=1)

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': str(first_day),
            'End': str(today + timedelta(days=1))
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )

    amount = float(
        response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    )

    print(f"Current AWS Cost: ${amount}")

    if amount > THRESHOLD:

        message = (
            f"AWS Billing Alert!\n\n"
            f"Current AWS cost is ${amount}\n"
            f"Threshold is ${THRESHOLD}"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='AWS Billing Alert',
            Message=message
        )

        print("SNS notification sent")

    else:
        print("Cost below threshold")

    return {
        'statusCode': 200,
        'body': f'Current Cost: ${amount}'
    }