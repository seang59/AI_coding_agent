from functions.run_python_file import run_python_file


def main():
    print("Running test 1:")
    test1 = run_python_file("calculator", "main.py")
    print(test1)
    print("--------------------------------------------------")

    print("Running test 2:")
    test2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(test2)
    print("--------------------------------------------------")

    print("Running test 3:")
    test3 = run_python_file("calculator", "tests.py")
    print(test3)
    print("--------------------------------------------------")

    print("Running test 4:")
    test4 = run_python_file("calculator", "../main.py")
    print(test4)
    print("--------------------------------------------------")

    print("Running test 5:")
    test5 = run_python_file("calculator", "nonexistent.py")
    print(test5)
    print("--------------------------------------------------")

    print("Running test 6:")
    test6 = run_python_file("calculator", "lorem.txt")
    print(test6)
    print("--------------------------------------------------")
    print("End of tests")

if __name__ == "__main__":
    main()

