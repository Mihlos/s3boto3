import boto3


# Let's use Amazon S3
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

class S3:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')
        

    def create_bucket(self, name):
        self.s3_client.create_bucket(Bucket=name, 
                                CreateBucketConfiguration={
                                    'LocationConstraint': 'eu-west-1'
                                    }
                                )

    def list_buckets_client(self):
        response = self.s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print('List of Buckets ==>')
        for bucket in buckets:
            print('Bucket name: {}'.format(bucket))

    def list_buckets_resource(self):
        buckets = [bucket.name for bucket in self.s3_resource.buckets.all()]
        print('List of Buckets ==>')
        for bucket in buckets:
            print('Bucket name: {}'.format(bucket))

    def list_content_client(self, name):
        response = self.s3_client.list_objects(Bucket=name)
        files = [file['Key'] for file in response['Contents']]
        print('List of Files in {} ==>'.format(name))
        for file in files:
            print('File name: {}'.format(file))

    def list_content_resource(self, name):
        my_bucket = self.s3_resource.Bucket(name)
        files = [file.key for file in my_bucket.objects.all()]
        print('List of Files in {} ==>'.format(name))
        for file in files:
            print('File name: {}'.format(file))



    