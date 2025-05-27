import pprint
import numpy
import numpy as np

PI = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147,
      46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1,
      142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72,
      171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135,
      21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61, 255, 53, 138, 126,
      109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3,
      224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26,
      184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88,
      179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83,
      170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
      116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

IV = [int(i) for i in '00000001' * 64]

TETA = (0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27,
        35, 43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7,
        15, 23, 31, 39, 47, 55, 63)

C = [
    0xb1085bda1ecadae9ebcb2f81c0657c1f2f6a76432e45d016714eb88d7585c4fc4b7ce09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507,
    0x6fa3b58aa99d2f1a4fe39d460f70b5d7f3feea720a232b9861d55e0f16b501319ab5176b12d699585cb561c2db0aa7ca55dda21bd7cbcd56e679047021b19bb7,
    0xf574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea7514b1297b7bd3e20fe490359eb1c1c93a376062db09c2b6f443867adb31991e96f50aba0ab2,
    0xef1fdfb3e81566d2f948e1a05d71e4dd488e857e335c3c7d9d721cad685e353fa9d72c82ed03d675d8b71333935203be3453eaa193e837f1220cbebc84e3d12e,
    0x4bea6bacad4747999a3f410c6ca923637f151c1f1686104a359e35d7800fffbdbfcd1747253af5a3dfff00b723271a167a56a27ea9ea63f5601758fd7c6cfe57,
    0xae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e,
    0xf4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c90992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493,
    0x9b1f5b424d93c9a703e7aa020c6e41414eb7f8719c36de1e89b4443b4ddbc49af4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e,
    0x378f5a541631229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d0984800a440bdbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb,
    0xabbedea680056f52382ae548b2e4f3f38941e71cff8a78db1fffe18a1b3361039fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced,
    0x7bcd9ed0efc889fb3002c6cd635afe94d8fa6bbbebab076120018021148466798a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd85d6bcaa4cd81f32d1b,
    0x378ee767f11631bad21380b00449b17acda43c32bcdf1d77f82012d430219f9b5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720]

a_matrix_compressed = []
with open("ssss") as f:
    a_matrix_compressed = [i.rstrip() for i in f.readlines()]

A_MATRIX = []
for i in a_matrix_compressed:
    new_line = []
    for j in i:
        j_to_bits = [int(bit) for bit in format(int(j, 16), '04b')]
        new_line += j_to_bits
    A_MATRIX.append(new_line)


# for i in a_matrix:
#       print(*i)

def X(k: list[int], a: list[int]) -> list[int]:
    return [a[i] ^ k[i] for i in range(min(len(k), len(a)))]


def L(v: list[int]) -> list[int]:
    a = [v[i * 64:i * 64 + 64] for i in range(8)]
    res = []
    for i in range(len(a)):  # mb reverse
        res += [int(k) for k in np.array(a[i]) @ np.array(A_MATRIX)]
    return res


def S(v: list[int]) -> list[int]:
    a = [int(''.join(map(str, v[i * 8:i * 8 + 8])), 2) for i in range(64)]
    res = []
    for i in range(len(a)):  # mb reverse
        new_value_bin = bin(PI[a[i]])[2:]
        res += [int(i) for i in new_value_bin]
    return res


def P(v: list[int]) -> list[int]:
    a = [int(''.join(map(str, v[i * 8:i * 8 + 8])), 2) for i in range(64)]
    res = []
    for i in range(len(a)):  # mb reverse
        new_value_bin = bin(a[TETA[len(a) - i - 1]])[2:]
        res += [int(i) for i in new_value_bin]
    return res


def E(k: list[int], m: list[int]):
    res = m.copy()
    K_list = [k.copy()]
    for i in range(1, 13):
        K_list.append(L(P(S(X(K_list[i - 1], C[i - 1])))))

    for i in range(12):
        res = L(P(S(X(K_list[i], res))))
    res = X(K_list[12], res)
    return res


def g(n: list[int], h: list[int], m: list[int]) -> list[int]:
    return X(X(E(L(P(S(X(h, n)))), m), h), m)
