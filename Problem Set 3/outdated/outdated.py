from datetime import datetime
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def validate(date_str):
    formats = ['%m/%d/%Y','%B %d, %Y']
    for fmt in formats:
        try:
            date = datetime.strptime(date_str,fmt)  #strptime通过fmt中的格式指令来解析字符串
            return date
        except ValueError:
            continue
    return False
while True:
    date_str = input("Date: ").strip()
    if not validate(date_str):
        continue
    else:
        date = validate(date_str)  # eg: 2023-08-15 00:00:00
        break
print(date.strftime('%Y-%m-%d'))  #使用 strftime() 方法来格式化输出


'''
常用的格式化指令：

%Y：四位数的年份（例如：2023）
%m：月份（01到12）
%d：月份中的日（01到31）
%H：小时（24小时制，00到23）
%I：小时（12小时制，01到12）
%M：分钟（00到59）
%S：秒（00到59）
%b：月份的缩写名称（Jan, Feb, ...）
%B：月份的全称名称（January, February, ...）
%a：星期的缩写名称（Mon, Tue, ...）
%A：星期的全称名称（Monday, Tuesday, ...）
'''
