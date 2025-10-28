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


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]
        print(f"Talo luotu: kerrokset {alin}-{ylin}, hissejä {hissien_lkm} kpl.\n")

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print("Virhe: hissin numero ei ole olemassa.")
            return
        hissi = self.hissit[hissin_numero - 1]
        print(f"==> Ajetaan hissiä {hissin_numero}:")
        hissi.siirry_kerrokseen(kohdekerros)



def main():

    talo = Talo(1, 10, 3)

    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(2, 8)
    talo.aja_hissiä(3, 3)

    talo.aja_hissiä(1, 1)


if __name__ == "__main__":
    main()
