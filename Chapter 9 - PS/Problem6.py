# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt", "r") as file:
    log_content = file.read()

    if "python" in log_content:
        print("The log file contains 'python'.")
    else:
        print("The log file does not contain 'python'.")
