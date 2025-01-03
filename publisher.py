import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()

    await nc.connect("nats://localhost:4222")

    # Небольшая задержка, чтобы дать подписчику время на подписку
    await asyncio.sleep(2)

    # Отправка сообщения
    await nc.publish("my_subject", b'Hello, NATS!')
    print("Message published")

    await nc.close()

if __name__ == '__main__':
    asyncio.run(run())
