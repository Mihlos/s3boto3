import boto3


# Let's use Amazon S3
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

class S3:
    def __init__(self, name):
        self.name = name
        self.s3_client = boto3.client('s3')

    def create_bucket(self):
        self.s3_client.create_bucket(Bucket=self.name, 
                                CreateBucketConfiguration={
                                    'LocationConstraint': 'eu-west-1'
                                    }
                                )