EESchema Schematic File Version 4
LIBS:Projet_ControlledEnvironment-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 4
Title "Connecteurs du bloc de contrôle"
Date "2021-03-22"
Rev "1.0"
Comp "Cégep de Sherbrooke"
Comment1 "Projet de fin d'études"
Comment2 "247-67P-SH"
Comment3 "William Bouchard"
Comment4 "Simon Jourdenais"
$EndDescr
$Comp
L Connector_Generic:Conn_01x02 J406
U 1 1 606B5882
P 6400 2500
F 0 "J406" H 6320 2175 50  0000 C CNN
F 1 "Conn_01x02" H 6320 2266 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6400 2500 50  0001 C CNN
F 3 "~" H 6400 2500 50  0001 C CNN
	1    6400 2500
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J407
U 1 1 606B28EC
P 6400 2925
F 0 "J407" H 6320 2600 50  0000 C CNN
F 1 "Conn_01x02" H 6320 2691 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6400 2925 50  0001 C CNN
F 3 "~" H 6400 2925 50  0001 C CNN
	1    6400 2925
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J408
U 1 1 606B296A
P 6400 3450
F 0 "J408" H 6320 3125 50  0000 C CNN
F 1 "Conn_01x02" H 6320 3216 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6400 3450 50  0001 C CNN
F 3 "~" H 6400 3450 50  0001 C CNN
	1    6400 3450
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J409
U 1 1 606B29ED
P 6400 3950
F 0 "J409" H 6320 3625 50  0000 C CNN
F 1 "Conn_01x02" H 6320 3716 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6400 3950 50  0001 C CNN
F 3 "~" H 6400 3950 50  0001 C CNN
	1    6400 3950
	-1   0    0    1   
$EndComp
Text GLabel 6600 2500 2    50   Input ~ 0
VAC-
Text GLabel 6600 2925 2    50   Input ~ 0
VAC-
Text GLabel 6600 3450 2    50   Input ~ 0
VAC-
$Comp
L Projet_lib:SHT2x U?
U 1 1 606BB7FC
P 3750 5175
AR Path="/60567BB2/606BB7FC" Ref="U?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB7FC" Ref="U?"  Part="1" 
AR Path="/606B5193/606BB7FC" Ref="U?"  Part="1" 
AR Path="/60567BAF/606BB7FC" Ref="U?"  Part="1" 
AR Path="/60568659/606BB7FC" Ref="U401"  Part="1" 
F 0 "U401" H 3570 5221 50  0000 R CNN
F 1 "SHT2x" H 3570 5130 50  0000 R CNN
F 2 "Package_DFN_QFN:DFN-6-1EP_3x3mm_P1mm_EP1.5x2.4mm" H 3400 5125 50  0001 C CNN
F 3 "" H 3400 5125 50  0001 C CNN
	1    3750 5175
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 606BB803
P 3700 4650
AR Path="/60567BB2/606BB803" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB803" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606BB803" Ref="#PWR?"  Part="1" 
AR Path="/60567BAF/606BB803" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606BB803" Ref="#PWR0407"  Part="1" 
F 0 "#PWR0407" H 3700 4500 50  0001 C CNN
F 1 "+3.3V" H 3715 4823 50  0000 C CNN
F 2 "" H 3700 4650 50  0001 C CNN
F 3 "" H 3700 4650 50  0001 C CNN
	1    3700 4650
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 606BB809
P 3700 5475
AR Path="/60567BB2/606BB809" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB809" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606BB809" Ref="#PWR?"  Part="1" 
AR Path="/60567BAF/606BB809" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606BB809" Ref="#PWR0408"  Part="1" 
F 0 "#PWR0408" H 3700 5225 50  0001 C CNN
F 1 "GND" H 3705 5302 50  0000 C CNN
F 2 "" H 3700 5475 50  0001 C CNN
F 3 "" H 3700 5475 50  0001 C CNN
	1    3700 5475
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C?
U 1 1 606BB80F
P 3500 4775
AR Path="/60567BB2/606BB80F" Ref="C?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB80F" Ref="C?"  Part="1" 
AR Path="/606B5193/606BB80F" Ref="C?"  Part="1" 
AR Path="/60567BAF/606BB80F" Ref="C?"  Part="1" 
AR Path="/60568659/606BB80F" Ref="C404"  Part="1" 
F 0 "C404" V 3450 4675 50  0000 C CNN
F 1 "0.1 uF" V 3600 4775 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 3500 4775 50  0001 C CNN
F 3 "~" H 3500 4775 50  0001 C CNN
	1    3500 4775
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 4775 3700 4775
Wire Wire Line
	3700 4775 3700 4875
Wire Wire Line
	3700 4775 3700 4650
Connection ~ 3700 4775
Wire Wire Line
	3400 4775 3325 4775
Wire Wire Line
	3325 4775 3325 4875
$Comp
L power:GND #PWR?
U 1 1 606BB81C
P 3325 4875
AR Path="/60567BB2/606BB81C" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB81C" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606BB81C" Ref="#PWR?"  Part="1" 
AR Path="/60567BAF/606BB81C" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606BB81C" Ref="#PWR0406"  Part="1" 
F 0 "#PWR0406" H 3325 4625 50  0001 C CNN
F 1 "GND" H 3330 4702 50  0000 C CNN
F 2 "" H 3325 4875 50  0001 C CNN
F 3 "" H 3325 4875 50  0001 C CNN
	1    3325 4875
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 606BB822
P 2750 5025
AR Path="/606B5193/606BB822" Ref="J?"  Part="1" 
AR Path="/60567BAF/606BB822" Ref="J?"  Part="1" 
AR Path="/60568659/606BB822" Ref="J404"  Part="1" 
F 0 "J404" H 2670 5342 50  0000 C CNN
F 1 "Conn_01x04" H 2670 5251 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 2750 5025 50  0001 C CNN
F 3 "~" H 2750 5025 50  0001 C CNN
	1    2750 5025
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 606BB829
P 2350 4900
AR Path="/60567BB2/606BB829" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB829" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606BB829" Ref="#PWR?"  Part="1" 
AR Path="/60567BAF/606BB829" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606BB829" Ref="#PWR0401"  Part="1" 
F 0 "#PWR0401" H 2350 4750 50  0001 C CNN
F 1 "+3.3V" H 2365 5073 50  0000 C CNN
F 2 "" H 2350 4900 50  0001 C CNN
F 3 "" H 2350 4900 50  0001 C CNN
	1    2350 4900
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 606BB82F
P 2100 5025
AR Path="/60567BB2/606BB82F" Ref="#PWR?"  Part="1" 
AR Path="/60567BB2/605AE801/606BB82F" Ref="#PWR?"  Part="1" 
AR Path="/606B5193/606BB82F" Ref="#PWR?"  Part="1" 
AR Path="/60567BAF/606BB82F" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606BB82F" Ref="#PWR0402"  Part="1" 
F 0 "#PWR0402" H 2100 4775 50  0001 C CNN
F 1 "GND" H 2105 4852 50  0000 C CNN
F 2 "" H 2100 5025 50  0001 C CNN
F 3 "" H 2100 5025 50  0001 C CNN
	1    2100 5025
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2100 5025 2550 5025
Wire Wire Line
	2550 4925 2350 4925
Wire Wire Line
	2350 4925 2350 4900
Text GLabel 2550 5125 0    50   Input ~ 0
SDA_PI
Text GLabel 2550 5225 0    50   Input ~ 0
SCL_PI
Text GLabel 4100 5025 2    50   Input ~ 0
SDA_PI
Text GLabel 4100 5325 2    50   Input ~ 0
SCL_PI
$Comp
L Connector_Generic:Conn_01x02 J410
U 1 1 606D77E8
P 6400 4425
F 0 "J410" H 6320 4100 50  0000 C CNN
F 1 "Conn_01x02" H 6320 4191 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6400 4425 50  0001 C CNN
F 3 "~" H 6400 4425 50  0001 C CNN
	1    6400 4425
	-1   0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J401
U 1 1 606D77EF
P 7825 2500
F 0 "J401" H 7745 2175 50  0000 C CNN
F 1 "Conn_01x02" H 7745 2266 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7825 2500 50  0001 C CNN
F 3 "~" H 7825 2500 50  0001 C CNN
	1    7825 2500
	-1   0    0    1   
$EndComp
Text GLabel 6600 4425 2    50   Input ~ 0
VAC-
$Comp
L Connector_Generic:Conn_01x02 J402
U 1 1 606D7B73
P 7825 3000
F 0 "J402" H 7745 2675 50  0000 C CNN
F 1 "Conn_01x02" H 7745 2766 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7825 3000 50  0001 C CNN
F 3 "~" H 7825 3000 50  0001 C CNN
	1    7825 3000
	-1   0    0    1   
$EndComp
Text GLabel 8500 3350 2    50   Input ~ 0
EXT_OPT_FAN_IN
Text GLabel 8500 2850 2    50   Input ~ 0
BOITIER_FAN_IN
$Comp
L Connector_Generic:Conn_01x02 J403
U 1 1 606D8900
P 7825 3500
F 0 "J403" H 7745 3175 50  0000 C CNN
F 1 "Conn_01x02" H 7745 3266 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7825 3500 50  0001 C CNN
F 3 "~" H 7825 3500 50  0001 C CNN
	1    7825 3500
	-1   0    0    1   
$EndComp
Wire Wire Line
	8025 2400 8100 2400
Wire Wire Line
	8100 2400 8100 2350
Wire Wire Line
	8025 2500 8100 2500
Wire Wire Line
	8100 2500 8100 2525
Wire Wire Line
	8025 2900 8100 2900
Wire Wire Line
	8100 2900 8100 2850
Wire Wire Line
	8025 3000 8100 3000
Wire Wire Line
	8100 3000 8100 3050
Wire Wire Line
	8025 3400 8100 3400
Wire Wire Line
	8100 3400 8100 3350
Wire Wire Line
	8025 3500 8100 3500
Wire Wire Line
	8100 3500 8100 3550
$Comp
L Connector_Generic:Conn_01x02 J405
U 1 1 606DE3CA
P 2850 3075
F 0 "J405" H 2930 3067 50  0000 L CNN
F 1 "Conn_01x02" H 2930 2976 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 2850 3075 50  0001 C CNN
F 3 "~" H 2850 3075 50  0001 C CNN
	1    2850 3075
	1    0    0    -1  
$EndComp
Text GLabel 2650 3175 0    50   Input ~ 0
VAC-
Text GLabel 2650 3075 0    50   Input ~ 0
VAC+
Text GLabel 6600 2400 2    50   Input ~ 0
Heater
Text GLabel 6600 2825 2    50   Input ~ 0
DuctFan
Text GLabel 6600 3350 2    50   Input ~ 0
Dehumidificateur
Text GLabel 6600 4325 2    50   Input ~ 0
Ext_Light
Text GLabel 6600 3850 2    50   Input ~ 0
Humidificateur
Wire Notes Line
	5975 2050 9300 2050
Wire Notes Line
	4650 4375 4650 5950
Wire Notes Line
	4650 5950 1925 5950
Wire Notes Line
	1925 4375 4650 4375
Wire Notes Line
	1925 4375 1925 5950
Wire Notes Line
	2150 4075 4350 4075
Wire Notes Line
	4350 4075 4350 1975
Wire Notes Line
	4350 1975 2150 1975
Wire Notes Line
	2150 1975 2150 4075
Wire Wire Line
	8100 3350 8500 3350
Wire Wire Line
	8100 2850 8500 2850
Wire Wire Line
	8100 3050 8500 3050
Wire Wire Line
	8100 2350 8500 2350
Text GLabel 8500 2350 2    50   Input ~ 0
LED_FAN_IN
Wire Wire Line
	8100 3550 8500 3550
Text GLabel 8500 3550 2    50   Input ~ 0
EXT_OPT_FAN_OUT
Text GLabel 8525 2525 2    50   Input ~ 0
LED_FAN_OUT
Wire Wire Line
	8525 2525 8100 2525
Text GLabel 8500 3050 2    50   Input ~ 0
BOITIER_FAN_OUT
Text GLabel 6600 3950 2    50   Input ~ 0
24VAC-
Text GLabel 8525 3775 2    50   Input ~ 0
100W_LED+
Text GLabel 8525 3975 2    50   Input ~ 0
100W_LED-
$Comp
L Connector_Generic:Conn_01x02 J411
U 1 1 6061C7A8
P 7850 3925
F 0 "J411" H 7770 3600 50  0000 C CNN
F 1 "Conn_01x02" H 7770 3691 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7850 3925 50  0001 C CNN
F 3 "~" H 7850 3925 50  0001 C CNN
	1    7850 3925
	-1   0    0    1   
$EndComp
Wire Wire Line
	8050 3825 8125 3825
Wire Wire Line
	8125 3825 8125 3775
Wire Wire Line
	8050 3925 8125 3925
Wire Wire Line
	8125 3925 8125 3975
Wire Wire Line
	8125 3775 8525 3775
Wire Wire Line
	8125 3975 8525 3975
$Comp
L Connector_Generic:Conn_01x02 J?
U 1 1 6062459A
P 3900 3225
AR Path="/60567BAF/6062459A" Ref="J?"  Part="1" 
AR Path="/60568659/6062459A" Ref="J412"  Part="1" 
F 0 "J412" H 3980 3217 50  0000 L CNN
F 1 "Conn_01x02" H 3980 3126 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3900 3225 50  0001 C CNN
F 3 "~" H 3900 3225 50  0001 C CNN
	1    3900 3225
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR?
U 1 1 606245A1
P 3550 3225
AR Path="/60567BAF/606245A1" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606245A1" Ref="#PWR0105"  Part="1" 
F 0 "#PWR0105" H 3550 3075 50  0001 C CNN
F 1 "+12V" H 3565 3398 50  0000 C CNN
F 2 "" H 3550 3225 50  0001 C CNN
F 3 "" H 3550 3225 50  0001 C CNN
	1    3550 3225
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 3225 3700 3225
$Comp
L power:GND #PWR?
U 1 1 606245A8
P 3550 3325
AR Path="/60567BAF/606245A8" Ref="#PWR?"  Part="1" 
AR Path="/60568659/606245A8" Ref="#PWR0106"  Part="1" 
F 0 "#PWR0106" H 3550 3075 50  0001 C CNN
F 1 "GND" H 3555 3152 50  0000 C CNN
F 2 "" H 3550 3325 50  0001 C CNN
F 3 "" H 3550 3325 50  0001 C CNN
	1    3550 3325
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 3325 3700 3325
$Comp
L Connector_Generic:Conn_01x02 J?
U 1 1 606245AF
P 2850 2675
AR Path="/60567BAF/606245AF" Ref="J?"  Part="1" 
AR Path="/60568659/606245AF" Ref="J413"  Part="1" 
F 0 "J413" H 2930 2667 50  0000 L CNN
F 1 "Conn_01x02" H 2930 2576 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 2850 2675 50  0001 C CNN
F 3 "~" H 2850 2675 50  0001 C CNN
	1    2850 2675
	1    0    0    -1  
$EndComp
Text GLabel 2650 2775 0    50   Input ~ 0
24VAC-
Text GLabel 2650 2675 0    50   Input ~ 0
24VAC+
$Comp
L Connector_Generic:Conn_01x02 J?
U 1 1 60625CD5
P 3900 2600
AR Path="/60567BAF/60625CD5" Ref="J?"  Part="1" 
AR Path="/60568659/60625CD5" Ref="J414"  Part="1" 
F 0 "J414" H 3980 2592 50  0000 L CNN
F 1 "Conn_01x02" H 3980 2501 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 3900 2600 50  0001 C CNN
F 3 "~" H 3900 2600 50  0001 C CNN
	1    3900 2600
	1    0    0    -1  
$EndComp
Text GLabel 3700 2600 0    50   Input ~ 0
30Vdc
$Comp
L power:GND #PWR0107
U 1 1 60626A4D
P 3650 2775
F 0 "#PWR0107" H 3650 2525 50  0001 C CNN
F 1 "GND" H 3655 2602 50  0000 C CNN
F 2 "" H 3650 2775 50  0001 C CNN
F 3 "" H 3650 2775 50  0001 C CNN
	1    3650 2775
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 2775 3650 2700
Wire Wire Line
	3650 2700 3700 2700
Wire Notes Line
	9300 2050 9300 4925
Wire Notes Line
	5975 4925 9300 4925
Wire Notes Line
	5975 2050 5975 4925
Text Notes 2300 4000 0    50   ~ 0
Connecteurs interne
Text Notes 6350 4850 0    50   ~ 0
Connecteurs "externe"
$Comp
L Connector_Generic:Conn_01x02 J416
U 1 1 606940E5
P 7850 4375
F 0 "J416" H 7770 4050 50  0000 C CNN
F 1 "Conn_01x02" H 7770 4141 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 7850 4375 50  0001 C CNN
F 3 "~" H 7850 4375 50  0001 C CNN
	1    7850 4375
	-1   0    0    1   
$EndComp
Text GLabel 8525 4225 2    50   Input ~ 0
GPIO23_SIGPLEIN
Wire Wire Line
	8050 4275 8125 4275
Wire Wire Line
	8125 4275 8125 4225
Wire Wire Line
	8050 4375 8125 4375
Wire Wire Line
	8125 4375 8125 4425
Wire Wire Line
	8125 4225 8525 4225
Wire Wire Line
	8125 4425 8525 4425
$Comp
L power:GND #PWR?
U 1 1 6069DC39
P 8525 4425
F 0 "#PWR?" H 8525 4175 50  0001 C CNN
F 1 "GND" H 8530 4252 50  0000 C CNN
F 2 "" H 8525 4425 50  0001 C CNN
F 3 "" H 8525 4425 50  0001 C CNN
	1    8525 4425
	1    0    0    -1  
$EndComp
$EndSCHEMATC
