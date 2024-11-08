import qrcode

f = open("links.txt", "rt")

for link in f:
    data = qrcode.make(link)
    data.save("qrCodes/bin_name.png")

f.close()