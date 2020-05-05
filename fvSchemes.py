fvschemes = (	"/*--------------------------------*- C++ -*----------------------------------*\\\n"
				"  =========       \n"
				"  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox\n"
				"   \\\\    /   O peration     | Website:  https://openfoam.org\n"
				"    \\\\  /    A nd           | Version:  6\n"
				"     \\\\/     M anipulation  |""\n"
				"\\*---------------------------------------------------------------------------*/"
				"\n"
				"FoamFile\n"
				"{\n"
				"	version     2.0;\n"	
				"	format      ascii;\n"
				"	class       dictionary;\n"
				"	object      fvSchemes;\n"
				"}\n"
				"// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n"
				"ddtSchemes\n"
				"{\n"
				"	default			steadyState;\n"
				"}\n\n"
				"gradSchemes\n"
				"{\n"
				"	default			cellLimited leastSquares 1.0;\n"
				"	grad(U)			cellLimited leastSquares 1.0;\n"
				"}\n\n"
				"divSchemes\n"
				"{\n"
				"	default			none;\n"
				"	div(phi,U)		bounded Gauss upwind;\n"
				"	div((nuEff*dev2(T(grad(U))))) Gauss linear;\n"
				"	div(phi,T)		bounded Gauss upwind;\n"
				"	div(phi,omega) 	bounded Gauss upwind;\n"
				"	div(phi,k)      bounded Gauss upwind;\n"
				"}\n\n"
				"laplacianSchemes\n"
				"{\n"
				"	default	    	Gauss linear limited 0.5;\n"
				"}\n\n"
				"interpolationSchemes\n"
				"{\n"
				"	default			linear;\n"
				"}\n\n"
				"snGradSchemes\n"
				"{\n"
				"	default			limited 0.5;\n"
				"}\n\n"
				"wallDist\n"
				"{\n"
				"	method meshWave;\n"
				"}\n\n"
				"// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //"
			)