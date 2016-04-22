import boto3
import botocore

BUCKET_NAME = 'mpa-bucket-1'
print('First S3 Example')
s3 = boto3.resource('s3')

#bucket_num = s3.buckets.all.size
#print(bucket_num)

#for bucket in s3.buckets.all():
#    print(bucket.name)
if not s3.Bucket(BUCKET_NAME) in s3.buckets.all():
	print('Creating bucket with name: ' + BUCKET_NAME)
	s3.create_bucket(Bucket=BUCKET_NAME)
else:
	print('Bucket ' + BUCKET_NAME + 'already exists!')

print('Storing a file to S3 bucket')

s3.Object(BUCKET_NAME, 'readme.txt').put(Body=open('./README.md', 'rb'))


