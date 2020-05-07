import redis

class Osztaly():
    def __init__(self):
        
        redis_host = '127.0.0.1'
        redis_port = 6379
        redis_password = 'student'

        self.r = redis.StrictRedis(host = redis_host, port = redis_port, password = redis_password, decode_responses = True)

    def uj_csapat_letrehozas(self, cs_nev, j_azon, j_nev, j_szul_dat, j_tel, j_ertekeles):
        if (self.r.sismember('csapat_lista', cs_nev) == 1):
            print('Letezo csapat: ' + cs_nev)
            return False
        else:     
            if (self.r.sismember('jatekos_lista', j_azon) == 1):
                print('Letezo jatekos: ' + j_azon)
                return False
            else:
                p = self.r.pipeline()
                p.sadd('csapat_lista', cs_nev)
                p.hmset('csapat_' + cs_nev, {'nev': cs_nev, 'ertekeles': j_ertekeles })
                p.sadd('jatekos_lista', j_azon)
                p.sadd('csapat_' + cs_nev + '_jatekosai', j_azon)
                p.hmset('jatekos_' + j_azon, {'nev': j_nev, 'szul_dat': j_szul_dat, 'tel': j_tel, 'ertekeles': j_ertekeles})
                p.zadd('jatekos_eletkor', {j_azon: j_szul_dat})
                p.execute(True)
                print(cs_nev + ' csapat letrejott')
                return True
            
    def csapat_lista(self):
        return self.r.smembers('csapat_lista')
    
    def csapat_jatekosai_lista(self, nev):
        return self.r.smembers('csapat_' + nev +'_jatekosai')
            
    def csapat_attr(self, nev):
        if (self.r.sismember('csapat_lista', nev) == 0):
            return 'A ' + nev + ' csapat nem lezetik'
        return self.r.hgetall('csapat_' + nev)
    
    def csapat_lista_attr(self):
        vissza = []
        for i in self.r.smembers('csapat_lista'):
            f = self.csapat_attr(i)
            vissza.append(i)
            vissza.append(f)
        return vissza
    
    def jatekos_neve(self, azon):
        return self.r.hget('jatekos_' + azon, 'nev')
    
    def csapat_torles(self, nev):
        for i in self.csapat_jatekosai_lista(nev):
            p = self.r.pipeline()
            p.srem('jatekos_lista', i)
            p.delete('jatekos_' + i)
            p.zrem('jatekos_eletkor', i)
            p.execute(True)
        p = self.r.pipeline(True, None)
        p.srem('csapat_lista', nev)
        p.delete('csapat_' + nev)
        p.delete('csapat_' + nev + '_jatekosai')
        print('A ' + nev + ' csapat torlesre kerult a jatekosaival egyutt.')
        p.execute(True)
        
    def uj_jatekos_letrehozas(self, azon, nev, szul_dat, tel, ertekeles):
        if (self.r.sismember('jatekos_lista', azon) == 1):
            print('Letezo jatekos azonosito')
            return False
        else:
            p = self.r.pipeline(True, None)
            p.sadd('jatekos_lista', azon)
            p.hmset('jatekos_' + azon, {'nev': nev, 'szul_dat': szul_dat, 'tel': tel, 'ertekeles': ertekeles})
            p.zadd('jatekos_eletkor', {azon: szul_dat})
            p.execute(True)
            print('Jatekos ' + nev + ' letrejott.')
            return True
    
    def jatekos_lista_eletkor(self):
        return self.r.zrange('jatekos_eletkor', 0, -1, withscores=True)
        
    def jatekos_attr(self, azon):
        return self.r.hgetall('jatekos_' + azon)
        
    def jatekos_lista(self):
        return self.r.smembers('jatekos_lista')
    
    def jatekos_igazol(self, j_azon, cs_nev):
        #Ha mar tagja a csapatnak
        if (self.r.sismember('csapat_' + cs_nev +'_jatekosai', j_azon) == 1):
            print('A jatekos mar a csapat tagja.')
            return False
        else:
            #Ha mar van egy csapatban, akkor atigazol
            for i in self.r.smembers('csapat_lista'):
                if (self.r.sismember('csapat_' + i + '_jatekosai', j_azon) == 1):
                    print('Jatekos ' + j_azon + ' leigazolt innen: ' + i + ' ide: ' + cs_nev)
                    p = self.r.pipeline(True, None)
                    p.sadd('csapat_' + cs_nev + '_jatekosai', j_azon)
                    p.srem('csapat_' + i + '_jatekosai', j_azon)
                    p.execute(True)
                    #Ha nincs tobb jatekosa a csapatnak, akkor toroljuk
                    if (self.r.scard('csapat_' + i + '_jatekosai') == 0):
                        p = self.r.pipeline()
                        p.srem('csapat_lista', i)
                        p.delete('csapat_' + i)
                        p.execute(True)
                    #Eloszor be adjuk a jatekost, hogy ne legyen nullaval valo osztas azert irtam kulon
                    self.r.hmset('csapat_' + i, {'nev': i, 'ertekeles': self.csapat_atlagertekeles(i)})
                    self.r.hmset('csapat_' + cs_nev, {'nev': cs_nev, 'ertekeles': self.csapat_atlagertekeles(cs_nev)})
                    return True
            #Ha meg nincs csapatban, akkor csak hozzaadjuk a kivant csapathoz
            self.r.sadd('csapat_' + cs_nev + '_jatekosai', j_azon)
            #Eloszor be adjuk a jatekost, hogy ne legyen nullaval valo osztas azert irtam kulon
            self.r.hmset('csapat_' + cs_nev, {'nev': cs_nev, 'ertekeles': self.csapat_atlagertekeles(cs_nev)})
            print('Jatekos ' + j_azon + ' elso igazolasa tortent ide: ' + cs_nev)
            return True
            
    def jatekos_ertekeles(self, azon):
        return self.r.hget('jatekos_' + azon, 'ertekeles')        
    
    def csapat_atlagertekeles(self, cs_nev):
        if (self.r.sismember('csapat_lista', cs_nev) == 0):
            print('Nem letezo csapat')
            return 0
        else: 
            db = 0
            sum = 0
            for i in self.r.smembers('jatekos_lista'):
                if (self.r.sismember('csapat_' + cs_nev + '_jatekosai', i) == 1):
                   sum += int(self.jatekos_ertekeles(i))
                   db = db + 1
            return sum/db
            
    def legidosebb_jatekos_azon(self):
        azon = self.r.zrange('jatekos_eletkor', 0, 0)[0]
        dat = self.r.hget('jatekos_' + azon, 'szul_dat')
        db = 0
        for i in self.r.smembers('jatekos_lista'):
            if (self.r.hget('jatekos_' + i, 'szul_dat') == dat):
                db = db + 1
        
        azonok = []
        for i in range(db):
            azonok.append(self.r.zrange('jatekos_eletkor', 0, db)[i])
        
        vissza = []    
        for i in range(db):
            vissza.append(azonok[i])
            vissza.append(self.jatekos_attr(azonok[i]))
        return vissza
        
    def legfiatalabb_jatekos_azon(self):
        azon = self.r.zrange('jatekos_eletkor', 0, 0, desc = True)[0]
        dat = self.r.hget('jatekos_' + azon, 'szul_dat')
        db = 0
        
        for i in self.r.smembers('jatekos_lista'):
            if (self.r.hget('jatekos_' + i, 'szul_dat') == dat):
                db = db + 1
        
        azonok = []
        for i in range(db):
            azonok.append(self.r.zrange('jatekos_eletkor', 0, db, desc = True)[i])
        
        vissza = []    
        for i in range(db):
            vissza.append(azonok[i])
            vissza.append(self.jatekos_attr(azonok[i]))
        return vissza
        
        
        
    