import global_variables
trans_prop = ("/*--------------------------------*- C++ -*----------------------------------*\\\n"
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
              "    format      ascii;\n"
              "    class       dictionary;\n"
              "    location    constant;\n"
              "    object      transportProperties;\n"
              "}\n"
              "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n"
              "transportModel Newtonian;\n\n"
              f"nu                [0 2 -1 0 0 0 0] {global_variables.kinematic_viscosity}"
              "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //"
              )
