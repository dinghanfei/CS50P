def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13 :
        print("lunch time")
    elif time >= 18 and time <= 19 :
        print("dinner time")
    else :
        return

def convert(time):
    time = time.split(":")
    t = int(time[0]) + int(time[1]) / 60.0
    return t

if __name__ == "__main__":
    main()
