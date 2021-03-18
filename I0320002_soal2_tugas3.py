#membuat dictionary pada python

dict = {'Name': 'Adrian', 'Hobi1': 'Nonton Film atau Drama', 'Hobi2': 'Baca Novel', 'Hobi3': 'Rebahan', 'Line': 'elnoir', 'Instagram': 'rlaxk_s', 'Twitter': 'rlaxk_s', 'Lagu Kesukaan1': 'Me After You', 'Lagu Kesukaan2': 'all of my life', 'Lagu Kesukaan3': 'Breathe', 'Makanan Favorit1': 'Steak', 'Makanan Favorit2': 'Keju', 'Makanan Favorit3': 'Ramyeon'}

print(dict)

#mengubah salah satu hobi dan sosial media

dict['Hobi3'] = 'Main Game'
dict['Instagram'] = 'kxx_as'

print(dict)

#menghapus dua makanan favorit

del dict['Makanan Favorit1']
del dict['Makanan Favorit2']

print(dict)

#menambah satu hobi

dict['Hobi4'] = 'Dengar Lagu'

print(dict)