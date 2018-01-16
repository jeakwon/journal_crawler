# Import Libraries
from ftplib import FTP
import datetime
from setdate import upcoming_weekday
# FTP login
host = '161.122.107.48'
port = 2222
userid = 'kwonjea'
password = '1123'
ftp = FTP()
ftp.connect(host, port)
ftp.login(userid, password)


datenow = datetime.datetime.now()
yearnow = datenow.strftime('%Y')

# Find directory
Tmp_dir = ftp.cwd('backup/journal club in JUSTIN LAB/'+yearnow)
Tmp_fld_name = [s for s in ftp.nlst() if "glance" in s.lower()][0]

Tmp_dir = ftp.cwd(Tmp_fld_name)
upcoming_friday = upcoming_weekday(datenow, 4).date()
Tmp_fld_name = upcoming_friday.strftime('%Y%m%d')

if Tmp_fld_name not in ftp.nlst():
    ftp.mkd(Tmp_fld_name)
    print("### ['"+Tmp_fld_name+"'] forder created ###")

ftp.cwd(Tmp_fld_name)
print("### Current Dir : "+ftp.pwd())
