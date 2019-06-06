from datetime import datetime
date_format = "%H:%M"
time1  = datetime.strptime('04:50', date_format)
time2  = datetime.strptime('05:50', date_format)
diff = time2 - time1
diff_btw_two_times = (diff.seconds) / 3600
hours = (diff.seconds) / 3600  
print (str(hours))
