print('------- Selamat datang di program menghitung status umur -------')

#INPUT
umur_kalian = int(input('\nSilahkan masukan umur kalian = '))
print('\n--------- MOHON DITUNGGU, SISTEM SEDANG MEMPROSES DATA ---------\n')

#PROSES + OUTPUT
if 0 <= umur_kalian <= 7:
    print('Yeay, kamu terdeteksi berstatus Balita')
elif 7 <= umur_kalian <= 17:
    print('Yeay, kamu terdeteksi berstatus Anak-anak')    
elif 17 <= umur_kalian <= 25:
    print('Yeay, kamu terdeteksi berstatus Dewasa')
elif 25 <= umur_kalian <= 50:
    print('Yeay, kamu terdeteksi berstatus Muda')
else :
    print('Yeay, kamu terdeteksi berstatus Tua')

print('Program telah selesai, ingin mencobanya lagi?')