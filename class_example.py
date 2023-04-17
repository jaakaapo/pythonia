class User:
    """Käyttäjä, Jolla on nimi ja ikä"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyytmmdd
        
        
 user = User("Mikko Virtanen", "19710315")
 print(user.name)
 print(user.birthday)