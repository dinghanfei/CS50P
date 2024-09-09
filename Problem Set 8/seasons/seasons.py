from datetime import date, datetime
import inflect
import sys


def get_delta(birth_date, today):
    delta_day = today - birth_date # 结果精确到秒
    delta_minutes = delta_day.days * 24 * 60. # tdelta_day.days 获取时间差的天数。
    return int(delta_minutes)

def get_word(delta_minutes):
    p = inflect.engine()
    word = p.number_to_words(delta_minutes, andword="")
    word = word + ' minutes'
    word = word.replace(" thousand ", " thousand, ").capitalize()
    return word

def main():
    try:
        # 将输入字符串转化成时间，再获取其中精确到日期的部分
        birth_date = datetime.strptime(input("Date of Birth: "), '%Y-%m-%d').date()
        today = date.today()  # 2024-09-09
    except ValueError:
        sys.exit("Invalid date")

    delta_minutes = get_delta(birth_date, today)
    # print(delta_minutes)

    word = get_word(delta_minutes)

    print(word)


if __name__ == "__main__":
    main()
