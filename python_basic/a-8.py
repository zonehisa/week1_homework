users_info = [
    ["Bob", 79],
    ["Tom", 59],
    ["Ken", 61]
    ]
for user_info in users_info:
    print(f"Name: {user_info[0]}, Age: {user_info[1]}")

print('\n'.join([f"Name: {user_info[0]}, Age: {user_info[1]}" for user_info in users_info]))
