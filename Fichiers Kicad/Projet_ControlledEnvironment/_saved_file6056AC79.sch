EESchema Schematic File Version 4
LIBS:Projet_Exoplanter-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Transistor_FET:IRF540N Q?
U 1 1 605E8C09
P 4525 2075
F 0 "Q?" H 4730 2121 50  0000 L CNN
F 1 "IRF540N" H 4730 2030 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 4775 2000 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 4525 2075 50  0001 L CNN
	1    4525 2075
	1    0    0    -1  
$EndComp
$Comp
L Device:LED_ALT D?
U 1 1 605E8C10
P 4625 2425
F 0 "D?" V 4663 2308 50  0000 R CNN
F 1 "DEL 100w" V 4572 2308 50  0000 R CNN
F 2 "" H 4625 2425 50  0001 C CNN
F 3 "~" H 4625 2425 50  0001 C CNN
	1    4625 2425
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 605E8C17
P 4625 3125
F 0 "#PWR?" H 4625 2875 50  0001 C CNN
F 1 "GND" H 4630 2952 50  0000 C CNN
F 2 "" H 4625 3125 50  0001 C CNN
F 3 "" H 4625 3125 50  0001 C CNN
	1    4625 3125
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R?
U 1 1 605E8C1D
P 4625 2975
F 0 "R?" H 4693 3021 50  0000 L CNN
F 1 "R_US" H 4693 2930 50  0000 L CNN
F 2 "" V 4665 2965 50  0001 C CNN
F 3 "~" H 4625 2975 50  0001 C CNN
	1    4625 2975
	1    0    0    -1  
$EndComp
Wire Wire Line
	4625 2825 4625 2575
$EndSCHEMATC
