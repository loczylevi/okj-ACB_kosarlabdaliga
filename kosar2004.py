#  hazai          idegen       hazai_pont            idegen_pont            helyszín        időpont
#    0               1              2                      3                    4              5

with open("eredmenyek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
hazai = len([sor for sor in lista if "Real Madrid" in sor[0]])
idegen = len([sor for sor in lista if "Real Madrid" in sor[1]])

print(f"3. feladat: Real Madrid: Hazai: {hazai}, Idegen: {idegen}")

volt_e_dontetlen = len([sor for sor in lista if sor[2] == sor[3]])

if volt_e_dontetlen > 0:
    print("4. feladat: Volt döntetlen? igen")
else:
    print("4. feladat: Volt döntetlen? nem")
    
barcelona_pontos_nev = [sor[0] for sor in lista if "Barcelona" in sor[0]][0]

print(f"5. feladat: barcelonai csapat neve: {barcelona_pontos_nev}")

merkozesek_datum_szerint = [sor for sor in lista if sor[5] == "2004-11-21"]

print("6. feladat:")
[print(f"        {sor[0]}-{sor[1]} ({sor[2]}:{sor[3]})") for sor in merkozesek_datum_szerint]

statisztika = dict()
print("7.feladat:")
for sor in lista:
    helyszin = sor[4]
    statisztika[helyszin] = statisztika.get(helyszin, 0) + 1
helyszinek_20_tobb = [print(f' {helyszin}: {db}') for helyszin, db in statisztika.items() if db > 20]
