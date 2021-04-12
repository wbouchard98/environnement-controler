EESchema Schematic File Version 4
LIBS:Projet_Exoplanter-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 5
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
L Device:Heater R?
U 1 1 6056F0C3
P 7375 1725
F 0 "R?" H 7445 1771 50  0000 L CNN
F 1 "Heater" H 7445 1680 50  0000 L CNN
F 2 "" V 7305 1725 50  0001 C CNN
F 3 "~" H 7375 1725 50  0001 C CNN
	1    7375 1725
	1    0    0    -1  
$EndComp
Wire Wire Line
	6175 1925 6650 1925
Wire Wire Line
	7375 1575 7375 1525
Wire Wire Line
	7375 1525 6650 1525
Wire Wire Line
	6175 1825 6650 1825
Wire Wire Line
	6650 1525 6650 1625
Wire Wire Line
	6650 1625 6175 1625
Wire Wire Line
	6650 1525 6175 1525
$Comp
L Motor:Fan M?
U 1 1 6056F0D8
P 7250 3175
F 0 "M?" H 7408 3271 50  0000 L CNN
F 1 "Fan" H 7408 3180 50  0000 L CNN
F 2 "" H 7250 3185 50  0001 C CNN
F 3 "~" H 7250 3185 50  0001 C CNN
	1    7250 3175
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 1825 6650 1925
Wire Wire Line
	7375 1875 7375 1925
Connection ~ 6650 1525
Wire Wire Line
	6650 1925 7375 1925
Connection ~ 6650 1925
$EndSCHEMATC
