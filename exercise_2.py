try:
	T = int(input("Enter the number of test cases (from 1 to 10^5) : "))
	if not 1 <= T <= 10**5:
		raise ValueError("Incorrect number")

	word_list = []
	for w in range(T):
		w = input("Enter the word (Lowercase English letters) : ")
		if w.islower() and w.isalpha() and 1 <= len(w) <= 100:             
			word_list.append(w)
		else:
			raise ValueError("Incorrect letters")

except ValueError as e:
	print(e)
except Exception as e:
	print(e)

def compare(ls):
	if len(ls) == 1:  
		return False
	elif ls[-1] > ls[-2]:
		return (ls[:-1])  
	else:
		return compare(ls[:-1])  

for w in word_list:
	w = list(w)
	first_half = compare(w)
	if not first_half:  
		print("no answer")
		continue      
	second_half = w[len(first_half):]  
	second_half.sort()  

	for index, item  in enumerate(second_half):  
		if first_half[-1] < item:
			a = second_half.pop(index) 
			b = first_half.pop(-1) 
			second_half.insert(index, b)  
			first_half.append(a) 
			break

	print(''.join(first_half + second_half))


