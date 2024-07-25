string = input()
max_len = 0
current_len = 0
for i in string:
    if i == "0":
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 0

print(max_len)
