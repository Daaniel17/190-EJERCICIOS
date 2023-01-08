import speedtest

wifi = speedtest.Speedtest()

print("La velocidad de descarga es: ", wifi.download())
print("La velocidad de carga es: ", wifi.upload())