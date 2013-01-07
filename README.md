STREAMENC
=========

An encryption system based on the on one time pad in which the random pad is generated from the cryptographic hash of a password. The pad may be infinitely extended by taking the hash of the previous hash.

How-to
======

The program is run from the command line with three(3) arguments: 
the first is the password/passphrase (you can use quotes to have spaces in your passphrase)
the second is the number of times the password is hashed before its value is used, think of this like a salt value however
the third is the filename to encrypt

The encrypted version is saved to a file of the same name with a .enc extension appended.

To decrypt, run the program again with the exact same passphrase and hash-count and the plaintext file will have a .enc.enc extension.