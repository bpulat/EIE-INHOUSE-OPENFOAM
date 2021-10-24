import functions
import os
from os import system

# Window title
system("title " + "EIE-CFD Initializer")
# Clear the current cmd screen
def clear(): return os.system('cls')


clear()
# BEGINNING TEXT
functions.input_function()
# MAIN MENU
functions.main_menu()
