import boto3 as aws

class AWSUtils:
    def __init__(self, region="us-west-1"):
        self.region = region

    def get_ssm_parameter(self, param_name: str) -> str:
        """
        Returns value corresponding to param_name from AWS SSM
        """
        ssm_client = aws.client('ssm', region_name=self.region)
        response = ssm_client.get_parameter(Name=param_name)
        
        ssm_client.close()
        return response["Parameter"]["Value"]
    
