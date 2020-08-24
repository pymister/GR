# import datetime
# import pytz
# # tz_info = pytz.timezone("UTC")
# # now = datetime.datetime.now().replace(tzinfo=tz_info)  # 获取当前世界协调时间
# #
# # print(now.hour)
# #
# #
# # now = datetime.datetime.now().replace(tzinfo=tz_info)  # 获取当前世界协调时间
# # if now.hour > 21:
# #     yesterday = now - datetime.timedelta(hours=(now.hour - 21), minutes=now.minute, seconds=now.second,
# #                                          microseconds=now.microsecond)
# # else:
# #     yesterday = now - datetime.timedelta(hours=(now.hour + 3), minutes=now.minute, seconds=now.second,
# #                                          microseconds=now.microsecond)
# # print(yesterday)
# SYSTEM_TIMEZONE = pytz.timezone('UTC')  #生成时区对象,来作为datatime.datatime.now()的参数传入,能将当前时间转化为对应时区的时间
#
# date_range = [
#     [datetime.datetime(2019, 3, 10, 21), datetime.datetime(2019, 11, 2, 21)],#夏令时时间
#     [datetime.datetime(2020, 3, 8, 21), datetime.datetime(2020, 10, 31, 21)],
#     [datetime.datetime(2021, 3, 14, 21), datetime.datetime(2021, 11, 6, 21)],
#     [datetime.datetime(2022, 3, 13, 21), datetime.datetime(2022, 11, 5, 21)],
#     [datetime.datetime(2023, 3, 12, 21), datetime.datetime(2023, 11, 4, 21)],
# ]
# now = datetime.datetime.now().astimezone(SYSTEM_TIMEZONE)
# now_five_hours = now - datetime.timedelta(hours=now.hour + 3, seconds=now.second, minutes=now.minute,
#                                           microseconds=now.microsecond)  # 当前时间 - 今天已过时间 + 3小时,就是昨天的21:00了
#
#
# print(now)
# print(now_five_hours)
# # TODO:settings的date_range改造成字典
# time_data = {2019: date_range[0], 2020: date_range[1], 2021: date_range[2]}
# # 获取今年的夏令时时间
# time_range_data = time_data[now.year]
# print(time_range_data)
# print('___________')
# print(time_range_data[0].replace(tzinfo=SYSTEM_TIMEZONE))
# print(time_range_data[1].replace(tzinfo=SYSTEM_TIMEZONE))
# if not (time_range_data[0].replace(tzinfo=SYSTEM_TIMEZONE) <= now_five_hours <= time_range_data[1].replace(
#         tzinfo=SYSTEM_TIMEZONE)):
#     now_five_hours += datetime.timedelta(hours=1)

