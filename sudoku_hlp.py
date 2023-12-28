def insert_initial_values(initial_layout):
    """
    function for entry of initial conditions (assuming that they are not entered to code directly)

    Parameters:
    - initial_layout (np.array): initial layout of digits
    """

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

def can_be_in_line(q, i, j, ar):
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

def interchange_vectors(a, b, ListOfLists):
    """
    interchange of components of 2D-vectors within bubblesort algorithm

    Parameters:
    - a (int): order number of first interchanging position
    - b (int): order number of second interchanging position
    - ListOfLists (2D list): sorting 2D-list
    """

def bubblesort(ListOfLists1, ListOfLists2):
    """
    algorithm bubblesort - it orders components (created by lists) of given 2D-lists according to the size (number of digits included in particular components)

    Parameters:
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
    """

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

def find_hidden_singles(temp, ListOfLists1, ListOfLists2):
    """
    next improvement: for the purpose of simplification on the base of found acceptable digits we search possible positions which
    are the only admitting location of some digits within given line, column or cell (so-called hidden single)

    Parameters:
    - temp (np.array): investigated number layout
    - ListOfLists1 (2D list): list of acceptable digits at particular positions
    - ListOfLists2 (2D list): coordinates of positions in list of acceptable digits
    """

def main_iteration(ar, ListOfLists1, ListOfLists2, ptemp_size, previous_temp, previous_acceptable_values,
                   previous_index_order):
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

def main():
    """
    main block: from the initial values (entered manually or directly from code) it creates from boolean functions at the
    beginning of code the 2D-lists named acceptable_values and indices_order containing the list of digits which can occupy the
    particular positions, this will be afterwards adjusted by searching hidden singles, this will simplify the 2D-lists even more;
    after sorting, we execute the main cycle which is running unless the last position is occupied (in that case all values from the
    2D-list acceptable_values are erased)
    """
