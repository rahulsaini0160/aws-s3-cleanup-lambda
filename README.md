# AWS S3 Bucket Cleanup Lambda Function

## Overview
This AWS Lambda function automatically deletes files older than 30 days from a specified S3 bucket. It checks each object's metadata for a custom `upload-date` tag to determine its age.

## Steps Followed

### Uploading Files with Metadata
1. Upload files normally to the S3 bucket without metadata.
2. In the AWS S3 console, select the uploaded file.
3. Use the **Actions → Copy** feature to copy the file to the same bucket.
4. During the copy process, specify metadata by adding:
   - Key: `upload-date`
   - Value: A date string older than 30 days (e.g., `2024-08-10`)
5. Complete the copy operation. The copied file now has the custom metadata.
6. Optionally, delete the original file without metadata.
7. Confirm the metadata on the copied file under the **Properties → Metadata** tab.

### Preparing Test Event in Lambda Console
1. Open your Lambda function in AWS Console.
2. Click on the **Test** button.
3. Create a new test event named `manual_test`.
4. Use an empty JSON object `{}` as the event input.
5. Save the test event.

### Running the Lambda Function
1. With the test event selected, click **Test** to invoke the Lambda.
2. The Lambda will process the files in the bucket, deleting any older than 30 days based on the `upload-date` metadata.

### Fix to Lambda Timeout Issue
1. In the Lambda console, go to **Configuration → General Configuration → Edit**.
2. Increase the **Timeout** from the default 3 seconds to 30 seconds or longer.
3. Save the configuration.
4. This allows the Lambda enough time to list objects, read metadata, and delete old files.

---

## Usage

- Update the `bucket` variable in the Lambda code with your bucket name.
- Ensure the IAM role attached to Lambda has **AmazonS3FullAccess** permissions.
- Upload files, add metadata as described, and invoke the Lambda function manually for testing.

---

## Screenshots
_Add screenshots here showing:_

- Lambda function code in AWS Console
- CloudWatch logs of successful execution
- S3 bucket object list before and after cleanup
- Metadata properties view of uploaded files

---

## Summary

This function demonstrates automating S3 cleanup tasks using AWS Lambda and Boto3 with a focus on object metadata and scheduled/manual invocations.

