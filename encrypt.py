import sys

if len( sys.argv ) < 2:
	print("usage: python %s <plaintext (spaces allowed)> <outFileName>\n" % sys.argv[0])
	exit()

plaintxt = ''.join( sys.argv[1:-1] )
outFileName = sys.argv[-1]
key = open( '/dev/urandom' ).read( len( plaintxt ) )

encrypted = ''
for c, keyLetter in zip( plaintxt, key ):
	encrypted += chr(  ord(keyLetter) ^ ord(c) )

open(outFileName + '_encrypted', 'w').write( encrypted )
open(outFileName + '_key', 'w').write( key )
