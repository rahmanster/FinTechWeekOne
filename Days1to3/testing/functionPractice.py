#Tell the user if they have good taste

name = input("What is your name?\n")
faveSport = input("What's your favorite sport?\n")

def goodTasteTest(name, faveSport):
    if faveSport=="basketball":
        return(name+", you have good taste!")
    else:
        return(name+", you have bad taste!")
        
print(goodTasteTest(name, faveSport))
    