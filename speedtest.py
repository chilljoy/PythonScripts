import os
import subprocess

#os.system("ssh Trendkite@10.101.20.251")
#os.system("speedtest-cli")
mbps = subprocess.check_output('speedtest-cli', shell=True)
mbps = mbps.splitlines()[6]
mbps = mbps.split(' ', 1)[1]
mbps = mbps.split(' ',1)[0]
mbps_float = float(mbps)

if mbps_float > 40:
	print "holy crap " + mbps + "mbps!"
else:
	print "Bad news... Only" + mbps + "mbps"