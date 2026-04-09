import sys

commands = {"add", "add-category", "list", "total"}

if len(sys.argv) >= 5 or (sys.argv[1] not in commands):
    print("Неизвестная команда!")
    print(sys.argv)
    sys.exit(1)

if sys.argv[1] == "add-category":
    