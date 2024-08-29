def pattern_plus(val):
	num = int(val);
	row = num*2+1;
	col = num*2+1;
	plus = '+';
	minus = '-';
	for i in range((row // 2) + 1):
		for j in range(col):  
			if (j+i) == col // 2 or (j-i) == col //2:
				print(" "+plus,end=""); 
			else:
				print("  ",end="");
		print();
	for i in range((row//2)-1,-1,-1):
		for j in range(col):
			if(i == 0 and j == col//2):
				print(" "+minus,end="");
			elif(i+j ==col//2) or (j-i == col//2):
				print(" "+plus,end="");
			else :
				print("  ",end="");

		print();

pattern_plus(13);