import asyncio
from nats.aio.client import Client as NATS

async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")

async def run():
    nc = NATS()

    await nc.connect("nats://localhost:4222")

    # Подписка на сообщения
    await nc.subscribe("my_subject", cb=message_handler)

    print("Subscriber is waiting for messages...")

    # Ожидание сообщений
    await asyncio.sleep(60)  # Увеличим время ожидания до 60 секунд

    await nc.close()

if __name__ == '__main__':
    asyncio.run(run())
