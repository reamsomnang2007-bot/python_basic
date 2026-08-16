import datetime

date = datetime.date(2007, 10,  1)
today = datetime.date.today()
print(f"My birthday was {date}")
print(f"Today is {today}")

time = datetime.time(23, 16, 3)
now = datetime.datetime.now()
now_change = now.strftime("%H:%M:%S")
print(f"Time {time}")
print(f"Now: {now_change}")


target_datetime = datetime.datetime(2026, 20, 23, 11, 20, 3)
curren_datetime = datetime.datetime.now()


if target_datetime < curren_datetime:
    print("Target has passed.")
else:
    print("Target has NOT passed. ")