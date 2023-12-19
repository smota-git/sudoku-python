from __future__ import print_function

import numpy as np
import time

import copy as cp

start_time = time.time()   

sqrt_of_max = 3
maximal_value = sqrt_of_max * sqrt_of_max

def search_position_index(i, j, ListOfLists2):
    k = 0
    while ListOfLists2[k][0] != i or ListOfLists2[k][1] != j:
        k += 1
    return k

def test1(qa, ia , ja, ar):
    for m in range(maximal_value):
        if m == ja or ar[ia, m] == 0:
            continue
        if qa == ar[ia, m]:
            return False
    return True

def test2(qa, ia, ja, ar):
    for m in range(maximal_value):
        if m == ia or ar[m, ja] == 0:
            continue
        if qa == ar[m, ja]:
            return False
    return True

def test3(qa, ia, ja, ar):
    a = int(ia/3)
    b = int(ja/3)
    for m in range(3):
        for n in range(3):
            if (3*a+m == ia and 3*b+n == ja) or ar[3*a+m, 3*b+n] == 0:
                continue
            if qa == ar[3*a+m,3*b+n]:
                return False
    return True

def count_in_line(q, i, j, temp, ListOfLists1, ListOfLists2):
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
    count = 0

    for m in range(maximal_value):
        if temp[m, j] != 0:
            continue
        position_index = search_position_index(m, j, ListOfLists2)
        for n in range(len(ListOfLists1[position_index])):
            if ListOfLists1[position_index][n] == q:
                count += 1

def count_in_cell(q, i, j, temp, ListOfLists1, ListOfLists2):
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
    ListOfLists_a = cp.deepcopy(ListOfLists[a])
    ListOfLists_b = cp.deepcopy(ListOfLists[b])

    ListOfLists[a][:] = ListOfLists_b
    ListOfLists[b][:] = ListOfLists_a

def bubblesort(ListOfLists1, ListOfLists2):
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
            condition3 = int(ListOfLists2[k][0] / 3) == int(i / 3) and int(ListOfLists2[k][1] / 3) == int(j / 3)

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

init = np.zeros((maximal_value,maximal_value))

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
            if test1(q, i, j, temp) * test2(q, i, j, temp) * test3(q, i, j, temp):
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

while len(acceptable_values) > 0:
    iteration_order += 1
    print(f"  {iteration_order}.iterace")
    ptemp_size = main_iteration(temp, acceptable_values, index_order, ptemp_size, previous_temp, previous_acceptable_values, previous_index_order)

print("Počáteční stav:\n")

for i in range(maximal_value):
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

for i in range(maximal_value):
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



































