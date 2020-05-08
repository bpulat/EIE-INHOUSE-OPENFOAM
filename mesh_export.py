import os
import time
import numpy as np
from tkinter import filedialog
from tkinter import *
import global_variables

# assign the mesh input as a global variable to be able to use in another function


def select_mesh():
	# read the boundary conditions from the .msh file
	# tkinter opens a dialog box to select the .msh file
	root = Tk()
	root.update()
	root.withdraw()
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select the mesh file",filetypes = (("msh files","*.msh"),("all files","*.*")))
	root.destroy()
	print("Importing Mesh variables...")
	try:
		with open(root.filename, "r", errors='ignore') as f:
			global_variables.contents = f.readlines()
		print("Mesh imported successfully")
	except:
		print("There was a problem while importing .msh file")


def bc_reader(parser_name_bc, output_boundaries = list()):

	# Variables definition
	all_variables = list()
	parser_name = "(45"
	input_boundaries = list()


	for i in range(len(global_variables.contents)):
		cd = global_variables.contents[i].rfind(parser_name)
		if cd != -1:
			all_variables.append(global_variables.contents[i])

	for i in range(len(all_variables)):
		control1 = all_variables[i].rfind(parser_name_bc)
		if control1 != -1 :
			input_boundaries.append(all_variables[i])

	for i in range(len(input_boundaries)):
		input_boundaries[i] = input_boundaries[i].split(" ")
	try:
		arr = np.array(input_boundaries)
		array_size = arr.shape
		arr_row = array_size[0]
		arr_column = array_size[1]
	except:
		print("No boundary condition named", parser_name_bc)


	for i in range(arr_row):
		for j in range(arr_column):
			control = input_boundaries[i][j].rfind(parser_name_bc)
			if control != -1:
				output_boundaries.append(input_boundaries[i][j+1])
				break

	for i in range(len(output_boundaries)):
		output_boundaries[i] = output_boundaries[i].rstrip("\n()")
	print("Exported " + parser_name_bc + " successfully")
	return output_boundaries


#print("--- %s seconds ---" % (time.time() - start_time))
