def Comm(Usrn, Com):
    Com = Com.strip().lower().capitalize()
    if Com == "":
         print("")
    elif Com == "About":
        print("HFterm is a terminal application in dev.\nIt is on the Github Repo HfTerm.\nSee License for more details")
    else:
        print(f"The command \"{Com}\" is not a command for {Usrn}.\n")