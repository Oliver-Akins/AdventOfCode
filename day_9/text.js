let potato = {
	'.Faerun': {'Norrath': 129, 'Tristram': 58, 'AlphaCentauri': 13, 'Arbre': 24, 'Snowdin': 60, 'Tambi': 71, 'Straylight': 67},
	'.Norrath': {'Faerun': 129, 'Tristram': 142, 'AlphaCentauri': 15, 'Arbre': 135, 'Snowdin': 75, 'Tambi': 82, 'Straylight': 54},
	'.Tristram': {'Faerun': 58, 'Norrath': 142, 'AlphaCentauri': 118, 'Arbre': 122, 'Snowdin': 103, 'Tambi': 49, 'Straylight': 97},
	'.AlphaCentauri': {'Faerun': 13, 'Norrath': 15, 'Tristram': 118, 'Arbre': 116, 'Snowdin': 12, 'Tambi': 18, 'Straylight': 91},
	'.Arbre': {'Faerun': 24, 'Norrath': 135, 'Tristram': 122, 'AlphaCentauri': 116, 'Snowdin': 129, 'Tambi': 53, 'Straylight': 40},
	'.Snowdin': {'Faerun': 60, 'Norrath': 75, 'Tristram': 103, 'AlphaCentauri': 12, 'Arbre': 129, 'Tambi': 15, 'Straylight': 99},
	'.Tambi': {'Faerun': 71, 'Norrath': 82, 'Tristram': 49, 'AlphaCentauri': 18, 'Arbre': 53, 'Snowdin': 15, 'Straylight': 70},
	'.Straylight': {'Faerun': 67, 'Norrath': 54, 'Tristram': 97, 'AlphaCentauri': 91, 'Arbre': 40, 'Snowdin': 99, 'Tambi': 70}};

/*
Faerun (0) -> Norrath (+129) -> Tristram (+142) -> Arbre (+122) -> Snowdin (+129) -> Straylight (+99) -> AlphaCentauri (+91) -> Tambi (+15)

AlphaCentauri (0) -> Tristram (+118) -> Norrath (+142) -> Arbre (+135) -> Snowdin (+129) -> Straylight (+99) -> Tambi (+70) -> Faerun (+71)  ==== 764

*/