lampColor = input('Masukkan warna lampu (hijau/merah): ')
if lampColor == 'merah':
    distance = int(input('Masukkan jarak persembunyian: '))
    if distance >= 5:
        message = 'Baik, mari kita ke tempat persembunyian dengan motor'
    else:
        message = 'Baik, mari kita ke tempat persembunyian dengan jalan kaki'
if lampColor == 'hijau':
    Enemy = int(input('Masukkan jumlah musuh: '))
    if Enemy >= 5:
        message = 'Okey, kita serang musuh dengan granat'
    else:
        message = 'Okey, kita serang musuh dengan pisau'

print(message)

    