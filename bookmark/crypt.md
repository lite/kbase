Terminology
----

The following are some of the terms useful in understanding the table below:

+ cipher id - a unique 2-3 byte cipher identifier. For example, SSL2_RC4_128_WITH_MD5 is identified as 0x010080 and TLS_RSA_WITH_3DES_EDE_CBC_SHA is identified as 0x00000A or simply 0x000A.
+ Name - common cipher suite name. TLS ciphers have TLS_Kx_[Au]_FROM_Enc_MAC format. SSL2 only use RSA for key exchange and authentication, so their names have SSL2_Enc_WITH_MAC format.
+ Protocol - Most ciphers suites fall into either TLS or SSL/SSL2 protocols. The only exception is Microsoft's proprietary PCT protocol.
+ Kx - Key exchange algorithm. Most popular exchange methods are RSA and Diffie-Hellman (DH/DHE). Some of the more exotic methods include Kerberos (KRB5), Pre-Shared Key (PSK), and others.
+ Au - Authentication algorithm. RSA is commonly used for key authentication.
+ Enc - Symmetric encryption algorithm (e.g. DES, 3DES, AES, RC4, etc.)
+ Bits - Effective symmetric encryption key size in bits. Export for export outside US are limited to 40-56 bits.
+ MAC - Hashing algorithm used for TLS/SSL data packets integrity and authentication checks.
+ Anon - Anonymous cipher suites with no key authentication. Highly vulnerable to man in the middle attack.
+ Export - Intentionally crippled cipher suite to conform to US export laws. Symmetric cipher used in export cipher suites typically does not exceed 56bits.
+ NULL - Null cipher suites do not provide any data encryption and/or data integrity. TLS_NULL_WITH_NULL_NULL (0x0000) cipher suite is used during initial session establishment.

Key exchange and Authentication algorithms:

+ RSA - Rivest, Shamir, Adleman
+ DH - Diffie-Hellman
+ DHE - Diffie-Hellman Ephemeral
+ ECDH - Elliptic-Curve Diffie-Hellman
+ KRB5 - Kerberos
+ SRP - Secure Remote Password Protocol
+ PSK - Pre-shared key
+ DSA - Digital Signature Algorithm
+ ECDSA - Elliptic Curve Digital Signature Algorithm
+ DSS - Digital Signature Standard

Encryption and MAC algorithms:

+ 3DES - Tripple Data Encryption Algorithm
+ AES - Advanced Encryption Standard
+ Camelia - Block cipher developed by Mitsubishi and NTT
+ DES - Data Encryption Standard
+ Fortezza - Security token based cipher
+ GOST - Block cipher developed in USSR
+ IDEA - International Data Encryption Algorithm
+ RC2 - Rivest Cipher 4
+ RC4 - Rivest Cipher 2
+ SEED - Block cipher developed by Korean Information Security Agency
+ SHA - Secure Hash Algorithm
+ MD5 - Message Digiest algorithm 5

LINKS
----
http://thesprawl.org/memdump/?entry=7



