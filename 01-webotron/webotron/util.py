# -*- coding: utf-8 -*-
"""Utilities for Webotron."""
from collections import namedtuple

Endpoint = namedtuple('Endpoint', ['name', 'host', 'zone'])

region_to_endpoint = {
    'us-east-2': Endpoint('US East (Ohio)', 's3-website.us-east-2.amazonaws.com', 'Z2O1EMRO9K5GLX'),
    'us-east-1': Endpoint('US East (N. Virginia)', 's3-website-us-east-1.amazonaws.com', 'Z3AQBSTGFYJSTF'),
    'us-west-1': Endpoint('US West (N. California)', 's3-website-us-west-1.amazonaws.com', 'Z2F56UZL2M1ACD'),
    'us-west-2': Endpoint('US West (Oregon)', 's3-website-us-west-2.amazonaws.com', 'Z3BJ6K6RIION7M'),
    'af-south-1': Endpoint('Africa (Cape Town)', 's3-website.af-south-1.amazonaws.com', 'Z83WF9RJE8B12'),
    'ap-east-1': Endpoint('Asia Pacific (Hong Kong)', 's3-website.ap-east-1.amazonaws.com', 'ZNB98KWMFR0R6'),
    'ap-south-1': Endpoint('Asia Pacific (Mumbai)', 's3-website.ap-south-1.amazonaws.com', 'Z11RGJOFQNVJUP'),
    'ap-northeast-3': Endpoint('Asia Pacific (Osaka)', 's3-website.ap-northeast-3.amazonaws.com', 'Z2YQB5RD63NC85'),
    'ap-northeast-2': Endpoint('Asia Pacific (Seoul)', 's3-website.ap-northeast-2.amazonaws.com', 'Z3W03O7B5YMIYP'),
    'ap-southeast-1': Endpoint('Asia Pacific (Singapore)', 's3-website-ap-southeast-1.amazonaws.com', 'Z3O0J2DXBE1FTB'),
    'ap-southeast-2': Endpoint('Asia Pacific (Sydney)', 's3-website-ap-southeast-2.amazonaws.com', 'Z1WCIGYICN2BYD'),
    'ap-northeast-1': Endpoint('Asia Pacific (Tokyo)', 's3-website-ap-northeast-1.amazonaws.com', 'Z2M4EHUR26P7ZW'),
    'ca-central-1': Endpoint('Canada (Central)', 's3-website.ca-central-1.amazonaws.com', 'Z1QDHH18159H29'),
    'cn-northwest-1': Endpoint('China (Ningxia)', 's3-website.cn-northwest-1.amazonaws.com.cn', 'Z282HJ1KT0DH03'),
    'eu-central-1': Endpoint('Europe (Frankfurt)', 's3-website.eu-central-1.amazonaws.com', 'Z21DNDUVLTQW6Q'),
    'eu-west-1': Endpoint('Europe (Ireland)', 's3-website-eu-west-1.amazonaws.com', 'Z1BKCTXD74EZPE'),
    'eu-west-2': Endpoint('Europe (London)', 's3-website.eu-west-2.amazonaws.com', 'Z3GKZC51ZF0DB4'),
    'eu-south-1': Endpoint('Europe (Milan)', 's3-website.eu-south-1.amazonaws.com', 'Z30OZKI7KPW7MI'),
    'eu-west-3': Endpoint('Europe (Paris)', 's3-website.eu-west-3.amazonaws.com', 'Z3R1K369G5AVDG'),
    'eu-north-1': Endpoint('Europe (Stockholm)', 's3-website.eu-north-1.amazonaws.com', 'Z3BAZG2TWCNX0D'),
    'ap-southeast-3': Endpoint('Asia Pacific (Jakarta)', 's3-website.ap-southeast-3.amazonaws.com', 'Z01613992JD795ZI93075'),
    'me-south-1': Endpoint('Middle East(Bahrain)', 's3-website.me-south-1.amazonaws.com', 'Z1MPMWCPA7YB62'),
    'sa-east-1': Endpoint('South America (São Paulo)', 's3-website-sa-east-1.amazonaws.com', 'Z7KQH4QJS55SO'),
    'us-gov-east-1': Endpoint('AWS GovCloud (US-East)', 's3-website.us-gov-east-1.amazonaws.com', 'Z2NIFVYYW2VKV1'),
    'us-gov-west-1': Endpoint('AWS GovCloud (US-West)', 's3-website-us-gov-west-1.amazonaws.com', 'Z31GFT0UA1I2HV')
}


def known_region(region):
    """Return true if this is a known region."""
    return region in region_to_endpoint


def get_endpoint(region):
    """Get the s3 website hosting endpoint for this region."""
    return region_to_endpoint[region]
