name = input("File name: ").strip()
name = name.lower()
if name.find(".gif") != -1 :
    print("image/gif")
elif name.find(".jpg") != -1 or name.find(".jpeg") != -1:
    print("image/jpeg")
elif name.find(".png") != -1 :
    print("image/png")
elif name.find(".pdf") != -1 :
    print("application/pdf")
elif name.find(".txt") != -1 :
    print("text/plain")
elif name.find(".zip") != -1 :
    print("application/zip")
else :
    print("application/octet-stream")


