def count(str,substr,isOverlapping):
	is_found=False;
	count_num =0;
	i =0;
	j=0;
	#0 < 3
	while i <= len(str)-len(substr):
		#2 < 2
		if isOverlapping :
			while j < len(substr):
				# 'G' == 'G'
				if str[i+j] == substr[j]:
					is_found = True;
					j += 1;
				
				else :
					is_found = False;
					break;
			i +=1;#1
			j=0;	
			if(is_found == True):
				is_found=False;
				count_num += 1;
		else :
	  		
			while j < len(substr):
				# 'G' == 'G'
				if str[i] == substr[j]:
					is_found = True;
					j += 1;
					i += 1;
				
				else :
					is_found = False;
					i +=1;#Here is issue
					break;
			
			j=0;	
			if(is_found == True):
				is_found=False;
				count_num += 1;
		
			
	return count_num;





print(count("FGFGFGFGGFG","GG",False));