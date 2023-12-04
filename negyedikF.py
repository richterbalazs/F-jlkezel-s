def negyedik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl=open("fajlok/negyedik.txt","w", encoding="utf-8")
    for index in range(0, len(lista),1):
        # a sorokat eldarabolom szóközök mentén.
        daraboltSor = lista[index].split(" ")
        # a lista 0-adik elemét (első szót) írom a fájlba
        print(daraboltSor[0], file=kiFajl)
    kiFajl.close()