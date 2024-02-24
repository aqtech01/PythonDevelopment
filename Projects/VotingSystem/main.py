def voting():
    print("""
    1_ Imran Khan
    2- Nawaz Sharif
    3- Saad Rizvi
    4- Siraj-ul-Haq
    5- Print the Result
    """)

    votes = {
        "Imran  Khan": 0,
        "Nawaz Sharif": 0,
        "SaadRizvi": 0,
        "Siraj - ul - Haq": 0,

    }

    while True:
        casting = input("Select the number 1-5 to cast vote:- ")
        if casting == "1":
            get = votes["Imran  Khan"]
            get += 1
            votes["Imran  Khan"] = get

        elif casting == "2":
            get = votes["Nawaz Sharif"]
            get += 1
            votes["Nawaz Sharif"] = get

        elif casting == "3":
            get = votes["SaadRizvi"]
            get += 1
            votes["SaadRizvi"] = get

        elif casting == "4":
            get = votes["Siraj - ul - Haq"]
            get += 1
            votes["Siraj - ul - Haq"] = get
        else:
            print("Invalid")
            print(votes)
            break
        print(votes)


voting()
