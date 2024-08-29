#implement DFA which acess all the string over {a,b} sych that each String ends with 'b'

def isDFA(data_str) :
	data_str = data_str.lower();
	ends_with_b=False;
	for ch in data_str :
		if ch == 'a' :
			ends_with_b =False;
		elif ch =='b':
			ends_with_b = True;
		else :
			return False;
	return ends_with_b;

s = input("Enter String");
if(isDFA(s)) :
	print("String Accepted");
else :
	print("String Rejected");
