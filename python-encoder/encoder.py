import base64

def encode_base64(text: str) -> str:
   text_bytes = text.encode('utf-8')
   base64_bytes = base64.b64encode(text_bytes)
   return base64_bytes.decode('utf-8')
