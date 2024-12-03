import base64

def encode_base64(text: str) -> str:
   """Кодирует текст в Base64."""
   text_bytes = text.encode('utf-8')
   base64_bytes = base64.b64encode(text_bytes)
   return base64_bytes.decode('utf-8')