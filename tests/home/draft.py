user_login_details = {}
user_login_details['username'] = ["kotarinaga1@gmail.com",'test1@gmail.com','test2@gmail.com']
user_login_details['password'] = ["Katasraj111#",'test1','test2']


#print(user_login_details)

## self.lp.login('kotarinaga1@gmail.com', 'Katasraj111#')

def get_username_password(user_login_details):

    first_key = next(iter(user_login_details))  # Dynamically get the first key in the dictionary

    l=[]
    j = 0
    while j < len(user_login_details[first_key]):
        for i in user_login_details.values():
            l.append(i[j])
        j += 1
    user_pswd_list = []
    for i in range(0, len(l), 2):
        user_pswd_list.append(l[i:i+2])
    return user_pswd_list

print(get_username_password(user_login_details))

#print(len(get_username_password(user_login_details)))

u = [['kotarinaga1@gmail.com', 'Katasraj111#'], ['test1@gmail.com', 'test1'], ['test2@gmail.com', 'test2']]

for i in range(len(u)):
    print(u[i][0])
    print(u[i][1])