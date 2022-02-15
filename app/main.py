import time

alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
password = "mjop2"

def bruteforce(word, length):
    if length <= 5:
        for char in alphanum:
            if password == word + char:
                print(f"The password is {word}{char}")
            else:
                print(f"{word}{char}")
                bruteforce(f"{word}{char}", length + 1)

start_time = time.time()
bruteforce('', 1)
print("--- %s seconds ---" % (time.time() - start_time))

