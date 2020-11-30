day = 0
body_condition = False
while (not body_condition):
    day += 1
    suhu_tubuh = float(input(f'Masukkan suhu tubuh hari ke-{day} : '))
    if suhu_tubuh >= 36.5 and suhu_tubuh <= 37.2:
        body_condition = True
        print('Suhu tubuh sudah normal, pengobatan selesai, terima kasih.')
    elif suhu_tubuh < 36.5:
        body_condition = False
        print('Anda harus makan obat hipotermia')
    elif suhu_tubuh > 37.2:
            body_condition = False
            print('Anda harus makan obat demam')