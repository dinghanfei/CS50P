import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d{1,2})(:\d{2})? (A|P)M to (\d{1,2})(:\d{2})? (A|P)M$", s)

    if match:
        start_hour = int(match.group(1))
        start_minute = match.group(2) if match.group(2) else ":00"

        if start_hour > 12 or int(start_minute.replace(":","")) >= 60 :
            raise ValueError
        start_period = match.group(3)
        if start_period == 'P' and start_hour != 12:
            start_hour += 12
        if start_period == 'A' and start_hour == 12:
            start_hour = 0
        if start_hour < 10:
            start_hour = f"0{start_hour}"

        end_hour = int(match.group(4))
        end_minute = match.group(5) if match.group(5) else ":00"
        if end_hour > 12 or int(end_minute.replace(":","")) >=60:
            raise ValueError
        end_period = match.group(6)
        if end_period == 'P' and end_hour != 12:
            end_hour += 12
        if end_hour < 10:
            end_hour = f"0{end_hour}"

        return f"{start_hour}{start_minute} to {end_hour}{end_minute}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
