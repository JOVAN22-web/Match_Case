str = input("Which season of Anime do you want to watch ?")
match str:
    case _ if (str=="Spring"):
        anime = int(input("Which anime to select:\n1.Toradora\n2.Noragami\n3.Pokemon\n"))
        match anime:
            case _ if ( anime == 1):
                print("Toradora is Currently playing")
            case _ if ( anime ==2 ):
                print("Noragami is Currently playing")
            case _ if (anime == 3):
                print("Pokemon is Currently playing")
    case _ if (str == "Winter"):
            anime2 = int(input("Which anime to select:\n1.Barakamon\n2.Vinland Saga\n3.ReZero\n"))
            match anime2:
                case _ if (anime2 == 1):
                    print("Barakamon is Currently playing")
                case _ if (anime2 == 2):
                    print("Vinland Saga is Currently playing")
                case _ if (anime2 == 3):
                    print("ReZero is Currently playing")
    case _ if (str == "Summer"):
        anime3 = int(input("Which anime to select:\n1.Attack on Titan\n2.ReLife\n3.Mushoku Tensei\n"))
        match anime3:
            case _ if (anime3 == 1):
                print("Attack on Titan is Currently playing")
            case _ if (anime3 == 2):
                print("ReLife is Currently playing")
            case _ if (anime3 == 3):
                print("Mushoku Tensei is Currently playing")


