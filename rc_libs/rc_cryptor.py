import json
import base64

class CBase64:
	def encryption(var):
		return base64.urlsafe_b64encode(json.dumps(var).encode())

	def decryption(var: bytes):
		return json.loads(base64.urlsafe_b64decode(var.decode()).decode())