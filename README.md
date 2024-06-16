# Реализация небольшой сети офиса
## Схема сети:
![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/network.jpg)
## Параметры конфигурации
## VPC1
```
VPCS> set pcname VPC1
VPC1> ip 10.0.10.1/24 10.0.10.2
Checking for duplicate address...
VPC1 : 10.0.10.1 255.255.255.0 gateway 10.0.10.2
```

## VPC2
```
VPCS> set pcname VPC2

VPC2> ip 10.0.20.1/24 10.0.20.2
Checking for duplicate address...
VPC2 : 10.0.20.1 255.255.255.0 gateway 10.0.20.2
```

## R1
```
enable
configure terminal
interface Gi0/0
no shutdown
exit

interface Gi0/0.10
encapsulation dot1q 10
ip address 10.0.10.2 255.255.255.0
exit

interface Gi0/0.20
encapsulation dot1q 20
ip address 10.0.20.2 255.255.255.0
exit
exit

write memory
```

## SW1
```
enable
configure terminal
vlan 10
exit
vlan 20
exit

interface Gi0/0
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Gi0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Gi0/2
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

spanning-tree mode pvst
spanning-tree extend system-id
spanning-tree vlan 10,20 priority 0
exit

write memory
```

## SW2
```
enable
configure terminal
vlan 10
exit
vlan 20
exit

interface Gi0/0
switchport mode access
switchport access vlan 10
exit

interface Gi0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Gi0/2
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

exit
write memory
```

## SW3
```
enable
configure terminal
vlan 10
exit
vlan 20
exit

interface Gi0/0
switchport mode access
switchport access vlan 20
exit

interface Gi0/1
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface Gi0/2
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

exit
write memory
```


## Validation
## Pings:
![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/ping1.jpg)
![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/ping2.jpg)
## Spanning Trees:

SW1

![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/treeSW1.jpg)

SW2

![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/treeSW2.jpg)

SW3

![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/treeSW2.jpg)
## Отказоустоичивость (на SW3 отключаем Gi0/1)
```
enable
configure terminal
interface Gi0/1
shutdown
exit
exit
exit
```

Пинги с обоих PC

![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/ping_stable1.jpg)
![image](https://github.com/GoldeneyeAF/networks_2024_labs/blob/main/images/ping_stable2.jpg)
