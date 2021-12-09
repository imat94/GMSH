
import gspread
import requests

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
reponse = requests.get('https://raw.githubusercontent.com/imat94/GMSH/main/okok.json').json()
client = gspread.service_account_from_dict(reponse)

data = client.open('TÀI KHOẢN DIỄN ĐÀN GMSH').values_get(range='THÁNG 12' + '!B:D')['values']
for lists in data:
	if 'NHUNGLKLK' in lists:
		print(lists)
		