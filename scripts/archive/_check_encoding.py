with open(r'C:\Microsaas\obra\src\i18n\en.json', 'rb') as f:
    data = f.read()
pos = data.find(b'\x81')
if pos >= 0:
    print(f'Byte 0x81 at position {pos}')
    ctx = data[max(0,pos-30):pos+30]
    print(f'Context hex: {ctx.hex()}')
else:
    print('No byte 0x81 found')
# Try to decode as utf-8 with replacement
try:
    text = data.decode('utf-8')
    print('File is valid UTF-8')
except UnicodeDecodeError as e:
    print(f'UTF-8 decode error at {e.start}: {e.reason}')
