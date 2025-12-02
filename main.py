import qrcode

link_gdrive = "https://drive.google.com/file/d/1unWtTk4o5svtSo2Qe3tyeLOdSJgG-CrM/view?usp=sharing"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

qr.add_data(link_gdrive)
qr.make(fit=True)

# 4. Create the image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# 5. Save the QR code image (You can change the file name)
file_name = "qr_seminar_hasil_diffa.png"
img.save(file_name)

print(f"Success! QR code has been saved as: {file_name}")