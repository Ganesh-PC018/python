def display_pattern(val) :
	is_completed = False;
	for i in range((val*2)+1):
		space ='';
		star ="";
		for j in range((val*2)-i) :
			space = space+"   ";
		for k in range((i*2+1)) :
			#print("i",i);
			if i > val :
			 is_completed = True;
			 star = star +" * ";
			elif i==(val) and k == (val*2)/2 :
			 star = star+" "+ str(i);
			elif k==0 or k==i*2 :
			 star = star+" * ";
			else :
			 star = star +"   ";
		#if is_completed :
			#break;
		print(space + star);
		

	#for i in range(val+1) :
		#star ="";
		#for j in range((val*2)) :
			#star = star+" * ";
		#print(star);
	
		
		
		
		

def print_pattern(num) :
	val = int(num);
	if num < 1 or num > val:
		return "Entered Value less than 1 ";
	else :
		#return "valid value"
		display_pattern(val);


print(print_pattern(3.00000000000));

#int(input())) : not mention in Question

#str = isnum(num); is it applicable