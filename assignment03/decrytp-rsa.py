#2d2762062e20ffffa72e58a8ac86b493.pem
#92d3928a04087cba76bf91161f7a3e73.pem
#553a135f2c10f104b5a8d57f7cb5f3dd.pem
#ecdca7da6ad51315a0324ee68353d8b3.pem
import math
import os, sys, Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from sympy import *
import mpmath
from mpmath import *
mp.prec = 100000
import gmpy2
from gmpy2 import mpz,mpq,mpfr,mpc
from decimal import *
#import math


# Read you PEM files
filename = "2d2762062e20ffffa72e58a8ac86b493"                               #write inn the name of the .pem file
recipient_key = RSA.importKey(open(filename + ".pem").read())
n = recipient_key.n
e = recipient_key.e
print("n: ",n)
print("e: ",e)
#p=1
#q=1
#d=1
#b=1

d = mod_inverse(n, e)
print("d: ", d)

#x = Symbol('x')
#b = solve((e * d) % x == 1, x)
#print("b: ", b)


#test = totient(n)
#print("test: ",test)

# ...
# here you put your algorithm for breaking RSA (factorization of n)
# you need to find the corresponding values for d, p and q
# then you need to construct a new complete RSA key with

test = 125 // 5
print(test)
#print(list(primerange(2**1023, 2**1024)))

print("d:  ", d)

p = prevprime(nthroot(n,3))
# lage en if loop som går til den finner en prime som er delelig med n og gir en prime
print("p: ",p)
#n=125
#p=5
while not (isprime(n//p)):
    p = prevprime(p)
    print("new p:", p)

print("ferdig med while")

q = n//p
print("q: ",q)
#print(math.log10(a))
#print(len(string(a)))
#if(isprime(a)):
#    print("true")


#q = nextprime(a*a + randprime(2**1045, 2**1046-1))
#print(q)

if(p*q == n):
    print("true that p*q=n")
else:
    print("false that p*q=n")

if(isprime(p)):
    print("true that p is prime")
else:
    print("false that p is prime")

if(isprime(q)):
    print("true that q is prime")
else:
    print("false that q is prime")

print("n:   ", n)
print("p*q: ", (p*q))

b = ((p-1)*(q-1))
print("b:  ", b)

if(gcd(e,b) ==1):
    print("true gcd")
else:
    print("false gcd")

d = Crypto.Util.number.inverse(e, b)           #e=65537  && b=(p-1)(q-1)
#d = solve((13*d) % 9, d)
#solve((e*d) % b == 1, d)
#solve((e*d) % b == 1, d)
print("d:  ", d)

#p,x,y = Symbol("p,x,y")
#y>p
#2**1023 < p < 2**1024
#p = solveset(p**3 + p(x+y) == n, p)
#p = solve(p**3 + p**2 + px == n, p)
#print("p: ",p)
#p_range = primerange(2**1023, 2**1024)
#prime
#coprime - alle till som er prime med n (for 14 er det: 1,3,5,8,11,13 )
#phi(n) = (p-1)(q-1)

#kubikkrot =  int(cbrt(n))
#print("kubikk rot: ", kubikkrot)
#p = sympy.
#q = (n/kubikkrot)
#print("q: ", q);


newkey = RSA.construct((n, e, d, p, q))

# and in PKCS1_OAEP mode the ready cipher is constructed with
cipher_rsa = PKCS1_OAEP.new(newkey)


###############################################################################################################
#BIN -Files
#063e965fcd26152888ee373dca2b133e.bin
#084c8fd55f8740665aacb7b70d0f9a4c.bin
#77580531f75476b810cd268abaa2b5e8.bin
#d091feff5489487de36fa5089c2c4116.bin
# In your Python code you can use something like this
binfilename = "77580531f75476b810cd268abaa2b5e8"                #Add the name of the .bin file
file_in = open(binfilename + ".bin", "rb")
encmsg = file_in.read()
print("cryptert mld: ", encmsg)
# then you try to decrypt encmsg it with previously recovered cipher_rsa
try_decrypted_message = cipher_rsa.decrypt(encmsg)
print("decrypt mld: : ", try_decrypted_message)

