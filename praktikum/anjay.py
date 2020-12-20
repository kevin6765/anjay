b = 1
while b == 1:
    z = 0
    print('\n============================================================')
    print('\tSelamat Datang di Program List Dinamis Python')
    print('Terdapat 2 Mode yaitu 1. Mode langsung dan 2. Mode isi list')
    a = int(input('Masukan pilihan = '))
    if a == 1:
        while a == 1:
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            list5 = [13,31,2,19,96]
            print('============================================================')
            print('\tSelamat Datang di Mode langsung')
            print('Terdapat 4 pilihan yaitu\n1. Output satu\n2. Output dua\n3. Output tiga\n4. Output empat')
            pilihan = int(input('Silahkan pilih (1/2/3/4) = '))
            i = 0
            z = 0
            if pilihan == 1:
                while i < 13:
                    input1 = str(input('Masukan nama hewan hingga 13 ekor = '))
                    list1.append(input1)
                    i += 1
                while z < 5:
                    input2 = int(input('Masukan 5 tanggal lahir teman Anda = '))
                    list4.append(input2)
                    z += 1
                print('============================================================')
                print('Output 1 adalah = ', list1[0:5] + list4)

            elif pilihan == 2:
                while i < 5:
                    input1 = str(input('Masukan 5 nama teman terdekat anda = '))
                    list2.append(input1)
                    i += 1
                list2[4] = input('Masukan list pengganti untuk index ke empat = ')
                print('============================================================')
                print('Output 2 adalah = ', list2)

            elif pilihan == 3:
                list5.remove(96)
                list5.remove(2)
                print('============================================================')
                print('Output 3 adalah = ', list5)

            elif pilihan == 4:
                while z < 5:
                    input2 = int(input('Masukan 5 tanggal lahir teman Anda = '))
                    list4.append(input2)
                    z += 1
                    list7 = list4 + list5
                print('============================================================')
                print('Nilai max dan minimal antara list4 dan list5 adalah = ', 'max', max(list7), 'min', min(list7))
            else:
                print('============================================================')
                print('Perintah yang anda masukan salah, silahkan coba lagi')
                continue

            print('============================================================')
            print('Program telah selesai | 1. Ulang Program | 2. Selesai | 3. Balik Ke Menu Awal')
            y = 0
            while y == 0:
                ulang = int(input('Masukan pilihan Anda (1/2/3) = '))
                if ulang == 1:
                    y += 1
                    break
                elif ulang == 2:
                    y += 2
                    break
                elif ulang == 3:
                    y += 3
                    break
                else:
                    print('\nPerintah yang anda masukan error, silahkan coba lagi')
                    continue
            if y == 1:
                continue
            elif y == 2:
                z += 1
                break
            else:
                z += 2
                break 
    
    elif a == 2:
            i = 0
            while i == 0:
                list1 = []
                list2 = []
                list3 = []
                list4 = []
                list5 = [13,31,2,19,96]
                print('============================================================')
                print('\tSelamat Datang di Mode isi list')
                print('============================================================')
                for d in range(13):
                    input1 = str(input('Masukan nama hewan hingga 13 ekor = '))
                    list1.append(input1)
                for e in range(5):
                    input1 = str(input('Masukan nama hewan berkaki 2 hingga 5 ekor = '))
                    list2.append(input1)
                for f in range(5):
                    input1 = str(input('Masukan 5 nama teman terdekat anda = '))
                    list3.append(input1)
                for g in range(5):
                    input1 = int(input('Masukan 5 tanggal lahir teman tersebut = '))
                    list4.append(input1)
                print('Inputan telah selesai, silahkan pilih output yang inginkan\n1. Output satu\n2. Output dua\n3. Output tiga\n4. Output empat')

                pilihan = int(input('Silahkan masukan pilihan = '))
                if pilihan == 1:
                    print('============================================================')
                    print('Output 1 adalah = ', list1[0:5] + list4)
                elif pilihan == 2:
                    print('============================================================')
                    print('Output 2 adalah = ', list2)
                elif pilihan == 3:
                    list5.remove(96)
                    list5.remove(2)
                    print('============================================================')
                    print('Output 3 adalah = ', list5)
                elif pilihan == 4:
                    print('============================================================')
                    print('Nilai max dan minimal antara list4 dan list5 adalah', max(list7), min(list7))
                else:
                    print('\nPerintah yang anda masukan error, silahkan coba lagi')
                    continue
                print('============================================================')
                print('Program telah selesai | 1. Ulang Program | 2. Selesai | 3. Balik Ke Menu Awal')
                x = 0
                while x == 0:
                    ulang2 = int(input('Masukan pilihan Anda (1/2/3) = '))
                    if ulang2 == 1:
                        x += 1
                        break
                    elif ulang2 == 2:
                        x += 2
                        break
                    elif ulang2 == 3:
                        x += 3
                        break
                    else:
                        print('\nPerintah yang anda masukan error, silahkan coba lagi')
                        continue
                if x == 1:
                    continue
                elif x == 2:
                    z += 1
                    break
                else:
                    z += 2
                    break 

    else:
        print('Perintah yang anda masukan salah, silahkan coba lagi')
        continue

    e = 0
    while z < 3:
        if z == 1:
            e += 1
            break
        elif z == 2:
            e += 2
            break
    
    if e == 1:
        break
    else:
        continue