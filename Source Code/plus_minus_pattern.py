def plus_pattern(val) :
	num = int(val);
	row = 2*num+1;
	col = 2*num+1;
	plus ='+'
	minus ='-';
	for i in range(row):
		if i<=row//2 :
			for j in range(col):
				if i+j == col//2 or j-i == col//2:
					print(" "+plus,end="");sfghjkl;'

				else :
					print("  ",end="");
			print();
		else :
			for j in range(col):
				if (i-j) == (row//2) or (i-row//2+1)+j == col:
					print(" "+minus,end="");
				else :
					print("  ",end="");
			print();
	

plus_pattern(4);