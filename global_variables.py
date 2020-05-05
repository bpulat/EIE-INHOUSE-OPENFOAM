# This file is for all the global variables
# All Tuple properties are for dry air

Altitude = (0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800,
            2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600,
            3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400,
            5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 8000,
            9000, 10000, 12000, 14000, 16000, 18000)

Pressure = (101.33, 98.95, 96.61, 94.32, 92.08, 89.88, 87.72, 85.6,
            83.53, 81.49, 79.5, 77.55, 75.63, 73.76, 71.92, 70.12,
            68.36, 66.63, 64.94, 63.28, 61.66, 60.07, 58.52, 57, 55.51,
            54.05, 52.62, 51.23, 49.86, 48.52, 47.22, 45.94, 44.69, 43.47,
            42.27, 41.11, 35.65, 30.8, 26.5, 19.4, 14.17, 10.53, 7.57)

Density = (1.225, 1.202, 1.179, 1.156, 1.134, 1.112, 1.090, 1.069, 1.048, 1.027, 1.007,
           0.987, 0.967, 0.947, 0.928, 0.909, 0.891, 0.872, 0.854, 0.837, 0.819, 0.802,
           0.785, 0.769, 0.752, 0.736, 0.721, 0.705, 0.690, 0.675, 0.660, 0.646, 0.631,
           0.617, 0.604, 0.59, 0.526, 0.467, 0.414, 0.312, 0.228, 0.166, 0.122)

Dynamic_Viscosity = (1.789 * 0.00001, 1.783 * 0.00001, 1.777 * 0.00001,
                     1.771 * 0.00001, 1.764 * 0.00001, 1.758 * 0.00001, 1.752 * 0.00001, 1.745 * 0.00001,
                     1.739 * 0.00001, 1.732 * 0.00001, 1.726 * 0.00001, 1.720 * 0.00001, 1.713 * 0.00001,
                     1.707 * 0.00001, 1.700 * 0.00001, 1.694 * 0.00001, 1.687 * 0.00001, 1.681 * 0.00001,
                     1.674 * 0.00001, 1.668 * 0.00001, 1.661 * 0.00001, 1.655 * 0.00001, 1.648 * 0.00001,
                     1.642 * 0.00001, 1.635 * 0.00001, 1.628 * 0.00001, 1.622 * 0.00001, 1.615 * 0.00001,
                     1.608 * 0.00001, 1.602 * 0.00001, 1.595 * 0.00001, 1.588 * 0.00001, 1.582 * 0.00001,
                     1.575 * 0.00001, 1.568 * 0.00001, 1.561 * 0.00001, 1.527 * 0.00001, 1.493 * 0.00001,
                     1.458 * 0.00001, 1.422 * 0.00001, 1.422 * 0.00001, 1.422 * 0.00001, 1.422 * 0.00001)
# Table for Dry air isobaric specific heat
Temperature_K = (60, 78.79, 81.61, 100, 120, 140, 160, 180, 200, 220, 240, 260, 273.2, 280, 288.7, 300, 320, 340, 360,
                 380, 400, 500, 600, 700, 800, 900, 1100, 1500, 1900)
# Table for Thermal conductivity
Temperature_C = (-190, -150, -100, -75, -50, -25, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100, 125, 150,
                 175, 200, 225, 300, 412, 500, 600, 700, 800, 900, 1000, 1100)

Dry_air_cp_table = (1.901, 1.933, 1.089, 1.04, 1.022, 1.014, 1.011, 1.008, 1.007, 1.006, 1.006, 1.006, 1.006, 1.006,
                    1.006, 1.006, 1.007, 1.009, 1.01, 1.012, 1.014, 1.03, 1.051, 1.075, 1.099, 1.121, 1.159, 1.21,
                    1.241)


Thermal_conductivity_table = (0.782, 1.169, 1.62, 1.834, 2.041, 2.241, 2.32, 2.359, 2.397, 2.436, 2.474, 2.512, 2.55,
                              2.587, 2.624, 2.662, 2.735, 2.808, 2.88, 3.023, 3.162, 3.333, 3.5, 3.664, 3.825, 3.983,
                              4.441, 5.092, 5.579, 6.114, 6.632, 7.135, 7.626, 8.108, 8.583)
# Total number of elements in the tuples
array_length = len (Altitude)

# An empirical constant specified in the turbulence model (the value is approximation)
Cmu = 0.09

# Basic input control value
error = False

# Initial values
velocity_component_x = 0
velocity_component_y = 0
velocity_component_z = 0
velocity = 0
domain_x = 0
domain_y = 0
domain_z = 0
altitude = 0
altitude_choice = 0
density = 0
dynamic_viscosity = 0
kinematic_viscosity = 0
pressure = 0
thermal_choice = 0
temperature = 0
thermal_conductivity = 0
isobaric_specific_heat = 0
reynolds = 0
turbulence_intensity = 0
turbulence_length_scale = 0
turbulence_kinetic_energy = 0
turbulence_dissipation_rate = 0
turbulence_specific_dissipation_rate = 0
prandtl = 0
temperature_kelvin = 0
input_yplus = 0
first_layer_thickness = 0
input_permeability = 0
input_porous_thickness = 0
permeability_resistance = 0
incompressible_ras_turbulence_model = 0
incompressible_ras_turbulence_model_name = ""
analysis_model = 0
time_dependency = 0
solution_algorithm = ""
# reading mesh propeties
wall_output = list()
inlet_output = list()
outlet_output = list()
symmetry_output = list()
# mesh input
contents = list()
