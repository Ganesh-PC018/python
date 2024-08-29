def alternative_case(str,style,is_even = True,is_odd = False,case = 32) :
	#print(type(case));
	l = ["C","S","R","U","c","s","r",'u']
	
	for char in str :
		if l.count(char) >= 1 :
			style += char;
			continue;
		if is_even and (ord(char) >=97 and ord(char) <= 122) :
			if case == 32 :
				style  += chr(ord(char)-32);
			else :
				style += chr(ord(char)+case)
			is_even = False;
			is_odd  = True;
		elif is_odd and (ord(char) >=65 and ord(char) <= 90):
			if case == 32 :
				style  += chr(ord(char)+32);
			else :
				style += chr(ord(char)+case)
			is_even = True;
			is_odd  = False;
		elif is_even :
			style += char;
			is_even = False;
			is_odd  = True;
		else :
			style += char;
			is_even = True;
			is_odd  = False;
	return style;

def change_case(str,opt) :
	style = "";
	result = [];
	my_list = opt.split(" ");
	if(len(str) == 0):
		return -1;
	if(my_list.count("c") >= 1 or my_list.count("C") >= 1 ) :
		for char in str :
			if ord(char) >=65 and ord(char) <=90 :
				style += chr(ord(char)+32);
			else :
				style += char;
		result.append(style);
	style = "";
	if(my_list.count("s") >= 1  or my_list.count("S") >= 1 ) : 
		for char in str :
			if ord(char) >=97 and ord(char) <=122 :
				style += chr(ord(char)-32);
			else :
				style += char;
		result.append(style);
	style = "";
	if(my_list.count("r") >= 1  or my_list.count("R") >= 1 ) :
		for char in str :
			if ord(char) >=97 and ord(char) <=122 :
				style += chr(ord(char)-32);
			elif ord(char) >=65 and ord(char) <=90 :
				style += chr(ord(char)+32);
			else :
				style += char;
		result.append(style);
	style = "";
	if(my_list.count("u") >= 1  or my_list.count("U") >= 1 ):
		ch = str[0];
		#style += ch;
		if(ord(ch) >= 97) :
			result.append(alternative_case(str,style,is_even = False,is_odd = True,case = -32));
		result.append(alternative_case(str,style))
	return result;

str = input("Enter String : ");
opt = input("Enter option 'c' 's' 'r' 'u  : ");
print("Answer : ",change_case(str,opt));	
	