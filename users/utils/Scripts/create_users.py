from datetime import datetime,timedelta

# date1 = datetime.now()
# print(date1)
# three_days = timedelta(days=3)
# date2 = three_days+date1

# time_difference = date2 - date1
# print (time_difference.total_seconds()//3600)

# def is_within_days_from_current_time(self,days=1):
#         cur_time = datetime.now()
#         time_diff = cur_time-self.datetime_employee_registered
#         return time_diff.days < days
cur_Date = datetime.now()
past_date = cur_Date - timedelta(days=1)

print(cur_Date-past_date)