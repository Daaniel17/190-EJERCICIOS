from pyzbar.pyzbar import decode
from PIL import Image

decodificado=decode(Image.open("youtube.png"))
print(decodificado[0].data.decode("ascii"))