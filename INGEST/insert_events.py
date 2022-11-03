from urllib import response
from fake_web_events import Simulation
import json
import boto3 # Biblioteca que interage com a AWS
from botocore.exceptions import ClientError
from botocore import exceptions
from dotenv import load_dotenv # Carrega as variáveis de ambiente na execução do programa
from os import getenv # Transforma no código

load_dotenv('/home/amadeus/.env') # Carrega as minhas variáveis de ambiente que passei anteriormente

firehose_client = boto3.client(
    'firehose',
    aws_access_key_id = getenv('AWS_ID'),
    aws_secret_access_key = getenv('AWS_KEY')
)

# Função para inserir eventos
def put_record(event: dict):
    data = json.dumps(event) + "\n" # Quebra de linha após a string do Json
    response = firehose_client.put_record( # Coloco o record no firehose
        DeliveryStreamName='kineses-amadeus-poc',
        Record={"Data": data}
    )
    print(event)
    return response

# Dados fakes aleatórios
simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=600)

for event in events:
    put_record(event)