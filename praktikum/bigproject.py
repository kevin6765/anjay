a = 0
e = 0

def command2():
	j = 0
	while j == 0:
		T = []
		T2 = (10, 30, 45, 21, 12, 13, 31, 90)
		T3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')
		print('============================================================')
		print('\tSelamat Datang di Mode langsung')
		print('Terdapat 2 pilihan yaitu 1. Output satu dan 2. Output dua')
		pilihan1 = int(input('Silahkan masukan pilihan Anda (1/2) = '))
		print('============================================================')
		if pilihan1 == 1:
			k = 0
			for i in range(0, 5):
				T.append(str(input('masukan nama kendaraan hingga 5 buah = ')))
			print('============================================================')
			T1 = tuple(T)
			print('Output 1 adalah =', T3[1], T3[3], T3[4], T1[4], T1[2])

		elif pilihan1 == 2:
			print('Output 2 adalah =')
			for c in range(3):
				print(T2[3], 'dan', T2[5])
		else:
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
			a += 1
			break
			return
		else:
			menu()
			return
	return

def command3():
	m = 0
	while m == 0:
		T = []
		T2 = (10, 30, 45, 21, 12, 13, 31, 90)
		T3 = ('pRaktikum', 'praktikum', 'Praktikum', 'PraKtIkuM', 'PRAKTIKUM')
		print('============================================================')
		print('\tSelamat Datang di Mode isi list')
		print('============================================================')
		for i in range(0, 5):
			T.append(str(input('masukan nama kendaraan hingga 5 buah = ')))
		T1 = tuple(T)
		print('Silahkan pilih 1. Output satu | 2. Output dua')
		pilihan3 = int(input('Masukan pilihan Anda (1/2) = '))

		if pilihan3 == 1:
			print('Output 1 adalah =', T3[1], T3[3], T3[4], T1[4], T1[2])
		elif pilihan3 == 2:
			print('Output 2 adalah =')
			for c in range(3):
				print(T2[3], 'dan', T2[5])
		else:
			print('perintah yang anda masukan salah, silahkan coba lagi')
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
			menu()
			return

def menu():
	i = 0
	while i == 0:
		print('\n============================================================')
		print('\tSelamat Datang di Program Tuple Dinamis Python')
		print('Terdapat 2 Mode yaitu 1. Mode langsung dan 2. Mode isi list')
		pilihan = int(input('Silahkan masukan pilihan Anda (1/2) = '))

		if pilihan == 1:
			command2()
		elif pilihan == 2:
			command3()
		else:
			print('Perintah yang anda masukan salah, silahkan coba lagi')
			continue
		
		if a == 1:
			return
	return menu()
print(menu())