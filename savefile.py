from myS3 import S3


if __name__ == "__main__":
    s3mihlos = S3('mihlos-bucket-test')
    s3mihlos.create_bucket()