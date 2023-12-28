import numpy as np
import time

import copy as cp

#determination of size of table (not necessarily only 9x9, but also 4x4, 16x16, 25x25 etc. - always second power of any number)
sqrt_of_max = 3
maximal_value = sqrt_of_max * sqrt_of_max

def insert_initial_values(initial_layout):
    """
    function for entry of initial conditions (assuming that they are not entered to code directly)

    Parameters:
    - initial_layout (np.array): initial layout of digits
    """
    print("Enter initial values:\n")

    for i in range(maximal_value):
        print(f"  i = {i}:\n")
        feedback = input('    Will you enter for concrete values of "j" (yes/no)? ')
        while feedback != "y" and feedback != "n" and feedback != "yes" and feedback != "no":
            feedback = input()
        if feedback == "y" or feedback == "yes":
            print('    "j" should be in interval <0,8>, choice of another value causes cancellation of this line (corresponding to given "i")\n')
            while True:
                j = int(input("    j = "))
                if j < 0 or j > maximal_value - 1:
                    break
                initial_layout[i, j] = input(f"    M({i},{j}) = ")
                while True:
                    if abs(initial_layout[i, j] - 5) <= 4:
                        break
                    initial_layout[i, j] = input()
                print()
            print()
        else:
            print()

def search_position_index(i, j, ListOfLists2):
    """
    function for searching of order number of position with given coordinates of position in corresponding composite vector

    Parameters:
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ListOfLists2 (2D list): list of coordinates of positions in ordered vector of acceptable digits

    Output:
    - k (int): order number of position in current ordering
    """
    k = 0
    while ListOfLists2[k][0] != i or ListOfLists2[k][1] != j:
        k += 1
    return k

def can_be_in_line(q, i , j, ar):
    """
    test if regarding the digits ordering in given LINE the given position can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
    """
    for m in range(maximal_value):
        if m == j or ar[i, m] == 0:
            continue
        if q == ar[i, m]:
            return False
    return True

def can_be_in_column(q, i, j, ar):
    """
    test if regarding the digits ordering in given COLUMN the given position can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
    """
    for m in range(maximal_value):
        if m == i or ar[m, j] == 0:
            continue
        if q == ar[m, j]:
            return False
    return True

def can_be_in_cell(q, i, j, ar):
    """
    test if regarding the digits ordering in given CELL the given position can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
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
    counting of number of positions in given LINE which can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits

    Output:
    - count (int): number of positions with given property
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
    counting of number of positions in given COLUMN which can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits

    Output:
    - count (int): number of positions with given property
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
    counting of number of positions in given CELL which can include a concrete digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits

    Output:
    - count (int): number of positions with given property
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
    interchange of components of 2D-vectors within bubblesort algorithm

    Parameters:
    - a (int): order number of first interchanging position
    - b (int): order number of second interchanging position
    - ListOfLists (2D list): sorting 2D-list
    """
    ListOfLists_a = cp.deepcopy(ListOfLists[a])
    ListOfLists_b = cp.deepcopy(ListOfLists[b])

    ListOfLists[a][:] = ListOfLists_b
    ListOfLists[b][:] = ListOfLists_a

def bubblesort(ListOfLists1, ListOfLists2):
    """
    algorithm bubblesort - it orders components (created by lists) of given 2D-lists according to the size (number of digits included in particular components)

    Parameters:
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
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
    during choice of digit for given position the corresponding number is erased here from list of acceptable digits for all other
    positions located in the same line, column and cell; after that the components of corresponding 2D-lists whose size is eliminated
    are excluded

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
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
    next improvement: for the purpose of simplification on the base of found acceptable digits we search possible positions which
    are the only admitting location of some digits within given line, column or cell (so-called hidden single)

    Parameters:
    - temp (np.array): investigated number layout
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
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
    main iteration: for improvement of calculation, initially, the 2D-lists of acceptable digits are ordered by size; next, the
    function chooses the digit for filling the actual position and controls if for given choice some components corresponding to
    not yet filled positions from the list of acceptable digits are not erased (which means that for actual choice of occupation
    of yet unfilled positions the task has no solution); if yes, we choose another digit (which undergoes the same control mechanism),
    if no, we first find possible hidden singles and if this does not corrupt the favorable case, the given digit layout is together
    with list of acceptable digits (reduced by currently selected digit) added to alternates (this serves for the case that given
    choice will not finally appear suitable in any of next iterations); if, finally, all acceptable digits corresponding to given
    position will not appear suitable we choose from alternates the last case when the digit was for any of the previous positions
    chosen from more possibilities and we choose the combination of parameters for next iteration together with layout of digits and
    list of acceptable possibilities corresponding to this previous situation

    Parameters:
    - ar (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
    - ptemp_size (int): number of positions admitting alternating combinations of parameters for the case when we achieve the contradiction
    - previous_temp (3D list): layouts of digits corresponding to alternates
    - previous_acceptable_values (3D list): acceptable digits corresponding to alternates
    - previous_temp (3D list): coordinates to positions corresponding to alternates

    Output:
    - ptemp_size (int): actualized number of positions admitting alternating combinations of parameters
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
main block: from the initial values (entered manually or directly from code) it creates from boolean functions at the
beginning of code the 2D-lists named acceptable_values and indices_order containing the list of digits which can occupy the
particular positions, this will be afterwards adjusted by searching hidden singles, this will simplify the 2D-lists even more;
after sorting, we execute the main cycle which is running unless the last position is occupied (in that case all values from the
2D-list acceptable_values are erased)
"""
manual_entry = input("Will you enter the initial values manually (yes/no)? ")

while manual_entry != "y" and manual_entry != "n" and manual_entry != "yes" and manual_entry != "no":
    manual_entry = input()

print()

init = np.zeros((maximal_value, maximal_value))

if manual_entry == "y" or manual_entry == "yes":
    insert_initial_values(init)
else:
    '''
    print("Insert initial values:\n\n")

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

#initial conditions entered - we switch the timer
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

print("Progress:")

while len(acceptable_values) > 0:
    iteration_order += 1
    print(f"  {iteration_order}.iteration")
    ptemp_size = main_iteration(temp, acceptable_values, index_order, ptemp_size, previous_temp, previous_acceptable_values, previous_index_order)

print()

print("Initial state:\n")

for i in range(maximal_value):
    for j in range(maximal_value):
        print(int(init[i, j]), end=' ')
    print("\n")

print("Final state:\n")

for i in range(maximal_value):
    for j in range(maximal_value):
        print(int(temp[i, j]), end=' ')
    print("\n")

end_process_time = time.process_time()

print("Total processing time:", end_process_time - start_process_time, "s")






























