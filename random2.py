kwh_pln = int(input('Masukan kwhmu '))
harga1 = 1000
harga2 = 500
if kwh_pln > 20:
    kwh_total = kwh_pln - 20
    print(kwh_total)
    kwh_harga = (kwh_pln * harga1) + (kwh_total * harga2)
else:
    kwh_harga = (kwh_pln * harga1)

print (kwh_harga)