def Comm(Usrn, Com):
    Com = Com.strip().lower().capitalize()
    if Com == "":
         print("")
    elif Com == "About":
        print("")
    else:
        print(f"The command \"{Com}\" is not a command for {Usrn}.\n")