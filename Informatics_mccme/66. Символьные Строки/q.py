hex_str = input() 
minus_flag = 0
if hex_str[0] == '-': 
	minus_flag = 1
	hex_str = hex_str[1:]

bin_str = bin(int(hex_str, 16))[2:]
print(minus_flag and '-' + bin_str)
