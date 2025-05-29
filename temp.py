from gost_hash import gost_hash

p = 0xee8172ae8996608fb69359b89eb82a69854510e2977a4d63bc97322ce5dc3386ea0a12b343e9190f23177539845839786bb0c345d165976ef2195ec9b1c379e3
q = 0x98915e7eb064bdc7c8265edf285dd50dcda31e887289f0acf24809dd6f49dd2d
g = 0x9e96031500c8774a869582d4afde2127afad2538b4b6270a67fc8837b50d50f206755984a49e509304d648be2ab5aab18ebe2cd46ac3d8495b142aa6ce232e1c

r = 12345 % q
R = pow(g, r, p)
x = 67890 % q
P = pow(g, x, p)
m = "test"
R_bytes = R.to_bytes(64, byteorder='big')
P_bytes = P.to_bytes(64, byteorder='big')
e = int(gost_hash(R_bytes + P_bytes + m.encode('utf-8')), 16) % q
s = (r + e * x) % q
# Verify
e_verify = int(gost_hash(R_bytes + P_bytes + m.encode('utf-8')), 16) % q
lvalue = (R * pow(P, e_verify, p)) % p
rvalue = pow(g, s, p)
print(lvalue == rvalue)