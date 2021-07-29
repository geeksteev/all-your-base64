import base64
import argparse
from sys import stdout

def EncodeBase64(message):
    base64_bytes = base64.b64encode(message.encode('ascii'))
    message_result = base64_bytes.decode('ascii')
    return message_result

def DecodeBase64(message):
    base64_bytes = message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message_result = message_bytes.decode('ascii')
    return message_result

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        '-i', '--input', help='Text to encode/decode.', required=True)
    argParser.add_argument(
        '-e', '--encode', help='Encode some text.', required=False, action='store_true')
    argParser.add_argument(
        '-d', '--decode', help='Decode some text.', required=False, action='store_true')

args = argParser.parse_args()

if args.encode == True:
    print("Let's encode!")

elif args.decode == True:
    print("Let's decode!")

