# coding: utf-8
import boto3
import os, stat
import datetime, time
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName='key_name')
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ami_name = 'amzn2-ami-kernel-5.10-hvm-2.0.20220606.1-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img = ec2.Image('ami-0cff7528ff583bf9a')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
sg_id = inst.security_groups[0]['GroupId']
security_group = ec2.SecurityGroup(sg_id)
security_group.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': "0.0.0.0/0"}]}])
security_group.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': "41.210.146.128/32"}]}])
time.sleep(120)
inst.reload()
inst.public_dns_name
