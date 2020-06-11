from datetime import datetime
import asyncio
import time
import requests

SLEEP_SECONDS = .1
BATCH = 2**5
URL = "http://www.google.com"

# Vamos compara tempo de execução de uma fila de tarefas.
# Tarefas: Print requisições para google.com

def task(index):
    print(index, "\t", requests.get(URL))


async def get_number_async(number):
    await asyncio.sleep(SLEEP_SECONDS)
    print(datetime.utcnow(), number)


def run_async():
    start = datetime.utcnow()

    loop = asyncio.get_event_loop()
    tasks = []
    for number in range(10):
        tasks.append(get_number_async(number))

    loop.run_until_complete(asyncio.wait(tasks))
    print(f"stamp: {datetime.utcnow() - start}")


def run_sync():
    start = datetime.utcnow()
    for ii in range(1, BATCH + 1):
        task(ii)
    print("stamp: ", datetime.utcnow() - start)


if __name__ == "__main__":
    run_sync()
