import pandas as pd
import numpy as np

class make_reply():
	
	def ImportData(self):
		link = "https://www.mohfw.gov.in/#"
		dfs = pd.read_html(link, index_col=0)

		data = dfs[0]
		data = data[:-2]
		data = data.rename(columns = {'Name of State / UT' : 'Name',
		                       'Total Confirmed cases (Including 76 foreign Nationals)' : 'Cases',
		                       'Cured/Discharged/Migrated' : 'Cured'})

		data['Cases'] = data['Cases'].astype(str)
		data['Cured'] = data['Cured'].astype(str)
		data['Death'] = data['Death'].astype(str)
		data['Name']['Total number of confirmed cases in India'] = 'Total'
		data['Name'] = data['Name'].str.lower()
		data.reset_index(drop=True)
		return data

	def SearchStats(self, msg):
		Data = self.ImportData()
		i = 0
		for State in Data['Name']:
			if State == msg:
				break
			i += 1

		if i >= len(Data):
			reply = "No such State/UT is found in data"
		elif msg != 'total':
			reply = "In {}\nConfirmed Cases : {}\nCured : {}\nNumber of Deaths : {}".format(msg.upper(), Data['Cases'][i], Data['Cured'][i], Data['Death'][i])
		else:
			reply = "In INDIA\nConfirmed Cases : {}\nCured : {}\nNumber of Deaths : {}".format(Data['Cases'][i], Data['Cured'][i], Data['Death'][i])
		return reply

	def Reply(self, msg):
		if msg is not None:
			reply = self.SearchStats(msg.lower())
		return reply