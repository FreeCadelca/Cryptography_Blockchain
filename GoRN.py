from gost_hash import gost_hash

name_of_student = "Kuleshov Dmitriy Sergeevich BIB233"
name_of_student_hex = ''.join(hex(byte)[2:] for byte in name_of_student.encode('utf-8'))
name_of_student_hex += '0' * (128 - len(name_of_student_hex))


# print(f'hex view of student\'s personal string: {name_of_student_hex}')


class RandomGenerator:
    def __init__(self):
        self.iteration = 0
        self.h0 = gost_hash(name_of_student_hex, isHex=True)
        self.seed = self.h0
        # print(f'seed = h0 = {self.seed}')

    def generate_random(self):
        self.iteration += 1
        new_input_for_hash = self.h0 + hex(self.iteration)[2:]
        new_input_for_hash += '0' * (512 - len(new_input_for_hash))  # дополнение нулями до 512 бит
        return gost_hash(new_input_for_hash, isHex=True)


if __name__ == "__main__":
    my_random = RandomGenerator()
    for i in range(10):
        print(my_random.generate_random())
