import datetime
date = "June 30, 2020"
formatted_date = datetime.datetime.strptime(date,"%B %d, %Y")
print(formatted_date)