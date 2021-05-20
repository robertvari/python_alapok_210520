from utilities.file_utils import get_all_files


def call_myself(i):
    if i >= 10:
        print("I called myself 10 times.")

    else:
        print(f"I called myself {i} times")
        call_myself(i+1)


result = get_all_files(r"C:\Work\_PythonSuli\python_alapozo\alapok_02")
print(result)
print(len(result))