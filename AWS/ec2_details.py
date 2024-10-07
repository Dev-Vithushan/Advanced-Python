import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def fetch_ec2_details():
    try:
        # Create an EC2 client
        ec2_client = boto3.client('ec2')

        # Describe EC2 instances
        response = ec2_client.describe_instances()

        # Loop through the instances and fetch details
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                instance_state = instance['State']['Name']
                public_ip = instance.get('PublicIpAddress', 'N/A')  # Public IP may not always be available
                launch_time = instance['LaunchTime']
                availability_zone = instance['Placement']['AvailabilityZone']

                print(f"Instance ID: {instance_id}")
                print(f"Instance Type: {instance_type}")
                print(f"Instance State: {instance_state}")
                print(f"Public IP: {public_ip}")
                print(f"Launch Time: {launch_time}")
                print(f"Availability Zone: {availability_zone}")
                print("-" * 40)

    except NoCredentialsError:
        print("AWS credentials not available. Please configure your credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please check your AWS configuration.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    fetch_ec2_details()
