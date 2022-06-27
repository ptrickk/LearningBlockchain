import rsa

# publicKey, privateKey = rsa.newkeys(512)

# publicKey = rsa.PublicKey(11463448871646640232317610049778306743924507583756111373828195256129605642885397372393976249999771295075994163104405692664910120900245900588325488692345413, 65537)
# privateKey = rsa.PrivateKey(11463448871646640232317610049778306743924507583756111373828195256129605642885397372393976249999771295075994163104405692664910120900245900588325488692345413, 65537, 4125911042379128580800277489878552565355315087441279812714336477128723282178931501098551382582026354208890090894775998943285867647092486928405020193355825, 6792441893875039069711718808880026244220324447628488154629219296960350864883130807, 1687677134490262882338581540769322272561174980176932135431142344327615459)

class Key:
    def __init__(self, filename):
        self.filename = filename
        self.readKey()

    def readKey(self):
        f = open(self.filename, "r")
        n = int(f.readline())
        e = int(f.readline())
        d = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())
        self.publicKey = rsa.PublicKey(n, e)
        self.privateKey = rsa.PrivateKey(n, e, d, p, q)
        self.address = hex(n)


class KeyGenerator:
    def __init__(self, keysize, filename):
        self.keySize = keysize
        self.filename = filename

    def generate(self):
        publicKey, privateKey = rsa.newkeys(512)
        f = open(self.filename, "w")
        f.write(str(privateKey.n) + '\n' + str(privateKey.e) + '\n' + str(privateKey.d) + '\n' + str(
            privateKey.p) + '\n' + str(privateKey.q))
        f.close()


'''
message = "Hello this is a test message!"
sig = "Signature Patrick Geertz"

enc = rsa.encrypt(message.encode(), publicKey)
dec = rsa.decrypt(enc, privateKey).decode()

signature = rsa.sign(sig.encode(), privateKey, 'SHA-1')
verification = rsa.verify(sig.encode(), signature, publicKey)

print(message)
print(enc)
print(dec)

print(sig)
print(signature)
print(signature == signature)
print(verification)

print(publicKey)
print(privateKey)'''
