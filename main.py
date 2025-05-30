from GoRN import *
from schnorr_signature import SchnorrSignature


def generate_transaction(string: str = None):
    bytes = ''
    if string is not None:
        bytes += string.encode('utf-8').hex()
    while len(bytes) < 400:
        bytes += my_random.generate_random()
    bytes = bytes[:400]
    return bytes


def sum_of_hashes(h1: str, h2: str):
    return hex((int(h1, 16) + int(h2, 16)) % (2 ** 256))[2:]


# Generation of transactions
signature_algorythm = SchnorrSignature()
transactions = [generate_transaction("Dmitriy Kuleshov BIB233")] + [generate_transaction() for _ in range(5)]
signatured_transactions = [signature_algorythm.create_signature(transaction) for transaction in transactions]

# Using the second way to calculate the tree is when the number of transactions is not a power of two.
Merkle_tree = [gost_hash(transaction) for transaction in transactions]
# Now, Merkle Tree list: [H1, H2, H3, H4, H5]
Merkle_tree.append(gost_hash(sum_of_hashes(Merkle_tree[0], Merkle_tree[1])))
Merkle_tree.append(gost_hash(sum_of_hashes(Merkle_tree[2], Merkle_tree[3])))
# Now, Merkle Tree list: [H1, H2, H3, H4, H5, H12, H34]
Merkle_tree.append(gost_hash(sum_of_hashes(Merkle_tree[5], Merkle_tree[6])))
# Now, Merkle Tree list: [H1, H2, H3, H4, H5, H12, H34, H1234]
Merkle_tree.append(gost_hash(sum_of_hashes(Merkle_tree[7], Merkle_tree[4])))
# Now, Merkle Tree list: [H1, H2, H3, H4, H5, H12, H34, H1234, H12345]

# Creating parts of header
size_of_block = my_random.generate_random()[:8]
while bin(int(size_of_block[0], 16))[2] == '0':
    size_of_block = my_random.generate_random()[:8]

hash_of_previous_header = my_random.generate_random()

timestamp = format(23, '02x') + format(30, '02x') + format(5, '02x') + format(25, '02x')

for nonce in range(1, 1000):
    current_header = f'{size_of_block}{hash_of_previous_header}{Merkle_tree[-1]}{timestamp}{format(nonce, '08x')}'
    print(f'current header: {current_header}\nnonce = {nonce}')
    hash_current_header = gost_hash(current_header)
    bin_hash = bin(int(hash_current_header, 16))[2:].zfill(len(hash_current_header) * 4)
    print(f'hash: {hash_current_header}\n')
    if bin_hash[:5] == '00000':
        print("first 5 bits of hash are 00000!!!")
        break
