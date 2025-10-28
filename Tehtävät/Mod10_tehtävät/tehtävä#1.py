class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa!")

    def siirry_kerrokseen(self, kohde):
        print(f"\nSiirretään hissi kerrokseen {kohde}...")
        if kohde > self.ylin or kohde < self.alin:
            print("Virhe: Kerros on hissin toiminta-alueen ulkopuolella.")
            return

        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()
        print(f"Hissi on saapunut kerrokseen {self.nykyinen_kerros}.\n")


def main():
    hissi = Hissi(1, 10)
    hissi.siirry_kerrokseen(5)
    hissi.siirry_kerrokseen(1)


if __name__ == "__main__":
    main()
