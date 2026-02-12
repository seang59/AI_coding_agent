from functions.get_file_content import get_file_content

def main():
    test1 = get_file_content("calculator", "main.py")
    print(test1)
    print("--------------------------------------------------")

    test2 = get_file_content("calculator", "pkg/calculator.py")
    print(test2)
    print("--------------------------------------------------")

    test3 = get_file_content("calculator", "/bin/cat")
    print(test3)
    print("--------------------------------------------------")

    test4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(test4)
    print("--------------------------------------------------")
    print("End of tests")

if __name__ == "__main__":
    main()