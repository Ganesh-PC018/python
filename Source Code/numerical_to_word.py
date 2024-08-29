def print_number_to_word(num) :
	words_li =["One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine ","Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen ","Twenty ","Thirty ","Fourty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety ","Hundred ","Thousand ","Million ","Billion"]
	str_temp = str(num);
	reverse_str = str_temp[::-1];
	ans ="";
	i=0;
	while i < len(reverse_str) :
		if(reverse_str[i] == "1" and reverse_str[i+1] !="1") :
			ans =words_li[0] + ans ;
			i +=1;
		elif(reverse_str[i] == "2" and reverse_str[i+1] !="1") :
			ans =  words_li[1] + ans;
			i += 1;
		elif(reverse_str[i] == "3" and reverse_str[i+1] !="1") :
			ans =  words_li[2] + ans;
			i += 1;
		elif(reverse_str[i] == "4" and reverse_str[i+1] != "1") :
			ans =  words_li[3] + ans;
			i += 1;
		elif(reverse_str[i] == "5" and reverse_str[i+1] != "1") :
			ans =  words_li[4] + ans ;
			i += 1;
		elif(reverse_str[i] == "6" and reverse_str[i+1] != "1") :
			ans = words_li[5] + ans;
			i += 1;
		elif(reverse_str[i] == "7" and reverse_str[i+1] != "1") :
			ans = words_li[6] + ans;
			i += 1;
		elif(reverse_str[i] == "8" and reverse_str[i+1] != "1") :
			ans = words_li[7] + ans;
			i += 1;
		elif(reverse_str[i] == "9" and reverse_str[i+1] != "1") :
			ans = words_li[8] + ans;
			i += 1;
		if(reverse_str[i] == "1" and reverse_str[i+1] =="1") :
			ans =words_li[10] + ans ;
			i +=1;
		elif(reverse_str[i] == "2" and reverse_str[i+1] =="1") :
			ans =  words_li[11] + ans;
			i += 1;
		elif(reverse_str[i] == "3" and reverse_str[i+1] =="1") :
			ans =  words_li[12] + ans;
			i += 1;
		elif(reverse_str[i] == "4" and reverse_str[i+1] == "1") :
			ans =  words_li[13] + ans;
			i += 1;
		elif(reverse_str[i] == "5" and reverse_str[i+1] == "1") :
			ans =  words_li[14] + ans ;
			i += 1;
		elif(reverse_str[i] == "6" and reverse_str[i+1] == "1") :
			ans = words_li[15] + ans;
			i += 1;
		elif(reverse_str[i] == "7" and reverse_str[i+1] == "1") :
			ans = words_li[16] + ans;
			i += 1;
		elif(reverse_str[i] == "8" and reverse_str[i+1] == "1") :
			ans = words_li[17] + ans;
			i += 1;
		elif(reverse_str[i] == "9" and reverse_str[i+1] == "1") :
			ans = words_li[18] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "1") :
			ans =  words_li[9] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "2") :
			ans =  words_li[19] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "3") :
			ans =  words_li[20] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "4") :
			ans =  words_li[21] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "5") :
			ans =  words_li[22] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "6") :
			ans =  words_li[23] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "7") :
			ans =  words_li[24] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "8") :
			ans =  words_li[25] + ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "9") :
			ans =  words_li[26] + ans;
			i += 1;
		elif(i+1 < len(reverse_str) and len(ans) == 2 ):
			val = words_li[i-1];
			ans = val+words_li[27]+"and" +ans;
			i += 1;
		elif(reverse_str[i] == "0" and reverse_str[i+1] == "0" and reverse_str[i+2] == "0") :
			val = reverse_str[i+3];
			ans =  word_li[val-1]+words_li[28] + ans;
			i += 3;
		else :
			print("Error");
		i += 1;
	
	
	print("Answer : "+ans);

print_number_to_word(124);
	