def hetedik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # visszafelé lista kiírása
    kiFajl = open("fajlok/hetedik.txt", "w", encoding="utf-8")
    for index in range(len(lista)-1,-1,-1):
        print(lista[index])
        print(lista[index], file=kiFajl)

    kiFajl.close()