## CTF Scripts

This repository contains script solutions for various CTF challenges. 

## Contents

### CryptoPals
| Challenge                                     | Set   | Script                                 |
|-----------------------------------------------|-------|----------------------------------------|
| 01. Convert hex to base64                     | Set 1 |[challenge_01.py](set1/challenge_01.py) |
| 02. Fixed XOR                                 | Set 1 |[challenge_02.py](set1/challenge_02.py) |
| 03. Single-byte XOR cipher                    | Set 1 |[challenge_03.py](set1/challenge_03.py) |
| 04. Detect single-character XOR               | Set 1 |[challenge_04.py](set1/challenge_04.py) |
| 05. Implement repeating-key XOR               | Set 1 |[challenge_05.py](set1/challenge_05.py) |
| 06. Break repeating-key XOR                   | Set 1 |[challenge_06.py](set1/challenge_06.py) |
| 07. AES in ECB mode                           | Set 1 |[challenge_07.py](set1/challenge_07.py) |
| 08. Detect AES in ECB mode                    | Set 1 |[challenge_08.py](set1/challenge_08.py) |
| 09. Implement PKCS#7 padding                  | Set 2 |[challenge_09.py](set2/challenge_09.py) |
| 10. Implement CBC mode                        | Set 2 |[challenge_10.py](set2/challenge_10.py) |
| 11. An ECB/CBC detection oracle               | Set 2 |[challenge_11.py](set2/challenge_11.py) |
| 12. Byte-at-a-time ECB decryption (Simple)    | Set 2 |[challenge_12.py](set2/challenge_12.py) |
| 13. ECB cut-and-paste                         | Set 2 |[challenge_13.py](set2/challenge_13.py) |
| 14. Byte-at-a-time ECB decryption (Harder)    | Set 2 |[challenge_14.py](set2/challenge_14.py) |
| 15. PKCS#7 padding validation                 | Set 2 |[challenge_15.py](set2/challenge_15.py) |
| 16. CBC bitflipping attacks                   | Set 2 |[challenge_16.py](set2/challenge_16.py) |
| 17. The CBC Padding oracle                    | Set 3 |[challenge_17.py](set3/challenge_17.py) |

### Hack The Box 
| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| Alpashcii Clashing    | crypto   | [alphascii_clashing.py](htb/crypto/alphascii_clashing.py)              | MD5 hash collision.                                               |
| Ancient Encodings     | crypto   | [ancient_encodings.py](htb/crypto/ancient_encodings.py)                | Base64, hex encodings.                                            |
| Android in the Middle | crypto   | [android_in_the_middle.py](htb/crypto/android_in_the_middle.py)        | Diffie-Hellman. Choosen Public Key Attack.                        |
| Arranged              | crypto   | [arranged.py](htb/crypto/arranged.py)                                  | ECC. Small subgroup discrete log.                                 |
| Baby quick maffs      | crypto   | [baby_quick_maffs.py](htb/crypto/baby_quick_maffs.py)                  | Modular arithmetic. Equation manipulation.                        |
| Binary basis          | crypto   | [binary_basis.py](htb/crypto/binary_basis.py)                          | RSA. Multiple primes encoding.                                    |
| Brainy's Cipher       | crypto   | [brainys_cipher.py](htb/crypto/brainys_cipher.py)                      | RSA. Chinese Remainder Theorem.                                   |
| Brevi Moduli          | crypto   | [brevi_moduli.py](htb/crypto/brevi_moduli.py)                          | RSA. Small modulus factorization.                                 |
| Digital Safety Annex  | crypto   | [digital_safety_annex.py](htb/crypto/digital_safety_annex.py)          | DSA. Nonce $k$ brute force.                                       |
| Fast Carmichael       | crypto   | [fast_carmichael.py](htb/crypto/fast_carmichael.py)                    | Carmichael numbers. Find the paper challenge.                     |
| Flippin Bank          | crypto   | [flippin_bank.py](htb/crypto/flippin_bank.py)                          | AES. Flipping bit attack.                                         |
| Gonna lift em all     | crypto   | [gonna_lift_em_all.py](htb/crypto/gonna_lift_em_all.py)                | ElGamal. Implementation flaw.                                     |
| Hidden Handshake      | crypto   | [hidden_handshake.py](htb/crypto/hidden_handshake.py)                  | AES CTR. Known Plaintext attack.                                  |
| Initialization        | crypto   | [initialization.py](htb/crypto/initialization.py)                      | AES.CTR. Known Plaintext attack.                                  |
| Lost Key              | crypto   | [lostkey.py](htb/crypto/lostkey.py)                                    | ECC. Curve parameters recovery. Pohlig-Hellman.                   |
| Lost Modulus          | crypto   | [lost_modulus.py](htb/crypto/lost_modulus.py)                          | RSA. Small exponent without message padding.                      |
| Lost Modulus Again    | crypto   | [lost_modulus_again.py](htb/crypto/lost_modulus_again.py)              | RSA. Coppersmith's short pad attack.                              |
| Nuclear Sale          | crypto   | [nuclear_sale.py](htb/crypto/nuclear_sale.py)                          | .pcap analysis                                                    |
| Optimus Prime         | crypto   | [optimus_prime.py](htb/crypto/optimus_prime.py)                        | RSA. Shared prime on different keys. GCD attack                   |
| Quadratic Points      | crypto   | [quadratic_points.py](htb/crypto/quadratic_points.py)                  | Integer polynomial coefficients recovery. ECC discrete log. CRT.  |
| RLotto                | crypto   | [rlotto.py](htb/crypto/rlotto.py)                                      | PRNG. Time seed                                                   |
| Rookie Mistake        | crypto   | [rookie_mistake.py](htb/crypto/rookie_mistake.py)                      | RSA. Implementation fault.                                        |
| Secure Signing        | crypto   | [secure_signing.py](htb/crypto/secure_signing.py)                      | SHA256. Byte at a time Oracle Attack                              |
| Sekur Julius          | crypto   | [sekur_julius.py](htb/crypto/sekur_julius.py)                          | Caesar cipher brute force.                                        |
| SPG                   | crypto   | [spg.py](htb/crypto/spg.py)                                            | AES. Weak random key recovery.                                    |
| Spooky RSA            | crypto   | [spooky_rsa.py](htb/crypto/spooky_rsa.py)                              | RSA. Encrypted prime. GCD attack.                                 |
| Sugar Free Candies    | crypto   | [sugar_free_candies.py](htb/crypto/sugar_free_candies.py)              | Integer equation system.                                          |
| Symbols               | crypto   | [symbols.py](htb/crypto/symbols.py)                                    | Legendre symbol.                                                  |
| Two for One           | crypto   | [two_for_one.py](htb/crypto/two_for_one.py)                            | RSA. Polynomial gcd. Franklin-reiter attack.                      |
| Weak RSA              | crypto   | [weak_rsa.py](htb/crypto/weak_rsa.py)                                  | RSA. Small $d$. Wiener Attack.                                    |

### TAMUctf 2026
| Challenge             | Category | Script                                                                                         | Topics                                    |
|-----------------------|----------|------------------------------------------------------------------------------------------------|-------------------------------------------|
| Abnormal Ellipse      | crypto   | [abnormal_ellipse.py](TAMUctf-2026/crypto/abnormal-ellipse/abnormal_ellipse.py)                | ECC. Smart Attack.                        |
| Hidden Log Factoring  | crypto   | [hidden_log_factoring.py](TAMUctf-2026/crypto/hidden_log_factoring/hidden_log_factoring.py)    | RSA. Pohlig-Hellman. Factor $N$ from $d$. |
