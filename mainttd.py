from ttdau import *
import random
import string
import sys,os
import gspread
import requests
import pandas as pd
import concurrent.futures


# SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
reponse = requests.get('https://raw.githubusercontent.com/imat94/GMSH/main/okok.json').json()
client = gspread.service_account_from_dict(reponse)
mainclient = client.open_by_url(
	'https://docs.google.com/spreadsheets/d/1wx67vV8qPVgfxPkchs_3QnKmCbH16d_roeIQ4O-Qz2c/'
	)

sh = ['THÁNG 12','2020-2019','2021']
with concurrent.futures.ThreadPoolExecutor() as job:
	for sh_name in sh:
		future = job.submit(lambda:mainclient.worksheet(sh_name))
		return_value = future.result()
		if sh_name =='THÁNG 12':gctt = return_value
		elif sh_name =='2020-2019':gc1920= return_value
		else:gc21= return_value




LIST_TKTRONGTHANG = []
LIST_1920 = []
LIST_21 = []
LIST_QC = []
LIST_XUPHAT = []


LIST_CQ_C2, LIST_CQ_C3, LIST_CQ_Q, LIST_CQ_TH,LIST_CQ_Z =[],[],[],[],[]

all_list = [LIST_CQ_C2,LIST_CQ_C3,LIST_CQ_Q,LIST_CQ_TH,LIST_CQ_Z]
all_data = os.listdir('./data')
for i in range(len(all_list)):
	all_list[i] = open('data/'+all_data[i],encoding='utf-8').readlines()


class Main(QtWidgets.QMainWindow,Ui_MainWindow):
	def  __init__(self):
		super().__init__()

		self.setupUi(self)
		self.setupButton()
		if len(LIST_TKTRONGTHANG) <= 0:
			self.label_25.setText('Vui lòng nạp dữ liệu')


		self.auto_reload()

		self.list_username = gctt.col_values(2)
		

	def new_cell(self,value):
		global last_row 
		self.list_username = gctt.col_values(2)
		self.last_row = len(self.list_username)

		name = self.lineEdit.text()
		if name =='':
			self.label_25.setText('Vui lòng điền tên tài khoản')
			return
		elif name in self.list_username:
			row = self.list_username.index(name)
			self.label_25.setText(f'Tài khoản đã tồn tại dòng {row+1}')
			return

		daily = self.comboBox.currentText()
		note = self.lineEdit_22.text()

		gctt.update_acell(f"B{self.last_row+1}", value=name)
		gctt.update_acell(f"C{self.last_row+1}", value=daily)
		gctt.update_acell(f"D{self.last_row+1}", value=note)
		self.label_25.setText('Thêm thành công')
	# def update_cell(self):
	# 	self.list_username = gc.col_values(2)
	# 	self.last_row = len(self.list_username)
	# 	name = self.lineEdit.text()
	# 	row = self.list_username.index(name)
	# 	daily = self.lineEdit_20.text()
	# 	note  = self.comboBox_2.currentText()
	# 	if name in self.list_username:
	# 		if daily !='':
	# 			row = self.list_username.index(name)+1
	# 			gc.update_acell(f"C{row}", value=daily)
	# 		gc.update_acell(f"D{row}", value=note)

	def update_cell1920(self):
		self.list_username = gc1920.col_values(1)
		self.last_row = len(self.list_username)
		name = self.lineEdit.text()
		row = self.list_username.index(name)+1
		ghichu = self.lineEdit_20.text()
		trangthai  = self.comboBox_2.currentText()
		if name in self.list_username:
			if ghichu !='':
				gc1920.update_acell(f"C{row}", value=ghichu)
			gc1920.update_acell(f"E{row}", value=trangthai)

	def update_cell21(self):
		self.list_username = gc21.col_values(1)
		self.last_row = len(self.list_username)
		name = self.lineEdit.text()
		row = self.list_username.index(name)+1
		ghichu = self.lineEdit_21.text()
		trangthai  = self.comboBox_3.currentText()
		if name in self.list_username:
			if ghichu !='':
				gc21.update_acell(f"C{row}", value=ghichu)
			gc21.update_acell(f"E{row}", value=trangthai)
		print(row)



	def setupButton(self):

		#Cài đặt event click cho KHÁCH TÌM VỀ
		self.pushButton.clicked.connect(self.hoinguon)
		self.pushButton_2.clicked.connect(self.hoinguonn)
		self.pushButton_6.clicked.connect(self.chaocangi)
		self.pushButton_7.clicked.connect(self.ketbanfb)
		self.pushButton_3.clicked.connect(self.xinsdt1)
		self.pushButton_4.clicked.connect(self.xinsdt2)
		self.pushButton_5.clicked.connect(self.xinso)
		self.pushButton_88.clicked.connect(self.khoinhom)
		self.pushButton_8.clicked.connect(self.quyenloi)
		self.pushButton_12.clicked.connect(self.kulagi)
		#Cài đặt event click cho Tạo nhóm hướng dẫn
		self.pushButton_14.clicked.connect(self.taonhomku)
		self.pushButton_15.clicked.connect(self.taonhomtha)
		self.pushButton_33.clicked.connect(self.taonhomnap)
		self.pushButton_16.clicked.connect(self.timlaimk)
		self.pushButton_20.clicked.connect(self.angocanh)
		self.pushButton_21.clicked.connect(self.pngocanh)
		self.pushButton_23.clicked.connect(self.amytu)
		self.pushButton_25.clicked.connect(self.cmytu)
		self.pushButton_17.clicked.connect(self.thanhngan)
		self.pushButton_27.clicked.connect(self.ngochuong)
		self.pushButton_29.clicked.connect(self.kimoanh)
		self.pushButton_31.clicked.connect(self.nhiwinny)
		self.pushButton_19.clicked.connect(self.angocanhtl)
		self.pushButton_22.clicked.connect(self.pngocanhtl)
		self.pushButton_24.clicked.connect(self.amytutl)
		self.pushButton_26.clicked.connect(self.cmytutl)
		self.pushButton_18.clicked.connect(self.thanhngantl)
		self.pushButton_28.clicked.connect(self.ngochuongtl)
		self.pushButton_30.clicked.connect(self.kimoanhtl)
		self.pushButton_32.clicked.connect(self.nhiwinnytl)
		self.pushButton_60.clicked.connect(self.thongbaotaonhom)
		self.pushButton_61.clicked.connect(self.hoitinhhinh)
		#Cài đặt event click cho CẤP TÀI KHOẢN
		self.pushButton_77.clicked.connect(self.hdsudung)
		self.pushButton_79.clicked.connect(self.noiquy)
		self.pushButton_84.clicked.connect(self.nhactk)
		self.pushButton_47.clicked.connect(self.randommk)
		self.pushButton_81.clicked.connect(self.guitk)
		self.pushButton_78.clicked.connect(self.taodan)
		self.pushButton_80.clicked.connect(self.phongchat)
		#Cài đặt event click cho ZALO
		self.pushButton_49.clicked.connect(self.chaocangi)
		self.pushButton_48.clicked.connect(self.kosogg)
		self.pushButton_65.clicked.connect(self.khoinhom)
		self.pushButton_50.clicked.connect(self.gg)
		self.pushButton_51.clicked.connect(self.xintkdd)
		self.pushButton_52.clicked.connect(self.nhanadmin)
		self.pushButton_53.clicked.connect(self.cotelechua)
		self.pushButton_54.clicked.connect(self.xemhdtl)
		self.pushButton_55.clicked.connect(self.xongchua)
		self.pushButton_56.clicked.connect(self.linktlvn)
		self.pushButton_57.clicked.connect(self.hdviethoa)
		self.pushButton_58.clicked.connect(self.tladmin)
		self.pushButton_59.clicked.connect(self.chatvsadmin)
		self.pushButton_62.clicked.connect(self.ranhdtko)
		self.pushButton_63.clicked.connect(self.xemkenhyt)
		#Cài đặt event click cho KIỂM TRA TÀI KHOẢN
		self.pushButton_9.clicked.connect(self.sdtxanh)
		self.pushButton_10.clicked.connect(self.sdtdo)
		self.pushButton_11.clicked.connect(self.chuacotk)
		self.pushButton_93.clicked.connect(self.sdtcotk)
		self.pushButton_35.clicked.connect(self.chuptkku)
		self.pushButton_36.clicked.connect(self.chuptktha)
		self.pushButton_37.clicked.connect(self.chuplsgd)
		self.pushButton_38.clicked.connect(self.thalagi)
		self.pushButton_39.clicked.connect(self.gdht)
		self.pushButton_13.clicked.connect(self.eptha)
		self.pushButton_44.clicked.connect(self.epnap1)
		self.pushButton_45.clicked.connect(self.epnap2)
		self.pushButton_66.clicked.connect(self.napbn)
		self.pushButton_67.clicked.connect(self.epnap3)
		self.pushButton_68.clicked.connect(self.epnap4)
		self.pushButton_46.clicked.connect(self.xinlaitk)
		self.pushButton_94.clicked.connect(self.tkbikhoa)        
		self.pushButton_34.clicked.connect(self.dangnhapku)
		self.pushButton_40.clicked.connect(self.ltaiku)
		self.pushButton_41.clicked.connect(self.dangnhaptha)
		self.pushButton_42.clicked.connect(self.ltaitha)
		self.pushButton_95.clicked.connect(self.xthucku)
		self.pushButton_96.clicked.connect(self.xthuctha)
		self.pushButton_69.clicked.connect(self.onuocnao)
		self.pushButton_70.clicked.connect(self.covnbank)
		self.pushButton_82.clicked.connect(self.codokong)
		self.pushButton_83.clicked.connect(self.henmai)
		self.pushButton_85.clicked.connect(self.dongyhtko)
		self.pushButton_86.clicked.connect(self.nhacquaylaicv)
		self.pushButton_87.clicked.connect(self.ncngoaikoht)
		#Cài đặt event click cho TỪ CHỐI
		self.pushButton_64.clicked.connect(self.dockytl)
		self.pushButton_43.clicked.connect(self.hoisautk)
		self.pushButton_71.clicked.connect(self.vevnnhan)
		self.pushButton_72.clicked.connect(self.nho18)
		self.pushButton_73.clicked.connect(self.lon53)
		self.pushButton_74.clicked.connect(self.khongchiudk)
		self.pushButton_75.clicked.connect(self.tambiet)
		self.pushButton_76.clicked.connect(self.chucmayman)
		self.pushButton_98.clicked.connect(self.napdulieu)
		self.pushButton_89.clicked.connect(self.kiemtra)


		self.pushButton_90.clicked.connect(self.new_cell)
		self.pushButton_91.clicked.connect(self.update_cell1920)
		self.pushButton_92.clicked.connect(self.update_cell21)





		#Khai báo hàm khách tìm về
	def chaocangi(self):
		x="Chào anh em, ae cần tôi hỗ trợ gì?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def hoinguon(self):
		x="Xin chào ae. Anh em biết đến giaimasohoc qua đâu?\
		\n1. Youtube\
		\n2. Facebook\
		\n3. Google\
		\n4. Nguồn khác (bạn bè giới thiệu,...)"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def hoinguonn(self):
		x="Anh em biết đến giaimasohoc qua đâu?\
		\n1. Youtube\
		\n2. Facebook\
		\n3. Google\
		\n4. Nguồn khác (bạn bè giới thiệu,...)"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ketbanfb(self):
	   x="AE KẾT BẠN FB VỚI TÔI ĐỂ ĐƯỢC HỖ TRỢ NHÉ"
	   self.textEdit.setText(x)
	   a = QtWidgets.QApplication.clipboard()
	   a.setText(x)
	def xinsdt1(self):
	   x="Số điện thoại của anh em là gì để tôi duyệt cấp tài khoản diễn đàn tham khảo số cao thủ và cầu lô đề hàng ngày?"
	   self.textEdit.setText(x)
	   a = QtWidgets.QApplication.clipboard()
	   a.setText(x)
	def xinsdt2(self):
	   x=" Ae muốn XIN TÀI KHOẢN đăng nhập vào diễn đàn GIAIMASOHOC để tham khảo số Cao thủ chốt miễn phí hàng ngày thì để lại số điện thoại để tôi xét duyệt"
	   self.textEdit.setText(x)
	   a = QtWidgets.QApplication.clipboard()
	   a.setText(x)
	def xinso(self):
	   x="Tôi không chốt số riêng, anh em muốn xem số cao thủ thì lên Diễn đàn giải mã số học\
	   \nAe cần vào diễn đàn tham khảo số cao thủ thì để lại số điện thoại để tôi cấp tài khoản cho anh em"
	   self.textEdit.setText(x)
	   a = QtWidgets.QApplication.clipboard()
	   a.setText(x)
	def quyenloi(self):
		x=["AE ĐỌC THẬT KỸ",
		"Quyền lợi THAM GIA DIỄN ĐÀN Giaimasohoc HOÀN TOÀN MIỄN PHÍ",
		"+ Được tham khảo số, cầu kèo, phương pháp chơi của cao thủ TOP 1 miễn phí",
		"+ Sinh hoạt cùng cao thủ ở các câu lạc bộ XIÊN, 3 CÀNG, ĐỀ",
		"+ Được tham gia sinh hoạt cùng các thành viên và các cao thủ có kinh nghiệm SỐ trong nhóm",
		"+ Được tham gia dự thi CAO THỦ CHỐT SỐ hàng tháng và trở thành CAO THỦ trên diễn đàn",
		"+ Được tham gia diễn đàn trao đổi giao lưu với các CAO THỦ và CHỦ TỊCH CLB"]
		self.textEdit.setText('\n'.join(x))
		a = QtWidgets.QApplication.clipboard()
		a.setText('\n'.join(x))
	def kulagi(self):
		x="Tài khoản KUDV để A.e chơi ghi lô ghi đề, số má trên đấy\
		\nTài khoản diễn đàn chỉ sử dụng để xem các cao thủ chốt số và hoạt động\
		\nTài khoản KUDV không phải là tài khoản diễn đàn GMSH\
		\nAE có TK KUDV + đơn cược sẽ được cấp TK diễn đàn GMSH miễn phí"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	#Khai báo hàm cấp tài khoản
	def hdsudung(self):
		x="AE bấm vào link này để xem cách đăng nhập và sử dụng tk diễn đàn nhé\
		\nhttps://www.youtube.com/watch?v=vz9IPOGo3o0"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def noiquy(self):
		x="Ae đọc kĩ nội quy và tham gia.\
		\nChúc anh em có những con số may mắn!"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhactk(self):
		x="Để bảo mật TK, Mật khẩu ko thay đổi được\
		\nTài khoản và Mật khẩu Admin chỉ cấp 1 lần\
		\nAE CHÚ Ý ghi chép ra giấy cất đi, lưu lại\
		\nQUÊN hay MẤT sẽ KHÔNG được xem xét cấp lại nhé!"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def randommk(self):
		letters = string.ascii_lowercase
		digits = string.digits
		length = 9
		password = ''
		for i in range(length):
			if i > 3:
				text = random.choice(digits)
			else:
				text = random.choice(letters)
			password+=text 
		self.lineEdit_2.setText(password)
		a = QtWidgets.QApplication.clipboard()
		a.setText(password)
	def guitk(self):
		x=("- Tên tài khoản: {}\
		\n- Mật khẩu: {}\
		\nA/e Đăng nhập vào app diễn đàn GMSH hoặc truy cập google.com tìm trang GIẢI MÃ SỐ HỌC vào đăng nhập tài khoản theo thông tin tôi gửi phía trên để tham khảo.\
		\nMật khẩu TK không thay đổi được,AE có trách nhiệm bảo quản Mk. Quên sẽ mất thời gian xác nhận tham gia lại"\
		.format(self.lineEdit.text(),self.lineEdit_2.text()))
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def taodan(self):
		x="Ae xem clip \
		\nhttps://giaimasohoc.com/threads/huong-dan-tao-dan-so-2d-3d-4d.21147/"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def phongchat(self):
		x="Trên diễn đàn GMSH có các phòng chát, nơi ae giao lưu, chơi cùng cao thủ\
		\nĐấy chính là nhóm cho ae, ae lên đấy hoạt động.\
		\nChúc ae rực rỡ!"        
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	#Khai báo tạo nhóm hướng dẫn    
	def taonhomku(self):
		x=" Đăng kí và nạp chơi tài khoản KUDV có đơn cược để được cấp tài khoản DIỄN ĐÀN GIẢI MÃ SỐ HỌC MIỄN PHÍ.\
		\nCòn tiền nạp chơi là tiền của ae. Ae chơi bao nhiêu nạp bấy nhiêu diễn đàn chỉ cần xác định đơn cược để xác thực người chơi số sẽ được cấp TK Diễn đàn MIỄN PHÍ" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def taonhomtha(self):
		x=" Đăng kí và nạp chơi tài khoản THA có đơn cược để được cấp tài khoản DIỄN ĐÀN GIẢI MÃ SỐ HỌC MIỄN PHÍ.\
		\nCòn tiền nạp chơi là tiền của ae. Ae chơi bao nhiêu nạp bấy nhiêu diễn đàn chỉ cần xác định đơn cược để xác thực người chơi số sẽ được cấp TK Diễn đàn MIỄN PHÍ" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def taonhomnap(self):
		x=" nạp chơi để có đơn cược xác thực là người chơi số sẽ được cấp tài khoản DIỄN ĐÀN GIẢI MÃ SỐ HỌC MIỄN PHÍ."        
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def timlaimk(self):
		x=" tìm lại tài khoản KU nhé" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def angocanh(self):
		x="https://t.me/+-wT46Se9aA8yYTZl" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def pngocanh(self):
		x="https://t.me/+HXY6WN6en_85ZTll" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def amytu(self):
		x="https://t.me/+NwEoA3yGyI5kMDll" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cmytu(self):
		x="https://t.me/+UY9BoGo5YtI4NjA1" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def thanhngan(self):
		x="https://t.me/+Ws02Z409D1oyMDRl" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ngochuong(self):
		x="https://t.me/+qTNjYRckSnw1YmY1" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def kimoanh(self):
		x="https://t.me/+1KO_ofsamZ8yNDNl" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhiwinny(self):
		x="https://t.me/+DnOB5hdoeyQ1OTNl" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def angocanhtl(self):
		x="NGỌC ÁNH \
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé https://t.me/ngocanhkudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def pngocanhtl(self):
		x="NNGỌC ÁNH\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé https://t.me/ngocanhkudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def amytutl(self):
		x="TRỊNH MỸ TÚ\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé https://t.me/trinhmytukudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cmytutl(self):
		x="TRỊNH MỸ TÚ\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé https://t.me/trinhmytukudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def thanhngantl(self):
		x="THANH NGÂN\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé https://t.me/thanhngankudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ngochuongtl(self):
		x="NGỌC HƯƠNG\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé  https://t.me/ngochuongkudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def kimoanhtl(self):
		x="KIM OANH\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé  https://t.me/kimoanhkudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhiwinnytl(self):
		x="NHI WINNY\
		\nAE nhắn tin chuyên viên hướng dẫn cho nhé  https://t.me/nhiwinnykudv" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def thongbaotaonhom(self):
		x="Tôi đã liên hệ xong chuyên viên, AE vào nhóm kết bạn nhắn tin và làm theo hướng dẫn" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def hoitinhhinh(self):
		x="Lần trước tôi đã liên hệ chuyên viên hướng dẫn ae, ae làm xong chưa?" 
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	#Khai báo hàm TỪ CHỐI
	def dockytl(self):
		x="A.e đọc kỹ lại rồi trả lời để không mất lượt hỗ trợ"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def hoisautk(self):
		x="Các vấn đề về tài khoản KUDV AE liên hệ chuyên viên trang đã hướng dẫn AE tạo TK  để được Hỗ trợ, giải đáp.\
		\nTôi chỉ quản lý giải đáp các vấn đề trên diễn đàn GIAIMASOHOC. COM"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def vevnnhan(self):
		x="Khi nào ae về VN nhắn tôi hỗ trợ nhé Cám ơn anh em đã quan tâm, Chúc anh em có những con số may mắn"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nho18(self):
		x="AE chưa đủ tuổi tham gia rồi nhé. Cám ơn anh em đã quan tâm\
		\nChúc anh em có những con số may mắn"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def lon53(self):
		x="AE quá tuổi tham gia rồi nhé. Cám ơn anh em đã quan tâm\
		\nChúc anh em có những con số may mắn"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def khongchiudk(self):
		x="Toàn bộ quyền lợi và điều kiện Tôi đã gửi. Ae muốn được cấp tk diễn đàn để tham khảo số thì làm theo chuyên viên  ĐĂNG KÍ + NẠP CHƠI tài khoản để chứng thực người chơi số.\
		\nTất cả đều miễn phí, đơn giản thế không làm được thì AE vào diễn đàn cũng không giúp gì được ae đâu"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tambiet(self):
		x="Cám ơn anh em đã quan tâm, ĐÂY LÀ ĐIỀU KIỆN BẮT BUỘC RỒI AE THÔNG CẢM!\
		\nChúc anh em có những con số may mắn!"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chucmayman(self):
		x="Chúc anh em có những con số may mắn!"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	#Khai báo hàm KIỂM TRA TÀI KHOẢN
	def sdtxanh(self):
		x="ĐỂ THAM GIA DIỄN ĐÀN CẦN CÁC ĐIỀU KIỆN:\
		\n1. Từ 18 đến 60 tuổi\
		\n2. PHẢI có đơn cược chơi lô đề trên trang KUDV để chứng thực là người chơi số thì sẽ cấp tài khoản diễn đàn MIỄN PHÍ\
		\nAe đã có tài khoản KUDV chưa? CÓ RỒI hay CHƯA CÓ?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def sdtdo(self):
		x="ĐỂ THAM GIA DIỄN ĐÀN CẦN CÁC ĐIỀU KIỆN:\
		\n1. Từ 18 đến 60 tuổi\
		\n2. PHẢI có đơn cược chơi lô đề trên trang KUDV để chứng thực là người chơi số thì sẽ cấp tài khoản diễn đàn MIỄN PHÍ\
		\nAe Chụp màn hình tài khoản KUDV tôi xác nhận?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuacotk(self):
		x="Nếu ĐỒNG Ý tham gia diễn đàn thì nhắn ----OK---- để tôi cho chuyên viên hướng dẫn anh em lập tài khoản KUDV và vào nhóm MIỄN PHÍ.\
		\nLƯU Ý: LÀM THEO CHUYÊN VIÊN HƯỚNG DẪN, KHÔNG TỰ Ý ĐĂNG KÍ TK KUDV"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def sdtcotk(self):
		x="SĐT A/e cung cấp admin kiểm tra đã từng lập tk KUDV.\
		\nNếu ae quên để tôi liên hệ chuyên viên hỗ trợ ae tìm lại"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuptkku(self):
		x="A/e Chụp ảnh màn hình đăng nhập tài khoản KUDV tôi xác nhận"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuptktha(self):
		x="A/e Chụp ảnh màn hình đăng nhập tài khoản THA tôi xác nhận"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuplsgd(self):
		x="Anh em chụp ảnh LỊCH SỬ GIAO DỊCH + SAO KÊ ĐẶT CƯỢC tôi xác nhận nhé"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def thalagi(self):
		x="TK THA cũng tương tự như tk KU, ae có tk THA tôi sẽ cấp tk vào diễn đàn tham khảo số"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def gdht(self):
		x="Ae ấn về màn hình trang chủ, chụp ở chỗ Giao dịch -> mục Đã hoàn thành"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def eptha(self):
		x="Qua quá trình kiểm duyệt, tài khoản KUDV của anh em không đủ xác thực bảo mật. \
		\nVì thế, Ae cần lập thêm tài khoản THA để xác thực tham gia diễn đàn. Nếu đồng ý nhắn ----OK---- để tôi cho chuyên viên hướng dẫn anh em tiếp.\
		\nLưu ý: LÀM THEO CHUYÊN VIÊN HƯỚNG DẪN, KHÔNG TỰ Ý ĐĂNG KÍ.\
		\n(Nếu đã có tk THA thì không cần đăng ký thêm)"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def epnap1(self):
		x="Để tham gia diễn đàn, anh em cần NẠP chơi tài khoản để có GIAO DỊCH HIỆN TẠI & đơn cược xác minh là người chơi số thực sự tôi cấp TK"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def epnap2(self):
		x="Khi nào Tài khoản của ae nạp chơi, có đơn cược chơi và lịch sử giao dịch 2-3 ngày gần nhất chứng minh mình là người chơi số thực sự AE nhắn tôi cấp Tài khoản diễn đàn miễn phí"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def napbn(self):
		x="Việc anh em nạp chơi to hay nhỏ là tùy anh em.\
		 Ae có tài khoản KUDV của nhà tài trợ đã nạp chơi, có ĐƠN CƯỢC để xác thực người chơi số thì tôi cấp tài khoản diễn đàn miễn phí cho ae"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def epnap3(self):
		x="Để tham gia diễn đàn, anh em cần NẠP chơi tài khoản để có đơn cược xác minh là người chơi số thực sự. Tiền nạp chơi web là của ae hưởng, chứ BTC không có nhận một đồng nào từ đó. ĐÂY LÀ ĐIỀU KIỆN để chứng mình ae có chơi số chứ không phải bán số "
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def epnap4(self):
		x="Tiền nạp chơi là tiền của ae. Ae chơi bao nhiêu nạp bấy nhiêu diễn đàn chỉ cần xác định đơn cược để xác thực người chơi số không quan tâm ae chơi ít hay nhiều"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xinlaitk(self):
		x="Tên TK diễn đàn của AE là gì?\
		\nDiễn đàn đang trong quá trình lọc các thành viên còn hoạt động và chơi số. Anh em vui lòng cung cấp cho admin đơn cược chơi xổ số trên trang KUDV hoặc THA để chứng thực cấp lại tk diễn đàn"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tkbikhoa(self):
		x="Nếu tài khoản của anh em bị quên mật khẩu hoặc bị khóa thì ae gửi tôi ảnh chụp đăng nhập tài khoản KUDV hoặc THA của ae để tôi xác thực tài khoản này đúng là của ae và cấp lại cho ae mật khẩu mới nhé"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dangnhapku(self):
		x="A/e đăng nhập tại link sau và gửi tôi ảnh chụp tài khoản KU của ae\
		\nhttp://kudv.net"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ltaiku(self):
		x="Ae đăng nhập vào trang chủ KU kudv.net sẽ có nút tải app bên dưới"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dangnhaptha(self):
		x="A/e đăng nhập tại link sau và gửi tôi ảnh chụp tài khoản THA của ae\
		\nhttp://jb77.net"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ltaitha(self):
		x="Ae đăng nhập vào trang chủ THA jb77.net sẽ có nút tải app bên dưới"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xthucku(self):
		x=("Tài khoản diễn đàn của Ae trước đây được chúng tôi xét duyệt qua TK KUDV {} nên AE cần phải cung cấp TK KUDV: {} để tôi xác thực mới cấp lại Tài khoản cho AE được nhé"\
		.format(self.lineEdit_23.text(),self.lineEdit_23.text()))
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xthuctha(self):
		x=("Tài khoản diễn đàn của Ae trước đây được chúng tôi xét duyệt qua TK THA {} nên AE cần phải cung cấp TK THA: {} để tôi xác thực mới cấp lại Tài khoản cho AE được nhé"\
		.format(self.lineEdit_24.text(),self.lineEdit_24.text()))
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def onuocnao(self):
		x="Anh em đang ở quốc gia nào thế?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def covnbank(self):
		x="AE ở nước ngoài muốn tham gia diễn đàn cần chứng minh ae chơi số trên trang, do đó ae cần có tài khoản ngân hàng VN có đăng ký banking. Anh em có tài khoản Vn và banking không?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def codokong(self):
		x="Ae có đó không. ADMIN xét duyệt cấp tài khoản"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def henmai(self):
		x=" Giờ muộn rồi, hẹn anh em chiều mai lúc 16h00 liên hệ tôi xét duyệt "
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dongyhtko(self):
		x="Anh em đồng ý tham gia diễn đàn thì nhắn --OK-- để tôi cho chuyên viên hướng dẫn.\
		\nKhông thì nhắn --KHÔNG-- để qua lượt hỗ trợ"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhacquaylaicv(self):
		x="Ae quay lại nhắn chuyên viên để làm theo hướng dẫn, khi nào có đơn cược xác thực là người chơi số tôi sẽ cấp tài khoản diễn đàn MIỄN PHÍ"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ncngoaikoht(self):
		x="ĐIỀU KIỆN THAM GIA DIỄN ĐÀN:\
		\n-Từ 18 đến 60 tuổi\
		\n-PHẢI có đơn cược chơi lô đề trên trang KUDV để chứng thực là người chơi số thì mới cấp tài khoản diễn đàn\
		\nTrang KUDV không hỗ trợ quốc gia AE đang ở rồi, khi nào ae về VN nhắn tôi hỗ trợ nhé\
		\nCám ơn anh em đã quan tâm, Chúc anh em có những con số may mắn"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	#Khai báo hàm ZALO
	def kosogg(self):
		x="Tôi không chốt số riêng, Ae lên google tìm kiếm: Giaimasohoc.com để tìm hiểu thêm nhé."
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def khoinhom(self):
		x="Không có nhóm chốt số riêng, Ae lên google tìm kiếm: Giaimasohoc.com để tìm hiểu thêm nhé."
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)    
	def gg(self):
		x="Ae lên google tìm kiếm:Giaimasohoc.com để tìm hiểu thêm nhé."
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xintkdd(self):
		x="Còn nếu anh em muốn xin cấp tk diễn đàn thì nhắn tôi"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhanadmin(self):
		x="AE NHẮN TIN QUA TELEGRAM CHO ADMIN ĐỂ ĐƯỢC HƯỚNG DẪN NHẬN TÀI KHOẢN DIỄN ĐÀN NHÉ: https://t.me/giaimasohoc2"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cotelechua(self):
		x="AE ĐÃ CÓ TELEGRAM CHƯA?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xemhdtl(self):
		x="AE XEM VIDEO LÀM THEO HƯỚNG DẪN ĐỂ TẢI TELEGRAM"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xongchua(self):
		x="TẢI XONG NHẮN QUA CHO TÔI HƯỚNG DẪN"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def linktlvn(self):
		x="https://t.me/setlanguage/abcxyz"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def hdviethoa(self):
		x="Đây là link tiếng việt, chuyển telegram sang tiếng việt cho dễ dùng rồi nhắn ADMIN"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tladmin(self):
		x="https://t.me/giaimasohoc2"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chatvsadmin(self):
		x="Ae nhắn qua cho ADMIN nhé"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ranhdtko(self):
		x="Vào diễn đàn cũng cần thạo điện thoại 1 chút đấy. Ae có rành về sử dụng điện thoại chứ?"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def xemkenhyt(self):
		x="Nếu không rành về điện thoại thì anh em theo dõi trên youtube thôi nhé https://www.youtube.com/channel/UCeA66xzf-OaK9rzaSRf4hJg"
		self.textEdit.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
		  
	def msgBox(self,text,title):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setText(text)
		msgBox.setWindowTitle(title)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()
	

	def closeEvent(self, event):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setText("Mọi góp ý xin nhắn về IMAT-C3")
		msgBox.setWindowTitle("Bạn xác nhận muốn thoát")
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.No)
		return_vl = msgBox.exec_()
		if msgBox.clickedButton() is msgBox.button(QtWidgets.QMessageBox.Ok):
			event.accept()
		else:
			event.ignore()  
	def napdulieu(self):
		self.napdulieu = Threading()
		self.napdulieu.msg.connect(self.msgBoxX)
		self.napdulieu.start()   



	def kiemtra(self):
		self.lineEdit_4.setText('')
		self.lineEdit_5.setText('')
		self.lineEdit_6.setText('')
		self.lineEdit_7.setText('')
		self.lineEdit_15.setText('')
		self.lineEdit_16.setText('')
		self.lineEdit_17.setText('')
		self.lineEdit_18.setText('')
		self.lineEdit_19.setText('')
		self.lineEdit_8.setText('')
		username = self.lineEdit.text()
		a = False
		if username =='':
			return 
		for tkdd in LIST_TKTRONGTHANG:
			if username in tkdd:
				self.lineEdit_4.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_1920:
			if username in tkdd:
				self.lineEdit_5.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_21:
			if username in tkdd:
				self.lineEdit_6.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_QC:
			if username in tkdd:
				self.lineEdit_7.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_CQ_C3:
			if username in tkdd:
				self.lineEdit_15.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_CQ_TH:
			if username in tkdd:
				self.lineEdit_16.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_CQ_Z:
			if username in tkdd:
				self.lineEdit_17.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_CQ_Q:
			if username in tkdd:
				self.lineEdit_18.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_CQ_C2:
			if username in tkdd:
				self.lineEdit_19.setText(' | '.join(tkdd))                
				a = True
				break
		for tkdd in LIST_XUPHAT:
			if username in tkdd:
				self.lineEdit_8.setText(' | '.join(tkdd))                
				a = True
				return        

		if a == False:        
			self.label_25.setText('KHÔNG CÓ NHÉ')

	def closeEvent(self, event):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setText("Mọi góp ý xin nhắn về IMAT-C3")
		msgBox.setWindowTitle("Bạn xác nhận muốn thoát")
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.No)
		return_vl = msgBox.exec_()
		if msgBox.clickedButton() is msgBox.button(QtWidgets.QMessageBox.Ok):
			event.accept()
		else:
			event.ignore()    

	@QtCore.pyqtSlot(str)
	def msgBoxX(self,text):
		self.label_25.setText(text) 

	def auto_reload(self):
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.napdulieu)
		time_sleep = int(self.comboBox_4.currentText())*60*1000

		self.timer.start(time_sleep)
   
		




class Threading(QtCore.QThread):
	msg = QtCore.pyqtSignal(str)
	def __init__(self):
		super().__init__()
		self.files  =  'TÀI KHOẢN DIỄN ĐÀN GMSH'
		self.sheets = ['THÁNG 12!B:D','2020-2019!A:E','2021!A:E','TK QC Tự cấp!A:D','XỬ PHẠT!A:F']

	def run(self):
		global LIST_TKTRONGTHANG , LIST_1920 , LIST_21 , LIST_QC , LIST_XUPHAT
		
		with concurrent.futures.ThreadPoolExecutor() as job:
			for i in range(len(self.sheets)):
				future = job.submit(lambda:client.open(self.files).values_get(range=self.sheets[i])['values'])
				return_value = future.result()
				if self.sheets[i] == 'THÁNG 12!B:D':
					LIST_TKTRONGTHANG = return_value
					self.msg.emit('Đã nạp xong sheet THÁNG 12')
				elif self.sheets[i] =='2020-2019!A:E':
					LIST_1920 =return_value
					self.msg.emit('Đã nạp xong sheet 2020-2019')
				elif self.sheets[i] =='2021!A:E':
					LIST_21 =return_value
				elif self.sheets[i] =='TK QC Tự cấp!A:D':
					LIST_QC = return_value
					self.msg.emit('Đã nạp xong sheet TK QC Tự cấp')
				else :
					LIST_XUPHAT = return_value

		self.msg.emit(r'Đã nạp xong 100% dữ liệu')
		print(LIST_1920)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	win = Main()
	win.show()
	sys.exit(app.exec_())
