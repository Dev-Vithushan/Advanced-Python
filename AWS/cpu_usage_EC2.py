import boto3
from datetime import datetime, timedelta


def get_cpu_utilization(instance_id):
    # Create a CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Set the time range for CPU usage (last 1 hour)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=1)

    try:
        # Fetch CPU utilization data from CloudWatch
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,  # 5-minute intervals
            Statistics=['Average'],
            Unit='Percent'
        )

        # Check if the response contains data points
        if 'Datapoints' in response and len(response['Datapoints']) > 0:
            print(f"CPU utilization for instance {instance_id} (last hour):")
            for data_point in response['Datapoints']:
                timestamp = data_point['Timestamp']
                average_cpu = data_point['Average']
                print(f"Timestamp: {timestamp}, CPU usage: {average_cpu:.2f}%")
        else:
            print(f"No CPU utilization data found for instance {instance_id}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Replace with your EC2 instance ID
    instance_id = 'i-0e40f23528195df45'
    get_cpu_utilization(instance_id)
