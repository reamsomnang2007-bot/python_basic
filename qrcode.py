import qrcode
url_link = input("Enter the URL: ")
file_name = input("Enter the file name: ")
file_name = f"{file_name}.png"

qr = qrcode.QRCode(box_size = 10, border = 10)
qr.add_data(url_link)
qr.make()

qr_img = qr.make_image()
qr_img.save(file_name)
print(f"Qrcode saved as {file_name}")