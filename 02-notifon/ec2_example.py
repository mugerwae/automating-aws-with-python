# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName='key_name')
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
get_ipython().run_line_magic('clear', '')
key.key_name
key.key_material
key.key_name
key.name
key.name()
key.key_fingerprint
print(key)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ami_name
ami_name = "Amazon Linux 2 Kernel 5.10 AMI 2.0.20220606.1 x86_64 HVM gp2"
filters = [{'Name': 'name', 'Values': [ami_name]}]
ec2.images.filter(Owners=['amazon'], Filters=filters)
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ami_name = "Amazon Linux 2 AMI (HVM)"
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ami_name = "amzn2-ami-kernel-5.10-hvm-2.0.20220606.1-x86_64-gp2"
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ami_name = 'amzn2-ami-kernel-5.10-hvm-2.0.20220606.1-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img = ec2.Image('ami-0cff7528ff583bf9a')
img.Name
img.name
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2
img_apse2 = ec2_apse2.Image(ami-0cff7528ff583bf9a)
img_apse2 = ec2_apse2.Image('ami-0cff7528ff583bf9a')
img_apse2.name
get_ipython().run_line_magic('clear', '')
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img.id
instance = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2-micro', KeyName=key.key_name)
instance = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instance
instance.terminate()
inst = instance[0]
inst.terminate
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
get_ipython().run_line_magic('clear', '')
inst.reload()
inst.public_dns_name
inst.security_groups
inst.security_groups
sg_id = inst.security_groups[0]['GroupId']
sg_id
security_group = ec2.SecurityGroup(sg_id)
security_group
security_group.ip_permissions
security_group.authorize_ingress()
security_group.authorize_ingress()
security_group.authorize_ingress()
security_group.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': "41.210.146.128/32"}]}])
security_group.authorize_ingress(IpPermissions=[{'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': "0.0.0.0/0"}]}])
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ec2_example.py 1-76')
