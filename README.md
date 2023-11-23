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
<Max weight of the backpack>
```
Example datase file:
```bash
cat dataset.txt << EOF
3 
Satterfield, Goldner and Orn Mike Raffone;113,59;23;52;2484;3,7 
Thompson, Heller and Will Kent Cook;288,96;24;44;2271;4,5 
Skiles-Rodriguez Rusty Keyes;188,77;20;38;2213;0,6
EOF
```


### Run the project
Execute the following command in the root directory of the project:
```bash 
python3 main.py
```
