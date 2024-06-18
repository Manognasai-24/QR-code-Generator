import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
myqr = qrcode.make("https://www.salesforce.com/trailblazer/gudivadamanognasai")
myqr1 = qrcode.make("https://trailhead.salesforce.com/content/learn/superbadges/superbadge_developer_superset")
myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))