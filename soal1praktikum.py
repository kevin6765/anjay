#Opening untuk meperbagus tampilam
print('------------------------------- LOADING -------------------------------------')
print()
print('Selamat datang di program pengubah suhu dari celcius ke semua suhu')

#INPUT
celcius = int(input('Silahkan masukan angka celciusnya > '))

#PROSES
reamur = (4/5) * celcius
kelvin = celcius + 273
farenheit = (9/5) * celcius + 32
print()

#OUTPUT
print('-------------------- Sedang memproses pengubahan suhu ------------------------')
print()
print("Suhu awal yaitu", celcius, 'celcius berubah menjadi', round(reamur, 2), "reamur")
print("Suhu awal yaitu", celcius, 'celcius berubah menjadi', round(kelvin, 2), "kelvin")
print("Suhu awal yaitu", celcius, 'celcius berubah menjadi', round(farenheit, 2), "farenheit")
print()
print('-------------------- Proses pengubahan suhu telah selesai --------------------')