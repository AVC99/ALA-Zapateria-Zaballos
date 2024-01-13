# ALA-Zapateria-Zaballos
Optimization algorithms for a given problem resolved in Python.

## Problem description

The owner of the thousand-year-old and renowned "Zapatería Zaballos" hired PAED students to organize his inventory 
and grow as a company. In fact, it has gone so well that he is thinking about improvements and expansions. Since these 
improvements go through previous studies that require the implementation of more complex algorithms than the sorting 
ones, he has asked us - ALA students - the task of thinking about possible solutions to his new problems.
First of all, we have been asked for help in deciding how to send packages efficiently according to the price of the 
contents included in them (avoiding tariffs).
On the other hand, we have been commissioned with a feasibility study on a hypothetical second physical store, wanting 
to be able to distribute the products in such a way that none of the stores overshadows the other.
Seeing the complexity of the problems, we have decided that it will be necessary to apply combinatorial optimization 
algorithms to solve them. Next, we will compare them in terms of performance so that the shoe store owner can choose 
which one weighs the most

## Distribution of problems
### Alex 
  - [X] P1 Backtracking
  - [X] P1 Greedy
  
### Oscar
  - [X] P2 Bruteforce
  - [X] P2 Backtracking
  - [X] P2 B&B 

### Arnau 
  - [x] P1 Bruteforce
  - [] P1 B&B
  - [x] P2 Greedy


## How to run 
To run the entire project, you must have Python 3 installed on your computer.
### Create your dataset
The datasets are located on /data/datasets/ folder which in this git is empty.
You can create your own dataset or use the ones we have created for you.
To create your own dataset, you must create a file with the following format:
```bash
<Number of items>
[<Shoe>]*
```
For databases use names datasetXXS.txt, datasetXS.txt, datasetS.txt, datasetM.txt, datasetL.txt, datasetXXXL.txt
Example datase file run on the project directory:
#### For unix systems
```bash
cat > data/datasets/datasetXXS.txt << EOF
6
Abernathy, Witting and Lebsack Ferry;145,28;24;40;2702;6,7
Farrell-Powlowski Koch 2;491,62;27;38;2950;9,0
Abernathy, Torphy and Pfeffer Larson 0;295,11;29;43;3088;0,9
Farrell-Powlowski Shooe;93,43;16;45;1843;2,4
Farrell-Powlowski Gottlieb 50;174,89;15;34;3465;9,8
Farrell-Powlowski Tillman;121,62;17;42;2284;1,0
EOF
```
#### For windows systems
```bash echo 6 > data/datasets/datasetXXS.txt
echo Abernathy, Witting and Lebsack Ferry;145,28;24;40;2702;6,7 >> data/datasets/datasetXXS.txt
echo Farrell-Powlowski Koch 2;491,62;27;38;2950;9,0 >> data/datasets/datasetXXS.txt
echo Abernathy, Torphy and Pfeffer Larson 0;295,11;29;43;3088;0,9 >> data/datasets/datasetXXS.txt
echo Farrell-Powlowski Shooe;93,43;16;45;1843;2,4 >> data/datasets/datasetXXS.txt
echo Farrell-Powlowski Gottlieb 50;174,89;15;34;3465;9,8 >> data/datasets/datasetXXS.txt
echo Farrell-Powlowski Tillman;121,62;17;42;2284;1,0 >> data/datasets/datasetXXS.txt
```

### Run the project
Execute the following command in the root directory of the project:
```bash 
python3 main.py
```
