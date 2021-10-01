# flake8: noqa
import sys
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
mii = [ 'ISO/TC 68 and other industry assignments' ,
'Airlines' ,
"Airlines, financial and other future industry assignments" ,
"Travel and entertainment" ,
"Banking and financial" ,
"Banking and financial" ,
"Merchandising and banking/financial" ,
"Petroleum and other future industry assignments" ,
"Healthcare, telecommunications and other future industry assignments", "For assignment by national standards bodies"]

def main():
	print("Credit Card Validator")
	print("Supported Credit Cards:\n************************")
	for i in cc:
		print( ">",i)
	choice = 'y'
	while choice == 'y' or choice == 'Y':
		try:
			card_number = input("\nEnter the credit card number: ")
			if is_valid(card_number) and 13 <= len(card_number) and len(card_number) <= 19:
				print("\nThis is a valid credit card number.")
				digi = digits_of(card_number)
				lenn = len(digi)
				if card_number[0:1] == "4" and ( lenn == 16 or lenn == 13 ): # visa case
					print("Type:" , cc[0])
					print("Major Industry Identifier (MII):" , mii[digi[0]])
					if(lenn==13):
						print("Account Number:", card_number[6:12])
						print("Checksum:", digi[12])
					else: # 16 case
						print("Account Number:", card_number[6:15])
						print("Checksum:", digi[15])

				elif card_number[0:2] == "34" or card_number[0:2] == "37" and lenn == 15 : # american express card
					print("Type:" , cc[1])
					print("Major Industry Identifier (MII):", mii[digi[0]])
					print("Account Number:", card_number[4:11])
					print("Card Number within the account:", card_number[11:14])
					print("Checksum:", digi[14])

				elif card_number[0:2] == "300" or card_number[0:2] == "301" or card_number[0:2] == "302" or card_number[0:2] == "303" or card_number[0:2] == "304" or card_number[0:2] == "305" and lenn ==14 : #Diner club carte blanche
					print("Type:", cc[2])
					print("Major Industry Identifier (MII):", mii[digi[0]])
					print("Checksum:", digi[13])

				elif card_number[0:2] == "51" or card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55" and lenn == 16 :
					print("Type:", cc[3])
					print("Major Industry Identifier (MII):", mii[digi[0]])
					print("Account Number:", card_number[6:15])
					print("Checksum:", digi[15])

				elif card_number[0:4] == "6011" and lenn == 16 :
					print("Type:", cc[4])
					print("Major Industry Identifier (MII):", mii[digi[0]])
					print("Account Number:", card_number[4:15])
					print("Checksum:", digi[15])

				else:
					print("Other informations are not displayed as it doesn't belong to list shown below, however cc is valid")
					for i in cc:
						print(">", i)
			else:
				print("\nInvalid!! Credit card number.")

			choice = input("\nWant to check again? (y/n): ")

		except ValueError:
			print("\nErr! Credit card number should be numeric. Try again.")
		except:
			print("Unexpected error:", sys.exc_info()[0])
			raise

			

if __name__ == '__main__':
	main()
