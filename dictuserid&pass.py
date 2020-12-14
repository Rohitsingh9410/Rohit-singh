def id_password():
    dict_={"rohit":"1234"}
    username=input("enter username:")
    password=input("enter password:")
    if dict_.get(username)==password:
            print("logged in")
    else:
        print("invalid userid or password")
id_password()
