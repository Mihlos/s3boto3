from myS3 import S3


if __name__ == "__main__":
    s3mihlos = S3()
    # s3mihlos.create_bucket('mihlos-bucket-test')
    # s3mihlos.list_buckets_client()
    # s3mihlos.list_content_client('mihlos-test2')
    s3mihlos.list_buckets_resource()
    s3mihlos.list_content_resource('mihlos-test2')