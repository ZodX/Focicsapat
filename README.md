# [HUN]Focicsapatok

Ez egy redis NoSQL adatbázis, amit dolgozatként készítettem el az egyetemre.

## Ismertető
Csapatok vannak, tárolunk róluk: név, átlag értékelés (amit a játékosok értékeléséből számítunk ki).
A csapatokban játékosok vannak, tárolunk róluk: név, születési dátum, telefonszám, értékelés. 

## Amit tud
Osztály:
    1. Új csapat létrehozás
    2. Csapat adatainak lekérése
    3. Csapat játékosainak lekérése (Ez egy külön listába lett szedve)
    4. Csapat törlés: játékosokkal együtt, az ő adataik is törlődnek.
    5. Új játékos létrehozása
    6. Játékosok különféle adataihoz való hozzáférés
    7. Játékosok igazolása (Minden esetet kezelve: Ha már a csapat tagja, arról értesít, ha még nincs csapatban akkor leigazol, ha már van csapatban, akkor átigazol és a csapatok átlagértékelései újra számítódnak.)
Egy démon végezze azt a munkát, hogy ha egy csapatnak nem marad több játékosa igazolás után, akkor a csapat törlődik az adatbázisból.
Ezt megírtam az igazolás metódusba IS egyébként, hogy könnyebben nyomon követhető legyen a program jó működése.
    8. Legidősebb és legfiatalabb játékos minden adatával együtt(!) való lekérése zset segítségével.
