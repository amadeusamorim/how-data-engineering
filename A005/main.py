import datetime
import time

from schedule import repeat, every, run_pending
from ingestors import DaySummaryIngestor
from writers import DataWriter

# Ingere os dados das respectivas moedas
if __name__ == "__main__":
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter,
        coins=["BTC", "ETH", "LTC", "BCH"],
        default_start_date=datetime.date(2022, 10, 25)
    )

    # Repete a cada um segundo
    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()


    while True:
        run_pending()
        time.sleep(0.5)

