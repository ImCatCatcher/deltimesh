#!/usr/bin/python3
import os, json

#Запрашиваем список снапшотов, фильтруем и записываем в файл
os.system(f"timeshift --list | grep 'Before Offline Update' >> /tmp/.ccbuffer")

#Открываем файл и проводим подготовку
with open("/tmp/.ccbuffer") as f:
    r = list(i.strip() for i in f.readlines())
    r = list(i.split()[2] for i in r)
    
    #Перебираем снапшоты и удаляем каждый
    for i in r: os.system(f"timeshift --delete --snapshot '{i}'")

#Удаляем временный файл
os.system(f"rm /tmp/.ccbuffer")
