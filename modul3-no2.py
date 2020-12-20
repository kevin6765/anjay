#TAMPILAN AWAL
print('============= Selamat datang di program pendeteksi bilangan prima =============\n')
print('Kami menyediakan 2 Metode perhitungan bilangan prima, silahkan pilih salah satu')
print('Ketik 0 untuk metode satuan dan 1 untuk metode rentang')
y = 0

while y == 0:
    #INPUT AWAL + LOOPING
    perintah = int(input('\nMasukan pilihan anda = '))

    if perintah == 0:
        #INPUT LANJUTAN
        angka = int(input('Silahkan masukan angka yang ingin di deteksi = '))
        
        #PROSES & OUTPUT
        if angka > 1:
            for i in range(2,angka):
                if (angka % i) == 0:
                    print ("\nMaaf", angka, "bukan bilangan prima")
                    print ("karena", i,"dikalikan",angka//i,"hasilnya adalah",angka)
                    break
            else:
                print ("\nSelamat", angka, "adalah bilangan prima")
        else:
            print ("\nMaaf", angka, "bukan bilangan prima")
        print('\n====== PROSES TELAH SELESAI ========')
        break

    elif perintah == 1:
        #INPUT LANJUTAN
        Angka1 = int(input('\nSilahkan masukan angka pertama = ')) 
        Angka2 = int(input('Silahkan masukan angka kedua = '))
        print("\nBilangan prima antara", Angka1,"and", Angka2,":\n") 

        #PROSES & OUTPUT
        for a in range(Angka1, Angka2 + 1):
            if a > 1:  
                for z in range(2, a): 
                    if (a % z) == 0: 
                        break
                    else:
                        print(a)
                        break 
            else:
                print('Angka yang anda masukan salah, silahkan coba lagi!')
                break
        print('\n======= PROSES TELAH SELESAI =======')    
        break
    
    #LOOPING
    else:
        print('\nPerintah yang anda masukan salah, silahkan coba lagi')
        continue 