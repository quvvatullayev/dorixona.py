class Aptika:

    def __init__(self, aptika_nomi, **dorilar) -> None:
        self.aptika_nomi = aptika_nomi
        self.dorilar = dorilar

    def apteka_bazasi(self):
        print("\nMahsulotlar ruyhati")
        for k,q in self.dorilar.items():
            print(f"{k} dan {q} ta")

        return ' '

    def apteka_bazasi_qushish(self):
        input("\nDorilar bazasin shakillantiring: ")
        n = int(input("\nNecha turdagi dori kiritmoqchisiz: "))
        for k in range(n):
            dori = input(f"\n{k + 1} - dorini turini bazaga kiriting: ")
            qadoq = int(input(f"{dori} necha qadoq?: "))
            if dori not in self.dorilar.keys():
                self.dorilar[dori] = qadoq

            else:
                self.dorilar[dori] = self.dorilar[dori] + qadoq

        return ' '

    def dorilar_ruyxati(self):
        print("Mavjud dorilar ruyxati:")
        for k,q in self.dorilar.items():
            mahsulot = f"{k} dan {q} ta bor"
            print(mahsulot)

        return ' '

    def surov_dorilar(self):
        while True:
            dori = input("\nQanday dorini izlayapsiz? :")
            self.dorilar[dori] -= 1

            istak = int(input("\nYana biror dori kerakmi? ha(1)/yo'q(0):"))

            if istak == 0:
                break

            else:
                continue
        
        return ' '

aptika1 = Aptika("shifo top", trmol = 20, setramon = 30, mezen = 40, omes = 50)

def consol():

    print(f"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\
        \nHush kelipsiz! {aptika1.aptika_nomi.title()} aptikasiga.\
        \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    while True:
        istak = int(input("\nAptikaga mahsulot qushasizmi ha(1)/yo'q(0): "))

        if istak == 1:
            print(aptika1.apteka_bazasi_qushish())

        istak = int(input("\nAptikadagi mahsulotlar ruyhatin kurasizmi ha(1)/yo'q(0): "))
        
        if istak == 1:
            print(aptika1.dorilar_ruyxati())

        else:
            istak = int(input("\nDori izlayapsizmi ha(1)/yo'q(0): "))
        
        if istak == 1:
            try:
                print(aptika1.surov_dorilar())
            
            except:
                print("\nDori nomini tug'ri kritmadingiz.")
                

        else:
            istak = int(input("\nAptikadag qolgan dorilarni kurasizmi ha(1)/yo'q(0): "))
        
        if istak == 1:
            print(aptika1.apteka_bazasi())

        hohish = int(input("\nYana qidiyasizmi? ha(1)/yo'q(0):"))

        if hohish == 0:
            break

    return ''


consol1 = consol()
print(consol1)