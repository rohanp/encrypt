import sys

if len( sys.argv ) < 3:
	print("usage: python %s <encrypted file> <key file>\n" % sys.argv[0])
	exit()

encrypted = open( sys.argv[1], 'r' ).read().splitlines()[0]
key = open( sys.argv[2], 'r' ).read().splitlines()[0]

plaintext = ''
for c, keyLetter in zip( encrypted, key ):
	plaintext += chr(  ord(keyLetter) ^ ord(c) )

print("plaintext: %s"% plaintext)
