import os
for root, dirs, files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
    # 
    print('-' * 88)
for root, dirs, files in os.walk("/home/david"):
    print(root)
    print(dirs)
    print(files)
    print('-' * 88)
for root, dirs, files in os.walk("/home/david"):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        with open(file) as f:
            print(f.read())
    print('-' * 88)