# ALA-Zapateria-Zaballos
Optimization algorithms for a given problem resolved in Python

## Problem description

El propietari de la mil·lenària i reconeguda “Zapatería Zaballos” va contractar als alumnes de PAED per a fer 
una ordenació del seu inventari i poder créixer com a empresa. De fet ha anat tant bé que està pensant en 
millores  i  ampliacions.  Com  que  aquestes  millores  passen  per  uns  estudis  previs  que  requereixen  de  la 
implementació d’uns algorismes més complexos que els d’ordenació, ens ha demanat a nosaltres - alumnes 
d’ALA - la tasca de pensar en les possibles solucions als seus nous problemes. 
En primer lloc, se’ns ha demanat  ajuda per a decidir com enviar paquets de forma eficient segons  el preu 
dels continguts que s’hi incloguin (evitant aranzels). 
D’altra banda, se’ns ha encarregat un estudi de viabilitat sobre una hipotètica segona botiga física, volent 
poder repartir els productes de forma que cap de les botigues eclipsi l’altra. 
Veient la complexitat dels problemes, hem decidit que caldrà aplicar algorismes d’optimització combinatòria 
per a solucionar-los. A continuació, els compararem en termes de rendiment per a que  el propietari de la 
sabateria pugui escollir quin d’ells li fa més el pes

## How to run 
To run the entire project, you must have Python 3 installed on your computer.
### Create your dataset
To create your own dataset, you must create a file with the following format:
```bash
<Number of items>
[<Shoe>]*
```
For databases use names datasetXXS.txt, datasetXS.txt, datasetS.txt, datasetM.txt, datasetL.txt, datasetXXXL.txt
Example datase file run on the project directory:
```bash
cat > datasetXXS.txt << EOF
6
Abernathy, Witting and Lebsack Ferry;145,28;24;40;2702;6,7
Farrell-Powlowski Koch 2;491,62;27;38;2950;9,0
Abernathy, Torphy and Pfeffer Larson 0;295,11;29;43;3088;0,9
Farrell-Powlowski Shooe;93,43;16;45;1843;2,4
Farrell-Powlowski Gottlieb 50;174,89;15;34;3465;9,8
Farrell-Powlowski Tillman;121,62;17;42;2284;1,0
```


### Run the project
Execute the following command in the root directory of the project:
```bash 
python3 main.py
```
