EESchema Schematic File Version 4
LIBS:Section_SensorBlock-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
Title "Capteurs du bloc de capteurs"
Date "2021-03-23"
Rev "1.0"
Comp "Cégep de Sherbrooke"
Comment1 "247-67P-SH"
Comment2 "Projet de fin d'études"
Comment3 "William Bouchard"
Comment4 "Simon Jourdenais"
$EndDescr
$Comp
L power:+3.3V #PWR?
U 1 1 605B0B60
P 5775 975
AR Path="/60567BB2/605B0B60" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B60" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0B60" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0B60" Ref="#PWR0315"  Part="1" 
F 0 "#PWR0315" H 5775 825 50  0001 C CNN
F 1 "+3.3V" H 5790 1148 50  0000 C CNN
F 2 "" H 5775 975 50  0001 C CNN
F 3 "" H 5775 975 50  0001 C CNN
	1    5775 975 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 605B0B66
P 5775 1800
AR Path="/60567BB2/605B0B66" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B66" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0B66" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0B66" Ref="#PWR0316"  Part="1" 
F 0 "#PWR0316" H 5775 1550 50  0001 C CNN
F 1 "GND" H 5780 1627 50  0000 C CNN
F 2 "" H 5775 1800 50  0001 C CNN
F 3 "" H 5775 1800 50  0001 C CNN
	1    5775 1800
	1    0    0    -1  
$EndComp
Text Label 6175 1350 0    50   ~ 0
SDA_3V3
Text Label 6175 1650 0    50   ~ 0
SCL_3V3
$Comp
L Device:C_Small C?
U 1 1 605B0B6E
P 5575 1100
AR Path="/60567BB2/605B0B6E" Ref="C?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B6E" Ref="C?"  Part="1" 
AR Path="/606B5193/605B0B6E" Ref="C?"  Part="1" 
AR Path="/606F37DA/605B0B6E" Ref="C301"  Part="1" 
F 0 "C301" V 5525 1000 50  0000 C CNN
F 1 "0.1 uF" V 5675 1100 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 5575 1100 50  0001 C CNN
F 3 "~" H 5575 1100 50  0001 C CNN
	1    5575 1100
	0    1    1    0   
$EndComp
Wire Wire Line
	5675 1100 5775 1100
Wire Wire Line
	5775 1100 5775 1200
Wire Wire Line
	5775 1100 5775 975 
Connection ~ 5775 1100
Wire Wire Line
	5475 1100 5400 1100
Wire Wire Line
	5400 1100 5400 1200
$Comp
L power:GND #PWR?
U 1 1 605B0B7B
P 5400 1200
AR Path="/60567BB2/605B0B7B" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B7B" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0B7B" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0B7B" Ref="#PWR0314"  Part="1" 
F 0 "#PWR0314" H 5400 950 50  0001 C CNN
F 1 "GND" H 5405 1027 50  0000 C CNN
F 2 "" H 5400 1200 50  0001 C CNN
F 3 "" H 5400 1200 50  0001 C CNN
	1    5400 1200
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:DS18B20 U?
U 1 1 605B0B81
P 9325 1600
AR Path="/60567BB2/605B0B81" Ref="U?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B81" Ref="U?"  Part="1" 
AR Path="/606B5193/605B0B81" Ref="U?"  Part="1" 
AR Path="/606F37DA/605B0B81" Ref="U302"  Part="1" 
F 0 "U302" H 9095 1646 50  0000 R CNN
F 1 "DS18B20" H 9095 1555 50  0000 R CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 8325 1350 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 9175 1850 50  0001 C CNN
	1    9325 1600
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 605B0B88
P 9325 1900
AR Path="/60567BB2/605B0B88" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B88" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0B88" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0B88" Ref="#PWR0332"  Part="1" 
F 0 "#PWR0332" H 9325 1650 50  0001 C CNN
F 1 "GND" H 9330 1727 50  0000 C CNN
F 2 "" H 9325 1900 50  0001 C CNN
F 3 "" H 9325 1900 50  0001 C CNN
	1    9325 1900
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 605B0B8E
P 9325 975
AR Path="/60567BB2/605B0B8E" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B8E" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0B8E" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0B8E" Ref="#PWR0331"  Part="1" 
F 0 "#PWR0331" H 9325 825 50  0001 C CNN
F 1 "+3.3V" H 9340 1148 50  0000 C CNN
F 2 "" H 9325 975 50  0001 C CNN
F 3 "" H 9325 975 50  0001 C CNN
	1    9325 975 
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BSS138 Q?
U 1 1 605B0B94
P 2450 2000
AR Path="/60567BAF/605B0B94" Ref="Q?"  Part="1" 
AR Path="/60567BB2/605B0B94" Ref="Q?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B94" Ref="Q?"  Part="1" 
AR Path="/606B5193/605B0B94" Ref="Q?"  Part="1" 
AR Path="/606F37DA/605B0B94" Ref="Q301"  Part="1" 
F 0 "Q301" V 2700 2000 50  0000 C CNN
F 1 "BSS138" V 2791 2000 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2650 1925 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/BS/BSS138.pdf" H 2450 2000 50  0001 L CNN
	1    2450 2000
	0    -1   1    0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 605B0B9B
P 2900 1925
AR Path="/60567BAF/605B0B9B" Ref="R?"  Part="1" 
AR Path="/60567BB2/605B0B9B" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0B9B" Ref="R?"  Part="1" 
AR Path="/606B5193/605B0B9B" Ref="R?"  Part="1" 
AR Path="/606F37DA/605B0B9B" Ref="R304"  Part="1" 
F 0 "R304" V 2704 1925 50  0000 C CNN
F 1 "10k" V 2795 1925 50  0000 C CNN
F 2 "" H 2900 1925 50  0001 C CNN
F 3 "~" H 2900 1925 50  0001 C CNN
	1    2900 1925
	1    0    0    1   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 605B0BA2
P 2025 1925
AR Path="/60567BAF/605B0BA2" Ref="R?"  Part="1" 
AR Path="/60567BB2/605B0BA2" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0BA2" Ref="R?"  Part="1" 
AR Path="/606B5193/605B0BA2" Ref="R?"  Part="1" 
AR Path="/606F37DA/605B0BA2" Ref="R301"  Part="1" 
F 0 "R301" V 1829 1925 50  0000 C CNN
F 1 "10k" V 1920 1925 50  0000 C CNN
F 2 "" H 2025 1925 50  0001 C CNN
F 3 "~" H 2025 1925 50  0001 C CNN
	1    2025 1925
	1    0    0    1   
$EndComp
Wire Wire Line
	2650 2100 2900 2100
Wire Wire Line
	1750 2100 2025 2100
Wire Wire Line
	2450 1800 2450 1675
Wire Wire Line
	2450 1675 2900 1675
Wire Wire Line
	2900 1675 2900 1825
Wire Wire Line
	2900 2025 2900 2100
Connection ~ 2900 2100
Wire Wire Line
	2900 2100 3150 2100
Wire Wire Line
	2900 1675 2900 1600
Connection ~ 2900 1675
$Comp
L power:+3.3V #PWR?
U 1 1 605B0BB3
P 2900 1600
AR Path="/60567BAF/605B0BB3" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605B0BB3" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0BB3" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0BB3" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0BB3" Ref="#PWR0306"  Part="1" 
F 0 "#PWR0306" H 2900 1450 50  0001 C CNN
F 1 "+3.3V" H 2915 1773 50  0000 C CNN
F 2 "" H 2900 1600 50  0001 C CNN
F 3 "" H 2900 1600 50  0001 C CNN
	1    2900 1600
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 605B0BB9
P 2025 1575
AR Path="/60567BAF/605B0BB9" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605B0BB9" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/605B0BB9" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/605B0BB9" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/605B0BB9" Ref="#PWR0302"  Part="1" 
F 0 "#PWR0302" H 2025 1425 50  0001 C CNN
F 1 "+5V" H 2040 1748 50  0000 C CNN
F 2 "" H 2025 1575 50  0001 C CNN
F 3 "" H 2025 1575 50  0001 C CNN
	1    2025 1575
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2025 1575 2025 1825
Wire Wire Line
	2025 2025 2025 2100
Connection ~ 2025 2100
Wire Wire Line
	2025 2100 2250 2100
Text GLabel 1750 2100 0    50   Input ~ 0
AT_SCL
Text GLabel 1750 3175 0    50   Input ~ 0
AT_SDA
$Comp
L Transistor_FET:BSS138 Q?
U 1 1 6061F13B
P 2450 3075
AR Path="/60567BAF/6061F13B" Ref="Q?"  Part="1" 
AR Path="/60567BB2/6061F13B" Ref="Q?"  Part="1" 
AR Path="/60567BB2/605AE801/6061F13B" Ref="Q?"  Part="1" 
AR Path="/606B5193/6061F13B" Ref="Q?"  Part="1" 
AR Path="/606F37DA/6061F13B" Ref="Q302"  Part="1" 
F 0 "Q302" V 2700 3075 50  0000 C CNN
F 1 "BSS138" V 2791 3075 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2650 3000 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/BS/BSS138.pdf" H 2450 3075 50  0001 L CNN
	1    2450 3075
	0    -1   1    0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 6061F142
P 2900 3000
AR Path="/60567BAF/6061F142" Ref="R?"  Part="1" 
AR Path="/60567BB2/6061F142" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/6061F142" Ref="R?"  Part="1" 
AR Path="/606B5193/6061F142" Ref="R?"  Part="1" 
AR Path="/606F37DA/6061F142" Ref="R305"  Part="1" 
F 0 "R305" V 2704 3000 50  0000 C CNN
F 1 "10k" V 2795 3000 50  0000 C CNN
F 2 "" H 2900 3000 50  0001 C CNN
F 3 "~" H 2900 3000 50  0001 C CNN
	1    2900 3000
	1    0    0    1   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 6061F149
P 2025 3000
AR Path="/60567BAF/6061F149" Ref="R?"  Part="1" 
AR Path="/60567BB2/6061F149" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/6061F149" Ref="R?"  Part="1" 
AR Path="/606B5193/6061F149" Ref="R?"  Part="1" 
AR Path="/606F37DA/6061F149" Ref="R302"  Part="1" 
F 0 "R302" V 1829 3000 50  0000 C CNN
F 1 "10k" V 1920 3000 50  0000 C CNN
F 2 "" H 2025 3000 50  0001 C CNN
F 3 "~" H 2025 3000 50  0001 C CNN
	1    2025 3000
	1    0    0    1   
$EndComp
Wire Wire Line
	2650 3175 2900 3175
Wire Wire Line
	1750 3175 2025 3175
Wire Wire Line
	2450 2875 2450 2750
Wire Wire Line
	2450 2750 2900 2750
Wire Wire Line
	2900 2750 2900 2900
Wire Wire Line
	2900 3100 2900 3175
Connection ~ 2900 3175
Wire Wire Line
	2900 3175 3150 3175
Wire Wire Line
	2900 2750 2900 2675
Connection ~ 2900 2750
$Comp
L power:+3.3V #PWR?
U 1 1 6061F15A
P 2900 2675
AR Path="/60567BAF/6061F15A" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/6061F15A" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6061F15A" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6061F15A" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6061F15A" Ref="#PWR0307"  Part="1" 
F 0 "#PWR0307" H 2900 2525 50  0001 C CNN
F 1 "+3.3V" H 2915 2848 50  0000 C CNN
F 2 "" H 2900 2675 50  0001 C CNN
F 3 "" H 2900 2675 50  0001 C CNN
	1    2900 2675
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 6061F160
P 2025 2650
AR Path="/60567BAF/6061F160" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/6061F160" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6061F160" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6061F160" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6061F160" Ref="#PWR0303"  Part="1" 
F 0 "#PWR0303" H 2025 2500 50  0001 C CNN
F 1 "+5V" H 2040 2823 50  0000 C CNN
F 2 "" H 2025 2650 50  0001 C CNN
F 3 "" H 2025 2650 50  0001 C CNN
	1    2025 2650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2025 2650 2025 2900
Wire Wire Line
	2025 3100 2025 3175
Connection ~ 2025 3175
Wire Wire Line
	2025 3175 2250 3175
Text Label 3150 3175 0    50   ~ 0
SDA_3V3
Text Label 3150 2100 0    50   ~ 0
SCL_3V3
$Comp
L Device:R_Small R?
U 1 1 6061FB31
P 9850 1300
AR Path="/60567BAF/6061FB31" Ref="R?"  Part="1" 
AR Path="/60567BB2/6061FB31" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/6061FB31" Ref="R?"  Part="1" 
AR Path="/606B5193/6061FB31" Ref="R?"  Part="1" 
AR Path="/606F37DA/6061FB31" Ref="R310"  Part="1" 
F 0 "R310" V 9654 1300 50  0000 C CNN
F 1 "10k" V 9745 1300 50  0000 C CNN
F 2 "" H 9850 1300 50  0001 C CNN
F 3 "~" H 9850 1300 50  0001 C CNN
	1    9850 1300
	1    0    0    1   
$EndComp
Wire Wire Line
	9325 1300 9325 1125
Wire Wire Line
	9325 1125 9850 1125
Wire Wire Line
	9850 1125 9850 1200
Connection ~ 9325 1125
Wire Wire Line
	9325 1125 9325 975 
Wire Wire Line
	9625 1600 9850 1600
Wire Wire Line
	9850 1400 9850 1600
Connection ~ 9850 1600
Wire Wire Line
	9850 1600 10025 1600
Text GLabel 1750 4150 0    50   Input ~ 0
AT_1Wire
$Comp
L Transistor_FET:BSS138 Q?
U 1 1 606219FF
P 2450 4050
AR Path="/60567BAF/606219FF" Ref="Q?"  Part="1" 
AR Path="/60567BB2/606219FF" Ref="Q?"  Part="1" 
AR Path="/60567BB2/605AE801/606219FF" Ref="Q?"  Part="1" 
AR Path="/606B5193/606219FF" Ref="Q?"  Part="1" 
AR Path="/606F37DA/606219FF" Ref="Q303"  Part="1" 
F 0 "Q303" V 2700 4050 50  0000 C CNN
F 1 "BSS138" V 2791 4050 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2650 3975 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/BS/BSS138.pdf" H 2450 4050 50  0001 L CNN
	1    2450 4050
	0    -1   1    0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60621A06
P 2900 3975
AR Path="/60567BAF/60621A06" Ref="R?"  Part="1" 
AR Path="/60567BB2/60621A06" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/60621A06" Ref="R?"  Part="1" 
AR Path="/606B5193/60621A06" Ref="R?"  Part="1" 
AR Path="/606F37DA/60621A06" Ref="R306"  Part="1" 
F 0 "R306" V 2704 3975 50  0000 C CNN
F 1 "10k" V 2795 3975 50  0000 C CNN
F 2 "" H 2900 3975 50  0001 C CNN
F 3 "~" H 2900 3975 50  0001 C CNN
	1    2900 3975
	1    0    0    1   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60621A0D
P 2025 3975
AR Path="/60567BAF/60621A0D" Ref="R?"  Part="1" 
AR Path="/60567BB2/60621A0D" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/60621A0D" Ref="R?"  Part="1" 
AR Path="/606B5193/60621A0D" Ref="R?"  Part="1" 
AR Path="/606F37DA/60621A0D" Ref="R303"  Part="1" 
F 0 "R303" V 1829 3975 50  0000 C CNN
F 1 "10k" V 1920 3975 50  0000 C CNN
F 2 "" H 2025 3975 50  0001 C CNN
F 3 "~" H 2025 3975 50  0001 C CNN
	1    2025 3975
	1    0    0    1   
$EndComp
Wire Wire Line
	2650 4150 2900 4150
Wire Wire Line
	1750 4150 2025 4150
Wire Wire Line
	2450 3850 2450 3725
Wire Wire Line
	2450 3725 2900 3725
Wire Wire Line
	2900 3725 2900 3875
Wire Wire Line
	2900 4075 2900 4150
Connection ~ 2900 4150
Wire Wire Line
	2900 4150 3150 4150
Wire Wire Line
	2900 3725 2900 3650
Connection ~ 2900 3725
$Comp
L power:+3.3V #PWR?
U 1 1 60621A1E
P 2900 3650
AR Path="/60567BAF/60621A1E" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/60621A1E" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/60621A1E" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/60621A1E" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/60621A1E" Ref="#PWR0308"  Part="1" 
F 0 "#PWR0308" H 2900 3500 50  0001 C CNN
F 1 "+3.3V" H 2915 3823 50  0000 C CNN
F 2 "" H 2900 3650 50  0001 C CNN
F 3 "" H 2900 3650 50  0001 C CNN
	1    2900 3650
	-1   0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 60621A24
P 2025 3625
AR Path="/60567BAF/60621A24" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/60621A24" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/60621A24" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/60621A24" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/60621A24" Ref="#PWR0304"  Part="1" 
F 0 "#PWR0304" H 2025 3475 50  0001 C CNN
F 1 "+5V" H 2040 3798 50  0000 C CNN
F 2 "" H 2025 3625 50  0001 C CNN
F 3 "" H 2025 3625 50  0001 C CNN
	1    2025 3625
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2025 3625 2025 3875
Wire Wire Line
	2025 4075 2025 4150
Connection ~ 2025 4150
Wire Wire Line
	2025 4150 2250 4150
Text Label 3150 4150 0    50   ~ 0
1Wire_3V3
Text Label 10025 1600 0    50   ~ 0
1Wire_3V3
$Comp
L Connector_Generic:Conn_01x04 J302
U 1 1 606286AF
P 4175 1450
F 0 "J302" H 4095 1767 50  0000 C CNN
F 1 "Conn_01x04" H 4095 1676 50  0000 C CNN
F 2 "" H 4175 1450 50  0001 C CNN
F 3 "~" H 4175 1450 50  0001 C CNN
	1    4175 1450
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J306
U 1 1 60629146
P 7900 1650
F 0 "J306" H 7820 1967 50  0000 C CNN
F 1 "Conn_01x03" H 7820 1876 50  0000 C CNN
F 2 "" H 7900 1650 50  0001 C CNN
F 3 "~" H 7900 1650 50  0001 C CNN
	1    7900 1650
	-1   0    0    -1  
$EndComp
Text Label 4375 1550 0    50   ~ 0
SDA_3V3
Text Label 4375 1650 0    50   ~ 0
SCL_3V3
$Comp
L power:+3.3V #PWR?
U 1 1 6062A432
P 4575 1325
AR Path="/60567BB2/6062A432" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6062A432" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6062A432" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6062A432" Ref="#PWR0309"  Part="1" 
F 0 "#PWR0309" H 4575 1175 50  0001 C CNN
F 1 "+3.3V" H 4590 1498 50  0000 C CNN
F 2 "" H 4575 1325 50  0001 C CNN
F 3 "" H 4575 1325 50  0001 C CNN
	1    4575 1325
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6062A488
P 4825 1450
AR Path="/60567BB2/6062A488" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6062A488" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6062A488" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6062A488" Ref="#PWR0312"  Part="1" 
F 0 "#PWR0312" H 4825 1200 50  0001 C CNN
F 1 "GND" H 4830 1277 50  0000 C CNN
F 2 "" H 4825 1450 50  0001 C CNN
F 3 "" H 4825 1450 50  0001 C CNN
	1    4825 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	4825 1450 4375 1450
Wire Wire Line
	4375 1350 4575 1350
Wire Wire Line
	4575 1350 4575 1325
Text Label 8100 1650 0    50   ~ 0
1Wire_3V3
$Comp
L power:+3.3V #PWR?
U 1 1 6062C0DF
P 8300 1550
AR Path="/60567BB2/6062C0DF" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6062C0DF" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6062C0DF" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6062C0DF" Ref="#PWR0326"  Part="1" 
F 0 "#PWR0326" H 8300 1400 50  0001 C CNN
F 1 "+3.3V" H 8315 1723 50  0000 C CNN
F 2 "" H 8300 1550 50  0001 C CNN
F 3 "" H 8300 1550 50  0001 C CNN
	1    8300 1550
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 1550 8100 1550
$Comp
L power:GND #PWR?
U 1 1 6062DE7E
P 8100 1750
AR Path="/60567BB2/6062DE7E" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6062DE7E" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6062DE7E" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6062DE7E" Ref="#PWR0324"  Part="1" 
F 0 "#PWR0324" H 8100 1500 50  0001 C CNN
F 1 "GND" H 8105 1577 50  0000 C CNN
F 2 "" H 8100 1750 50  0001 C CNN
F 3 "" H 8100 1750 50  0001 C CNN
	1    8100 1750
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Gas:CCS811 U301
U 1 1 6062F62C
P 8675 3175
F 0 "U301" H 8850 3725 50  0000 C CNN
F 1 "CCS811" H 8850 3625 50  0000 C CNN
F 2 "Package_LGA:AMS_LGA-10-1EP_2.7x4mm_P0.6mm" H 8675 2575 50  0001 C CNN
F 3 "http://ams.com/eng/Products/Environmental-Sensors/Air-Quality-Sensors/CCS811" H 8675 2975 50  0001 C CNN
	1    8675 3175
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6062FB7E
P 8675 3775
AR Path="/60567BB2/6062FB7E" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6062FB7E" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6062FB7E" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6062FB7E" Ref="#PWR0330"  Part="1" 
F 0 "#PWR0330" H 8675 3525 50  0001 C CNN
F 1 "GND" H 8680 3602 50  0000 C CNN
F 2 "" H 8675 3775 50  0001 C CNN
F 3 "" H 8675 3775 50  0001 C CNN
	1    8675 3775
	1    0    0    -1  
$EndComp
Wire Wire Line
	8675 3775 8675 3675
$Comp
L Device:R_Small R?
U 1 1 60631568
P 7225 3050
AR Path="/60567BAF/60631568" Ref="R?"  Part="1" 
AR Path="/60567BB2/60631568" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/60631568" Ref="R?"  Part="1" 
AR Path="/606B5193/60631568" Ref="R?"  Part="1" 
AR Path="/606F37DA/60631568" Ref="R307"  Part="1" 
F 0 "R307" V 7029 3050 50  0000 C CNN
F 1 "10k" V 7120 3050 50  0000 C CNN
F 2 "" H 7225 3050 50  0001 C CNN
F 3 "~" H 7225 3050 50  0001 C CNN
	1    7225 3050
	1    0    0    1   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 606316BD
P 7225 3150
AR Path="/60567BB2/606316BD" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606316BD" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606316BD" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/606316BD" Ref="#PWR0322"  Part="1" 
F 0 "#PWR0322" H 7225 2900 50  0001 C CNN
F 1 "GND" H 7230 2977 50  0000 C CNN
F 2 "" H 7225 3150 50  0001 C CNN
F 3 "" H 7225 3150 50  0001 C CNN
	1    7225 3150
	1    0    0    -1  
$EndComp
Text Label 8275 2975 2    50   ~ 0
CO2_!Int
Text Label 8275 3075 2    50   ~ 0
SDA_3V3
Text Label 8275 3175 2    50   ~ 0
SCL_3V3
$Comp
L Device:R_Small R?
U 1 1 60633324
P 7950 3625
AR Path="/60567BAF/60633324" Ref="R?"  Part="1" 
AR Path="/60567BB2/60633324" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/60633324" Ref="R?"  Part="1" 
AR Path="/606B5193/60633324" Ref="R?"  Part="1" 
AR Path="/606F37DA/60633324" Ref="R309"  Part="1" 
F 0 "R309" V 7754 3625 50  0000 C CNN
F 1 "10k" V 7845 3625 50  0000 C CNN
F 2 "" H 7950 3625 50  0001 C CNN
F 3 "~" H 7950 3625 50  0001 C CNN
	1    7950 3625
	1    0    0    1   
$EndComp
Wire Wire Line
	7225 2875 7225 2950
Wire Wire Line
	7225 2875 8275 2875
$Comp
L power:+3.3V #PWR0329
U 1 1 6063621E
P 8675 2675
F 0 "#PWR0329" H 8675 2525 50  0001 C CNN
F 1 "+3.3V" H 8690 2848 50  0000 C CNN
F 2 "" H 8675 2675 50  0001 C CNN
F 3 "" H 8675 2675 50  0001 C CNN
	1    8675 2675
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0323
U 1 1 60636256
P 7825 3100
F 0 "#PWR0323" H 7825 2950 50  0001 C CNN
F 1 "+3.3V" H 7840 3273 50  0000 C CNN
F 2 "" H 7825 3100 50  0001 C CNN
F 3 "" H 7825 3100 50  0001 C CNN
	1    7825 3100
	1    0    0    -1  
$EndComp
Text Label 7425 3450 2    50   ~ 0
CO2_!Reset
$Comp
L Jumper:SolderJumper_2_Open JP301
U 1 1 6063A42E
P 6850 2700
F 0 "JP301" H 6850 2600 50  0000 C CNN
F 1 "Jumper_Address_I2C" H 6825 2800 50  0000 C CNN
F 2 "" H 6850 2700 50  0001 C CNN
F 3 "~" H 6850 2700 50  0001 C CNN
	1    6850 2700
	1    0    0    1   
$EndComp
Connection ~ 7225 2875
$Comp
L power:+3.3V #PWR0319
U 1 1 6063B35D
P 6700 2625
F 0 "#PWR0319" H 6700 2475 50  0001 C CNN
F 1 "+3.3V" H 6715 2798 50  0000 C CNN
F 2 "" H 6700 2625 50  0001 C CNN
F 3 "" H 6700 2625 50  0001 C CNN
	1    6700 2625
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 2700 6700 2625
Wire Wire Line
	7000 2700 7225 2700
Wire Wire Line
	7225 2700 7225 2875
$Comp
L Device:R_Small R?
U 1 1 606332CC
P 7825 3250
AR Path="/60567BAF/606332CC" Ref="R?"  Part="1" 
AR Path="/60567BB2/606332CC" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/606332CC" Ref="R?"  Part="1" 
AR Path="/606B5193/606332CC" Ref="R?"  Part="1" 
AR Path="/606F37DA/606332CC" Ref="R308"  Part="1" 
F 0 "R308" V 7750 3250 50  0000 C CNN
F 1 "10k" V 7900 3250 50  0000 C CNN
F 2 "" H 7825 3250 50  0001 C CNN
F 3 "~" H 7825 3250 50  0001 C CNN
	1    7825 3250
	1    0    0    1   
$EndComp
Wire Wire Line
	7825 3350 7825 3375
Wire Wire Line
	7825 3375 8275 3375
$Comp
L Device:D_Small D301
U 1 1 60645309
P 7575 3450
F 0 "D301" H 7575 3655 50  0000 C CNN
F 1 "1N4148" H 7575 3564 50  0000 C CNN
F 2 "" V 7575 3450 50  0001 C CNN
F 3 "~" V 7575 3450 50  0001 C CNN
	1    7575 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	7475 3450 7425 3450
Wire Wire Line
	7675 3450 7825 3450
Wire Wire Line
	7825 3450 7825 3375
Connection ~ 7825 3375
$Comp
L Device:D_Small D302
U 1 1 60646F5B
P 7600 3750
F 0 "D302" H 7600 3850 50  0000 C CNN
F 1 "1N4148" H 7600 3675 50  0000 C CNN
F 2 "" V 7600 3750 50  0001 C CNN
F 3 "~" V 7600 3750 50  0001 C CNN
	1    7600 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7950 3525 7950 3125
Wire Wire Line
	7950 3125 7825 3125
Wire Wire Line
	7825 3125 7825 3150
Wire Wire Line
	7825 3125 7825 3100
Connection ~ 7825 3125
Wire Wire Line
	7700 3750 7950 3750
Wire Wire Line
	7950 3750 7950 3725
Wire Wire Line
	7950 3750 8275 3750
Wire Wire Line
	8275 3750 8275 3475
Connection ~ 7950 3750
Text Label 7500 3750 2    50   ~ 0
CO2_!Wake
$Comp
L Device:Thermistor_NTC TH301
U 1 1 60651155
P 9825 3125
F 0 "TH301" H 9922 3171 50  0000 L CNN
F 1 "10k" H 9922 3080 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 9825 3175 50  0001 C CNN
F 3 "~" H 9825 3175 50  0001 C CNN
	1    9825 3125
	1    0    0    -1  
$EndComp
Wire Wire Line
	9075 2975 9400 2975
Wire Wire Line
	9825 3275 9075 3275
Wire Wire Line
	9075 3075 9400 3075
Wire Wire Line
	9400 3075 9400 2975
Connection ~ 9400 2975
Wire Wire Line
	9400 2975 9825 2975
Wire Wire Line
	9825 3275 10425 3275
Connection ~ 9825 3275
$Comp
L power:+3.3V #PWR0335
U 1 1 6065604F
P 10425 2850
F 0 "#PWR0335" H 10425 2700 50  0001 C CNN
F 1 "+3.3V" H 10440 3023 50  0000 C CNN
F 2 "" H 10425 2850 50  0001 C CNN
F 3 "" H 10425 2850 50  0001 C CNN
	1    10425 2850
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 6065610F
P 10425 2950
AR Path="/60567BAF/6065610F" Ref="R?"  Part="1" 
AR Path="/60567BB2/6065610F" Ref="R?"  Part="1" 
AR Path="/60567BB2/605AE801/6065610F" Ref="R?"  Part="1" 
AR Path="/606B5193/6065610F" Ref="R?"  Part="1" 
AR Path="/606F37DA/6065610F" Ref="R312"  Part="1" 
F 0 "R312" V 10229 2950 50  0000 C CNN
F 1 "100k" V 10320 2950 50  0000 C CNN
F 2 "" H 10425 2950 50  0001 C CNN
F 3 "~" H 10425 2950 50  0001 C CNN
	1    10425 2950
	1    0    0    1   
$EndComp
Wire Wire Line
	10425 3050 10425 3275
Wire Wire Line
	7500 3750 7500 4000
$Comp
L Jumper:SolderJumper_2_Bridged JP302
U 1 1 6065901B
P 7650 4000
F 0 "JP302" H 7650 4075 50  0000 C CNN
F 1 "Jumper_Enable_Wake" H 7625 3900 50  0000 C CNN
F 2 "" H 7650 4000 50  0001 C CNN
F 3 "~" H 7650 4000 50  0001 C CNN
	1    7650 4000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 60659300
P 8125 4025
AR Path="/60567BB2/60659300" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/60659300" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/60659300" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/60659300" Ref="#PWR0325"  Part="1" 
F 0 "#PWR0325" H 8125 3775 50  0001 C CNN
F 1 "GND" H 8130 3852 50  0000 C CNN
F 2 "" H 8125 4025 50  0001 C CNN
F 3 "" H 8125 4025 50  0001 C CNN
	1    8125 4025
	1    0    0    -1  
$EndComp
Wire Wire Line
	8125 4025 8125 4000
Wire Wire Line
	8125 4000 7800 4000
$Comp
L Connector_Generic:Conn_01x07 J304
U 1 1 6065CB92
P 5625 3200
F 0 "J304" H 5545 3717 50  0000 C CNN
F 1 "Conn_Keyes_CCS" H 5545 3626 50  0000 C CNN
F 2 "" H 5625 3200 50  0001 C CNN
F 3 "~" H 5625 3200 50  0001 C CNN
	1    5625 3200
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J303
U 1 1 6065CD1C
P 4400 3175
F 0 "J303" H 4400 3675 50  0000 C CNN
F 1 "Conn_Adafruit_CCS" H 4525 3600 50  0000 C CNN
F 2 "" H 4400 3175 50  0001 C CNN
F 3 "~" H 4400 3175 50  0001 C CNN
	1    4400 3175
	-1   0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 6066134B
P 4925 2975
AR Path="/60567BB2/6066134B" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6066134B" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6066134B" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6066134B" Ref="#PWR0313"  Part="1" 
F 0 "#PWR0313" H 4925 2825 50  0001 C CNN
F 1 "+3.3V" H 4940 3148 50  0000 C CNN
F 2 "" H 4925 2975 50  0001 C CNN
F 3 "" H 4925 2975 50  0001 C CNN
	1    4925 2975
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 2975 4925 2975
Wire Wire Line
	4600 3075 4650 3075
Wire Wire Line
	4650 3075 4650 3000
$Comp
L power:GND #PWR?
U 1 1 606647DB
P 4800 3000
AR Path="/60567BB2/606647DB" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606647DB" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606647DB" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/606647DB" Ref="#PWR0311"  Part="1" 
F 0 "#PWR0311" H 4800 2750 50  0001 C CNN
F 1 "GND" H 4700 2900 50  0000 C CNN
F 2 "" H 4800 3000 50  0001 C CNN
F 3 "" H 4800 3000 50  0001 C CNN
	1    4800 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 3000 4800 3000
Wire Wire Line
	4600 3175 4925 3175
Wire Wire Line
	4600 3275 4925 3275
Wire Wire Line
	5825 2900 5875 2900
Wire Wire Line
	5875 2900 5875 2825
$Comp
L power:GND #PWR?
U 1 1 60669D36
P 6025 2825
AR Path="/60567BB2/60669D36" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/60669D36" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/60669D36" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/60669D36" Ref="#PWR0317"  Part="1" 
F 0 "#PWR0317" H 6025 2575 50  0001 C CNN
F 1 "GND" H 5925 2725 50  0000 C CNN
F 2 "" H 6025 2825 50  0001 C CNN
F 3 "" H 6025 2825 50  0001 C CNN
	1    6025 2825
	1    0    0    -1  
$EndComp
Wire Wire Line
	5875 2825 6025 2825
$Comp
L power:+3.3V #PWR?
U 1 1 6066BB3A
P 6150 3000
AR Path="/60567BB2/6066BB3A" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6066BB3A" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6066BB3A" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6066BB3A" Ref="#PWR0318"  Part="1" 
F 0 "#PWR0318" H 6150 2850 50  0001 C CNN
F 1 "+3.3V" H 6165 3173 50  0000 C CNN
F 2 "" H 6150 3000 50  0001 C CNN
F 3 "" H 6150 3000 50  0001 C CNN
	1    6150 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 3000 5825 3000
Text Label 5825 3100 0    50   ~ 0
SDA_3V3
Text Label 5825 3200 0    50   ~ 0
SCL_3V3
Text Label 5825 3300 0    50   ~ 0
CO2_!Reset
Text Label 5825 3400 0    50   ~ 0
CO2_!Wake
Text Label 5825 3500 0    50   ~ 0
CO2_!Int
Text Label 4600 3375 0    50   ~ 0
CO2_!Int
Text Label 4600 3475 0    50   ~ 0
CO2_!Reset
Text Label 4600 3575 0    50   ~ 0
CO2_!Wake
Text Label 4925 3275 0    50   ~ 0
SDA_3V3
Text Label 4925 3175 0    50   ~ 0
SCL_3V3
$Comp
L Connector_Generic:Conn_01x05 J305
U 1 1 60670ABA
P 6625 5450
F 0 "J305" H 6545 5867 50  0000 C CNN
F 1 "Conn_SGP30" H 6545 5776 50  0000 C CNN
F 2 "" H 6625 5450 50  0001 C CNN
F 3 "~" H 6625 5450 50  0001 C CNN
	1    6625 5450
	-1   0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0320
U 1 1 60672B69
P 7025 5250
F 0 "#PWR0320" H 7025 5100 50  0001 C CNN
F 1 "+3.3V" H 7040 5423 50  0000 C CNN
F 2 "" H 7025 5250 50  0001 C CNN
F 3 "" H 7025 5250 50  0001 C CNN
	1    7025 5250
	1    0    0    -1  
$EndComp
Wire Wire Line
	7025 5250 6825 5250
NoConn ~ 6825 5350
Wire Wire Line
	6825 5450 6875 5450
Wire Wire Line
	6875 5450 6875 5375
$Comp
L power:GND #PWR?
U 1 1 6067697C
P 7025 5375
AR Path="/60567BB2/6067697C" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6067697C" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6067697C" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6067697C" Ref="#PWR0321"  Part="1" 
F 0 "#PWR0321" H 7025 5125 50  0001 C CNN
F 1 "GND" H 6925 5275 50  0000 C CNN
F 2 "" H 7025 5375 50  0001 C CNN
F 3 "" H 7025 5375 50  0001 C CNN
	1    7025 5375
	1    0    0    -1  
$EndComp
Wire Wire Line
	6875 5375 7025 5375
Text Label 7125 5550 0    50   ~ 0
SCL_3V3
Text Label 7125 5650 0    50   ~ 0
SDA_3V3
Wire Wire Line
	7125 5550 6825 5550
Wire Wire Line
	6825 5650 7125 5650
$Comp
L power:GND #PWR0328
U 1 1 606805DE
P 8650 5725
F 0 "#PWR0328" H 8650 5475 50  0001 C CNN
F 1 "GND" H 8655 5552 50  0000 C CNN
F 2 "" H 8650 5725 50  0001 C CNN
F 3 "" H 8650 5725 50  0001 C CNN
	1    8650 5725
	1    0    0    -1  
$EndComp
Wire Wire Line
	8700 5325 8650 5325
Wire Wire Line
	9100 5675 8650 5675
Connection ~ 8650 5675
Wire Wire Line
	8650 5675 8650 5725
Wire Wire Line
	8700 5475 8650 5475
Wire Wire Line
	8650 5325 8650 5475
Connection ~ 8650 5475
Wire Wire Line
	8650 5475 8650 5675
Text Label 9500 5475 0    50   ~ 0
SDA_3V3
Text Label 9500 5325 0    50   ~ 0
SCL_3V3
$Comp
L Device:C_Small C?
U 1 1 6068AC96
P 10175 5350
AR Path="/60567BB2/6068AC96" Ref="C?"  Part="1" 
AR Path="/60567BB2/605AE801/6068AC96" Ref="C?"  Part="1" 
AR Path="/606B5193/6068AC96" Ref="C?"  Part="1" 
AR Path="/606F37DA/6068AC96" Ref="C302"  Part="1" 
F 0 "C302" V 10350 5350 50  0000 C CNN
F 1 "0.1 uF" V 10275 5350 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 10175 5350 50  0001 C CNN
F 3 "~" H 10175 5350 50  0001 C CNN
	1    10175 5350
	-1   0    0    1   
$EndComp
Wire Wire Line
	10175 5250 10175 5175
Wire Wire Line
	9500 5175 10175 5175
$Comp
L Device:R_Small R311
U 1 1 6068DCF5
P 10175 5075
F 0 "R311" H 10234 5121 50  0000 L CNN
F 1 "4.7 Ohms" H 10234 5030 50  0000 L CNN
F 2 "" H 10175 5075 50  0001 C CNN
F 3 "~" H 10175 5075 50  0001 C CNN
	1    10175 5075
	1    0    0    -1  
$EndComp
Connection ~ 10175 5175
$Comp
L power:GND #PWR0334
U 1 1 6068DE27
P 10175 5450
F 0 "#PWR0334" H 10175 5200 50  0001 C CNN
F 1 "GND" H 10180 5277 50  0000 C CNN
F 2 "" H 10175 5450 50  0001 C CNN
F 3 "" H 10175 5450 50  0001 C CNN
	1    10175 5450
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 6068DFC5
P 8575 5075
AR Path="/60567BB2/6068DFC5" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/6068DFC5" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/6068DFC5" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/6068DFC5" Ref="#PWR0327"  Part="1" 
F 0 "#PWR0327" H 8575 4925 50  0001 C CNN
F 1 "+3.3V" H 8590 5248 50  0000 C CNN
F 2 "" H 8575 5075 50  0001 C CNN
F 3 "" H 8575 5075 50  0001 C CNN
	1    8575 5075
	1    0    0    -1  
$EndComp
Wire Wire Line
	8575 5075 8575 5175
Wire Wire Line
	8575 5175 8700 5175
$Comp
L power:+5V #PWR0310
U 1 1 606914BB
P 4725 2875
F 0 "#PWR0310" H 4725 2725 50  0001 C CNN
F 1 "+5V" H 4740 3048 50  0000 C CNN
F 2 "" H 4725 2875 50  0001 C CNN
F 3 "" H 4725 2875 50  0001 C CNN
	1    4725 2875
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 2875 4725 2875
$Comp
L power:+3.3V #PWR?
U 1 1 606B45A0
P 10175 4975
AR Path="/60567BB2/606B45A0" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606B45A0" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606B45A0" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/606B45A0" Ref="#PWR0333"  Part="1" 
F 0 "#PWR0333" H 10175 4825 50  0001 C CNN
F 1 "+3.3V" H 10190 5148 50  0000 C CNN
F 2 "" H 10175 4975 50  0001 C CNN
F 3 "" H 10175 4975 50  0001 C CNN
	1    10175 4975
	1    0    0    -1  
$EndComp
Wire Notes Line
	3925 600  6650 600 
Wire Notes Line
	6650 600  6650 2225
Wire Notes Line
	6650 2225 3925 2225
Wire Notes Line
	3925 2225 3925 600 
Wire Notes Line
	10525 600  10525 2225
Wire Notes Line
	7525 600  7525 2225
Wire Notes Line
	7525 600  10525 600 
Wire Notes Line
	7525 2225 10525 2225
Wire Notes Line
	10700 2400 10700 4275
Wire Notes Line
	10700 4275 3850 4275
Wire Notes Line
	3850 4275 3850 2400
Wire Notes Line
	3850 2400 10700 2400
Wire Notes Line
	6300 4625 10675 4625
Wire Notes Line
	10675 4625 10675 6100
Wire Notes Line
	10675 6100 6300 6100
Wire Notes Line
	6300 6100 6300 4625
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 606AC69D
P 1750 5475
AR Path="/606B5191/606AC69D" Ref="J?"  Part="1" 
AR Path="/606B5193/606AC69D" Ref="J?"  Part="1" 
AR Path="/606F37DA/606AC69D" Ref="J301"  Part="1" 
F 0 "J301" H 1670 5792 50  0000 C CNN
F 1 "Conn_OLED_Screen" H 1670 5701 50  0000 C CNN
F 2 "" H 1750 5475 50  0001 C CNN
F 3 "~" H 1750 5475 50  0001 C CNN
	1    1750 5475
	-1   0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 606AC6A4
P 2450 5550
AR Path="/606B5191/606AC6A4" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606AC6A4" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/606AC6A4" Ref="#PWR0305"  Part="1" 
F 0 "#PWR0305" H 2450 5400 50  0001 C CNN
F 1 "+3.3V" H 2465 5723 50  0000 C CNN
F 2 "" H 2450 5550 50  0001 C CNN
F 3 "" H 2450 5550 50  0001 C CNN
	1    2450 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2450 5550 2450 5575
Wire Wire Line
	1950 5575 2450 5575
$Comp
L power:GND #PWR?
U 1 1 606AC6AC
P 1950 5675
AR Path="/60567BB2/605A3EA5/606AC6AC" Ref="#PWR?"  Part="1" 
AR Path="/606B5191/606AC6AC" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606AC6AC" Ref="#PWR?"  Part="1" 
AR Path="/606F37DA/606AC6AC" Ref="#PWR0301"  Part="1" 
F 0 "#PWR0301" H 1950 5425 50  0001 C CNN
F 1 "GND" H 1955 5502 50  0000 C CNN
F 2 "" H 1950 5675 50  0001 C CNN
F 3 "" H 1950 5675 50  0001 C CNN
	1    1950 5675
	-1   0    0    -1  
$EndComp
Text Label 1950 5375 0    50   ~ 0
SDA_3V3
Text Label 1950 5475 0    50   ~ 0
SCL_3V3
$Comp
L Projet_ControlledEnvironment-cache:Projet_lib:SHT2x U303
U 1 1 605A5FD7
P 5825 1500
F 0 "U303" H 5645 1546 50  0000 R CNN
F 1 "Projet_lib:SHT2x" H 5645 1455 50  0000 R CNN
F 2 "" H 5475 1450 50  0001 C CNN
F 3 "" H 5475 1450 50  0001 C CNN
	1    5825 1500
	1    0    0    -1  
$EndComp
$Comp
L Projet_lib:SGP30 U304
U 1 1 605AC30B
P 9100 5275
F 0 "U304" H 9100 5640 50  0000 C CNN
F 1 "SGP30" H 9100 5549 50  0000 C CNN
F 2 "" H 9100 5575 50  0001 C CNN
F 3 "" H 9100 5575 50  0001 C CNN
	1    9100 5275
	1    0    0    -1  
$EndComp
$EndSCHEMATC
