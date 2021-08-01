from API import OB_HAVO, KUNLAR


misol_uchun_viloyatlar = ["Toshkent", "Andijon", "Buxoro", "Guliston", "Jizzax", "Zarafshon", "Qarshi", "Novoiy", "Namangan", "Samarqand", "Termiz", "Urganch", "Farg'ina", "Xiva"]

viloyat = "Nukus" # O'zbekiston viloyatlaridan birini yozing


def bugungi_ob_havo():
	con = OB_HAVO(viloyat)
	
	print("Bugungi kun:", con.sana)
	print("Soat:", con.soat)
	print("Quyosh chiqishi:", con.quyosh_chiqishi)
	print("Quyosh botishi:", con.quyosh_botishi)
	print("O'rtacha harorat:", con.harorat_kun)
	print("Yuqori harorat:", con.harorat_max)
	print("Past harorat:", con.harorat_min)
	print("Tongi harorat:", con.harorat_tongi)
	print("Oqshomgi harorat:", con.harorat_oqshomgi)
	print("Namlik:", con.namlik)
	print("Shamol yonalishi:", con.shamol_yonalishi)
	print("Shamol tezligi:", con.shamol_tezligi)
	print("Bosim:", con.bosim, "\n")

		
def yetti_kunlik_ob_havo():
	for i in range(1, 8):
		conn = KUNLAR(viloyat, i)
		
		print("Sanasi:", conn.kun)
		print("Kudizgi harorat:", conn.kundiz)
		print("Tungi harorat:", conn.tun)
		print("Tavsif:", conn.tavsif,"\n")
		
def soralgan_kun():
	# bugundan keyingi 7 kun ob-havo malumotlarini aniqlab beradi
	# kiritilgan son 1 dan 8 gacha bo'lishi shart
	kun = 3
	connn = KUNLAR(viloyat, kun)
	
	print("Sanasi:", connn.kun)
	print("Kundizgi harorat:", connn.kundiz)
	print("Tungi harorat:", connn.tun)
	print("Tavsif:", connn.tavsif, "\n")
	
## bugungi kun malumoti
#bugungi_ob_havo()

## yetti kunlik malumot
yetti_kunlik_ob_havo()

## soralgan kun malumoti
#soralgan_kun()