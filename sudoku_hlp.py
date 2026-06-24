def insert_initial_values(initial_layout):
    """
    function for reading the initial Sudoku layout (assuming that it is not entered to code directly)

    Parameters:
    - initial_layout (np.array): initial layout of digits
    """

def search_position_index(i, j, ListOfLists2):
    """
    function for searching the index of a position with the specified coordinates in corresponding composite vector

    Parameters:
    - i (int): coordinates of line (from 0)
    - j (int): coordinates of column (from 0)
    - ListOfLists2 (2D list): list of coordinates of positions in ordered vector of  candidates
    
    Output:
    - k (int): order number of position in current ordering
    """

def can_be_in_row(q, i, j, ar):
    """
    test whether the specified digit can be placed at the given position with respect to the current ROW

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
    """

def can_be_in_column(q, i, j, ar):
    """
    test whether the specified digit can be placed at the given position with respect to the current COLUMN

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
    """

def can_be_in_subgrid(q, i, j, ar):
    """
    test whether the specified digit can be placed at the given position with respect to the current SUBGRID

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - ar (np.array): investigated layout of digits

    Output:
    - True or False
    """

def count_in_row(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    counts the positions in given ROW which can contain the specified digit

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates

    Output:
    - count (int): number of positions with given property
    """

def count_in_column(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    counts the positions in specified COLUMN which can contain the specified digit
    
    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates

    Output:
    - count (int): number of positions with given property
    """

def count_in_subgrid(q, i, j, temp, ListOfLists1, ListOfLists2):
    """
    counts the positions in specified SUBGRID which can contain the specified digit
    
    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates

    Output:
    - count (int): number of positions with given property
    """

def swap_vectors(a, b, ListOfLists):
    """
    swap components of 2D-vectors within bubble sort algorithm

    Parameters:
    - a (int): order number of first swapped position
    - b (int): order number of second swapped position
    - ListOfLists (2D list): sorting 2D-list
    """

def bubblesort(ListOfLists1, ListOfLists2):
    """
    bubble sort algorithm - it orders components (created by vectors) of given 2D-vectors according to the size (number of digits included in particular components)

    Parameters:
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates
    """

def adjust_acceptable_values(q, i, j, ListOfLists1, ListOfLists2):
    """
    during choice of digit for given position the corresponding number is erased here from list of candidates for all other
    positions located in the same row, column and subgrid; after that the components of corresponding 2D-lists whose size is eliminated
    are excluded

    Parameters:
    - q (int): investigated digit
    - i (int): coordinates of row (from 0)
    - j (int): coordinates of column (from 0)
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates
    """

def find_hidden_singles(temp, ListOfLists1, ListOfLists2):
    """
    next improvement: for the purpose of simplification on the base of found candidates we search possible positions which
    are the only admitting location of some digits within given row, column or subgrid (so-called hidden single)

    Parameters:
    - temp (np.array): investigated layout of digits
    - ListOfLists1 (2D list): list of candidates at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of candidates
    """

def main_iteration(ar, ListOfLists1, ListOfLists2, ptemp_size, previous_temp, previous_acceptable_values,
                   previous_index_order):
    """
    main iteration: for improvement of calculation, initially, the 2D-lists of candidates are ordered by size; next, the
    function chooses the digit for filling the actual position and controls if for given choice some components corresponding to
    not yet filled positions from the list of candidates are not erased (which means that for actual choice of occupation
    of yet unfilled positions the task has no solution); if yes, we choose another digit (which undergoes the same control mechanism),
    if no, we first find possible hidden singles and if this does not corrupt the favorable case, the given digit layout is together
    with list of candidates (reduced by currently selected digit) added to alternates (this serves for the case that given
    choice will not finally appear suitable in any of next iterations); if, finally, all candidates corresponding to given
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

def main():
    """
    main block: from the initial values (entered manually or directly from code) it creates from boolean functions at the
    beginning of code the 2D-lists named acceptable_values and indices_order containing the list of digits which can occupy the
    particular positions, this will be afterwards adjusted by searching hidden singles, this will simplify the 2D-lists even more;
    after sorting, we execute the main cycle which is running unless the last position is occupied (in that case all values from the
    2D-list acceptable_values are erased)
    """
