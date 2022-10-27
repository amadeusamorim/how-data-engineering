from urllib import response
from fake_web_events import Simulation
import json
import boto3 # Biblioteca que interage com a AWS

client = boto3.client('firehose')

# Função para inserir eventos
def put_record(event: dict):
    data = json.dumps(event) + "\n" # Quebra de linha após a string do Json
    response = client.put_record( # Coloco o record no firehose
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