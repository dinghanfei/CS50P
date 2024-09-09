import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # 使用了 [^"]+ 来匹配视频 ID，确保它不会超过引号的范围
    match = re.search(r'src="https?://(www\.)?youtube\.com/embed/([^"]+)"',s)
    if match:
        url = match.group(2)
        # print("url:",url)
        str = re.sub(r"^https?://(www\.)?youtube\.com/embed/","", url)
        return f"https://youtu.be/{str}"
    else:
        return "None"
if __name__ == "__main__":
    main()
