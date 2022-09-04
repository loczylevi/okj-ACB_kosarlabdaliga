class Acb_kosarlabda:
    def __init__(self,sor):
        hazai,idegen,hazai_pont,idegen_pont,helyszin,idopont = sor.strip().split(";")
        self.hazai = hazai
        self.idegen = idegen
        self.hazai_pont = hazai_pont
        self.idegen_pont = idegen_pont
        self.helyszin = helyszin
        self.idopont = idopont

with open("eredmenyek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Acb_kosarlabda(sor) for sor in f]
    
hazai = len([sor for sor in lista if "Real Madrid" in sor.hazai])
idegen = len([sor for sor in lista if "Real Madrid" in sor.idegen])

print(f"3. feladat: Real Madrid: Hazai: {hazai}, Idegen: {idegen}")

volt_e_dontetlen = len([sor for sor in lista if sor.hazai_pont == sor.idegen_pont])

if volt_e_dontetlen > 0:
    print("4. feladat: Volt döntetlen? igen")
else:
    print("4. feladat: Volt döntetlen? nem")
    
barcelona_pontos_nev = [sor.hazai for sor in lista if "Barcelona" in sor.hazai][0]

print(f"5. feladat: barcelonai csapat neve: {barcelona_pontos_nev}")

merkozesek_datum_szerint = [sor for sor in lista if sor.idopont == "2004-11-21"]

print("6. feladat:")
[print(f"        {sor.hazai}-{sor.idegen} ({sor.hazai_pont}:{sor.idegen_pont})") for sor in merkozesek_datum_szerint]

statisztika = dict()
print("7.feladat:")
for sor in lista:
    helyszin = sor.helyszin
    statisztika[helyszin] = statisztika.get(helyszin, 0) + 1
helyszinek_20_tobb = [print(f' {helyszin}: {db}') for helyszin, db in statisztika.items() if db > 20]