from firebase import firebase
firebase = firebase.FirebaseApplication("https://chat-app-d2935-default-rtdb.firebaseio.com/", None)

data = firebase.get(f"chat-app-d2935-default-rtdb/admin/users", "")
for i in range(len(data)):
    print(i)

username = input("Enter the username: ")

id = input("Enter the id: ")

print("1. Block User")  
print("2. Unblock User")

choice = int(input("Enter your choice: "))

if choice == 1:
    data = firebase.get(f"chat-app-d2935-default-rtdb/admin/users/{username}", "")
    for i in data.keys():
        p = data[i]["status"]
        if p == "active":
            data = firebase.put(f"chat-app-d2935-default-rtdb/admin/users/{username}/{id}", "status", "blocked")
            print("User blocked successfully")
            break
    else:
        print("User is already blocked")

elif choice == 2:
    data = firebase.put(f"chat-app-d2935-default-rtdb/admin/users/{username}/{id}", "status", "active")
    print("User unblocked successfully")









