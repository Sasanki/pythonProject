class Citizen:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
if __name__ == "__main__":
    P1 = Citizen("Jan", "Kowalski")
    print(P1.name, P1.surname)


