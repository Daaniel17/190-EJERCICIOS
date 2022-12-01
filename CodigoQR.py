import pyqrcode
import png

link="https://www.youtube.com/watch?v=qYSkrETBnYI"

codigo_qr=pyqrcode.create(link)

codigo_qr.png("youtube.png", scale=5)