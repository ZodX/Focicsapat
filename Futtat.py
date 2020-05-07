from Osztaly import Osztaly
from Demonok import Demon

rf = Osztaly()

rf.uj_csapat_letrehozas('Debrecen', '1', 'Dezso', '1999', '5312', '75')
rf.uj_csapat_letrehozas('Sarospatak', '2', 'Anger Zsolt', '2002', '2345', '87')

print(rf.jatekos_lista())
print(rf.jatekos_attr('1'))
print(rf.jatekos_attr('2'))

print(rf.csapat_lista())

print(rf.csapat_attr('Debrecen'))
print(rf.csapat_attr('Sarospatak'))

#rf.csapat_torles('Debrecen')
#rf.csapat_torles('Sarospatak')
#print(rf.csapat_lista())

print(rf.csapat_lista_attr())
print(rf.csapat_jatekosai_lista('Debrecen'))
print(rf.csapat_jatekosai_lista('Sarospatak'))

rf.uj_jatekos_letrehozas('3', 'Gedeon', "1999", '1234', '70')
rf.jatekos_igazol('3', 'Debrecen')
rf.uj_jatekos_letrehozas('4', 'Arpad', '2001', '1236', '80')
rf.jatekos_igazol('4', 'Debrecen')
rf.uj_jatekos_letrehozas('5', 'Arpad', '2004', '1237', '93')
rf.jatekos_igazol('5', 'Sarospatak')
rf.uj_jatekos_letrehozas('6', 'Arpad', '2001', '1239', '82')
rf.jatekos_igazol('6', 'Sarospatak')

rf.uj_jatekos_letrehozas('7', 'Gergely', "1999", '123435', '73')

rf.uj_jatekos_letrehozas('8', 'Amanda', "1999", '123465', '75')

rf.uj_jatekos_letrehozas('9', 'Tihamer', '2004', '42356', '90')

#print(rf.jatekos_attr('1'))
#print(rf.jatekos_attr('2'))
#print(rf.jatekos_attr('3'))

print(rf.csapat_jatekosai_lista('Debrecen'))

#print(rf.jatekos_ertekeles('1'))

#print(rf.csapat_atlagertekeles('Debrecen'))

#rf.csapat_torles('Debrecen')

#print(rf.csapat_attr('Debrecen'))

#rf.jatekos_igazol('1', 'Sarospatak')

#print(rf.csapat_lista_attr())

print('Jatekos lista eletkor: ')
print(rf.jatekos_lista_eletkor())
print('Legidosebb jatekos(ok) adatai:')
print(rf.legidosebb_jatekos_azon())
print('Legfiatalabb jatekos(ok) adatai:')
print(rf.legfiatalabb_jatekos_azon())

print('Debrecen jatekosai azonositok:')
print(rf.csapat_jatekosai_lista('Debrecen'))
rf.csapat_torles('Debrecen')
#print('Debrecen jatekosai azonositok:')
#print(rf.csapat_jatekosai_lista('Debrecen'))
#print('1 -es jatekos adatai:')

rf.jatekos_igazol('1', 'Sarospatak')
rf.jatekos_igazol('2', 'Sarospatak')
print(rf.csapat_lista())

print('Jatekos lista eletkor: ')
print(rf.jatekos_lista_eletkor())

print(rf.jatekos_attr('1'))
rf.csapat_torles('Sarospatak')

print('Jatekos lista eletkor: ')
print(rf.jatekos_lista_eletkor())


d = Demon()
d.csapat_takarito()

