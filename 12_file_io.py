with open("example.txt", "w") as f:
    f.write("Hello file!\n)

with open("example.txt", "r") as f:
    content = f.read()
    print(content)
