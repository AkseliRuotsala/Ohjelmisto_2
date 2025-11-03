class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


def main():
    s_auta = Sähköauto("ABC-15", 180, 52.5)
    p_auta = Polttomoottoriauto("ACD-123", 165, 32.3)

    s_auta.kiihdytä(120)
    p_auta.kiihdytä(110)

    s_auta.kulje(3)
    p_auta.kulje(3)

    print(f"Sähköauto {s_auta.rekisteritunnus} kulki {s_auta.kuljettu_matka} km.")
    print(f"Polttomoottoriauto {p_auta.rekisteritunnus} kulki {p_auta.kuljettu_matka} km.")


if __name__ == "__main__":
    main()

