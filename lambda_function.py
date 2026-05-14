import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.describe_instances()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            
            # Stop only running instances
            if state == 'running':
                print(f"Stopping instance: {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])
    
    return "Stopped idle instances"