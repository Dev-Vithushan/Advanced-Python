import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def list_s3_buckets():
    try:
        # Create an S3 client using boto3
        s3 = boto3.client('s3')

        # List all S3 buckets
        response = s3.list_buckets()

        if 'Buckets' in response:
            print(f"Total Buckets: {len(response['Buckets'])}")
            print("\nFetching S3 bucket details:\n")

            for bucket in response['Buckets']:
                bucket_name = bucket['Name']
                creation_date = bucket['CreationDate']

                # Fetch the bucket's location (region)
                bucket_location = s3.get_bucket_location(Bucket=bucket_name)
                region = bucket_location['LocationConstraint']

                print(f"Bucket Name: {bucket_name}")
                print(f"Creation Date: {creation_date}")
                print(f"Bucket Region: {region if region else 'us-east-1 (default)'}")
                print("-" * 40)

        else:
            print("No S3 buckets found.")

    except NoCredentialsError:
        print("Credentials not available. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please check your AWS configuration.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    list_s3_buckets()
