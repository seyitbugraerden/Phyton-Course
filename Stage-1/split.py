kullanici = "Ankara Yenimahalle 06"
user = "Ankara;Yenimahalle;06"
print(kullanici.split()) #Diziye dönüşüm için kullanım ['Ankara', 'Yenimahalle', '06']
print(user.split(";")) #split içine hangi ifadeye göre ayırmak istediğimi seçebiliyoruz

print("Adı = " + kullanici.split()[0]) # İki string değerleri bu şekilde kullanılabilir.