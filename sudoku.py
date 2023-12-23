import numpy as np
import time

import copy as cp

#určení rozměrů tabulky (nemusí být jen 9x9, ale taky 4x4, 16x16, 25x25 atd. - vždy druhá mocnina nějakého čísla)
sqrt_of_max = 3
maximal_value = sqrt_of_max * sqrt_of_max

def insert_initial_values(initial_layout):
    """
    funkce pro zadání počátečních podmínek (za předpokladu, že nejsou zadány přímo v kódu)

    Parametry:
    - initial_layout (np.array): počáteční rozložení číslic
    """
    print("Zadej pocatecni hodnoty:\n")

    for i in range(maximal_value):
        print(f"  i = {i}:\n")
        feedback = input('    Budete zadávat pro konkrétní hodnoty "j" (ano/ne)? ')
        while feedback != "a" and feedback != "n" and feedback != "ano" and feedback != "ne":
            feedback = input()
        print()
        if feedback == "a" or feedback == "ano":
            while True:
                j = int(input("    j = "))
                if j < 0 or j > maximal_value - 1:
                    break
                initial_layout[i, j] = input(f"    M({i},{j}) = ")
                print()
            print()
    print()

def search_position_index(i, j, ListOfLists2):
    """
    funkce pro vyhledání pořadového čísla pozice s danými souřadnicemi pozice v příslušném složeném vektoru

    Parametry:
    - i (int): souřadnice řádku (od O)
    - j (int): souřadnice sloupce (od O)
    - ListOfLists2 (2D list): vektor souřadnic pozic v uspořádaném vektoru přípustných čísel

    Výstup:
    - k (int): pořadové číslo pozice v aktuálním uspořádání
    """
    k = 0
    while ListOfLists2[k][0] != i or ListOfLists2[k][1] != j:
        k += 1
    return k

def can_be_in_line(q, i , j, ar):
    """
    test, zda s ohledem na rozložení číslic v daném ŘÁDKU může daná pozice obsahovat konkrétní číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - ar (np.array): zkoumané rozložení číslic

    Výstup:
    - True nebo False
    """
    for m in range(maximal_value):
        if m == j or ar[i, m] == 0:
            continue
        if q == ar[i, m]:
            return False
    return True

def can_be_in_column(q, i, j, ar):
    """
    test, zda s ohledem na rozložení číslic v daném SLOUPCI může daná pozice obsahovat konkrétní číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - ar (np.array): zkoumané rozložení číslic

    Výstup:
    - True nebo False
    """
    for m in range(maximal_value):
        if m == i or ar[m, j] == 0:
            continue
        if q == ar[m, j]:
            return False
    return True

def can_be_in_cell(q, i, j, ar):
    """
    test, zda s ohledem na rozložení číslic v dané BUŇCE může daná pozice obsahovat konkrétní číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - ar (np.array): zkoumané rozložení číslic

    Výstup:
    - True nebo False
    """
    a = int(i/sqrt_of_max)
    b = int(j/sqrt_of_max)
    for m in range(sqrt_of_max):
        for n in range(sqrt_of_max):
            if (sqrt_of_max * a + m == i and sqrt_of_max * b + n == j) or ar[sqrt_of_max * a + m, sqrt_of_max * b + n] == 0:
                continue
            if q == ar[sqrt_of_max * a + m, sqrt_of_max * b + n]:
                return False
    return True

def count_in_line(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    zjištění počtu pozic v daném ŘÁDKU, které mohou obsahovat konkrétní  číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - temp (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel

    Výstup:
    - count (int): počet pozic s danou vlastností
    """
    count = 0

    for m in range(maximal_value):
        if temp[i, m] != 0:
            continue
        position_index = search_position_index(i, m, ListOfLists2)
        for n in range(len(ListOfLists1[position_index])):
            if ListOfLists1[position_index][n] == q:
                count += 1
    return count

def count_in_column(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    zjištění počtu pozic v daném SLOUPCI, které mohou obsahovat konkrétní  číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - temp (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel

    Výstup:
    - count (int): počet pozic s danou vlastností
    """
    count = 0

    for m in range(maximal_value):
        if temp[m, j] != 0:
            continue
        position_index = search_position_index(m, j, ListOfLists2)
        for n in range(len(ListOfLists1[position_index])):
            if ListOfLists1[position_index][n] == q:
                count += 1

def count_in_cell(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    zjištění počtu pozic v dané BUŇCE, které mohou obsahovat konkrétní  číslo

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - temp (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel

    Výstup:
    - count (int): počet pozic s danou vlastností
    """
    count = 0

    line_quotient = int(i / sqrt_of_max) * sqrt_of_max
    column_quotient = int(j / sqrt_of_max) * sqrt_of_max

    for m in range(maximal_value):
        needed_i = line_quotient + int(m / sqrt_of_max)
        needed_j = column_quotient + m % sqrt_of_max

        if temp[needed_i, needed_j] != 0:
            continue

        position_index = search_position_index(needed_i, needed_j, ListOfLists2)
        for n in range(len(ListOfLists1[position_index])):
             if ListOfLists1[position_index][n] == q:
                 count += 1
    return count

def interchange_vectors(a, b, ListOfLists):
    """
    prohození složek 2D-seznamů v rámci bubblesortu

    Parametry:
    - a (int): pořadové číslo první prohazované pozice
    - b (int): pořadové číslo druhé prohazované pozice
    - ListOfLists (2D list): uspořádávaný 2D-seznam
    """
    ListOfLists_a = cp.deepcopy(ListOfLists[a])
    ListOfLists_b = cp.deepcopy(ListOfLists[b])

    ListOfLists[a][:] = ListOfLists_b
    ListOfLists[b][:] = ListOfLists_a

def bubblesort(ListOfLists1, ListOfLists2):
    """
    algoritmus bubblesort - uspořádává složky (tvořené seznamy) daných 2D-seznamů podle velikosti (počtu prvků obsažených v jednotlivých složkách)

    Parametry:
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    """
    unsorted = True
    i = 0
    while i < len(ListOfLists1) and unsorted:
        unsorted = False
        for j in range(len(ListOfLists1)-i-1):
            if len(ListOfLists1[j]) > len(ListOfLists1[j+1]):
                unsorted = True
                interchange_vectors(j, j + 1, ListOfLists1)
                interchange_vectors(j, j + 1, ListOfLists2)
        i += 1

def adjust_acceptable_values(q, i, j, ListOfLists1, ListOfLists2):
    """
    při výběru čísla pro vyplnění dané pozice se zde odpovídající číslo vyškrtává ze seznamu přípustných čísel pro všechny ostatní
    pozice nacházející se ve stejném řádku, sloupci a buňce; následně jsou složky příslušných 2D-seznamů, jejichž velikost se vynuluje,
    vyloučeny

    Parametry:
    - q (int): zkoumané číslo
    - i (int): souřadnice řádku (od 0)
    - j (int): souřadnice sloupce (od 0)
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    """
    PomList1 = []
    PomList2 = []

    k = 0

    while k < len(ListOfLists1):

        TempList = []

        for l in range(len(ListOfLists1[k])):
            TempList.append(ListOfLists1[k][l])

        if q in TempList:

            condition1 = ListOfLists2[k][0] == i
            condition2 = ListOfLists2[k][1] == j
            condition3 = int(ListOfLists2[k][0] / sqrt_of_max) == int(i / sqrt_of_max) and int(ListOfLists2[k][1] / sqrt_of_max) == int(j / sqrt_of_max)

            if condition1 or condition2 or condition3:

                just_filled = condition1 and condition2
                TempList.remove(q)

                if len(TempList) > 0 and not just_filled:
                    PomList1.append(TempList)
                    PomList2.append(ListOfLists2[k])
            else:
                PomList1.append(TempList)
                PomList2.append(ListOfLists2[k])
        else:
            PomList1.append(TempList)
            PomList2.append(ListOfLists2[k])

        k += 1

    ListOfLists1[:] = cp.deepcopy(PomList1)
    ListOfLists2[:] = cp.deepcopy(PomList2)

    bubblesort(ListOfLists1, ListOfLists2)

def find_hidden_singles(temp, ListOfLists1, ListOfLists2):
    """
    další zefektivnění: pro účely zjednodušení na základě zjištěných přípustných číslic hledáme případné pozice, které jako jediné
    připouštějí umístění některých číslic v rámci daného řádku, sloupce nebo buňky (tzv. skrytý singl)

    Parametry:
    - temp (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    """
    new_values = True
    while new_values:
        new_values = False
        for q in range(1, maximal_value + 1):
            for i in range(maximal_value):
                for j in range(maximal_value):

                    if temp[i, j] != 0:
                        continue

                    position_index = search_position_index(i, j, ListOfLists2)
                    element_not_found = True
                    for k in range(len(ListOfLists1[position_index])):
                        if ListOfLists1[position_index][k] == q:
                            element_not_found = False
                            break
                    if element_not_found:
                        continue

                    one_in_line = count_in_line(q, i, j, temp, ListOfLists1, ListOfLists2) == 1
                    one_in_column = count_in_column(q, i, j, temp, ListOfLists1, ListOfLists2) == 1
                    one_in_cell = count_in_cell(q, i, j, temp, ListOfLists1, ListOfLists2) == 1

                    if (one_in_line or one_in_column or one_in_cell) and (len(ListOfLists1[position_index]) > 1):
                        ListOfLists1[position_index] = [q]
                        new_values = True

def main_iteration(ar, ListOfLists1, ListOfLists2, ptemp_size, previous_temp, previous_acceptable_values, previous_index_order):
    """
    hlavní iterace: pro zefektivnění výpočtu jsou na začátku 2D-vektory přípustných číslic seřazeny podle velikosti; funkce dále
    vybírá číslo pro vyplnění aktuální pozice a kontroluje, jestli pro danou volbu nedojde k vyškrtnutí některých složek odpovídajících
    dosud nevyplněným pozicím z vektoru přípustných číslic (a tedy pro stávající volbu obsazení nevyplněných pozic úloha nemá řešení);
    pokud ano, je vybrána jiná číslice (která projde stejným kontrolním mechanizmem), pokud ne, vyhledáme nejdřív případné skryté singly,
    a pokud se tím příznivý případ nenaruší, je dané rozložení číslic spolu s vektorem přípustných číslic (zmenšeným o číslici aktuálně
    vybranou) zapsáno do alternativ (pro případ, že se daná volba nakonec stejně ukáže ve výsledku nevyhovující v některé z dalších
    iterací); jestliže se všechny přípustné číslice odpovídající dané pozici nakonec ukážou být nevyhovující, je z alternativ vyvolán
    poslední případ, kdy byla číslice pro některou z předchozích pozic vybrána z více možností a spolu s rozložením čísel a vektorem
    přípustných možností odpovídajících této předešlé situaci je vybrána kombinace parametrů pro další iteraci

    Parametry:
    - ar (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    - ptemp_size (int): počet pozic připouštějících alternativní kombinace parametrů pro případ, že se dostaneme do sporu
    - previous_temp (3D list): rozložení číslic odpovídající alternativám
    - previous_acceptable_values (3D list): přípustné číslice odpovídající alternativám
    - previous_temp (3D list): souřadnice pozic odpovídajících alternativám

    Výstup:
    - ptemp_size (int): aktualizovaný počet pozic připouštějících alternativní kombinace parametrů
    """
    newI = ListOfLists2[0][0]
    newJ = ListOfLists2[0][1]

    newQ = ListOfLists1[0][0]

    empty_values_count = len(ListOfLists1)
    new_acceptable_values = cp.deepcopy(ListOfLists1)
    new_index_order = cp.deepcopy(ListOfLists2)

    new_temp = cp.deepcopy(ar)
    new_temp[newI, newJ] = newQ

    adjust_acceptable_values(newQ, newI, newJ, new_acceptable_values, new_index_order)
    if len(new_acceptable_values) == empty_values_count - 1:
        find_hidden_singles(new_temp, new_acceptable_values, new_index_order)

    contradiction = False

    while len(new_acceptable_values) < empty_values_count-1 and not contradiction:

        TempList = cp.deepcopy(ListOfLists1[0])
        TempList.remove(newQ)
        ListOfLists1[0] = cp.deepcopy(TempList)

        if len(ListOfLists1[0]) > 0:
            newQ = ListOfLists1[0][0]

            new_acceptable_values = cp.deepcopy(ListOfLists1)
            new_index_order = cp.deepcopy(ListOfLists2)

            new_temp[newI, newJ] = newQ

            adjust_acceptable_values(newQ, newI, newJ, new_acceptable_values, new_index_order)
            if len(new_acceptable_values) == empty_values_count - 1:
                find_hidden_singles(new_temp, new_acceptable_values, new_index_order)

        else:

            ptemp_size -= 1
            new_acceptable_values = cp.deepcopy(previous_acceptable_values[ptemp_size])
            new_index_order = cp.deepcopy(previous_index_order[ptemp_size])

            previous_acceptable_values.pop()
            previous_index_order.pop()

            for i in range(maximal_value):
                for j in range(maximal_value):
                    ar[i, j] = previous_temp[ptemp_size][i][j]
                    previous_temp[ptemp_size][i][j] = 0

            contradiction = True

    if not contradiction:
        if len(ListOfLists1[0]) > 1:
            previous_list = cp.deepcopy(ListOfLists1)
            previous_list[0].remove(previous_list[0][0])
            previous_acceptable_values.append(previous_list)
            previous_index_order.append(cp.deepcopy(ListOfLists2))

            for i in range(maximal_value):
                for j in range(maximal_value):
                    previous_temp[ptemp_size][i][j] = ar[i, j]

            ptemp_size += 1

        ar[:] = cp.deepcopy(new_temp)

    ListOfLists1[:] = cp.deepcopy(new_acceptable_values)
    ListOfLists2[:] = cp.deepcopy(new_index_order)

    return ptemp_size

"""
hlavní blok: ze vstupních hodnot (zadaných ručně nebo z kódu) vytvoří z booleanovských funkcí na začátku kódu 2D-seznamy
acceptable_values a index_order obsahující výčet čísel, které mohou obsadit jednotlivé pozice, toto je ještě následně upraveno
hledáním skrytých singlů, čímž se výčet ještě o něco zjednoduší; po uspořádání spustím hlavní cyklus, který běží tak dlouho,
dokud není obsazena poslední pozice (v takovém případě dojde k vymazání veškerých hodnot z 2D-seznamu acceptable_values)
"""
manual_entry = input("Budete počáteční hodnoty zadávat  ručně (ano/ne)? ")

while manual_entry != "a" and manual_entry != "n" and manual_entry != "ano" and manual_entry != "ne":
    manual_entry = input()

print()

init = np.zeros((maximal_value, maximal_value))

if manual_entry == "a" or manual_entry == "ano":
    insert_initial_values(init)
else:
    '''
    print("Zadej pocatecni hodnoty:\n\n")

    for i in range(maximal_value):
        init[i,0]=input("  M("+str(i+1)+",1) = ", end = '  ')
        init[i,1]=input("  M("+str(i+1)+",2) = ", end = '  ')
        init[i,2]=input("  M("+str(i+1)+",3) = ", end = '  ')
        init[i,3]=input("  M("+str(i+1)+",4) = ", end = '  ')
        init[i,4]=input("  M("+str(i+1)+",5) = ", end = '  ')
        init[i,5]=input("  M("+str(i+1)+",6) = ", end = '  ')
        init[i,6]=input("  M("+str(i+1)+",7) = ", end = '  ')
        init[i,7]=input("  M("+str(i+1)+",8) = ", end = '  ')    
        init[i,8]=input("  M("+str(i+1)+",9) = ")
        print("\n\n")
    
    print("\n\n")
    '''
    #init=np.array(((3,0,0,8,0,9,0,0,7),(0,0,1,4,0,3,6,0,0),(0,5,0,1,2,6,0,3,0),(6,9,5,0,0,0,8,2,1),(0,0,7,0,0,0,9,0,0),(2,1,3,0,0,0,7,5,4),(0,4,0,2,3,5,0,7,0),(0,0,6,7,0,4,5,0,0),(5,0,0,6,0,1,0,0,9)))
    #init=np.array(((0,0,3,0,0,0,2,0,0),(0,0,0,4,0,2,0,0,0),(2,0,0,3,5,9,0,0,6),(0,3,7,0,0,0,4,2,0),(0,0,2,0,7,0,6,0,0),(0,1,8,0,0,0,3,5,0),(3,0,0,9,4,6,0,0,5),(0,0,0,7,0,8,0,0,0),(0,0,9,0,0,0,1,0,0)))
    #init=np.array(((0,0,0,1,0,4,0,0,0),(0,3,0,9,6,5,0,4,0),(0,0,8,0,0,0,6,0,0),(5,8,0,0,0,0,0,1,3),(0,7,0,0,0,0,0,6,0),(4,1,0,0,0,0,0,9,2),(0,0,7,0,0,0,4,0,0),(0,6,0,5,7,2,0,8,0),(0,0,0,8,0,3,0,0,0)))
    #init=np.array(((1,0,0,6,0,4,0,0,2),(0,0,0,0,5,0,0,0,0),(0,0,9,3,0,7,1,0,0),(7,0,1,0,0,0,2,0,6),(0,5,0,0,1,0,0,8,0),(8,0,2,0,0,0,4,0,3),(0,0,6,5,0,8,7,0,0),(0,0,0,0,6,0,0,0,0),(3,0,0,4,0,1,0,0,8)))
    #init=np.array(((3,6,4,8,5,9,2,1,7),(8,2,1,4,7,3,6,9,5),(7,5,9,1,2,6,4,3,8),(6,9,5,3,4,7,8,2,1),(0,0,7,0,0,0,9,0,0),(2,1,3,0,0,0,7,5,4),(0,4,0,2,3,5,0,7,0),(0,0,6,7,0,4,5,0,0),(5,0,0,6,0,1,0,0,9)))
    init=np.array(((0, 0, 0, 4, 0, 0, 0, 7, 1),(0, 8, 0, 0, 3, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0, 0, 0, 0),(5, 0, 0, 1, 0, 4, 0, 0, 0),(0, 0, 0, 6, 0, 0, 8, 0, 0), (0, 9, 0, 0, 0, 0, 0, 3, 0),(0, 0, 0, 0, 2, 0, 9, 0, 0),(7, 0, 4, 0, 0, 0, 0, 0, 0),(1, 0, 0, 0, 0, 0, 0, 0, 0)))

    #init=np.array(((1, 2, 0, 0),(0, 0, 1, 0),(2, 0, 0, 0),(0, 0, 0, 4)))

#počáteční podmínky uloženy - zapínáme časovač
start_process_time = time.process_time()

temp = cp.deepcopy(init)

index_order = []
acceptable_values = []

i = -1
j = maximal_value - 1

for index in range(maximal_value * maximal_value):
    acceptable_values_array = []
    j += 1
    if j == maximal_value:
        j = 0
        i += 1
    if temp[i, j] == 0:
        for value_index in range(maximal_value):
            q = value_index + 1
            if can_be_in_line(q, i, j, temp) * can_be_in_column(q, i, j, temp) * can_be_in_cell(q, i, j, temp):
                acceptable_values_array.append(q)
        acceptable_values.append(acceptable_values_array)
        index_order.append([i, j])

find_hidden_singles(temp, acceptable_values, index_order)

previous_acceptable_values = []
previous_index_order = []

previous_temp = []
previous_temp1 = []
previous_temp0 = []

for i in range(maximal_value):
    previous_temp0.append(0)
for j in range(maximal_value):
    previous_temp1.append(cp.deepcopy(previous_temp0))
for k in range(100):
    previous_temp.append(cp.deepcopy(previous_temp1))

bubblesort(acceptable_values, index_order)

iteration_order = 0
ptemp_size = 0

print("Průběh:")

while len(acceptable_values) > 0:
    iteration_order += 1
    print(f"  {iteration_order}.iterace")
    ptemp_size = main_iteration(temp, acceptable_values, index_order, ptemp_size, previous_temp, previous_acceptable_values, previous_index_order)

print()

print("Počáteční stav:\n")

for i in range(maximal_value):
    for j in range(maximal_value):
        print(int(init[i, j]), end=' ')
    print("\n")

print("Koncový stav:\n")

for i in range(maximal_value):
    for j in range(maximal_value):
        print(int(temp[i, j]), end=' ')
    print("\n")

end_process_time = time.process_time()

print("Celkový čas procesu:", end_process_time - start_process_time, "s")






























