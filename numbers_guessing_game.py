import random


def g_base_numb():
    pwd_len = 5
    pwd_ls = []
    while len(pwd_ls) < pwd_len:
        rnd_numb = random.randint(0, 9)
        if rnd_numb not in pwd_ls:
            pwd_ls.append(rnd_numb)
    return pwd_ls


def g_usr_input():
    usr_guess = input("Please enter the pwd: ")
    usr_guess_tols = []
    for i in range(len(usr_guess)):
        usr_guess_tols.append(int(usr_guess[i]))
    return usr_guess_tols


def comp(base_pwd, usr_pwd):
    ans_ls = ['Red' for k in range(len(base_pwd))]
    for i in range(len(base_pwd)):
        if usr_pwd[i] in base_pwd:
            ans_ls[i] = 'Yellow'
            if usr_pwd[i] == base_pwd[i]:
                ans_ls[i] = 'Green'
    return ans_ls


def play():
    base_pwd = g_base_numb()
    print("The password has been generated! Now try to guess it.")
    print(f'There\'s {len(base_pwd)} ditgits in the password')
    usr_pwd = g_usr_input()
    ans_ls = comp(base_pwd, usr_pwd)
    print(ans_ls)
    while ans_ls != ['Green' for i in range(len(base_pwd))]:
        usr_pwd = g_usr_input()
        ans_ls = comp(base_pwd, usr_pwd)
        print(ans_ls)
    print('You Win!')


play()
