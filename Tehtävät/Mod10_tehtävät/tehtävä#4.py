import random

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


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            # Arvotaan nopeuden muutos väliltä -10 … +15 km/h
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteri':<10} {'Huippunopeus':<14} {'Nopeus':<8} {'Kuljettu matka (km)':<20}")
        print("-" * 60)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<14} {auto.nopeus:<8} {auto.kuljettu_matka:<20.1f}")
        print("-" * 60)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


def main():
    autot = []
    for i in range(1, 11):
        rek = f"ABC-{i}"
        huippu = random.randint(100, 200)  # satunnainen huippunopeus 100–200 km/h
        autot.append(Auto(rek, huippu))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    tunti = 0

    print(f"\nKilpailu alkaa! 🏁 ({kilpailu.nimi}, {kilpailu.pituus_km} km)\n")

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunti += 1

        if tunti % 10 == 0:
            print(f"\n--- TILANNE {tunti} TUNNIN JÄLKEEN ---")
            kilpailu.tulosta_tilanne()

    print(f"\n🏆 KILPAILU PÄÄTTYI {tunti} TUNNIN JÄLKEEN! 🏆")
    kilpailu.tulosta_tilanne()


if __name__ == "__main__":
    main()
