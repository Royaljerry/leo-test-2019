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

# =========== Task #2 ===========

car_statuses = [
	"ki",
	"be"
]

user_input = input("Nap: ")

for record in car_records: 
	fields = record.strip().split()
	if (fields[0] == user_input):
		car_status = car_statuses[int(fields[5])]
		car_out_string = fields[1] + fields[2] + fields[4] + str(car_status)
		print(car_out_string)

# =========== Task #3 ===========

cars_rented = []

for record in car_records: 
	fields = record.strip().split()

	if (fields[5] == "0"): 
		cars_rented.append(fields[2])
	else: 
		cars_rented.remove(fields[2])
print ("A hónap végén " + str(len(cars_rented)) +" autót nem hoztak vissza.")