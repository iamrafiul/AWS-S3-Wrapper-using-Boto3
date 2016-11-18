# Amazon AWS S3 experiment using Boto3

## Introduction
This is an example of using Boto3, AWS API for python, for creating S3(Simple Storage Service) bucket(s) as well as uploading/downloading/deleting files from bucket(s).

The main file is the Amazon_S3_Wrapper.py and I have done the following steps.

###Note: I haven't set up the aws_access_key_id and aws_secret_access_key in this example. Please follow this [link](https://github.com/boto/boto3) for a quickstart.

## Functionalities: 
#### Creating S3 resource and client
Resource and client are created once during the construction of class and will be available throughout the program lifecycle.
```
def __init__(self):
    self.s3 = boto3.resource('s3')
    self.client = boto3.client('s3')
```

#### List all the buckets in S3
List all the buckets of a given region. Return the list of bucket names.

```
list_buckets(region)
```

#### Create bucket in S3
Create buckets of same name in different regions. You can repeat the bucket creation using the last param 'repeat'. Return None if successful, otherwise error.

```
create_buckets(bucket_name=None, regions=[], repeat=1)
```

#### Upload file in S3 bucket
Upload a file of name 'filename' in the bucket named 'bucket' and set the key for the server file as 'key'. Return the key . Key for success, False otherwise.

```
upload_file(filename, bucket, key)
```

#### Download file from S3 bucket
Download a file from bucket 'bucket' using the key 'key' and save it as 'filename'(Can be in the working directory or in any valid directory). Returns True if successful, otherwise False.

```
download_file(bucket, key, filename)
```

#### Delete file from S3 bucket
Delete the file having key 'key' from the bucket named 'bucket'. Returns True if successful, otherwise False.

```
delete_file(bucket, key)
```

#### Benchmarking Tool
Custom Benchmarking for calculating Upload and Download latency of different server regions for files of different size. Generates 2(two) graphs; one for Upload latency plotting and the other for Download latency plotting.

```
test_latency()
```
