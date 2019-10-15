#!/usr/bin/env python3

car_obj = open('autok.txt', 'r')
car_records = car_obj.readlines()
car_obj.close()

# =========== Task #1 ===========

car_returned_day = ''
car_returned_id = ''

for record in car_records:
	fields = record.strip().split()
	if (fields[5] == "0"):
		car_returned_day = fields[0]
		car_returned_id = fields[2]

if (car_returned_day != ''):
	print (car_returned_day + ". nap rendszám: " + car_returned_id)
else:
	print ("Nincs ilyen autó")

