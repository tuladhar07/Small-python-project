import qrcode
#img= qr.make("https://nhujawtuladhar.com.np/")
#--img.save("Selfwebsite.png")

from PIL import Image

qr=qrcode.QRCode( version=1 , error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=5,)

qr.add_data("https://nhujawtuladhar.com.np/")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="black")
img.save("profile2.png ")