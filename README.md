## CTF Scripts

This repository contains script solutions for various CTF challenges. 

## Contents

## CryptoPals

| Challenge                                     | Set   | Script                                            |
|-----------------------------------------------|-------|---------------------------------------------------|
| 01. Convert hex to base64                     | Set 1 |[challenge_01.py](cryptopals/set1/challenge_01.py) |
| 02. Fixed XOR                                 | Set 1 |[challenge_02.py](cryptopals/set1/challenge_02.py) |
| 03. Single-byte XOR cipher                    | Set 1 |[challenge_03.py](cryptopals/set1/challenge_03.py) |
| 04. Detect single-character XOR               | Set 1 |[challenge_04.py](cryptopals/set1/challenge_04.py) |
| 05. Implement repeating-key XOR               | Set 1 |[challenge_05.py](cryptopals/set1/challenge_05.py) |
| 06. Break repeating-key XOR                   | Set 1 |[challenge_06.py](cryptopals/set1/challenge_06.py) |
| 07. AES in ECB mode                           | Set 1 |[challenge_07.py](cryptopals/set1/challenge_07.py) |
| 08. Detect AES in ECB mode                    | Set 1 |[challenge_08.py](cryptopals/set1/challenge_08.py) |
| 09. Implement PKCS#7 padding                  | Set 2 |[challenge_09.py](cryptopals/set2/challenge_09.py) |
| 10. Implement CBC mode                        | Set 2 |[challenge_10.py](cryptopals/set2/challenge_10.py) |
| 11. An ECB/CBC detection oracle               | Set 2 |[challenge_11.py](cryptopals/set2/challenge_11.py) |
| 12. Byte-at-a-time ECB decryption (Simple)    | Set 2 |[challenge_12.py](cryptopals/set2/challenge_12.py) |
| 13. ECB cut-and-paste                         | Set 2 |[challenge_13.py](cryptopals/set2/challenge_13.py) |
| 14. Byte-at-a-time ECB decryption (Harder)    | Set 2 |[challenge_14.py](cryptopals/set2/challenge_14.py) |
| 15. PKCS#7 padding validation                 | Set 2 |[challenge_15.py](cryptopals/set2/challenge_15.py) |
| 16. CBC bitflipping attacks                   | Set 2 |[challenge_16.py](cryptopals/set2/challenge_16.py) |
| 17. The CBC Padding oracle                    | Set 3 |[challenge_17.py](cryptopals/set3/challenge_17.py) |

---

## Hack The Box 

### Crypto

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| Alpashcii Clashing    | crypto   | [alphascii_clashing.py](htb/crypto/alphascii_clashing.py)              | MD5 hash collision                                                |
| Ancient Encodings     | crypto   | [ancient_encodings.py](htb/crypto/ancient_encodings.py)                | Base64, hex encodings                                             |
| Android in the Middle | crypto   | [android_in_the_middle.py](htb/crypto/android_in_the_middle.py)        | Diffie-Hellman, choosen public key attack                         |
| Arranged              | crypto   | [arranged.py](htb/crypto/arranged.py)                                  | ECC, small subgroup discrete log                                  |
| Baby quick maffs      | crypto   | [baby_quick_maffs.py](htb/crypto/baby_quick_maffs.py)                  | Modular arithmetic, equation manipulation                         |
| Binary basis          | crypto   | [binary_basis.py](htb/crypto/binary_basis.py)                          | RSA, Multiple primes encoding                                     |
| Brainy's Cipher       | crypto   | [brainys_cipher.py](htb/crypto/brainys_cipher.py)                      | RSA, Chinese Remainder Theorem                                    |
| Brevi Moduli          | crypto   | [brevi_moduli.py](htb/crypto/brevi_moduli.py)                          | RSA, Small modulus factorization                                  |
| Digital Safety Annex  | crypto   | [digital_safety_annex.py](htb/crypto/digital_safety_annex.py)          | DSA, Nonce $k$ brute force                                        |
| Fast Carmichael       | crypto   | [fast_carmichael.py](htb/crypto/fast_carmichael.py)                    | Carmichael numbers, find the paper challenge                      |
| Flippin Bank          | crypto   | [flippin_bank.py](htb/crypto/flippin_bank.py)                          | AES, flipping bit attack                                          |
| Gonna lift em all     | crypto   | [gonna_lift_em_all.py](htb/crypto/gonna_lift_em_all.py)                | ElGamal, implementation flaw                                      |
| Hidden Handshake      | crypto   | [hidden_handshake.py](htb/crypto/hidden_handshake.py)                  | AES CTR, known plaintext attack                                   |
| Infinite Descent      | crypto   | [infinite_descent.py](htb/crypto/infinite_descent.py)                  | RSA, fermat prime factorization                                   |
| Initialization        | crypto   | [initialization.py](htb/crypto/initialization.py)                      | AES CTR, known plaintext attack                                   |
| Lost Key              | crypto   | [lostkey.py](htb/crypto/lostkey.py)                                    | ECC, curve parameters recovery, Pohlig-Hellman                    |
| Lost Modulus          | crypto   | [lost_modulus.py](htb/crypto/lost_modulus.py)                          | RSA, small exponent without message padding                       |
| Lost Modulus Again    | crypto   | [lost_modulus_again.py](htb/crypto/lost_modulus_again.py)              | RSA, Coppersmith's short pad attack                               |
| Nuclear Sale          | crypto   | [nuclear_sale.py](htb/crypto/nuclear_sale.py)                          | .pcap analysis                                                    |
| Optimus Prime         | crypto   | [optimus_prime.py](htb/crypto/optimus_prime.py)                        | RSA, shared prime on different keys, GCD attack                   |
| Quadratic Points      | crypto   | [quadratic_points.py](htb/crypto/quadratic_points.py)                  | Integer polynomial coefficients recovery, ECC discrete log, CRT   |
| RLotto                | crypto   | [rlotto.py](htb/crypto/rlotto.py)                                      | PRNG, time seed                                                   |
| Rookie Mistake        | crypto   | [rookie_mistake.py](htb/crypto/rookie_mistake.py)                      | RSA, implementation fault                                         |
| Secure Signing        | crypto   | [secure_signing.py](htb/crypto/secure_signing.py)                      | SHA256, byte at a time oracle attack                              |
| Sekur Julius          | crypto   | [sekur_julius.py](htb/crypto/sekur_julius.py)                          | Caesar cipher brute force                                         |
| SPG                   | crypto   | [spg.py](htb/crypto/spg.py)                                            | AES, weak random key recovery                                     |
| Spooky RSA            | crypto   | [spooky_rsa.py](htb/crypto/spooky_rsa.py)                              | RSA, encrypted prime, GCD attack                                  |
| Sugar Free Candies    | crypto   | [sugar_free_candies.py](htb/crypto/sugar_free_candies.py)              | Integer equation system                                           |
| Symbols               | crypto   | [symbols.py](htb/crypto/symbols.py)                                    | Legendre symbol                                                   |
| Two for One           | crypto   | [two_for_one.py](htb/crypto/two_for_one.py)                            | RSA, polynomial gcd, Franklin-reiter attack                       |
| Weak RSA              | crypto   | [weak_rsa.py](htb/crypto/weak_rsa.py)                                  | RSA, small $d$, Wiener Attack                                     |

### Pwn

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| Assemblers Avenge     | pwn      | [assemblers_avenge.py](htb/pwn/assemblers_avenge.py)                   | Shellcode                                                         |
| Bad grades            | pwn      | [bad_grades.py](htb/pwn/bad_grades.py)                                 | Libc addr leakage, ROP, stack aligment, float encoding            |                                       
| Bat Computer          | pwn      | [bat_computer.py](htb/pwn/bat_computer.py)                             | ret2shellcode                                                     |             
| Blacksmith            | pwn      | [blacksmith.py](htb/pwn/blacksmith.py)                                 | shellcode                                                         |
| Blessing              | pwn      | [blessing.py](htb/pwn/blessing.py)                                     | heap, malloc abuse                                                |
| El Mundo              | pwn      | [el_mundo.py](htb/pwn/el_mundo.py)                                     | ret2win noob tutorial                                             |
| El Teteo              | pwn      | [el_teteo.py](htb/pwn/el_teteo.py)                                     | shellcode                                                         |
| Entity                | pwn      | [entity.py](htb/pwn/entity.py)                                         | C code understanding (union, int to bytes)                        |
| Fleet Management      | pwn      | [fleet_management.py](htb/pwn/fleet_management.py)                     | Shellcode, seccomp sandbox                                        |
| Format                | pwn      | [format.py](htb/pwn/format.py)                                         | Format String, malloc hook, PIE leak, libc leak, libc version identification |
| Getting Started       | pwn      | [getting_started.py](htb/pwn/getting_started.py)                       | Buffer Overflow tutorial                                          |
| Great Old Talisman    | pwn      | [great_old_talisman.py](htb/pwn/great_old_talisman.py)                 | GOT overwrite                                                     |
| Hellhound             | pwn      | [hellhound.py](htb/pwn/hellhound.py)                                   | Heap, house of spirit, fake heap chunk construction               |
| Hunting               | pwn      | [hunting.py](htb/pwn/hunting.py)                                       | egg hunting, shellcode x86                                        |
| HTB Console           | pwn      | [htb_console.py](htb/pwn/htb_console.py)                               | ROP                                                               |
| Jeeves                | pwn      | [jeeves.py](htb/pwn/jeeves.py)                                         | Buffer Overflow                                                   |
| Laconic               | pwn      | [laconic.py](htb/pwn/laconic.py)                                       | SROP                                                              |
| Leet Test             | pwn      | [leet_test.py](htb/pwn/leet_test.py)                                   | Format string, stack read, global write                           |
| Mathematricks         | pwn      | [mathematricks.py](htb/pwn/mathematricks.py)                           | Integer overflow                                                  |
| Nightmare             | pwn      | [nightmare.py](htb/pwn/nightmare.py)                                   | Format string, PIE leak, libc leak, GOT overwrite                 |
| Optimistic            | pwn      | [optimistic.py](htb/pwn/optimistic.py)                                 | ret2shellcode, constrained shellcode                              |
| Power Greed           | pwn      | [power_greed.py](htb/pwn/power_greed.py)                               | ROP, ret2libc                                                     |
| Que onda              | pwn      | [que_onda.py](htb/pwn/que_onda.py)                                     | pwntools noob tutorial                                            |
| Quack Quack           | pwn      | [quack_quack.py](htb/pwn/quack_quack.py)                               | printf canary leak, ret2win                                       |
| Racecar               | pwn      | [racecar.py](htb/pwn/racecar.py)                                       | Format string, leak stack                                         |
| Reconstruction        | pwn      | [reconstruction.py](htb/pwn/reconstruction.py)                         | shellcode                                                         |
| Reg                   | pwn      | [reg.py](htb/pwn/reg.py)                                               | Buffer Overflow                                                   |
| Regularity            | pwn      | [regularity.py](htb/pwn/regularity.py)                                 | ret2reg/ret2shellcode                                             |
| Rocket Blaster XXX    | pwn      | [rocket_blaster_xxx.py](htb/pwn/rocket_blaster_xxx.py)                 | ROP, stack alignment                                              |
| Shooting star         | pwn      | [shooting_star.py](htb/pwn/shooting_star.py)                           | ROP, libc leak, ret2libc, libc version identification             |
| Sick ROP              | pwn      | [sick_rop.py](htb/pwn/sick_rop.py)                                     | Sigreturn-Oriented Programming (SROP)                             |
| Space                 | pwn      | [space.py](htb/pwn/space.py)                                           | x86 Shellcode, limited shellcode size                             |
| Space pirate: Entrypoint|pwn     | [space_pirate_entrypoint.py](htb/pwn/space_pirate_entrypoint.py)       | Format strings, write to stack variable                           |
| Space pirate: Going Deeper| pwn  | [space_pirate_going_deeper.py](htb/pwn/space_pirate_going_deeper.py)   | Buffer Overflow                                                   |
| Space pirate: Retribution| pwn    | [space_pirate_retribution.py](htb/pwn/space_pirate_retribution.py)    | PIE leak, libc leak, ROP, ret2libc                                |
| Spooky Time           | pwn      | [spooky_time.py](htb/pwn/spooky_time.py)                               | PIE leak, libc leak, GOT overwrite                                |
| Trick or Deal         | pwn      | [trick_or_deal.py](htb/pwn/trick_or_deal.py)                           | PIE leak, heap, UAF (Use-After-Free)                              |
| Vault-breaker         | pwn      | [vault_breaker.py](htb/pwn/vault_breaker.py)                           | strcpy, null byte ending string, byte at a time                   |
| Void                  | pwn      | [void.py](htb/pwn/void.py)                                             | ret2dlresolve                                                     |
| Writing on the Wall   | pwn      | [writing_on_the_wall](htb/pwn/writing_on_the_wall.py)                  | Null byte ending strings                                          |

---

## PicoCTF

### PicoCTF-2019

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| 13                    | crypto   | [13.py](picoCTF/picoCTF-2019/crypto/13.py)                             | rot13                                                             |
| b00tle3gRSA2          | crypto   | [b00tl3gRSA2.py](picoCTF/picoCTF-2019/crypto/b00tl3gRSA2.py)           | wiener attack                                                     |
| b00tl3gRSA3           | crypto   | [b00tl3gRSA3.py](picoCTF/picoCTF-2019/crypto/b00tl3gRSA3.py)           | RSA, multiple primes key                                          |
| caesar                | crypto   | [caesar.py](picoCTF/picoCTF-2019/crypto/caesar.py)                     | Caesar brute force                                                |
| john_pollard          | crypto   | [john_pollard.py](picoCTF/picoCTF-2019/crypto/john_pollard.py)|        | RSA, small N                                                               |
| miniRSA               | crypto   | [mini_rsa.py](picoCTF/picoCTF-2019/crypto/mini_rsa.py)                 | RSA, no padding, small message                                    | 
| rsa-pop-quiz          | crypto   | [rsa_pop_quiz.py](picoCTF/picoCTF-2019/crypto/rsa_pop_quiz.py)         | RSA quiz                                                          | 
| The Numbers           | crypto   | [the_numbers.py](picoCTF/picoCTF-2019/crypto/the_numbers.py)           | Substitution cipher                                               | 


### PicoCTF-2021

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| Dachshund Attacks     | crypto   | [dachshund_attacks.py](picoCTF/picoCTF-2021/crypto/dachshund_attacks.py)| Wiener attack                                                    |
| Easy Peasy            | crypto   | [easy_peasy.py](picoCTF/picoCTF-2021/crypto/easy_peasy.py)             | One Time Pad                                                      |
| Mini RSA              | crypto   | [mini_rsa.py](picoCTF/picoCTF-2021/crypto/mini_rsa.py)                 | RSA, no padding, small message                                    |
| Mod 26                | crypto   | [mod26.py](picoCTF/picoCTF-2021/crypto/mod26.py)                       | Rot13                                                             |
| No Padding, No Problem| crypto   | [no_padding_no_problem.py](picoCTF/picoCTF-2021/crypto/no_padding_no_problem.py)| RSA, chosen ciphertext attack, decription oracle         | 

### PicoCTF-2022

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| basic-mod1            | crypto   | [basic_mod1.py](picoCTF/picoCTF-2022/crypto/basic_mod1.py)             | Modular arithmetic                                                |
| basic-mod2            | crypto   | [basic_mod2.py](picoCTF/picoCTF-2022/crypto/basic_mod2.py)             | Modular arithmetic                                                |
| NSA Backdoor          | crypto   | [nsa_backdoor.py](picoCTF/picoCTF-2022/crypto/nsa_backdoor.py)         | Pohlig Hellman, Chinese Remainder Theorem                         |
| Sequences             | crypto   | [sequences.py](picoCTF/picoCTF-2022/crypto/sequences.py)               | Linear Algebra, Secuences                                         |
| Sum-O-Primes          | crypto   | [sum_o_primes.py](picoCTF/picoCTF-2022/crypto/sum_o_primes.py)         | RSA, p+q leak                                                     | 
| transposition-trial   | crypto   | [transposition_trial.py](picoCTF/picoCTF-2022/crypto/transposition_trial.py)| Transposition cipher                                         | 
| Very Smooth           | crypto   | [very_smooth.py](picoCTF/picoCTF-2022/crypto/very_smooth.py)           | RSA, Pollard's p-1 algorithm                                      | 
| Vigenere              | crypto   | [vigenere.py](picoCTF/picoCTF-2022/crypto/vigenere.py)                 | Vigenere cipher                                                   | 

### PicoCTF-2023

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| rotation              | crypto   | [rotation.py](picoCTF/picoCTF-2023/crypto/rotation.py)                 | Caesar brute force                                                |
| SRA                   | crypto   | [sra.py](picoCTF/picoCTF-2023/crypto/sra.py)                           | RSA, $$N,\ \phi(N)$$ recover                                       |

### PicoCTF-2024

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| C3                    | crypto   | [c3.py](picoCTF/picoCTF-2024/crypto/c3.py)                             | Substitution cipher                                               |                                                                   |
| interencdec           | crypto   | [interencdec.py](picoCTF/picoCTF-2024/crypto/interencdec.py)           | Multiple encoding, caesar brute force                             |

### PicoCTF-2026

| Challenge             | Category | Script                                                                 | Topics                                                            |
|-----------------------|----------|------------------------------------------------------------------------|-------------------------------------------------------------------|
| ClusterRSA            | crypto   | [cluster_rsa.py](picoCTF/picoCTF-2026/crypto/cluster_rsa.py)           | RSA, multiple primes                                              |
| cryptomaze            | crypto   | [cryptomaze.py](picoCTF/picoCTF-2026/crypto/cryptomaze.py)             | Linear Feedback Shift Register, AES                               |
| Related Messages      | crypto   | [related_messages.py](picoCTF/picoCTF-2026/crypto/related_messages.py) | RSA, Franklin Reiter Attack                                       |
| Shared Secrets        | crypto   | [shared_secrets.py](picoCTF/picoCTF-2026/crypto/shared_secrets.py)     | Diffie Hellman Key Echange, private key leak                      |
| Sum-O-Primes          | crypto   | [shift_registers.py](picoCTF/picoCTF-2026/crypto/shift_registers.py)   | Linear Feedback Shift Register                                    | 
| Small Trouble         | crypto   | [small_trouble.py](picoCTF/picoCTF-2026/crypto/small_trouble.py)       | Wiener attack                                                     | 
| StegoRSA              | crypto   | [stego_rsa.py](picoCTF/picoCTF-2026/crypto/stego_rsa.py)               | RSA, Steganography                                                | 
| Timestamped Secrets   | crypto   | [timestamped_secrets.py](picoCTF/picoCTF-2026/crypto/timestamped_secrets.py)| AES, timestamp key                                           | 

---

## TAMUctf 2026

| Challenge             | Category | Script                                                                                         | Topics                                    |
|-----------------------|----------|------------------------------------------------------------------------------------------------|-------------------------------------------|
| Abnormal Ellipse      | crypto   | [abnormal_ellipse.py](TAMUctf-2026/crypto/abnormal-ellipse/abnormal_ellipse.py)                | ECC. Smart Attack.                        |
| Hidden Log Factoring  | crypto   | [hidden_log_factoring.py](TAMUctf-2026/crypto/hidden_log_factoring/hidden_log_factoring.py)    | RSA. Pohlig-Hellman. Factor $N$ from $d$. |
