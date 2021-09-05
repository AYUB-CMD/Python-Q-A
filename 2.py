#  Read Full name and interpret first name middlename(optional) and last name separated by single or more contigousspace exception need to be proceed

def name(name):
    fullName=name.split()
    try:
        if len(fullName) < 3:
            print("First Name:",fullName[0])
            print("Last Name:",fullName[1])
        else:
            print("First Name:",fullName[0])
            print("middle Name:",fullName[1])
            print("Last Name:",fullName[2])
    except Exception as e:
        print(e)

name('AyubrajThapa')        