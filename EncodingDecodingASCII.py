def encode():
    encode = input("Enter message that needs to be encoded.")
    
    encodedMessage = []
    for e in encode:
        encodedMessage.append(ord(e))

    print(encode)
    print(encodedMessage)

def decode():
    decode = input("Enter message that needs to be decoded.")
	
    message = []
    message.append(decode)
    message = [int(i) if i.isdigit() else i for i in message[0].replace(',', '').split()]
	
    decodeMessage = ""

    for m in message:
        decodeMessage = decodeMessage + chr(m)
	
    print(message)
    print(decodeMessage)
	
def decision():
    decide = input("Are you decoding or encoding?").lower() 
    if (decide == "decoding"):
        decode()
    elif (decide == "encoding"):
        encode()

def main():
    decision()
main()