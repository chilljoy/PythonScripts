import dns.resolver
import pandas as pd

my_resolver_old = dns.resolver.Resolver()
my_resolver_old.nameservers = ['216.69.185.10']

data = pd.read_csv("cnames.csv", header=0)

cname = list(data.Name)
cname_actual = list(data.Value)

A_record = []
TXT = []
MX = []
NS = []

cn = 0
print 'CNAME:'
for x in cname:
	try:	
		answers = my_resolver_old.query(x+'.trendkite.com', 'CNAME')
		for rdata in answers:
			#print rdata
			csv_var = cname_actual[cn] + '.'
			#print csv_var
			rdata = str(rdata)
			if csv_var != rdata:
				print "UH OH"
				print 'godaddy says: ' + rdata
				print 'spreadsheet says: ' +csv_var
				print '\n'
			#else:
			#	print "no match!"
			cn = cn+1
	except:
		print x + '.trendkite.com not found!!!!'
	#print '\n'	