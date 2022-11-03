import time

def cTab():
    liste = []
    rep = int(input("Nombre de valeurs à trier: "))
    for x in range(rep):
        liste.append(int(input("Nombre: ")))
    return liste

def tri(type,tab,direction):

    if type == "fusion":  #tri adapté au big data

        if len(tab) > 1:
            mid = len(tab)//2
            A = tab[:mid]
            B = tab[mid:]
            tri(type,A,direction)
            tri(type,B,direction)
            i = j = k = 0
            while i < len(A) and j < len(B):
                if direction == "increase":

                    if A[i] < B[j]:
                        tab[k] = A[i]
                        i += 1
                    else:
                        tab[k] = B[j]
                        j += 1

                elif direction == "decrease":

                    if A[i] > B[j]:
                        tab[k] = A[i]
                        i += 1
                    else:
                        tab[k] = B[j]
                        j += 1
                k += 1

            while i < len(A):
                tab[k] = A[i]
                i += 1
                k += 1

            while j < len(B):
                tab[k] = B[j]
                j += 1
                k += 1

    elif type == "buble":  #tri adapté aux petites listes

        a = 0
        while a < len(tab):
            for i in range(len(tab)-1):

                if direction == "increase":
                    
                    if tab[i] > tab[i+1]:
                        temp = tab[i+1]
                        tab.pop(i+1)
                        tab.insert(i,temp)

                elif direction == "decrease":

                    if tab[i] < tab[i+1]:
                        temp = tab[i+1]
                        tab.pop(i+1)
                        tab.insert(i,temp)
            a+=1

tab = cTab()
typeTri = input("Entrez le type de tri: buble or fusion : ")
direction = input("Entrez l'ordre du tri: increase ou decrease : ")

start = time.perf_counter()
tri(typeTri, tab, direction)
end = time.perf_counter()

time = end - start

print(f"Tri {typeTri} {direction}\nliste:",tab)
print(f"temps éxécution: {time:.4f}")


