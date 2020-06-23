import global_variables
from datetime import datetime
import file_creator
import mesh_export
import os
from tkinter import filedialog
from tkinter import *
clear = lambda: os.system('cls') # lambda function to clear prompt


def linear_interpolator(input_value, array_compare, array_result):
    '''
    Basic linear interpolator to calculate the interpolation values
    '''
    position = 0
    for index in range (global_variables.array_length):
        if array_compare[position] < input_value:
            position = position + 1
    return ((input_value - array_compare[position - 1]) / (array_compare[position] - array_compare[position - 1])) * (
            array_result[position] - array_result[position - 1]) + array_result[position - 1]


def user_input(input_variable, variable_string, variable_dimension):
    '''
    User input function but the input can be 0 or bigger
    '''
    input_variable = 0
    while not global_variables.error:
        try:
            # Assign the input as float to the variable and return to the variable
            input_variable = float (input ("Enter your " + variable_string + " value" +
                                           " [" + variable_dimension + "]" + ": "))

            # Exit the loop if conditions are met
            if not global_variables.error and input_variable >= 0:
                break
        except ValueError:
            print ("Invalid Input!")
    return input_variable


def user_input_0(input_variable, variable_string, variable_dimension):

    '''
        User input function but the input should be bigger than 0
    '''
    input_variable = 0
    while not global_variables.error:
        try:
            # Assign the input as float to the variable and return to the variable
            input_variable = float (input ("Enter your " + variable_string + " value" +
                                           " [" + variable_dimension + "]" + ": "))
            if input_variable <= 0:
                print("Input can't be 0 or negative!")
            # Exit the loop if conditions are met
            if not global_variables.error and input_variable > 0:
                break
        except ValueError:
            print ("Invalid Input!")
    return input_variable


def input_function():
    clear()
    print ("\t\t##### WELCOME TO THE CFD INPUT CALCULATOR  #####\n\n" +
           "- This tool is used for calculating CFD inputs with dry air properties.\n" +
           "- Aim of this program is to find characteristics of Turbulent Flows!\n" +
           "- The software will run properly only on Windows Machines.\n\n" +
           "\t\t\t\t##### INPUTS #####\n")

    # GET THE USER INPUTS
    print("             ------------------                 -----------  \n"
		  "            |                  |               |           | \n"
		  "     Z      |       SIDE       |       Z       |   FRONT   | \n"
		  "     ^      |       VIEW       |       ^       |   VIEW    | \n"
		  "     |      |                  |       |       |           | \n"
		  "     ---> X  ------------------   Y <---        -----------  \n\n"
          " X is the flow direction\n"
          " Z is the domain height\n"
          " Y is the 3rd axis\n")
    # Velocity Input [m/s]
    global_variables.velocity_component_x = user_input(global_variables.velocity_component_x, \
                                                        "Velocity Component(X)", "m/s")
    global_variables.velocity_component_y = user_input(global_variables.velocity_component_y, \
                                                        "Velocity Component(Y)", "m/s")
    global_variables.velocity_component_z = user_input(global_variables.velocity_component_z, \
                                                        "Velocity Component(Z)", "m/s")
    global_variables.velocity = (global_variables.velocity_component_x**2 + \
                                global_variables.velocity_component_y**2 + \
                                global_variables.velocity_component_z**2)** 0.5
    # Domain X length [m]
    global_variables.domain_x = user_input_0 (global_variables.domain_x, \
                                            "Domain size dimension(X)", "m")
    # Domain Y length [m]
    global_variables.domain_y = user_input_0 (global_variables.domain_y, \
                                            "Domain size dimension(Y)", "m")
    # Domain Z length (downstream) [m]
    global_variables.domain_z = user_input_0 (global_variables.domain_z, \
                                            "Domain size dimension(Z)", "m")

    # Enter Altitude choice to automatically determine dry air properties or to do manual input of all air properties
    while not global_variables.error:
        try:
            print ("Altitude Input:\n" +
                   "If your case depends on the altitude \t(PRESS 1) \n" +
                   "If you have individual parameters \t(PRESS 2)")
            # Assign the input as int to the variable
            global_variables.altitude_choice = int (input ("Your choice: "))
            # Exit the loop if conditions are met
            if global_variables.altitude_choice == 1 or global_variables.altitude_choice == 2:
                break
            # Print the error message if conditions are not met
            if global_variables.altitude_choice != 1 or global_variables.altitude_choice != 2:
                print ("Invalid Choice!\n")
                continue
        except ValueError:
            print ("Invalid Input!\n")
    # Based on the selection above
    # Choice
    if global_variables.altitude_choice == 1:
        global_variables.altitude = user_input (global_variables.altitude, "altitude", "m")
        # Calculate the variables with linear interpolation from the tuples
        global_variables.density = linear_interpolator (global_variables.altitude, global_variables.Altitude,
                                                        global_variables.Density)
        global_variables.dynamic_viscosity = linear_interpolator (global_variables.altitude,
                                                                  global_variables.Altitude,
                                                                  global_variables.Dynamic_Viscosity)
        global_variables.pressure = linear_interpolator (global_variables.altitude, global_variables.Altitude,
                                                         global_variables.Pressure)
    if global_variables.altitude_choice == 2:
        global_variables.density = user_input_0 (global_variables.density, "Density", "kg/m^3")
        global_variables.dynamic_viscosity = user_input_0 (global_variables.dynamic_viscosity, "Dynamic Viscosity",
                                                         "Pa*s")
        global_variables.pressure = user_input_0 (global_variables.pressure, "Pressure", "kPa")

    # Enter Thermal choice to automatically (linear interpolation from the Tuples) determine dry air thermal properties
    # (Yes if 1 No if 2)
    while not global_variables.error:
        try:
            print ("Thermal Input:\n" +
                   "If your case depends on thermal properties \t\t(PRESS 1) \n" +
                   "If your case doesn't depend on the thermal properties \t(PRESS 2)")
            # Assign the input as int to the variable
            global_variables.thermal_choice = int (input ("Your choice: "))
            # Exit the loop if conditions are met
            if global_variables.thermal_choice == 1 or global_variables.thermal_choice == 2:
                break
            # Print the error message if conditions are not met
            if global_variables.thermal_choice != 1 or global_variables.thermal_choice != 2:
                print ("Invalid Choice!\n")
                continue
        except ValueError:
            print ("Invalid Input!\n")

    # Based on the selection above
    # Choice
    if global_variables.thermal_choice == 1:
        # In here we need to  correct the dimension by dividing with 100
        global_variables.temperature = user_input (global_variables.temperature, "Temperature", "Celsius")
        global_variables.thermal_conductivity = linear_interpolator (global_variables.temperature,
                                                                     global_variables.Temperature_C,
                                                                     global_variables.Thermal_conductivity_table) / 100
        # In here we also need to convert the input temperature to Kelvin and correct the dimension by multiplying
        # with 1000
        global_variables.temperature_kelvin = global_variables.temperature + 273.15
        global_variables.isobaric_specific_heat = linear_interpolator (global_variables.temperature_kelvin,
                                                                       global_variables.Temperature_K,
                                                                       global_variables.Dry_air_cp_table)
        # PRANDTL NUMBER [-]
        global_variables.prandtl = global_variables.isobaric_specific_heat * 1000 * global_variables.dynamic_viscosity / \
                                   global_variables.thermal_conductivity
    else:
        print("No Thermal condition selected !")
    # CALCULATIONS
    # KINEMATIC VISCOSITY
    global_variables.kinematic_viscosity = global_variables.dynamic_viscosity / global_variables.density

    # KINEMATIC VISCOSITY [m^2/s]
    kinematic_viscosity = global_variables.dynamic_viscosity / global_variables.density
    # HYDRAULIC DIAMETER [m]
    hydraulic_diameter = 2 * global_variables.domain_z * global_variables.domain_y / (
            global_variables.domain_z + global_variables.domain_y)
    # REYNOLDS
    global_variables.reynolds = global_variables.velocity * global_variables.density * hydraulic_diameter / \
                                global_variables.dynamic_viscosity
    # TURBULENCE LENGTH SCALE [m]
    reynolds_downstream = global_variables.velocity * global_variables.density * global_variables.domain_x / \
                          global_variables.dynamic_viscosity
    boundary_layer_thickness = 0.37 * global_variables.domain_x / pow (reynolds_downstream, 0.2)
    global_variables.turbulence_length_scale = 0.4 * boundary_layer_thickness
    global_variables.max_turbulence_length_scale = 0.07 * hydraulic_diameter
    # TURBULENCE INTENSITY [%]
    # The estimation here is that the flow is inside a tube
    global_variables.turbulence_intensity = 0.16 * pow (global_variables.reynolds, -0.125) * 100
    # TURBULENCE KINETIC ENERGY (k) [m^2/s^2]
    global_variables.turbulence_kinetic_energy = 1.5 * (
            global_variables.velocity * global_variables.turbulence_intensity / 100) ** 2
    # TURBULENCE DISSIPATION RATE (epsilon) [m^2/s^3]
    global_variables.turbulence_dissipation_rate = pow (global_variables.Cmu, 0.75) * \
                                                   pow (global_variables.turbulence_kinetic_energy, 1.5) \
                                                   / global_variables.turbulence_length_scale
    # TURBULENCE SPECIFIC DISSIPATION RATE (omega) [1/s]
    global_variables.turbulence_specific_dissipation_rate = pow (global_variables.turbulence_kinetic_energy, 0.5) / \
                                                            (global_variables.Cmu
                                                             * global_variables.turbulence_length_scale)


def permeability_calculator():
    '''
    Permability calculator based on Idelchik formulation for the thin perforated
    plates
    '''
    print ("\t\t Permeability Calculation\n")
    while not global_variables.error:
        try:
            global_variables.input_permeability = float (input ("Enter the open area in as a percentage [%]: "))
            global_variables.input_porous_thickness = float (input ("Enter the modeled porous domain thickness [m]: "))
            # To check if the input value is not lower than 0
            if global_variables.input_permeability <= 0 or global_variables.input_porous_thickness <= 0:
                print ("Permeability can't be lower than 0 or Porous thickness can't be 0 or lower")
            # Exit the loop if conditions are met
            if not global_variables.error and global_variables.input_permeability and \
                    global_variables.input_porous_thickness > 0:
                break
        except ValueError:
            print ("Invalid Input!")

    # Assign the input permeability
    f = global_variables.input_permeability / 100
    global_variables.permeability_resistance = (1 / pow (f, 2)) * pow ((0.707 * pow ((1 - f), 0.5) + 1 - f), 2) \
                                               / global_variables.input_porous_thickness
    print ("Permeability resistance: ", '{:.2f}'.format(global_variables.permeability_resistance))


def print_function():
    '''
    Function to print the calculated values to the console
    '''
    print ("\n\t\t#####PRINTED VALUES#####")
    # Print all the output variables by checking the input variables
    if global_variables.altitude_choice == 1:
        print (f"Density [kg/m^3]: {global_variables.density}")
        print (f"Dynamic Viscosity [Pa*s]: {global_variables.dynamic_viscosity:.2e}")
        print (f"Pressure [kPa]: {global_variables.pressure:.3f}")
    print (f"Kinematic Viscosity [m^2/s]: {global_variables.kinematic_viscosity:.2e}")
    print (f"Reynolds Number [-]: {global_variables.reynolds:.2e}")
    print (f"Turbulence Intensity [%]: {global_variables.turbulence_intensity:.3f}")
    print (f"Turbulence Length Scale [m]: {global_variables.turbulence_length_scale:.5f}")
    print (f"Max Turbulence Length Scale [m]: {global_variables.max_turbulence_length_scale:.2f}")
    print (f"Turbulence Kinetic Energy (k) [m^2/s^2]: {global_variables.turbulence_kinetic_energy:.3f}")
    print (f"Turbulence Dissipation Rate (epsilon) [m^2/s^3]: {global_variables.turbulence_dissipation_rate:.5f}")
    print (f"Turbulence Specific Dissipation Rate (omega) [1/s]: {global_variables.turbulence_specific_dissipation_rate:.5f}")
    # Control if the temperature input is selected or not
    if global_variables.thermal_choice == 1:
        print (f"Thermal Conductivity [W/(m.K)]: {global_variables.thermal_conductivity:.5f}")
        print (f"Prandtl number [-]: {global_variables.prandtl:.3f}")
        print (f"Isobaric specific heat [kJ/(kg.K)]: {global_variables.isobaric_specific_heat:.3f}")


def write_function():
    '''
    Write the files to a txt file
    '''
    # Get the date and time
    now = datetime.now ()
    today = now.strftime ("%d/%m/%Y %H:%M:%S")

    # tkinter opens a dialog box to save the file
    while True:
        try:
            root = Tk()
            root.update()
            root.withdraw()
            root.filename =  filedialog.asksaveasfilename(initialdir = global_variables.current_directory,title = "Save as",filetypes = (("txt files","*.txt"),("all files","*.*")))
            root.destroy()

            # control if the extension to not to overwrite .txt
            if root.filename[-4] + root.filename[-3] + root.filename[-2] + root.filename[-1] != ".txt":
                write_file_name = root.filename + ".txt"
            else:
                write_file_name = root.filename
            if root.filename == "":
                break
            # Create a file and overwrite if there is already an existing one
            f = open (write_file_name, "w")
            # Append to the created file above
            a = open (write_file_name, "a")

            f.write ("Inputs:\n"
                     "Velocity = " + str (global_variables.velocity) + " [m/s]\n"
                     "Domain size (X): " + str (global_variables.domain_x) + " [m]\n"
                     "Domain_size (Y): " + str (global_variables.domain_y) + " [m]\n"
                     "Domain_size (Z): " + str (global_variables.domain_z) + " [m]\n")
            if global_variables.altitude_choice == 1:
                a.write ("Altitude: " + str (global_variables.altitude) + " [m]\n")
            elif global_variables.altitude_choice == 2:
                a.write ("Density: " + str (global_variables.density) + " [kg/m^3]\n"
                         "Dynamic Viscosity: " + str (global_variables.dynamic_viscosity) + " [Pa*s]\n")
            if global_variables.thermal_choice == 1:
                a.write ("Temperature: " + str (global_variables.temperature) + " [Celsius]\n")
            elif global_variables.thermal_choice == 2:
                a.write ("No Thermal condition selected !\n")
            a.write ("\nOutputs:\n")
            if global_variables.altitude_choice == 1 and global_variables.thermal_choice == 1:
                a.write ("Density: " + str ('{:.3f}'.format (global_variables.density)) + " [kg/m^3]\n"
                         "Dynamic Viscosity: " + str ('{:.7f}'.format (global_variables.dynamic_viscosity)) + " [Pa*s]\n"
                         "Kinematic Viscosity: " + str ('{:.7f}'.format (global_variables.kinematic_viscosity)) + " [m^2/s]\n"
                         "Pressure: " + str ('{:.3f}'.format (global_variables.pressure)) + " [kPa]\n"
                         "Prandtl number: " + str ('{:.3f}'.format (global_variables.prandtl)) + " [-]\n"
                         "Thermal Conductivity: " + str ('{:.5f}'.format (global_variables.thermal_conductivity))
                         + " [W/(m.K)]\n"
                         "Isobaric specific heat: " + str ('{:.3f}'.format (global_variables.isobaric_specific_heat))
                         + " [kJ/(kg.K)]\n")
            if global_variables.altitude_choice == 1 and global_variables.thermal_choice == 2:
                a.write ("Density: " + str ('{:.3f}'.format (global_variables.density)) + " [kg/m^3]\n"
                         "Dynamic Viscosity: " + str ('{:.7f}'.format (global_variables.dynamic_viscosity)) + " [Pa*s]\n"
                         "Kinematic Viscosity: " + str ('{:.7f}'.format (global_variables.kinematic_viscosity)) + " [m^2/s]\n"
                         "Pressure: " + str ('{:.3f}'.format (global_variables.pressure)) + " [kPa]\n")

            if global_variables.altitude_choice == 2 and global_variables.thermal_choice == 1:
                a.write ("Pressure: " + str ('{:.3f}'.format (global_variables.pressure)) + " [kPa]\n"
                         "Thermal Conductivity: " + str ('{:.3f}'.format (global_variables.thermal_conductivity))
                         + " [W/(m*K)]\n"
                         "Specific heat constant (Cp): " + str ('{:.3f}'.format (global_variables.isobaric_specific_heat))
                         + " [J/(kg*K)]\n" + "Prandtl number: " + str ('{:.3f}'.format (global_variables.prandtl)) + " [-]\n")

            if global_variables.altitude_choice == 2 and global_variables.thermal_choice == 2:
                a.write ("Pressure: " + str ('{:.3f}'.format (global_variables.pressure)) + " [kPa]\n")
            a.write ("Reynolds Number: " + str ('{:.0f}'.format (global_variables.reynolds)) + " [-]\n"
                     "Turbulence Intensity: " + str ('{:.3f}'.format (global_variables.turbulence_intensity)) + " [%]\n"
                     "Turbulence Length Scale: " + str ('{:.5f}'.format (global_variables.turbulence_length_scale)) + " [m]\n"
                     f"Max Turbulence Length Scale: {global_variables.max_turbulence_length_scale:.1f} [%]\n"
                     "Turbulence Kinetic Energy (k): " + str ('{:.5f}'.format (global_variables.turbulence_kinetic_energy))
                     + " [m^2/s^2]\n"
                     "Turbulence Dissipation Rate (epsilon): "
                     + str ('{:.5f}'.format (global_variables.turbulence_dissipation_rate)) + " [m^2/s^3]\n"
                     "Turbulence Specific Dissipation Rate (omega): "
                     + str ('{:.3f}'.format (global_variables.turbulence_specific_dissipation_rate)) + " [1/s]\n")

            # Check if user selected the function
            if global_variables.input_yplus != 0:
                a.write ("\nWall Space Calculation\n"
                         "Input:\n"
                         "Desired y+ value: " + str (global_variables.input_yplus) + " [-]\n"
                         "Output:\n"
                         "Required First Layer Thickness: " + str ('{:.3f}'.format (global_variables.first_layer_thickness))
                         + " [m]\n")
            # Check if user selected the function
            if global_variables.input_permeability != 0 and global_variables.input_porous_thickness != 0:
                a.write ("\nPermeability Calculation\n"
                         "Input:\n"
                         "Desired Permeability: " + str (global_variables.input_permeability) + " [%]\n"
                         "Geometry Thickness: " + str (global_variables.input_porous_thickness) + " [m]\n"
                         "Output:\n"
                         "Resistance coefficient: " + str ('{:.3f}'.format (global_variables.permeability_resistance))
                         + " [1/m]\n")
            a.write("\nDate and Time: " + str(today))
            f.close()
            a.close()
            root.filename = ""  #clear the filename
            print("File Saved successfully")
            break
        except:
            print("There was a problem while saving the file")
            break


def wall_space_calculator():
    '''
    Calculation for the y+ value
    '''
    print ("\t\tWall Space Calculation\n")
    while not global_variables.error:
        try:
            global_variables.input_yplus = float (input ("Enter your desired y+ value: "))
            # To check if the input value is not lower than 0
            if global_variables.input_yplus <= 0:
                print ("Permeability can't be lower than 0")
            # Exit the loop if conditions are met
            if not global_variables.error and global_variables.input_yplus > 0:
                break
        except ValueError:
            print ("Invalid Input!")
    friction_coefficient = 0.059 / pow (global_variables.reynolds, 0.2)
    wall_shear = global_variables.density * friction_coefficient * pow (global_variables.velocity, 2) / 2
    frictional_velocity = (wall_shear / global_variables.density) ** 0.5
    global_variables.first_layer_thickness = global_variables.dynamic_viscosity * global_variables.input_yplus \
                                             / frictional_velocity / global_variables.density
    print ("First layer thickness[m]: ", '{:.5f}'.format(global_variables.first_layer_thickness))


def openfoam_model():
    '''
    Menu for the openfoam initiliaser and selections
    '''
    clear()
    # clearing the datas
    global_variables.wall_output = list()
    global_variables.inlet_output = list()
    global_variables.outlet_output = list()
    global_variables.symmetry_output = list()
    print("\t\tOpenfoam model initiliaser\n")
    # Selection between incompressible and compressible
    while True:
        try:
            print(  "\nIncompressible Fluid Flow\n"
                    "Simulate flow of a single fluid for which the maximum Mach number is \n"
                    "lower than 0.3 (100 m/s air speed at standard pressure).\n"
                    "In this regime fluid density variations usually are negligible \n"
                    "and the behavior of the fluid can be approximated as incompreesible\n"
                    "\nCompressible Fluid Flow\n"
                    "Simulate compressible fluid flow for which the maximum Mach number is \n"
                    "higher than 0.3 (100 m/s air speed at standard pressure). In this regime \n"
                    "fluid density variations have significant influence on the system and it is\n"
                    "important to model the compressibility of the fluid (gas or liquid)\n")
            # For the selection update the compressible later
            print(  "Analysis:\n" +
                    "Incompressible \t(PRESS 1) \n")# +
                    #"Compressible \t(PRESS 2)")
            # Assign the input as int to a global variable
            global_variables.analysis_model = int(input("Your choice: "))
            # Exit the loop if conditions are met
            if global_variables.analysis_model == 1 or global_variables.analysis_model == 2:
                break
            # Print the error message if conditions are not met
            if global_variables.analysis_model != 1 or global_variables.analysis_model != 2:
                print ("Invalid Choice!\n")
                continue
        except ValueError:
            print ("Invalid Input!\n")

    if global_variables.analysis_model == 1:
        while True:
            try:
                print ("Turbulence Model:\n" +
                       "realizableKE \t(PRESS 1) \n" +
                       "kOmegaSST \t(PRESS 2)")
                # Assign the input as int to the variable
                global_variables.incompressible_ras_turbulence_model = int(input ("Your choice: "))
                # Exit the loop if conditions are met
                if global_variables.incompressible_ras_turbulence_model == 1 or global_variables.incompressible_ras_turbulence_model == 2:
                    break
                # Print the error message if conditions are not met
                if global_variables.incompressible_ras_turbulence_model != 1 or global_variables.incompressible_ras_turbulence_model != 2:
                    print ("Invalid Choice!\n")
                    continue
            except ValueError:
                print ("Invalid Input!\n")
    if global_variables.incompressible_ras_turbulence_model == 1:
        global_variables.incompressible_ras_turbulence_model_name == "realizableKE"
    elif global_variables.incompressible_ras_turbulence_model == 2:
        global_variables.incompressible_ras_turbulence_model_name == "kOmegaSST"
    # Selection for Time Dependency
    while True:
        try:
            print ("Time dependency:\n" +
                   "Steady-state \t(PRESS 1) \n")# +
                   #"Transient \t(PRESS 2)")
            # Assign the input as int to the variable
            global_variables.time_dependency = int(input ("Your choice: "))
            # Exit the loop if conditions are met
            if global_variables.time_dependency == 1 or global_variables.time_dependency == 2:
                break
            # Print the error message if conditions are not met
            if global_variables.time_dependency != 1 or global_variables.time_dependency != 2:
                print ("Invalid Choice!\n")
                continue
        except ValueError:
            print ("Invalid Input!\n")
    if global_variables.time_dependency == 1 and global_variables.analysis_model == 1:
        global_variables.solution_algorithm == "SIMPLE"

    if mesh_export.select_mesh() == 0:
        return 0
    print("Exporting boundary conditions...")
    mesh_export.bc_reader("wall",global_variables.wall_output) # export wall conditions
    mesh_export.bc_reader("velocity-inlet",global_variables.inlet_output) # export inlet conditions
    mesh_export.bc_reader("pressure-outlet",global_variables.outlet_output) # export outlet conditions
    mesh_export.bc_reader("symmetry",global_variables.symmetry_output) # export symmetry conditions
    file_creator.create_working_directory(R"\openfoam_inputs") # create the openfoam input directory
    file_creator.create_working_directory(R"\openfoam_inputs\0") # create the 0 directory
    file_creator.write_0_files() # create 0 files
    # file_creator.create_working_directory(R"\openfoam_inputs\system") #create the system directory
    # file_creator.write_system_files()
    # file_creator.create_working_directory(R"\openfoam_inputs\constant") #create the constant directory
    # file_creator.write_constant_files()



def main_menu():
    '''
    Main menu selection with main loop
    '''
    clear()
    while True:
        print ("\n\t\t ##### OUTPUT SELECTION #####\n"
               "1. To print calculated values\n"
               "2. Wall Space Calculator\n"
               "3. Permeability Calculator\n"
               "4. Write everything in a .txt file\n"
               "5. To change inputs\n"
               "6. Create openfoam files\n"
               "7. Quit\n")
        menu_input = input ("Choice: ")
        if menu_input == "1":
            print_function ()
        if menu_input == "2":
            wall_space_calculator ()
        if menu_input == "3":
            permeability_calculator ()
        if menu_input == "4":
            write_function ()
        if menu_input == "5":
            input_function ()
        if menu_input == "6":
            openfoam_model()
        if menu_input == "7":
            print ("You have chosen Quit, Goodbye\n")
            break
