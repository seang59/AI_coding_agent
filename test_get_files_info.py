from functions.get_files_info import get_files_info

def main():
    test1 = get_files_info("calculator", ".")
    print(test1)
    print("--------------------------------------------------")

    test2 = get_files_info("calculator", "pkg")
    print(test2)
    print("--------------------------------------------------")

    test3 = get_files_info("calculator", "/bin")
    print(test3)
    print("--------------------------------------------------")

    test4 = get_files_info("calculator", "../")
    print(test4)
    print("--------------------------------------------------")
    print("End of tests")

if __name__ == "__main__":
    main()