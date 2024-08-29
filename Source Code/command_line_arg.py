from sys import argv;
def sumAdd():
	sum =0;
	#return eval(argv[1])+eval(argv[2]);
	for x in argv[1:]:
		data = int(x);
		if(type(data) == type(1)):
			sum += data;
	return sum;


print("Sum ",sumAdd());