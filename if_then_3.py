ikä = int(input("Kerro ikäsi: "))
if ikä < 18:
    print("Olet alaikäinen.")
elif ikä > 17 and ikä < 65:
    print("Olet työikäinen.")
elif ikä > 64 and ikä < 121:
    print("Olet eläkeläinen.") 
elif ikä < 0:
    print("et ole syntynyt.")
elif ikä > 120:
    print("Et ole hengissä todennäköisesti enään.")