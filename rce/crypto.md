struct
{
  BIGNUM *n;              // public modulus
  BIGNUM *e;              // public exponent
  BIGNUM *d;              // private exponent
  BIGNUM *p;              // secret prime factor
  BIGNUM *q;              // secret prime factor
  BIGNUM *dmp1;           // d mod (p-1)
  BIGNUM *dmq1;           // d mod (q-1)
  BIGNUM *iqmp;           // q^-1 mod p
  // ...
};
RSA

struct
{
  BIGNUM *p;              // prime number (public)
  BIGNUM *q;              // 160-bit subprime, q | p-1 (public)
  BIGNUM *g;              // generator of subgroup (public)
  BIGNUM *priv_key;       // private key x
  BIGNUM *pub_key;        // public key y = g^x
  // ...
}
DSA;

struct bignum_st
{
  BN_ULONG *d; /* Pointer to an array of 'BN_BITS2' bit chunks. */
  int top; /* Index of last used d +1. */
  /* The next are internal book keeping for bn_expand. */
  int dmax; /* Size of the d array. */
  int neg; /* one if the number is negative */
  int flags;
};