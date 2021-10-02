import tqdm
import time
listnya = input('input list : ')
output  = input('Output Destination : ')
lists = open(listnya)
cok =  set(lists.readlines())
total = len(list(open(listnya)))
print ("[+] Found Total {} List".format(str(total)))
print ("[+] Start Remove Duplicate ...\n\n")
time.sleep(1)
count = 0
result = listnya.replace(".txt","")
file = result+'-clean.txt'
folder = str(output)
for i in tqdm.tqdm(cok):
	time.sleep(0)
	count +=1
	open(folder+file,'a').write(i)
final = total-count
print ("\nSuccess Remove {} From list".format(str(final)))
