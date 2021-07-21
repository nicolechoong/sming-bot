
from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("images/screenshot.jpeg")
font = ImageFont.truetype('Arial Unicode MS Bold.ttf', 40)
text = u"210721/11PM/nichyung/1번째"
editable = ImageDraw.Draw(my_image)
editable.text((30,80), text, (255, 255, 255), font)
my_image.save("timestamp.jpg")