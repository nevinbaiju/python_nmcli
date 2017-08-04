#################################################################################################################
# courtesy of https://github.com/joshvillbrandt/wireless.git
# modified and written for personal use by https://github.com/nevinbaiju
# github repository at https://github.com/nevinbaiju/python_nmcli.git
# 
# platforms		: python3, nmcli 0.9.10.0, debian.
#################################################################################################################

import subprocess
def cmd(cmd):
    return subprocess.Popen(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).stdout.read().decode()

class Wireless():
	"""docstring for Wireless"""
	def __init__(self):
		scan = cmd('nmcli device wifi list').split()

		self.WIFI_LIST = self.SetWifiData(scan)
		print(self.WIFI_LIST)
		self.GetAvailableNetworks()

	def SetWifiData(self, scan):

		scan = [x for x in scan if ((x != '*')&(x != 'Mbit/s' ))]

		scan.remove('SSID')
		scan.remove('MODE')
		scan.remove('CHAN')
		scan.remove('RATE')
		scan.remove('SIGNAL')
		scan.remove('BARS')
		scan.remove('SECURITY')

		WIFI_DESC =['SSID','MODE','CHAN','RATE','SIGNAL','BARS','SECURITY']

		n = 0
		total = len(scan)-1

		WIFI_LIST = []
		while(n <= total):
			CURRENT_WIFI = {}
			for i in range(0, 7):
				CURRENT_WIFI[WIFI_DESC[i]] = scan[n+i]
			WIFI_LIST.append(CURRENT_WIFI)
			n = n+7
		
		return WIFI_LIST

	def GetAvailableNetworks(self):

		LIST = []

		for CONNECTION in self.WIFI_LIST:
			CURRENT_CONNECTION = {}
			CURRENT_CONNECTION['SSID'] = CONNECTION['SSID']
			CURRENT_CONNECTION['SIGNAL'] = CONNECTION['SIGNAL']
			CURRENT_CONNECTION['SECURITY'] = CONNECTION['SECURITY']
			LIST.append(CURRENT_CONNECTION)
		print(LIST)

	def ConnectWifi(self, SSID, PASSWORD):
		if(PASSWORD == '--'):
			cmd("sudo nmcli dev wifi connect '"+SSID+"'")
		else:
			cmd("sudo nmcli dev wifi connect '"+SSID+"' password '"+PASSWORD+"'")
		


if __name__ == "__main__":
	n = Wireless()