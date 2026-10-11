#soal1
print('soal no 1')
usia = int(input('Masukkan usia: '))
departemen = input('Masukkan nama departemen: ')
hasil = usia >= 19 and 'Statistika' in departemen
print({hasil})
#soal 2
print('soal no 2')
data_pelanggan = ('Andi', 'Premium')
berat_kardus = [40, 35, 30]
nama, status = data_pelanggan
total_berat = sum(berat_kardus)
vip = status == 'Premium' or total_berat > 100
print('Nama pelanggan: ', {nama})
print('Total berat: ', {total_berat}, 'kg')
print('Apakah pengiriman masuk jalur VIP? ', {vip})
#soal 3
print('soal no 3')
ipk = float(input('Masukkan IPK: '))
riwayat_nilai = ['A', 'B', 'A', 'C']
hasil = ipk >= 3.50 and 'E' not in riwayat_nilai
print({hasil})