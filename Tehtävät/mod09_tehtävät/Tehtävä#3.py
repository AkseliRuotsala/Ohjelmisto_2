class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        """Muuttaa auton nopeutta annetulla määrällä (km/h),
        mutta ei ylitä huippunopeutta tai laske alle nollan."""
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        """Kasvattaa kuljettua matkaa nykyisen nopeuden ja ajan perusteella."""
        self.kuljettu_matka += self.nopeus * tunnit


def main():
    auto = Auto("ABC-123", 142)

    auto.kiihdytä(30)
    auto.kiihdytä(70)
    auto.kiihdytä(50)

    print(f"Nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

    auto.kiihdytä(-200)
    print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h\n")
    auto.kiihdytä(60)
    print(f"Nykyinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka ennen ajoa: {auto.kuljettu_matka} km")

    auto.kulje(1.5)

    print(f"Kuljettu matka ajon jälkeen: {auto.kuljettu_matka} km")


if __name__ == "__main__":
    main()
