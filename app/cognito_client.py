"""`AWS Cognito`のクライアントを作成するモジュールです。
"""
import boto3

cognito_client = boto3.client(
    'cognito-idp',
    region_name='ap-northeast-1',
)
