#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
	print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING  UPDATES \033[1;37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
