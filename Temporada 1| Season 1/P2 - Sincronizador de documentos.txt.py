with open('file1.txt', 'r+', encoding='utf-8') as f1, open('file2.txt', 'r+', encoding='utf-8') as f2, open('parity.txt', 'r+', encoding='utf-8') as f:

    content1 = f1.read()
    content2 = f2.read()
    
    if content1 != content2:
        print("The files are not identical. They must be for the program to start. ")
        f2.seek(0)
        f2.write(content1)
        f2.truncate()
        content2 = content1

    f.seek(0)
    f.write(content1)
    f.truncate()
    print("Startin the program... \n ")

    while True:
        f1.seek(0)
        f2.seek(0)
        f.seek(0)

        content1 = f1.read()
        content2 = f2.read()
        f_paridad = f.read()

        if content1 != f_paridad:
            print("Change detected in file 2, synchronizing...")
            f2.seek(0); f2.write(content1); f2.truncate()
            f.seek(0); f.write(content1); f.truncate()

        elif content2 != f_paridad:
            print("Change detected in file 2, synchronizing...")
            f1.seek(0); f1.write(content2); f1.truncate()
            f.seek(0); f.write(content2); f.truncate()