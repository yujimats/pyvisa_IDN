import pyvisa

rm = pyvisa.ResourceManager()
visa_list = rm.list_resources()
usb_1 = visa_list[0]
inst_1 = rm.open_resource(usb_1)

inst_1.write('*IDN?')
out = inst_1.read()

# queryを用いてももちろんOK
# out = inst_1.query('*IDN?')

print(out)
# (計測器の情報)
