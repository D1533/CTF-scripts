#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64

cert = """
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtVf6CDwFYrEnH
k4R/8NMG0Sb8m6mVUy4y1LAX8nbYlJI6llRp0gvi1wRbsoDdmZ48oCFBd26rlc01
EXA3xrN/Fw4gcITyxtqNsgq2r2x2dAOuZW6MxI1948iLDE4VAR+H2U8iJiQq5z3Y
51tjaS+JlW/rvu/W3rdDbrkSXgju/wmmMNmIR6z7kzn5l/twq3mXJxkOZZLzs7Bt
hzrDlH/JgUhWr0gxfR2wdvwQft6QJ82iXadqzH4C5ZEVVO350aJUta7QPao4R+11
ZWjtln5mssQUEAaM6DjYbEM66Uy3iplESy2Nsx0Qnk+LmogEQcRhXSq00HgOeBMO
Z0VHZPLHAgMBAAECggEACG3dIY//PcOrFtR6pgodCQDUx4X+Wi+gWIJ1ScTVuLSI
4+Z5lmfLgi14ncjxcVVOF56l31wiep+fSgxeC6hTBEQnwLYYEQJQkIFu+fFP8fa0
Ux/Fn3zTcKLKFtDzXxwd32pW6c83BQsXu9uMWyo7UJJ+zdUMLsPH37SbtWPzRUP3
CBhTRrE7fpeKuCptCVUiq61lXfmNX4kBwYcAyC4wsA27kWlntzdLEnpxnVaAfOt1
jv/xxcf2x9Ua0y034/WiLJ09JViQDmm6yDBsJggOlKKV/D0aLelvOpHMtk1xXO3f
rLWJi54WrRBJJMBk0R3XIEWSaGScxQVPDvEPeHN6QQKBgQC1ETs0f4jxPXDMr9pg
iNs8qk7UqMxKECUKmZ5os3ne4EU06Mif+lNRNNZmNxOnFTKF860ByLVP0PQVZ7Xf
I7q/orc2OlFQS0P972j0WJRzG2PCSU+dKHwwhgKlZ8k1hA8VOI4WW6dbo4iZehJp
U3Zqt0gOvf39R875GcrvcNuN5wKBgQD1Ea17V+fs/zIlVtJ5RKgnp1tvvkkXUg5D
TgZbFbqmMWoNjcrvLI86Tq700ALjBgHaUkY7n9zRg84WNBWIrVJlhufrKhGCkqpb
KsyiVOQdEi7oLpcXIxFAoV79pVOv3x7ubnFSi1Ff+mHDeuBu5UZkBHlNSY6CrW6J
gjdpjqYYIQKBgFhMxuqbJ1U9+TxYpc5d70xuYXMjvjyAExBQSggVPmGKTTW4L96U
XP1FHylJwrPAipr4cm5kSsdZxy6JHRBshC3gVCiF2BGoIsg7cJt4dyyLNuMQjVq+
25FuSOwQ6PbIJ/LZWbFdkQgHgB4YgdILebwhFWrbDHnwAudHxMdv6iIRAoGALckD
tEuUFP8Ii1lRMT7We7IUryfJ2AWIjKKDJXlFyc7plWasR0r351jT7wD9yRRSPEuq
u3D+fFY3poZMj6ByCG3P3muZod9s3GN+n8VkaNoA0XgC2lu+2WhMqu68V9tDmCAi
I93LcjcBFNhcHdvP7te3Ie1gJqHoSOB/IcV42oECgYEAj7DgOtLsNeDJOZhVwG0H
gzPgcC2eY2Q5ugW5vObtrEXJrEyo188E1tEuDeLnOJZUbsDKdGcRTRjEAazfChfE
XG0xDG9TSv9sq3hz9IvESH4Tp8ccfoK8+ulqTCCvz5g6l90B2qOpF7/6J8DuMNxn
N/OwBNoNPzMla2CJmbCsbGc=
"""

ct = b'\xa3c\xdd\x93\xee\x17~\x99gv\xe9\x00\xab\x16\xed\xcf9\xd3\xb6\x81\xed]\x80\xda\x82C\xed\xf0\xd1\xb4#\x02\x00\xeb>a\xbc\xe4\xc2\xf6\x0b\xd5:4]\x9c\x14\xcd~\x8e\xf8\x12`$#\x9f\xd2/\xfa?\x9f\xed)\xdaq\xf0\xc1F\xfd7fv\x07\xa7EW\xc9l\xfd\xe7\xeaP\xd8\x93:\x8b.%\x10a0c\xef\xe5\xb4\x15\xcc\xc0\xf0\xce\xfczd\xdf1\xab\xacqx\x87\xef\x15\xdf\xf4\xb2.\xff\xb4\x0c\n\xcb\xbc\x06\x9b\xb8\xc2\xc7%Q_A\xca\xado\xad\xc7\x14F\xb9+\x8dl\xee\xfc$\x82\xe2\xc6m\xd6\xc9\x86G\xad\xce>\xf5\xab\xbc\x04\x90\xcbHy\x12q\x85m\x87\xddq\x10\xba\x8d\x9eE\x04`m\x82\x1e.s{\x8b\x01yY\xce\xbfV,P<G\xa207U\xde]\xdb\xed\\\xb8\x95\x0b\xfbP\xb9z\xe1l\xa8\xda\xc3\x92\xf7\xf4\x19\xe2\x01\x9e-n\xfd\xb1\x90DL\xda\x8b\xdb\x0c\xf1\x0b#\xa5\xd3\x18|\x08\xcf\xa0\x03I\xe6^w\xa8M\xbf@\xb0\t\x84'

key = RSA.import_key(base64.b64decode(cert))
n = key.n
d = key.d

m = pow(bytes_to_long(ct), d, n)
flag = long_to_bytes(m)
print(flag)










