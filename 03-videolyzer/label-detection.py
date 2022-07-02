# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='ericvideolyzervideos')
from pathlib import Path
path = Path(pathname).expanduser().resolve()
path = Path(pathname).expanduser().resolve()
pathname = "~/Blurry Video Of People Working.mp4"
path = Path(pathname).expanduser().resolve()
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': { 'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
job_id
result = rekognition_client.get_label_detection(JobId=job_id)
result
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
