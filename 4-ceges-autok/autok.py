#!/usr/bin/env python3

autok_obj = open('autok.txt', 'r')
autok_content = autok_obj.readlines()
autok_obj.close()

for record in autok_content:
	field = record.strip().split()[0]
	print(field)
	# print(record.strip())

# iterálás az összes elemen (for…)
# ha az adott record utolsó field-je = 0 => első field megjegyzése