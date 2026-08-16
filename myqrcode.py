import qrcode

link_website = input("Enter link of make QRCode: ")
file_name = input("Enter File_Name: ")
file_name = f"{file_name}.png"

qr = qrcode.QRCode(version = 5, box_size = 5, border = 5 )
qr.add_data(link_website)
qr.make()

img = qr.make_image(fill_color = "red", back_color = "yellow")
img.save(file_name)
print(f"QRCode save as file_name '{file_name}'.")