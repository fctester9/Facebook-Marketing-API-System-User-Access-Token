import hmac
import hashlib

h = hmac.new(b'Enter your accesss token and leave the b on the left it is not a typo)', 'Enter your app secret'.encode('utf-8'), hashlib.sha256 )
print( h.hexdigest() )
