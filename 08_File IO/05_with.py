# shortcut for opening and closing a file in python is using with syntax.

with open("Ronak Pawar.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with synax
