r = [ ]
def leer_restricciones():
    i=1
    mala = []
    with open('scp.txt','r') as f:
        f_contents = f.read();
        wena = f_contents.split(' ');
        del(wena[0])

        for word in wena:
            mala.append(int(word.strip('\n')))

        muymala = mala[1002:]

        ##print(muymala)

    f.close()
    contador = muymala[0];

    print(muymala[2:10])
    top = 0
    arreglo = []
    while(i<len(muymala)):
        arreglo.append(muymala[i])
        #print(contador," var: ", muymala[i])
        contador = contador - 1;
        i = i+1
        if (contador < 0):
            r.append(arreglo)
            arreglo = []
            contador = muymala[i-1];

    r.append(arreglo)
    r[199].append(957)

    print(i)
    print(len(muymala))

    for l in range(len(r)):
        r[l].pop()
        print(r[l])

leer_restricciones()
