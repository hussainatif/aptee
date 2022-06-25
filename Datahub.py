import gspread

auth =  {
  "type": "service_account",
  "project_id": "aptee-353914",
  "private_key_id": "0f8783325d8b4b8400bf9f89a6d4b91c1317faf7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDW4TKM/wixM2BY\nFKQOXExwbNuChLFCjAJuP0MOFfirMISDlxK/HPaKd5iYg9uu/0IG4bC/vO/SzXae\nJXetb3yh3L0KFc4DeAq7fwW2BpJFSAY82ErOTcF6Rfxdq/JrQkXF1WRwHhikrdJy\nDEVfI2Xh2evaeesdLM7/CUPf71LHPrxD14cEsAgAVyIflzADnJagOCKxBNLvhIVL\n5mcXLhDbRiXAFxw2bq10VPI4Bu2dBYJJLXXcU1LV5Jn45Gj4PTYVq//OmOnbxUsU\nNCwgTfMFtgbtOsiULCjq1Zsb7d5YD8Csb/EDSnPqcGUo/dkjyd6nsovz6MDM7Ubo\nn+3/udMpAgMBAAECggEAC6j6MYD4U4dGa9ko4tea1UHu8mjpZoNK8XkQ1i+WiBGQ\nq0RUIdc8QJzHRMVo8xjKWC3AhdMGj4GTNXcyhJCHapAcGPNAc9s8d9qncG5wWv6S\nyhPxkTrSbCRmkp2tQKk+uILBGb1kWHFPOV2VmRlGYshMvlT9z146WEgELR9jNkkF\naOOIb7ZJHlCDOO63R6d04YO2HCmQbRXCPVQrw/CA3k2QCuiSNWCjn68evNQ5KEAl\n07I++ZeaMJzlExePD9BRlqX6lLqD+nLDyng69+QdqcHgMt/gQxgHxMEke3LrqKtO\n7p/S37/RYlJWj2KNY+6lnGzGyXv638exzv9hKGh7FQKBgQD/1DZ7m6N87KRP8WaE\nN9h9zH5EKnZxkBt77LdNWR0TjSE37TCls/SH88fUy0yL/9ZsJe/aHQWG0S7j8yHH\nBWId2xKoFfZUrYMv8csN+CAfDcwPas4Uz8wIvjsdXyfGuOOwtPL22l5NbT1J7TM5\np8kny4bkuif5eknv9IB/320pBQKBgQDXBfnQ2aMT/Kvs+yyttoNccSJ5TfHXL1is\nJMq1miBDqt3635RfXrFufZmqBFVQZKvHTmiymLIknhsSXQicIIDnPq3qBImNf7Fc\nbUGn7eZ8bLVUjSCMm+FeS6v8FYoaK7oejHsNOxpkR2j/EizvmxkYrwseSiDtD4rN\n17FaPMKK1QKBgQCQo62uEx/K2IxJuoUoid53uW9GIO/YYw528S3tqE19KVS3pv3T\nIbxGRTkdAVgk6x+TA5vpKHFgeNJXBLZ7LHr9wEd7Cve7hmJecAlKu5eFlyphKRSc\nxaNo6gzIHW2CuDPbS2L22B1rDzEQo/BLT6a2PiblGK7TKSW2aflg0rSH9QKBgEUd\nzKFPc9YW4AS68C+efTcXvqcTYOt0cqJS6T3anwhhQh1EBONrAsmrYdt+rRW8ZmMY\nVxshbhHLKJSMhxn4cLbkNO8GKljrdM1q6THbjLzuDJNzEcVgzd6LoGrVWaDz8U2k\nhmFIYEFfmuZypzMVvclrar1/wnmxB0MHVCDXawlJAoGBAOxOvLE5Dlm6cxPlGmGb\njam7kKBmNGI9mYRdPvtPsp6aAF9BJr7FlCCT4x3OHcXe3wXVswpWTvGKQ6qM6M9I\ncfRC/RvaUbZ23SwQ7B3Rse9GTHsT7yuniF01/G+kzZdwc/vNidlKCUA9wB8JSY84\nE/g2hHDsONLtOgcQC9XL1ako\n-----END PRIVATE KEY-----\n",
  "client_email": "datahub@aptee-353914.iam.gserviceaccount.com",
  "client_id": "118436377233006939242",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/datahub%40aptee-353914.iam.gserviceaccount.com"
}

gc = gspread.service_account_from_dict(auth)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CyWjl6Y5Gi_e3z7A8wtw-qOaBe3GvCD4sqWWvaMubXY/edit?usp=sharing')
wks=sh.worksheet("Client_Details")
print(wks.find("aaaaaa"))
if wks.find('adsawadadsa'):
  print("yp")
#worksheet = wks.insert_rows(last_row, number=1, values= ["YO"])
#df1 = wks.get_as_df()
#print(df1.head())
#print()
#print(len(df1[df1['email_id']=='dabc@aptee.com']))