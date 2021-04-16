from elGamal import PublicKey


def cipher_to_file(string):
    f = open('files/cipher.txt', 'w')
    f.write(string);
    f.close()


def cipher_from_file():
    f = open('files/cipher.txt', 'r')
    temp = f.read()
    f.close()
    return temp


def key_to_file(public_key, private_key):
    f = open('files/public.txt', 'w')
    f.write('P:' + str(public_key.p) + '\n')
    f.write('G:' + str(public_key.g) + '\n')
    f.write('Y:' + str(public_key.y))
    f.close()

    f = open('files/private.txt', 'w')
    f.write('X:' + str(private_key))
    f.close()


def key_from_file():
    f = open('files/public.txt', 'r')
    temp = f.readlines()
    public_key = PublicKey(int(temp[0][2:-1]), int(temp[1][2:-1]), int(temp[2][2:]))
    f.close()

    f = open('files/private.txt', 'r')
    temp = f.read()
    private_key = int(temp[2:])
    f.close()

    return public_key, private_key
