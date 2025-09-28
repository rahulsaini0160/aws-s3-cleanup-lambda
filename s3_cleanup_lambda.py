import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'my-cleanup-bucket-rahul'  # 🔁 Replace with your bucket name
    now = datetime.datetime.now(datetime.timezone.utc)

    response = s3.list_objects_v2(Bucket=bucket)

    for obj in response.get('Contents', []):
        key = obj['Key']
        print(f"Checking object: {key}")

        # Get metadata
        head = s3.head_object(Bucket=bucket, Key=key)
        meta = head.get('Metadata', {})

        upload_date = meta.get('upload-date')  # boto3 automatically strips x-amz-meta-

        if not upload_date:
            print(f"⚠️ {key}: No upload-date metadata found, skipping")
            continue

        try:
            file_date = datetime.datetime.strptime(upload_date, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
        except ValueError:
            print(f"⚠️ {key}: Invalid date format ({upload_date}), skipping")
            continue

        age_days = (now - file_date).days

        if age_days > 30:
            s3.delete_object(Bucket=bucket, Key=key)
            print(f"🗑️ Deleted {key} — {age_days} days old")
        else:
            print(f"✅ Kept {key} — {age_days} days old")
