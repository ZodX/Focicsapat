import redis
from time import sleep

class Demon():
    def __init__(self):
        
        redis_host = '127.0.0.1'
        redis_port = 6379
        redis_password = 'student'

        self.r = redis.StrictRedis(host = redis_host, port = redis_port, password = redis_password, decode_responses = True)

    def csapat_takarito(self):
        while True:          
            for i in self.r.smembers('csapat_lista'):
                if (self.r.scard('csapat_' + i + '_jatekosai') == 0):
                    print('Nincs tobb jatekos, csapat torlodik')
                    p = self.r.pipeline()
                    p.srem('csapat_lista', i)
                    p.delete('csapat_' + i)
                    p.execute(True)
            sleep(2)