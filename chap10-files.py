#chap 10 - files and exception
# with open("pi_digits.txt", "r") as f:
#     contents = f.read()
#     print(contents.rstrip())
#10.3
# name = input("Enter your name:")
# with open("guest.txt", "a") as fw:
#     fw.write(name)
# with open("guest.txt") as fr:
#     contents = fr.read()
#     print(contents)
#10.4
while True:
    name = input("Enter your name or 'q' for quit: ")
    if name == 'q':
        break
    comments = input("Enter your comments: ")
    print("Thank you " + name + " for your visit.")
    string = name + " " + comments + "\n"
    print(string)   
    with open("guest_book.txt", "a") as fa:
        fa.write(string)
    with open("guest_book.txt") as fr:
        contents = fr.read()
        print(contents)
#10.5

