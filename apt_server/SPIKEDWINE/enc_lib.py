from Crypto.Cipher import ARC4

hc_key = [0] * 256

def encrypt_data(stream):
    _arc4 = ARC4.new(hc_key)
    enc_data = _arc4.encrypt(stream)
    return enc_data

