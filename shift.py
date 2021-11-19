import string

shift_flag = b"snvfrghjokl;,mp[wtdyibecuxSNVFRGHJOKL:<MP{WTDYIBECUZ}|"
shift = b"abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ{}"

trans = bytes.maketrans(shift_flag, shift)

str = "G:SH}Djogy <u Lrunpstf Smf Yu[omh Dp,ryjomh|"
#K nry upi eo;; frvpfr yjod ,rddshr

print(str.translate(trans))
