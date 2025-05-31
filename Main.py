Groups = dict()
groupTransactions = dict()
Settlement = []


# Formatters
def clear():
    print("\n"*100)

def line(before=0,after=0):
    if(before):
        print("\n")
    print("=+"*20+"=")
    if(after):
        print("\n")

def printGroups():
    print("{:<8} {:<15}".format('Sr','Group'))

    for i,name in enumerate(Groups.keys()):
        print("{:<8} {:<15}".format(i,name))

def printSelGroup(Sel=0):
    print("{:<8} {:<15}".format('Sr',list((Groups.keys()))[Sel]))
    for i,name in enumerate(Groups[list(Groups.keys())[Sel]]):
        print("{:<8} {:<15}".format(i,name))


# Main-Option-1
def addTransac(to_re_enter=False):
    clear()
    line()
    if(to_re_enter):
        print("Invalid Choice! Please Try Again.")
        line()
    printGroups()
    line(0,1)
    gSel = int(input("Select Group: "))

    if(gSel not in range(len(Groups.keys()))):
        addTransac(True)

    clear()
    line()
    printSelGroup(gSel)
    line(0,1)
    mSel = int(input("Select Member: "))

    if(mSel not in Groups[list(Groups.keys())[gSel]]):
        addTransac(True)

    clear()
    line()
    print("Enter These Details:")
    line(0,1)
    shortDesc = input("Enter Transaction Name: ")
    transactionAmt = float(input("Enter Amount Paid: "))

    groupTransactions[list(Groups.keys())[gSel]].append([shortDesc,Groups[list(Groups.keys())[gSel]][mSel],transactionAmt])
    
    clear()
    line()
    print("Transaction has been Added Successfully!")
    line(0,1)
    input("press \"ENTER\" to exit: ")
    
    main()


# Main-Option-2
def groupOptions(to_re_enter=False):
    clear()
    line()
    
    if(to_re_enter):
        print("Invalid Selection. Please Try Again!")
        line()
    
    print("""Choose From the Following Options:
    
1] Add New Group
2] Add New Member
3] View Group
4] Go Back""")

    dgSelection = int(input(": "))

    if dgSelection == 1:
        createGroup()
    elif dgSelection == 2:
        addMember()
    elif dgSelection == 3:
        viewGroup()
    elif dgSelection == 4:
        main()
    else:
        groupOptions(True)
        
# Sub-Option-1-1
def createGroup(to_re_enter=False):
    clear()
    line()

    if(to_re_enter):
        print("Group Already Exists! Use another Name")
        line()

    gName = input("Enter Group Name: ")

    if gName in Groups.keys():
        createGroup(True)

    Groups[gName] = []
    groupTransactions[gName] = []

    groupOptions()

# Sub-Option-1-2
def addMember(to_re_enter=False):
    clear()
    line()

    if(to_re_enter):
        print("Invalid Selection. Please Try Again!")
        line()

    printGroups()

    gSel = int(input(": "))

    if gSel not in range(len(Groups.keys())):
        addMember(True)

    line(1,0)

    mName = input("Enter Name: ")

    Groups[ list(Groups.keys()) [gSel] ].append(mName)

    groupOptions()

# Sub-Option-1-3
def viewGroup(to_re_enter=False):
    clear()
    line()

    if(to_re_enter):
        print("Group Doesn't Exist. Please Try Again!")
        line()

    printGroups()

    gSel = int(input(": "))
    
    
    if gSel not in range(len(Groups.keys())):
        viewGroup(True)

    clear()
    line()
    
    printSelGroup(gSel)
    
    line(1,0)
    input("press \"ENTER\" to exit: ")
    
    groupOptions()

# Main-Option-3
def getSettlement():
    pass


# Main-Option-4
def close():
    clear()
    print("Thank you for Using, Visit Again!")
    exit()


def main(to_re_enter=False):
    
    clear()
    line()

    if(to_re_enter):
        print("Invalid Selection. Please Try Again!")
        line()

    print("""
Choose From the Following Options:
    
1] Add New Transaction
2] Group Options
3] Get Settlement
4] Exit""")

    selection = int(input(": "))
    if(selection==1):
        addTransac()
    elif(selection==2):
        groupOptions()
    elif(selection==3):
        getSettlement()
    elif(selection==4):
        close()
    else:
        main(True)

# Starting the Program
main()