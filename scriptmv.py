import boto3

# Initialize S3 clients for both AWS accounts
source_s3 = boto3.client('s3', aws_access_key_id='AKIARZ72SBTOSM2NJCIQ', aws_secret_access_key='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')
destination_s3 = boto3.client('s3', aws_access_key_id='AKIAX753NEBUUYW42E4A', aws_secret_access_key='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')

# Set the source and destination bucket names and file/key name
source_bucket = 'sourcebucketforme'
destination_bucket = 'destinationbucketformeonly'
file_key = 'Piyush resume.pdf'

# Copy the file from the source bucket to the destination bucket
source_s3.copy_object(
    CopySource={'Bucket': source_bucket, 'Key': file_key},
    Bucket=destination_bucket,
    Key=file_key
)

# Delete the file from the source bucket if required
source_s3.delete_object(Bucket=source_bucket, Key=file_key)

print('File transfer completed.')
