import json

from GoRN import RandomGenerator
from gost_hash import gost_hash


class SchnorrSignature:
    def __init__(self):
        self.p = 0xEE8172AE8996608FB69359B89EB82A69854510E2977A4D63BC97322CE5DC3386EA0A12B343E9190F23177539845839786BB0C345D165976EF2195EC9B1C379E3
        self.q = 0x98915E7EC8265EDFCDA31E88F24809DDB064BDC7285DD50D7289F0AC6F49DD2D
        self.g = 0x9E96031500C8774A869582D4AFDE2127AFAD2538B4B6270A6F7C8837B50D50F206755984A49E509304D648BE2AB5AAB18EBE2CD46AC3D8495B142AA6CE23E21C
        self.my_rand = RandomGenerator()

        self.__x = int(self.my_rand.generate_random(), 16) % self.q
        self.P = pow(self.g, self.__x, self.p)

    def create_signature(self, m: str) -> str:
        r = int(self.my_rand.generate_random(), 16) % self.q  # nonce of signature
        R = pow(self.g, r, self.p)
        R_bytes = format(R, '0128x')
        P_bytes = format(self.P, '0128x')
        my_hash = gost_hash(R_bytes + P_bytes + m)
        e = int(my_hash, 16) % self.q
        s = (r + e * self.__x) % self.q
        return json.dumps({'R': R, 's': s})

    def check_signature(self, m: str, sign: str) -> bool:
        sign_dict = json.loads(sign)
        R, s = sign_dict["R"], sign_dict["s"]
        R_bytes = format(R, '0128x')
        P_bytes = format(self.P, '0128x')
        my_hash = gost_hash(R_bytes + P_bytes + m)
        e = int(my_hash, 16) % self.q
        lvalue = (R * pow(self.P, e, self.p)) % self.p
        rvalue = pow(self.g, s, self.p)
        return lvalue == rvalue


if __name__ == "__main__":
    message = "Kuleshov Dmitriy"

    signature_algorythm = SchnorrSignature()
    signature = signature_algorythm.create_signature(message)
    flag_is_signature_fine = signature_algorythm.check_signature(message, signature)
    print(signature, flag_is_signature_fine)


