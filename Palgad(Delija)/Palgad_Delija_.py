palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    print(palk)
    print(inimesed)
    print("Средняя зарплата - k,\nМинимальная зарплата - min,\nМаксимальная зарплата -max,\nПоиск по имени -nimi,\nСортировка -sort, \nДобавить человека - add")
    print("Delete - del")
    print("Top - top_max")
    valik=input("Valik-...")
    if valik=="k":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
    elif valik=="min":
        m_palgad,nimed=minimum(palk,inimesed)
        for n in nimed:
            print(m_palgad[0], " saab kätte ",n)  
    elif valik=="max":
        max_palk,kellel=maksimum(palk,inimesed)
        print("Maksimaalne palk ", max_palk, " saab kätte ",kellel)
    elif valik=="nimi":
        ots_nimi,ots_palk=nimi(palk,inimesed)
        for i in range(len(ots_nimi)):
            print(ots_nimi[i]," saab kätte ", ots_palk[i])
    elif valik=="sort":
        p,i=sorteerimine(palk,inimesed)
        for i in range(len(inimesed)):
            print(inimesed[i]," saab kätte ", palk[i])
    elif valik=="del":
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tühi list")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," saab kätte ", palk[i])
    elif valik=="add":
        i=adding(palk,inimesed)
        print(palk,inimesed)

    elif valik=="top_max":
        p, i=topbogat(palk,inimesed)      

def topbogat(palk,inimesed):
    top,inimes=sorteerimine(palk,inimesed)
    k= int(input("Выберите значение топ: " ))
    palk.reverse()
    inimesed.reverse()
    for i in range(0,k,1):
        print(palk[i])
        print(inimesed[i])
    return palk, inimesed   

def adding(palk,inimesed):
    add=input("Кого добавить??? ")
    inimesed.append(add)
    add_zp=int(input("Какая зарплата???"))
    palk.append(add_zp)
    return palk,inimesed   

def delete(palk, inimesed):
    x=input("name or number")
    if x=="number":
        i=int(input("Chose number"))
        palk.pop(i-1)
        inimesed.pop(i-1)
    elif x=="name":
        i=0
        keda=input("Write the name =>")
        n=len(inimesed)
        while i<n:
            if keda==inimesed[i]:
                inimesed.pop(i)
                palk.pop(i)
                n=len(inimesed)
            else:
                i+=1
            
    
    return palk, inimesed      

def kustutamine():
    keskmin = keskmine(palk)
    print(keskmin)
    for i in palk:
        if i < kesk:
            index = palk.index(i)
            palk.pop(index)
            inimesed.pop(index)   
        
def sorteerimine(palk,inimesed):
    abi_p=0
    abi_i=""
    n=len(inimesed)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if palk[i]>palk[j]:
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
    return palk,inimesed

def nimi(palk,inimesed):
    ots_nimi=[]
    ots_palk=[]
    palk_keda=0
    keda=input("Sisesta nimi... ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
            palk_keda=palk[j]
            ots_nimi.append(inimesed[j])
            ots_palk.append(palk_keda)
        else:pass
    return ots_nimi,ots_palk


def maksimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
    n=palk.count(max_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(max_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed   

def minimum(palk,inimesed):      
    m_palgad=[]
    nimed=[]
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:      
        if p<min_palk:        
            min_palk=p         
            i=palk.index(min_palk) 
            kellel=inimesed[i]
    n=palk.count(min_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy() 
    for i in range(n):
        j=palk_copy.index(min_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed 
    
def keskmine(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k

while True:                             
    palgad(palk,inimesed)
