import qrcode

website_link = input("Enter link to generate to QRCode: ")
file_qr_name = input("Enter file name: ")

file_name = f"{file_qr_name}.png"

qr = qrcode.QRCode(box_size = 10, border = 10)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white")
img.save(file_name)
print(f"QRCode save as {file_qr_name}")

