from __future__ import print_function

import numpy as np
import time

import copy as cp

start_time = time.time()   

imax = 9

previous_acceptable_values = []
previous_index_order = []

previous_temp = []
previous_temp1 = []
previous_temp0 = []
for i in range(imax):
    previous_temp0.append(0)
for j in range(imax):
    previous_temp1.append(cp.deepcopy(previous_temp0))
for k in range(100):
    previous_temp.append(cp.deepcopy(previous_temp1))

def test1(qa,ia,ja,ar):
    r=True
    for m in range(imax):
        if m == ja or ar[ia,m] == 0:
            continue
        if qa-ar[ia,m]==0:
            r=r*False
        else:
            r=r*True
    return r

def test2(qa,ia,ja,ar):
    r=True
    for m in range(imax):
        if m == ia or ar[m,ja] == 0:
            continue
        if qa-ar[m,ja]==0:
            r=r*False
        else:
            r=r*True
    return r

def test3(qa,ia,ja,ar):
    a=int(ia/3)
    b=int(ja/3)
    r=True
    for m in range(3):
        for n in range(3):
            if (3*a+m == ia and 3*b+n == ja) or ar[3*a+m,3*b+n] == 0:
                continue
            if qa-ar[3*a+m,3*b+n]==0:
                r=r*False
            else:
                r=r*True
    return r

def bubblesort(ListOfLists1bs,ListOfLists2bs):

    test = True
    i = 0
    while i < len(ListOfLists1bs) and test:
        test = False
        for j in range(len(ListOfLists1bs)-i-1):
            if len(ListOfLists1bs[j]) > len(ListOfLists1bs[j+1]):
                test = True
                PomList1bs = cp.deepcopy(ListOfLists1bs[j])
                ListOfLists1bs[j] = cp.deepcopy(ListOfLists1bs[j+1])
                ListOfLists1bs[j+1] = cp.deepcopy(PomList1bs)
                PomList2bs = cp.deepcopy(ListOfLists2bs[j])
                ListOfLists2bs[j] = cp.deepcopy(ListOfLists2bs[j+1])
                ListOfLists2bs[j+1] = cp.deepcopy(PomList2bs)
        i += 1

def adjust_acceptable_values(q, i, j, ListOfLists1, ListOfLists2):

    PomList1aav = []
    PomList2aav = []

    k = 0

    while k < len(ListOfLists1):

        TempListaav = []

        for l in range(1, len(ListOfLists1[k])):
            TempListaav.append(ListOfLists1[k][l])

        if q in TempListaav:

            condition1 = ListOfLists2[k][1] == i
            condition2 = ListOfLists2[k][2] == j
            condition3 = (ListOfLists2[k][1] / 3 == i / 3) and (ListOfLists2[k][2] / 3 == j / 3)

            if condition1 or condition2 or condition3:

                just_filled = condition1 and condition2
                TempListaav.remove(q)

                if len(TempListaav) > 0 and not just_filled:
                    TempListaav.insert(0, ListOfLists1[k][0])
                    PomList1aav.append(TempListaav)
                    PomList2aav.append(ListOfLists2[k])
            else:
                TempListaav.insert(0, ListOfLists1[k][0])
                PomList1aav.append(TempListaav)
                PomList2aav.append(ListOfLists2[k])
        else:
            TempListaav.insert(0, ListOfLists1[k][0])
            PomList1aav.append(TempListaav)
            PomList2aav.append(ListOfLists2[k])

        k += 1


    ListOfLists1[:] = cp.deepcopy(PomList1aav)
    ListOfLists2[:] = cp.deepcopy(PomList2aav)

    '''
    for coef in range(len(PomList1aav)):
        ListOfLists1[coef] = PomList1aav[coef]
        ListOfLists2[coef] = PomList2aav[coef]

    if (len(PomList1aav) < len(ListOfLists1)):
        length_diff = len(ListOfLists1) - len(PomList1aav)
        for coef in range(length_diff):
            ListOfLists1.pop(len(ListOfLists1) - 1)
            ListOfLists2.pop(len(ListOfLists1) - 1)
    '''

    bubblesort(ListOfLists1, ListOfLists2)

def main_iteration(ListOfLists1, ListOfLists2, ar, ptemp_size):

    newI = ListOfLists2[0][1]
    newJ = ListOfLists2[0][2]

    newQ = ListOfLists1[0][1]

    empty_values_count = len(ListOfLists1)
    new_acceptable_values = cp.deepcopy(ListOfLists1)
    new_index_order = cp.deepcopy(ListOfLists2)

    adjust_acceptable_values(newQ, newI, newJ, new_acceptable_values, new_index_order)

    contradiction = False

    while len(new_acceptable_values) < empty_values_count-1 and not contradiction:

        TempList = cp.deepcopy(ListOfLists1[0])
        TempList.remove(TempList[0])
        TempList.remove(newQ)
        TempList.insert(0, ListOfLists1[0][0])
        ListOfLists1[0] = cp.deepcopy(TempList)

        if len(ListOfLists1[0]) > 1:
            newQ = ListOfLists1[0][1]

            new_acceptable_values = cp.deepcopy(ListOfLists1)
            new_index_order = cp.deepcopy(ListOfLists2)

            adjust_acceptable_values(newQ, newI, newJ, new_acceptable_values, new_index_order)

        else:

            ptemp_size -= 1
            new_acceptable_values = cp.deepcopy(previous_acceptable_values[ptemp_size])
            new_index_order = cp.deepcopy(previous_index_order[ptemp_size])

            previous_acceptable_values.pop()
            previous_index_order.pop()

            for i in range(imax):
                for j in range(imax):
                    ar[i, j] = previous_temp[ptemp_size][i][j]
                    previous_temp[ptemp_size][i][j] = 0

            contradiction = True

    if not contradiction:
        if len(ListOfLists1[0]) > 2:
            previous_list = cp.deepcopy(ListOfLists1)
            previous_list[0].remove(previous_list[0][1])
            previous_acceptable_values.append(previous_list)
            previous_index_order.append(cp.deepcopy(ListOfLists2))

            for i in range(imax):
                for j in range(imax):
                    previous_temp[ptemp_size][i][j] = ar[i, j]

            ptemp_size += 1

        ar[newI, newJ] = newQ

    ListOfLists1[:] = cp.deepcopy(new_acceptable_values)
    ListOfLists2[:] = cp.deepcopy(new_index_order)

    return ptemp_size

init = np.zeros((imax,imax))

'''
print("Zadej pocatecni hodnoty:\n\n")

for i in range(imax):
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
init=np.array(((1,0,0,6,0,4,0,0,2),(0,0,0,0,5,0,0,0,0),(0,0,9,3,0,7,1,0,0),(7,0,1,0,0,0,2,0,6),(0,5,0,0,1,0,0,8,0),(8,0,2,0,0,0,4,0,3),(0,0,6,5,0,8,7,0,0),(0,0,0,0,6,0,0,0,0),(3,0,0,4,0,1,0,0,8)))
#init=np.array(((3,6,4,8,5,9,2,1,7),(8,2,1,4,7,3,6,9,5),(7,5,9,1,2,6,4,3,8),(6,9,5,3,4,7,8,2,1),(0,0,7,0,0,0,9,0,0),(2,1,3,0,0,0,7,5,4),(0,4,0,2,3,5,0,7,0),(0,0,6,7,0,4,5,0,0),(5,0,0,6,0,1,0,0,9)))
#init=np.array(((0, 0, 0, 4, 0, 0, 0, 7, 1),(0, 8, 0, 0, 3, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0, 0, 0, 0),(5, 0, 0, 1, 0, 4, 0, 0, 0),(0, 0, 0, 6, 0, 0, 8, 0, 0), (0, 9, 0, 0, 0, 0, 0, 3, 0),(0, 0, 0, 0, 2, 0, 9, 0, 0),(7, 0, 4, 0, 0, 0, 0, 0, 0),(1, 0, 0, 0, 0, 0, 0, 0, 0)))

temp = cp.deepcopy(init)

index_order = []
acceptable_values = []

i = -1
j = 8

for index in range(81):
    acceptable_values_array = []
    acceptable_values_array.append(index + 1)
    j += 1
    if j == 9:
        j = 0
        i += 1
    if temp[i, j] == 0:
        for value_index in range(9):
            q = value_index + 1
            if test1(q, i, j, temp) * test2(q, i, j, temp) * test3(q, i, j, temp):
                acceptable_values_array.append(q)
        acceptable_values.append(acceptable_values_array)
        index_order.append([index+1, i, j])

bubblesort(acceptable_values, index_order)

iteration_order = 0
ptemp_size = 0

while len(acceptable_values) > 0:
    iteration_order += 1
    print(f"  {iteration_order}.iterace")
    ptemp_size = main_iteration(acceptable_values, index_order, temp, ptemp_size)

print("Počáteční stav:\n")

for i in range(imax):
    print(init[i, 0], end=' ')
    print(init[i, 1], end=' ')
    print(init[i, 2], end=' ')
    print(init[i, 3], end=' ')
    print(init[i, 4], end=' ')
    print(init[i, 5], end=' ')
    print(init[i, 6], end=' ')
    print(init[i, 7], end=' ')
    print(init[i, 8], end=' ')
    print("\n")

print("Koncový stav:\n")

for i in range(imax):
    print(temp[i, 0], end=' ')
    print(temp[i, 1], end=' ')
    print(temp[i, 2], end=' ')
    print(temp[i, 3], end=' ')
    print(temp[i, 4], end=' ')
    print(temp[i, 5], end=' ')
    print(temp[i, 6], end=' ')
    print(temp[i, 7], end=' ')
    print(temp[i, 8], end=' ')
    print("\n")



































