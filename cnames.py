import dns.resolver
import pandas as pd
import re
import subprocess

IPs = ['ns-1596.awsdns-07.co.uk','ns-1525.awsdns-62.org','ns-89.awsdns-11.com','ns-569.awsdns-07.net']

for ip in IPs:
	ip_num = ip
	ip = subprocess.check_output('dig ' + ip + ' +short', shell=True)
	ip = ip.strip("\n")
	my_resolver_old = dns.resolver.Resolver()
	my_resolver_old.nameservers = [ip] #[IP_of_nameserver]
	server = str(my_resolver_old.nameservers)
	server = server.strip("[]'")

	################## CNAME ####################

	data = pd.read_csv("cnames.csv", header=0)

	cname = list(data.Name)
	cname_actual = list(data.Value)



	cn = 0
	print 'CNAME '+ ip_num + ' ' + ip +':'
	for x in cname:
		try:	
			answers = my_resolver_old.query(x+'.trendkite.com', 'CNAME')
			for rdata in answers:
				# print rdata
				csv_var = cname_actual[cn] + '.'
				# print csv_var
				rdata = str(rdata)
				if csv_var != rdata:
					print "UH OHs"
					print x +'.trendkit.com \n' + server + ' says: ' + rdata + ' // ' 'spreadsheet says: ' +csv_var
					#print  'spreadsheet says: ' +csv_var
					print '\n'
				# else:
				# 	print x + ' is good'
				cn = cn+1
		except:
			print x + '.trendkite.com not found!!!!'
	print '----'

	################## A ####################

	data = pd.read_csv("A.csv", header=0)

	A = list(data.Name)
	A_actual = list(data.Value)


	cn = 0
	print 'A '+ ip_num + ' ' + ip +':'

	for x in A:
		try:
			answers = my_resolver_old.query(x, 'A')
			for rdata in answers:
				#print rdata
				A_var = A_actual[cn]
				# print A_var
				rdata = str(rdata)
				if A_var != rdata:
					print "UH OHs"
					print x + '\n' + server + ' says: ' + rdata + ' // ' 'spreadsheet says: ' +A_var
					#print  'spreadsheet says: ' +csv_var
					print '\n'
				# else:
				# 	print x + ' is good'
				cn = cn+1
		except:
			print x + ' not found!!!!'
	print '----\n----'