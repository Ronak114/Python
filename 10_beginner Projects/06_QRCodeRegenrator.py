import qrcode

url = input("Enter the URL to generate QR Code: ")
filename = input("Enter the filename to save the QR Code (with .png extension): ")

img = qrcode.make(url)
img.save(filename)