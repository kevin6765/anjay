jam_kerja = int(input('masukan jam kerjamu'))
gaji = 100000
tambahan = 20000
if jam_kerja >= 10:
    lembur = jam_kerja - 10
    rumus = (lembur * tambahan) + gaji
else:
    rumus = jam_kerja + gaji

print(rumus)