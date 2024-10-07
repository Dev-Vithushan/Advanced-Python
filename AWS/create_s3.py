import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_s3_bucket(bucket_name, region=None):
    try:
        # Create S3 client
        s3_client = boto3.client('s3')

        # If a region is specified, create the bucket in that region
        if region:
            location = {'LocationConstraint': region}
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        else:
            # Default to the 'us-east-1' region if no region is provided
            response = s3_client.create_bucket(Bucket=bucket_name)

        print(f"Bucket '{bucket_name}' created successfully.")
        return response

    except NoCredentialsError:
        print("AWS credentials not available. Please configure your credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please check your AWS configuration.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Replace with your desired bucket name and region
    bucket_name = 'checking-s3-bucket'
    region = 'ap-south-1'  # You can change this to any valid AWS region

    create_s3_bucket(bucket_name, region)
