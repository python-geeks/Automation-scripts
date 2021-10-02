# flake8: noqa
import sys
import random

def digits_of(number):
	return [int(i) for i in str(number)]

def checksum_luhn(card_number):
	digits = digits_of(card_number)
	odd_digits = digits[-1::-2]  # From right
	even_digits = digits[-2::-2]  # From right
	total = sum(odd_digits)
	for digit in even_digits:
		total += sum(digits_of(2 * digit))
	return total % 10

def is_valid(card_number):
	return checksum_luhn(card_number) == 0

cc = ["Visa card"  , "American Express card" ,   "Diners Club Carte Blanche" , "Mastercard card" , "Discover card"   ]

def fill_cc(ll , t_rn ):
	for i in range(t_rn):
		app = random.randrange(0, 10, 1)
		ll.append(app)
	# method to find check sum for random numbers
	even = ll[-1::-2]  # From right
	odd = ll[-2::-2]  # From right
	# doubling the even nd adding unit and tens place
	even2 = []
	for i in even:
		even2.append(sum(digits_of(i * 2)))
	even2 = sum(even2)
	odd = sum(odd)
	check_sum = odd + even2
	if (check_sum % 10 == 0):
		ll.append(0)
	else:
		modl = check_sum % 10
		ll.append(10 - modl)

	# ll contains valid numbers now so printing it
	res = str("".join(map(str, ll)))
	res = ''
	for i in ll:
		res += str(i)

	if(is_valid(res)):
		print(res)
	else:
		print("!ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")


def print_cc ( ccn , cca ):

	while(cca != 0):

		ccs = []
		if (ccn==1): # we have two cases for visa
			ccs.append(13)
			ccs.append(16)
		if ( ccn == 4 or ccn == 5 ):
			ccs.append(16)
		if(ccn == 2):
			ccs.append(15)
		if(ccn == 3):
			ccs.append(14)

		ll = [] # it will store-up the cc numbers
		fin_size = random.choice(ccs) # for visa we will choose 13 or 16 randomly
		if(ccn==1): #VISA
			ll.append(4)
			t_rn = fin_size -2
			fill_cc(ll , t_rn)
			cca-=1

		elif (ccn == 2):  # AMEX
			ll.append(3)
			second_dig = [4 , 7]
			second_dig = random.choice(second_dig)
			ll.append(second_dig)
			t_rn = fin_size - 3
			fill_cc(ll, t_rn)
			cca -= 1

		elif (ccn == 3):  # diner club carte blanche
			ll.append(3)
			ll.append(0)
			third_dig = [0,1,2,3,4,5]
			third_dig = random.choice(third_dig)
			ll.append(third_dig)
			t_rn = fin_size - 4
			fill_cc(ll, t_rn)
			cca -= 1

		elif (ccn == 4):  # master
			ll.append(5)
			second_dig = [1,2,3,4,5]
			second_dig = random.choice(second_dig)
			ll.append(second_dig)
			t_rn = fin_size - 3
			fill_cc(ll, t_rn)
			cca -= 1

		elif (ccn == 5):  # discover
			ll.append(6)
			ll.append(0)
			ll.append(1)
			ll.append(1)
			t_rn = fin_size - 5
			fill_cc(ll, t_rn)
			cca -= 1

def cc_generator():
	a=1
	print("Credit Card Generator")
	print("Supported Credit Cards:\n************************")
	for i in cc:
		print( a, ">", i)
		a+=1

	ccn = int(input("Choose the credit card number from the above list: [NOTE: Press -1 if you to generate random cc]::"))

	if(ccn == -1):
		print("Choose the total numbers of random credit cards you want to generate:" , end = '')
		cca = int(input())
		print("*************************** List of randomly generated credit card numbers/name are shown below ******************************")
		ccn_r = [1 , 2, 3, 4 , 5]

		for i in range(cca):
			rnd = random.choice(ccn_r)
			print(cc[rnd-1])
			print_cc(rnd, 1)
	else:

		if not( 1 <= ccn <= 5 ):
			print('wrong choice')
			return
		print("Choose the total numbers of credit cards you want to generate for " , cc[ccn-1]  , ":" , sep = '' , end='')
		cca = int(input())
		print("*************************** List of generated" , cc[ccn-1]  ,"numbers are shown below ******************************")
		print_cc(ccn , cca )

if __name__ == '__main__':
	cc_generator()
