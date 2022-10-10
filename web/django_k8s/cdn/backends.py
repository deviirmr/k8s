from storages.backends.s3boto3 import S3Boto3Storage
# created a static and media location in the bucet
class StaticRootS3BotoStorage(S3Boto3Storage):
    location = "static"

class MediaRootS3BotoStorage(S3Boto3Storage):
    location = "media"