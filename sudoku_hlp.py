def insert_initial_values(initial_layout):
    """
    funkce pro zadání počátečních podmínek (za předpokladu, že nejsou zadány přímo v kódu)

    Parametry:
    - initial_layout (np.array): počáteční rozložení číslic
    """

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

def can_be_in_line(q, i, j, ar):
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

def interchange_vectors(a, b, ListOfLists):
    """
    prohození složek 2D-seznamů v rámci bubblesortu

    Parametry:
    - a (int): pořadové číslo první prohazované pozice
    - b (int): pořadové číslo druhé prohazované pozice
    - ListOfLists (2D list): uspořádávaný 2D-seznam
    """

def bubblesort(ListOfLists1, ListOfLists2):
    """
    algoritmus bubblesort - uspořádává složky (tvořené seznamy) daných 2D-seznamů podle velikosti (počtu prvků obsažených v jednotlivých složkách)

    Parametry:
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    """

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

def find_hidden_singles(temp, ListOfLists1, ListOfLists2):
    """
    další zefektivnění: pro účely zjednodušení na základě zjištěných přípustných číslic hledáme případné pozice, které jako jediné
    připouštějí umístění některých číslic v rámci daného řádku, sloupce nebo buňky (tzv. skrytý singl)

    Parametry:
    - temp (np.array): zkoumané rozložení číslic
    - ListOfLists1 (2D list): vektor přípustných čísel na jednotlivých pozicích
    - ListOfLists2 (2D list): souřadnice pozic ve vektoru přípustných čísel
    """

def main_iteration(ar, ListOfLists1, ListOfLists2, ptemp_size, previous_temp, previous_acceptable_values,
                   previous_index_order):
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

def main():
    """
    hlavní blok: ze vstupních hodnot (zadaných ručně nebo z kódu) vytvoří z booleanovských funkcí na začátku kódu 2D-seznamy
    acceptable_values a index_order obsahující výčet čísel, které mohou obsadit jednotlivé pozice, toto je ještě následně upraveno
    hledáním skrytých singlů, čímž se výčet ještě o něco zjednoduší; po uspořádání spustím hlavní cyklus, který běží tak dlouho,
    dokud není obsazena poslední pozice (v takovém případě dojde k vymazání veškerých hodnot z 2D-seznamu acceptable_values)
    """
