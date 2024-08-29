def roman_num(val,base) :
	ans=0;
	k=0;
	while val > 0 :
		rem = val % 10;
		ans += rem *(base**k);
		val = val//10;
		k +=1;
	
	
	print("decimal : ",ans);
	li_word =['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','III','II','I']
	num_lis =[1000,900,500,400,100,90,50,40,10,9,5,4,3,2,1];
	final_ans="";
	for i in range(0,len(num_lis)) :
		while(ans >= num_lis[i]) :
			ans = ans - num_lis[i];
			final_ans = final_ans + li_word[i];
	return final_ans;

	

print("Ans : ",roman_num(100000,8)); 
print("Ans : ",roman_num(10,2));