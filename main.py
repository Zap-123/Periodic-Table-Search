# Michael Audi
# Element Search
# Given a query, search up an element

import time
import math

# Element Data
elements = [
    [1, "H", "Hydrogen", 1.01, "-1", "Non-metal"],
    [2, "He", "Helium", 4.00, "~", "Noble Gas"],
    [3, "Li", "Lithium", 6.94, "+1", "Alkali Metal"],
    [4, "Be", "Beryllium", 9.01, "+2", "Alkaline Earth Metal"],
    [5, "B", "Boron", 10.81, "+3", "Metalloid"],
    [6, "C", "Carbon", 12.01, "±4", "Non-metal"],
    [7, "N", "Nitrogen", 14.01, "-3", "Non-metal"],
    [8, "O", "Oxygen", 16.00, "-2", "Non-metal"],
    [9, "F", "Fluorine", 19.00, "-1", "Halogen"],
    [10, "Ne", "Neon", 20.18, "~", "Noble Gas"],
    [11, "Na", "Sodium", 22.99, "+1", "Alkali Metal"],
    [12, "Mg", "Magnesium", 24.31, "+2", "Alkaline Earth Metal"],
    [13, "Al", "Aluminum", 26.98, "+3", "Metal"],
    [14, "Si", "Silicon", 28.09, "±4", "Metalloid"],
    [15, "P", "Phosphorus", 30.97, "-3", "Non-metal"],
    [16, "S", "Sulfur", 32.07, "-2", "Non-metal"],
    [17, "Cl", "Chlorine", 35.45, "-1", "Halogen"],
    [18, "Ar", "Argon", 39.95, "~", "Noble Gas"],
    [19, "K", "Potassium", 39.10, "+1", "Alkali Metal"],
    [20, "Ca", "Calcium", 40.08, "+2", "Alkaline Earth Metal"],
    [21, "Sc", "Scandium", 44.96, "~", "Transition Metal"],
    [22, "Ti", "Titanium", 47.87, "~", "Transition Metal"],
    [23, "V", "Vanadium", 50.94, "~", "Transition Metal"],
    [24, "Cr", "Chromium", 52.00, "~", "Transition Metal"],
    [25, "Mn", "Manganese", 54.94, "~", "Transition Metal"],
    [26, "Fe", "Iron", 55.85, "~", "Transition Metal"],
    [27, "Co", "Cobalt", 58.93, "~", "Transition Metal"],
    [28, "Ni", "Nickel", 58.69, "~", "Transition Metal"],
    [29, "Cu", "Copper", 63.55, "+1", "Transition Metal"],
    [30, "Zn", "Zinc", 65.38, "+2", "Transition Metal"],
    [31, "Ga", "Gallium", 69.72, "+3", "Metal"],
    [32, "Ge", "Germanium", 72.63, "±4", "Metalloid"],
    [33, "As", "Arsenic", 74.92, "-3", "Metalloid"],
    [34, "Se", "Selenium", 78.96, "-2", "Non-metal"],
    [35, "Br", "Bromine", 79.90, "-1", "Halogen"],
    [36, "Kr", "Krypton", 83.80, "~", "Noble Gas"],
    [37, "Rb", "Rubidium", 85.47, "+1", "Alkali Metal"],
    [38, "Sr", "Strontium", 87.62, "+2", "Alkaline Earth Metal"],
    [39, "Y", "Yttrium", 88.91, "~", "Transition Metal"],
    [40, "Zr", "Zirconium", 91.22, "~", "Transition Metal"],
    [41, "Nb", "Niobium", 92.91, "~", "Transition Metal"],
    [42, "Mo", "Molybdenum", 95.95, "~", "Transition Metal"],
    [43, "Tc", "Technetium", 98.00, "~", "Transition Metal"],
    [44, "Ru", "Ruthenium", 101.07, "~", "Transition Metal"],
    [45, "Rh", "Rhodium", 102.91, "~", "Transition Metal"],
    [46, "Pd", "Palladium", 106.42, "~", "Transition Metal"],
    [47, "Ag", "Silver", 107.87, "+1", "Transition Metal"],
    [48, "Cd", "Cadmium", 112.41, "+2", "Transition Metal"],
    [49, "In", "Indium", 114.82, "+3", "Metal"],
    [50, "Sn", "Tin", 118.71, "+2", "Metal"],
    [51, "Sb", "Antimony", 121.76, "+3", "Metalloid"],
    [52, "Te", "Tellurium", 127.60, "-2", "Metalloid"],
    [53, "I", "Iodine", 126.90, "-1", "Halogen"],
    [54, "Xe", "Xenon", 131.29, "~", "Noble Gas"],
    [55, "Cs", "Cesium", 132.91, "+1", "Alkali Metal"],
    [56, "Ba", "Barium", 137.33, "+2", "Alkaline Earth Metal"],
    [57, "La", "Lanthanum", 138.91, "~", "Lanthanides"],
    [58, "Ce", "Cerium", 140.12, "~", "Lanthanides"],
    [59, "Pr", "Praseodymium", 140.91, "~", "Lanthanides"],
    [60, "Nd", "Neodymium", 144.24, "~", "Lanthanides"],
    [61, "Pm", "Promethium", 145.00, "~", "Lanthanides"],
    [62, "Sm", "Samarium", 150.36, "~", "Lanthanides"],
    [63, "Eu", "Europium", 151.96, "~", "Lanthanides"],
    [64, "Gd", "Gadolinium", 157.25, "~", "Lanthanides"],
    [65, "Tb", "Terbium", 158.93, "~", "Lanthanides"],
    [66, "Dy", "Dysprosium", 162.50, "~", "Lanthanides"],
    [67, "Ho", "Holmium", 164.93, "~", "Lanthanides"],
    [68, "Er", "Erbium", 167.26, "~", "Lanthanides"],
    [69, "Tm", "Thulium", 168.93, "~", "Lanthanides"],
    [70, "Yb", "Ytterbium", 173.05, "~", "Lanthanides"],
    [71, "Lu", "Lutetium", 174.97, "~", "Lanthanides"],
    [72, "Hf", "Hafnium", 178.49, "~", "Transition Metal"],
    [73, "Ta", "Tantalum", 180.95, "~", "Transition Metal"],
    [74, "W", "Tungsten", 183.84, "~", "Transition Metal"],
    [75, "Re", "Rhenium", 186.21, "~", "Transition Metal"],
    [76, "Os", "Osmium", 190.23, "~", "Transition Metal"],
    [77, "Ir", "Iridium", 192.22, "~", "Transition Metal"],
    [78, "Pt", "Platinum", 195.08, "~", "Transition Metal"],
    [79, "Au", "Gold", 196.97, "+1", "Transition Metal"],
    [80, "Hg", "Mercury", 200.59, "+2", "Transition Metal"],
    [81, "Tl", "Thallium", 204.38, "+3", "Metal"],
    [82, "Pb", "Lead", 207.2, "+2", "Metal"],
    [83, "Bi", "Bismuth", 208.98, "+3", "Metal"],
    [84, "Po", "Polonium", 209.00, "+2", "Metalloid"],
    [85, "At", "Astatine", 210.00, "-1", "Halogen"],
    [86, "Rn", "Radon", 222.00, "~", "Noble Gas"],
    [87, "Fr", "Francium", 223.00, "+1", "Alkali Metal"],
    [88, "Ra", "Radium", 226.03, "+2", "Alkaline Earth Metal"],
    [89, "Ac", "Actinium", 227.03, "~", "Actinide"],
    [90, "Th", "Thorium", 232.04, "~", "Actinide"],
    [91, "Pa", "Protactinium", 231.04, "~", "Actinide"],
    [92, "U", "Uranium", 238.03, "~", "Actinide"],
    [93, "Np", "Neptunium", 237.00, "~", "Actinide"],
    [94, "Pu", "Plutonium", 244.06, "~", "Actinide"],
    [95, "Am", "Americium", 243.00, "~", "Actinide"],
    [96, "Cm", "Curium", 247.00, "~", "Actinide"],
    [97, "Bk", "Berkelium", 247.00, "~", "Actinide"],
    [98, "Cf", "Californium", 251.00, "~", "Actinide"],
    [99, "Es", "Einsteinium", 252.00, "~", "Actinide"],
    [100, "Fm", "Fermium", 257.00, "~", "Actinide"],
    [101, "Md", "Mendelevium", 258.00, "~", "Actinide"],
    [102, "No", "Nobelium", 259.00, "~", "Actinide"],
    [103, "Lr", "Lawrencium", 262.00, "~", "Actinide"],
    [104, "Rf", "Rutherfordium", 267.00, "~", "Transition Metal"],
    [105, "Db", "Dubnium", 270.00, "~", "Transition Metal"],
    [106, "Sg", "Seaborgium", 271.00, "~", "Transition Metal"],
    [107, "Bh", "Bohrium", 270.00, "~", "Transition Metal"],
    [108, "Hs", "Hassium", 277.00, "~", "Transition Metal"],
    [109, "Mt", "Meitnerium", 276.00, "~", "Transition Metal"],
    [110, "Ds", "Darmstadtium", 281.00, "~", "Transition Metal"],
    [111, "Rg", "Roentgenium", 280.00, "~", "Transition Metal"],
    [112, "Cn", "Copernicium", 285.00, "~", "Transition Metal"],
    [113, "Nh", "Nihonium", 284.00, "~", "Post-transition Metal"],
    [114, "Fl", "Flerovium", 289.00, "~", "Post-transition Metal"],
    [115, "Mc", "Moscovium", 288.00, "~", "Post-transition Metal"],
    [116, "Lv", "Livermorium", 293.00, "~", "Post-transition Metal"],
    [117, "Ts", "Tennessine", 294.00, "~", "Halogen"],
    [118, "Og", "Oganesson", 294.00, "~", "Noble Gas"]
]

# Fancy print of element stats
def print_result(query):
    print(f'''
{RED}{BOLD}Atomic Name:{RESET} {query[2]}
{RED}{BOLD}Atomic Symbol:{RESET} {query[1]}
{RED}{BOLD}Atomic Number:{RESET} {query[0]}
{RED}{BOLD}Atomic Mass:{RESET} {atomic_mass_round(query[3])}
{RED}{BOLD}Electron Configuration:{RESET} {electron_configuration(int(query[0]))}
{RED}{BOLD}Atom Charge:{RESET} {query[4]}
{RED}{BOLD}Element Type:{RESET} {query[5]}
''')

# Fancy print of element card
def print_card(element):
    atomic_name = element[2]
    atomic_symbol = element[1]
    atomic_number = element[0]
    atomic_mass = atomic_mass_round(element[3])
    
    if len(atomic_name) + 2 <= 7:
        card_width = 11
    else:
        
        card_width = len(atomic_name) + 2

    print("-" * (card_width + 2))
    print("|" + ' ' * card_width + '|')
    print("|" + ' ' * math.floor((card_width - len(str(atomic_number))) / 2) + str(atomic_number) + ' ' * math.ceil((card_width - len(str(atomic_number))) / 2) + '|')
    print("|" + ' ' * math.floor((card_width - len(atomic_symbol)) / 2) + str(atomic_symbol) + ' ' * math.ceil((card_width - len(atomic_symbol)) / 2) + '|')
    print("|" + ' ' * math.floor((card_width - len(atomic_name)) / 2) + str(atomic_name) + ' ' * math.ceil((card_width - len(atomic_name)) / 2) + '|')
    print("|" + ' ' * math.floor((card_width - len(str(atomic_mass))) / 2) + str(atomic_mass) + ' ' * math.ceil((card_width - len(str(atomic_mass))) / 2) + '|')
    print("|" + ' ' * card_width + '|')
    print("-" * (card_width + 2))

# When asking for atomic mass, if it has two 0's in decimal place (e.g. 4.00 or 16.00),
# it will return with one 0 (e.g. 4.0 or 16.0) which messes with query search
# Function simply adds a 0 if necessary
def atomic_mass_round(atomic_mass):
    atomic_mass_str = str(atomic_mass)
    # Checks if it is actually atomic mass
    if '.' in atomic_mass_str:
        # Splits whole from decimal
        whole, decimal = atomic_mass_str.split('.')
        # Fixes bug
        if len(decimal) == 1:
            return whole + '.' + decimal + '0'
        return atomic_mass_str
    else:
        return atomic_mass
    #return atomic_mass_str + '.00'

    
# Given atomic number, return electron configuration
def electron_configuration(atomic_number):
    # Dictionaries
    super_scripts = {0:"⁰", 1:"¹", 2:"²", 3:"³", 4:"⁴", 5:"⁵", 6:"⁶", 7:"⁷", 8:"⁸", 9:"⁹", 10:"¹⁰", 11:"¹¹", 12:"¹²", 13:"¹³", '14':"¹⁴"}
    subshells_electrons = {'s':2, 'p':6, 'd':10, 'f':'14'}
    order = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
    
    
    total = atomic_number
    final_string = ""
    current_shell = 1
    
    
    for subshell in order:
        # if no more electrons, break
        if total == 0:
            break
        # If it can fill an octet, fill it and deduct electrons placed from total
        elif total - int(subshells_electrons[subshell[1]]) >= 0:
            final_string = final_string + f"{subshell[0]}{subshell[1]}{super_scripts[subshells_electrons[subshell[1]]]}"
            total -= int(subshells_electrons[subshell[1]])
        # If it can fill some of octet, use up rest of electrons, break
        elif total - int(subshells_electrons[subshell[1]]) < 0:
            final_string = final_string + f"{subshell[0]}{subshell[1]}{super_scripts[total]}"
            break
            
    return final_string



# Given an element identifier (query) find the element
# e.g. input: 1 output [(element info), elapsed time]
def QueryResult(query):
    # Begins stopwatch
    start = time.time()
    
    # begin looping through elements
    i = 0   
    for element in elements:
        time.sleep(0.02)
        i += 1
        
        # Prints checkmark
        print(RESET + f"Checking {RED}{BOLD}[{element[1]}] {RESET}for {GREEN}[{query}]{RESET} ... {RED}{i}{RESET}/{GREEN}118 {RESET}elements checked.")
        
        for value in element:
            # if found value is equal to query, print the associated element and stop the stop watch
            if atomic_mass_round(str(value).lower()) == query.lower():
                print()
                end = time.time()
                
                return [element, round((end-start) * 100)/100] # second index simply rounds the stopwatch to two decimal places
    
    # if none found, stop stopwatch and return
    end = time.time()
    return [None, round((end-start) * 100)/100]



RED="\033[31m"
GREEN="\033[32m"
BOLD = "\33[1m"
RESET = "\033[0m"

print("Look up any element on the periodic table by entering their query!")
print("It can be their atomic number, mass, symbol, or name!")
print()

while not debug:
    get_query = input(RESET + "What query do you want to search for?: ")
    result = QueryResult(get_query)
    
    element = result[0]
    time_elapsed = result[1]
    
    # If element is found,
    if element != None:
        print(GREEN + f"Element found! {BOLD}{RED}[{element[1]}]" + RESET + f" (Elapsed time {time_elapsed}s)")
        print()
        time.sleep(1)
        print_result(element)
        print_card(element)
        print()
    else:
        print()
        print(RED + f"No element found for... {BOLD}[{get_query}]" + RESET + f" (Elapsed time {time_elapsed}s)")
        print()
