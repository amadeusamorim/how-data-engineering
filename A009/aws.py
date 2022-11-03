#%%
import boto3
from botocore.exceptions import ClientError
from botocore import exceptions
import logging
from dotenv import load_dotenv # Carrega as variáveis de ambiente na execução do programa
from os import getenv # Transforma no código


# %%
load_dotenv('/home/amadeus/.env') # Carrega as minhas variáveis de ambiente que passei anteriormente

#%%
s3_client = boto3.client(
    's3',
    aws_access_key_id = getenv('AWS_ID'),
    aws_secret_access_key = getenv('AWS_KEY')
) # Construo o serviço, descrevendo qual eu quero, usuário e senha

# %%

def criar_bucket(nome):
    try:
        s3_client.create_bucket(Bucket=nome)
    except ClientError as e:
        logging.error(2)
        return False
    
    return True
# %%
criar_bucket('ama-s3-bucket')
# %%
