import boto3
import os

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

ec2 = session.client('ec2')

def create_machine(name_of_instance):    
    response = ec2.run_instances(
        ImageId = "ami-01a00762f46d584a1",
        InstanceType = "t3.micro",
        SecurityGroupIds = ["sg-0e9f9c2d147f3c3b6"],           
        MaxCount = 1,
        MinCount = 1,
        KeyName = "June-2026",
        TagSpecifications = [
            {
                "ResourceType": "instance",
                "Tags": [{"Key":"Name", "Value":name_of_instance}]
            }
        ]
    ) 
    print(response['Instances'])  

def stop_machine(name_of_Instance):    
    response = ec2.stop_instances(
        InstanceIds=["i-0704b92df39e9645f"])
    print(response)

stop_machine("Static_app_auto")    


