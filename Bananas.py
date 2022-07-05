# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:12:50 2021

@author: kYcu
"""


from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import csv


from random import*
from time import*


zip_url_lotto = "https://media.fdj.fr/static/csv/loto/loto_201911.zip"
zpi_url_euromillions ="https://media.fdj.fr/static/csv/euromillions/euromillions_202002.zip"


with urlopen(zip_url_lotto) as f:
    with BytesIO(f.read()) as b, ZipFile(b) as myzipfile:
         myzipfile.extract('loto_201911.csv')
#        foofile_lotto = myzipfile.open('loto_201911.csv')
#        print(foofile_lotto.read())


lol= open('loto_201911.csv', "r")
csv_lol_reader = csv.reader(lol,delimiter=";")

next(csv_lol_reader)
number_of_rows = 0
list_from_lol = []
list_stars = []
last_date = []

for row in csv_lol_reader:
    number_of_rows = number_of_rows + 1
    # print(row[4],row[5],row[6],row[7],row[8],row[9])
    list_from_lol.append(row[4])
    list_from_lol.append(row[5])
    list_from_lol.append(row[6])
    list_from_lol.append(row[7])
    list_from_lol.append(row[8])
    list_stars.append(row[9])
    last_date.append(row[2])
    if number_of_rows > 5:
        break

print(last_date[0])
print(list_from_lol)
print(list_stars)

main_list = list(map(int,list_from_lol))
main_stars_list = list(map(int,list_stars))


lucky = sample(main_list,k=5)
luckyStars = sample(main_stars_list,k=1)



lucky.sort()
luckyStars.sort()

print("Random prediction for next lotto game")
print(lucky)
print(luckyStars)