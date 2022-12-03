import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#client.open("koneksi").add_worksheet(title="worksheet baru",rows=1000,cols=20)
worksheets = client.open("koneksi").worksheet("data_kontak")
#client.open("koneksi").del_worksheet(worksheets)

list_data = worksheets.get_all_records()

dataframe = pd.DataFrame(list_data)

#data_baru = pd.DataFrame.from_records({'no_wa' : ['6282294004980'],'nama':['lisa'],'pesan': ['hai'],'status':['2']})

#dataframe = pd.concat([dataframe,data_baru])

#dataframe.loc[dataframe['no_wa'] == 6281279616871, ['status']] = 3 

#set_with_dataframe(worksheets,dataframe)
#print(dataframe)

filterData = 2+dataframe[(dataframe['no_wa'] == 6281279616871 ) & (dataframe['status'] == 3)].index.  item()
worksheets.delete_row(filterData)

print(filterData)