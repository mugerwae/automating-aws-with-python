from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Robin Norwood',
    author_email='robin@acloud.guru',
    description='Webotron 80 is a tool to deploy static webistes to S3',
    license='GPLLv3+',
    packages=['webotron'],
    url='https://github.com/AcloudGuru/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''

)