def harmadik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl=open("fajlok/harmadik.txt","w", encoding="utf-8")
    for index in range(0, len(lista),1):
        print(lista[index], file=kiFajl, end="")
    kiFajl.close()