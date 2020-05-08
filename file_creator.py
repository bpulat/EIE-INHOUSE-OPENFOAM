import os
import time
import mesh_export
import global_variables
import fvSchemes
import fvSolution
import controldict
import decomposer
import porosityProp
import turbulence_prop
import transportproperties
# Get the current directory and create the input folder
def create_working_directory(directory_name):
	global openfoam_inputs
	file_location = os.getcwd ()
	openfoam_inputs = file_location + directory_name
	try:
		os.mkdir(openfoam_inputs)
	except OSError:
		print("Creation of the directory %s failed" % openfoam_inputs)
		print("Check if the directory was already created !")
	else:
		print("Successfully created the directory %s " % openfoam_inputs)
	# Create the working directory


class Incompressible:
	def __init__(self, file_type, dimension_output, format_type, wall_type, inlet_type):
		self.file_type = file_type
		self.dimension_output = dimension_output
		self.format_type = format_type
		self.wall_type = wall_type
		self.inlet_type = inlet_type


	def file_0_creator(self):
	# R is used to assign escape character \
	# f is used to assign file_type in the string
		file_name = Rf"\{self.file_type}"
		file_location = openfoam_inputs + file_name

		def inner_velocity_creator(input_bc, output_inlet):
			if self.file_type == "p":
				for i in range(len(input_bc)):
					output_inlet.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.inlet_type};\n"
					"\t}\n")
			else:
				for i in range(len(input_bc)):
					output_inlet.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.inlet_type};\n"
					"\t\tvalue\t\t\t$internalField\n"
					"\t}\n")
		def inner_pressure_creator(input_bc, output_bc):
			for i in range(len(input_bc)):
				output_bc.append(f"\t{input_bc[i]}\n"
				"\t{\n"
				"\t\ttype\t\t\tinletOutlet;\n"
				"\t\tinletValue\t\tuniform (0 0 0);\n"
				"\t\tvalue\t\t\t$internalField;\n"
				"\t}\n")
		def inner_wall_creator(input_bc, output_bc):
			if self.file_type == "U":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t}\n")
			elif self.file_type == "epsilon":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t\tvalue\t\t\t$internalField;\n"
					"\t}\n")
			elif self.file_type == "omega":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t\tvalue\t\t\t$internalField;\n"
					"\t}\n")
			elif self.file_type == "k":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t\tvalue\t\t\t$internalField;\n"
					"\t}\n")
			elif self.file_type == "nut":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t\tvalue\t\t\t$internalField;\n"
					"\t}\n")
			elif self.file_type == "p":
				for i in range(len(input_bc)):
					output_bc.append(f"\t{input_bc[i]}\n"
					"\t{\n"
					f"\t\ttype\t\t\t{self.wall_type};\n"
					"\t}\n")
		def inner_symmetry_creator(input_bc, output_bc):
			for i in range(len(input_bc)):
				output_bc.append(f"\t{input_bc[i]}\n"
				"\t{\n"
				"\t\ttype\t\t\tsymmetry;\n"
				"\t}\n")

		#define-the outputs
		output_inlet = list()
		output_outlet = list()
		output_wall = list()
		output_symmetry = list()
		inner_velocity_creator(global_variables.inlet_output, output_inlet)
		inner_pressure_creator(global_variables.outlet_output, output_outlet)
		inner_wall_creator(global_variables.wall_output, output_wall)
		inner_symmetry_creator(global_variables.symmetry_output, output_symmetry)
		# Create a file and overwrite if there is already an existing one
		f = open (file_location,"w")
	    # Append to the created file above
		a = open (file_location,"a")
		f.write("/*--------------------------------*- C++ -*----------------------------------*\\\n"
				"  =========       \n"
				"  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox\n"
				"   \\\\    /   O peration     | Website:  https://openfoam.org\n"
				"    \\\\  /    A nd           | Version:  6\n"
				"     \\\\/     M anipulation  |""\n"
				"\\*---------------------------------------------------------------------------*/"
				"\n"
				"FoamFile\n"
				"{\n"
				"    version     2.0;\n"
				f"    format      {self.format_type};\n"
				"    class       volVectorField;\n"
				"    location    \"0\";\n"
				f"    object      {self.file_type};\n"
				"}\n"
				"// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n"
				"\n"
				f"dimensions      {self.dimension_output};\n\n"
				"internalField   uniform (0 0 0);\n"
				"\n"
				"boundaryField\n"
				"{\n")
		for i in range(len(output_inlet)):
			a.write(f"{output_inlet[i]}\n")
		for i in range(len(output_outlet)):
			a.write(f"{output_outlet[i]}\n")
		for i in range(len(output_wall)):
			a.write(f"{output_wall[i]}\n")
		for i in range(len(output_symmetry)):
			a.write(f"{output_symmetry[i]}\n")

		a.write("}")
		f.close()
		a.close()


def write_0_files():
		# assign the properties
	if global_variables.incompressible_ras_turbulence_model == 1:
		turbulence_prop = Incompressible("epsilon", "[0 2 -3 0 0 0 0]", "binary", "epsilonWallFunction", "turbulentMixingLengthDissipationRateInlet")
	if global_variables.incompressible_ras_turbulence_model == 2:
		turbulence_prop = Incompressible("omega", "[0 1 -1 0 0 0 0]", "binary", "omegaWallFunction", "fixedValue")
	u = Incompressible("U", "[0 1 -1 0 0 0 0]", "ascii", "noSlip", "fixedValue")
	k = Incompressible("k", "[0 2 -2 0 0 0 0]", "binary", "kqRWallFunction", "fixedValue")
	nut = Incompressible("nut", "[0 1 -1 0 0 0 0]", "binary", "nutkWallFunction", "fixedValue")
	p = Incompressible("p", "[0 1 -1 0 0 0 0]", "binary", "zeroGradient", "zeroGradient")
	u.file_0_creator()
	turbulence_prop.file_0_creator()
	k.file_0_creator()
	nut.file_0_creator()
	p.file_0_creator()


def write_system_files():
	with open(openfoam_inputs + R"\fvSchemes", "w", errors='ignore') as f:
		f.write(fvSchemes.fvschemes)
	with open(openfoam_inputs + R"\fvSolution", "w", errors='ignore') as f:
		f.write(fvSolution.fvSolution)
	with open(openfoam_inputs + R"\controldict", "w", errors='ignore') as f:
		f.write(controldict.control_dict)
	with open(openfoam_inputs + R"\decomposer", "w", errors='ignore') as f:
		f.write(decomposer.decomposepar)


def write_constant_files():
	with open(openfoam_inputs + R"\porosityProperties", "w", errors='ignore') as f:
		f.write(porosityProp.prsty_prop)
	with open(openfoam_inputs + R"\turbulenceProperties", "w", errors='ignore') as f:
		f.write(turbulence_prop.turb_prop)
	with open(openfoam_inputs + R"\transportProperties", "w", errors='ignore') as f:
		f.write(transportproperties.trans_prop)
