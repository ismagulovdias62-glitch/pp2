import datetime
now = datetime.datetime.now()
# # print(now)

# # s = input("пиши свою дату: ГГГГ-ММ-ДД")
# # date = datetime.datetime.strptime(s, "%Y-%m-%d")
# # age = now - date
# # print(age.days//365)
# d = input("YYYY-MM--DD")
# da= datetime.datetime.strptime(d, "%Y-%m-%d")
# new = datetime.datetime(now.year, da.month, da.day)
# if now > new:
#     new = datetime.datetime(now.year+1, da.month, da.day)
# qwe = new - now
# print(qwe.days)
# d = input("yyyy-mm-dd")
# e = input("yyyy-mm-dd")
# date_1=datetime.datetime.strptime(d, "%Y-%m-%d")
# date_2=datetime.datetime.strptime(e, "%Y-%m-%d")
# diff= date_1 - date_2
# days = abs(diff.days)
# week = days//7
# print(days, week)
d = input("yyyy-mm-dd")
date = datetime.datetime.strptime(d, "%Y-%m-%d")
age = now - date
print(age.total_seconds())