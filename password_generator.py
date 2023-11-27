import random
import array

Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

LwCaseChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

UpCaseChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

SplSymbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

CombinationAll = Digits + UpCaseChar + LwCaseChar + SplSymbol

RandDigit = random.choice(Digits)
RandUpChar = random.choice(UpCaseChar)
RandlwChar = random.choice(LwCaseChar)
RandSymbol = random.choice(SplSymbol)

temp_pass = RandDigit + RandUpChar + RandlwChar + RandSymbol

password = ""
try:
	Maxlen =int(input("Enter Length of password you want: "))
	if Maxlen >=4:
		for x in range(Maxlen - 4):
			temp_pass = temp_pass + random.choice(CombinationAll)
			temp_pass_list = array.array('u', temp_pass)
			random.shuffle(temp_pass_list)
		for x in temp_pass_list:
			password = password + x
	else:
		print("Enter length above 6")
		
except:
	print("Enter valid or positive value only::")
print(password)