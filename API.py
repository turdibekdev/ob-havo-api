import requests
from bs4 import BeautifulSoup
import datetime


class OB_HAVO():
	
	
	def __init__(self, viloyat):
		
		viloyat_nomi = link_aniqlash(viloyat)
		
		sahifa = f"https://obhavo.uz/{viloyat_nomi}"
		global request
		request = requests.get(sahifa)
		global soup
		soup = BeautifulSoup(request.text, "html.parser")
		dt = datetime.datetime.now()

		
		NSHB = soup.find_all(class_ = "col-1")[0].text.split()
		vaqt = soup.find_all(class_ = "current-day")[0].text.split()
		CHB = soup.find_all(class_ = "col-2")[0].text.split()
		TKO = soup.find_all(class_ = "forecast")
		MIN_h = str(soup.find_all(class_ = "current-forecast")).split()
		MIN_H = MIN_h[7].split("<")[1]
		
		
		self.sana = f"{vaqt[1]}-{vaqt[2]}"
		self.soat = f"{dt.hour}:{dt.minute}"
		self.quyosh_chiqishi = CHB[5]
		self.quyosh_botishi = CHB[-1]
		self.harorat_kun = TKO[1].text
		self.harorat_max = soup.strong.text
		self.harorat_min = MIN_H.split(">")[1]
		self.harorat_tongi = TKO[0].text
		self.harorat_oqshomgi = TKO[2].text
		self.namlik = NSHB[1]
		self.shamol_yonalishi = NSHB[3]
		self.shamol_tezligi = f"{NSHB[4]} {NSHB[5]}"
		self.bosim = f"{NSHB[7]} {NSHB[8]} {NSHB[9]} {NSHB[10]}"
		
		
		
	
class KUNLAR():
	
	def __init__(self, viloyat, i):
		if i >= 1 and i <= 7:
			
			viloyat_nomi = link_aniqlash(viloyat)
			
			sahifa = f"https://obhavo.uz/{viloyat_nomi}"
			global request
			request = requests.get(sahifa)
			global soup
			soup = BeautifulSoup(request.text, "html.parser")
			dt = datetime.datetime.now()
			
			KKUN = soup.find_all(class_ = "weather-row-day")[i].text.split()
			KKUNDIZ = soup.find_all(class_ = "forecast-day")[i-1].text.split()
			KTUN = soup.find_all(class_ = "forecast-night")[i-1].text.split()
			TAVSIF = soup.find_all(class_ = "weather-row-desc")[i].text.split()
			TAVSIFF = ""
			for t in TAVSIF:
				TAVSIFF += f"{t} "
			
			self.kun = f"{KKUN[0]} {KKUN[1]}-{KKUN[2]}"
			self.kundiz = KKUNDIZ[0]
			self.tun = KTUN[0]
			self.tavsif = TAVSIFF

		else:
			print("XATO: siz chegaradan chiqdingiz")
			
def link_aniqlash(viloyat):
	m = viloyat.upper()
	
	if m == "TOSHKENT":
		return "tashkent"
	elif m == "ANDIJON":
		return "andijan"
	elif m == "BUXORO":
		return "bukhara"
	elif m == "GULISTON":
		return "gulistan"
	elif m == "JIZZAH":
		return "jizzakh"
	elif m == "ZARAFSHON":
		return "zarafshan"
	elif m == "QARSHI":
		return "karshi"
	elif m == "NAVOIY":
		return "navoi"
	elif m == "NAMANGAN":
		return "namangan"
	elif m == "NUKUS":
		return "nukus"
	elif m == "SAMARQAND":
		return "samarkand"
	elif m == "TERMIZ":
		return "termez"
	elif m == "URGANH":
		return "urgench"
	elif m == "FARG'ONA":
		return "ferghana"
	elif m == "XIVA":
		return "khiva"