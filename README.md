# Базовый конфиг для отправки и принятия сообщение через брокер nats.

---

```sh
$ pip install -r ./requirements.txt
# запуск docker nats
$ docker run -p 4222:4222 nats
# new terminal
$ python ./subscriber.py
# new terminal
$ python ./publisher.py
```
