# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.resource('autoscaling')
as_client = session.client('autoscaling')
as_client
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
get_ipython().run_line_magic('save', 'autoscale_example.py 1-8')
