import datetime

def upcoming_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

from ftplib import FTP
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
Tmp_dir = ftp.cwd('backup/journal club in JUSTIN LAB/'+yearnow+'/')
Tmp_fld_name = [s for s in ftp.nlst() if "glance" in s.lower()][0]

print(Tmp_dir)
print(Tmp_fld_name)

Tmp_dir = ftp.cwd(Tmp_fld_name+'/')
upcoming_friday = upcoming_weekday(datenow, 4).date()
Tmp_fld_name = upcoming_friday.strftime('%Y%m%d')

print(Tmp_dir)
print(Tmp_fld_name)

# Tmp_fld_datelist = [datetime.strptime(Tmp_fld,'%Y%m%d').date() for Tmp_fld in ftp.nlst()]
#
# Fld = [date for date in Tmp_fld_datelist if date < datenow.date()]
# if Fld:
#     Fld_weekday = [ i.weekday() for i in Fld]
