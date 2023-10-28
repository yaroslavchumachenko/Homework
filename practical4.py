
id_text = input("Введіть Transaction ID:")
new_id = ""

for i in id_text:
    if i == "&":
        pass
    else:
        new_id += i

print(new_id)