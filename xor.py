#KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
#KEY_2 = 911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d

key_1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
a =  bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
b= bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key_2 =  int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
c = bytes.fromhex('911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d')
key_2 = bytes.fromhex('911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d')
d = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')

key_3 = bytes.fromhex('504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc')
flag = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag_hex = int.from_bytes(key_1, byteorder="big") ^ int.from_bytes(key_2, byteorder="big") ^ int.from_bytes(key_3, byteorder="big")^int.from_bytes(flag, byteorder="big")

print(hex(flag_hex))

print(bytes().fromhex('63727970746f7b7830725f69355f61737330633161743176337d'))