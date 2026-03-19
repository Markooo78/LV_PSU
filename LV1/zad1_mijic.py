#Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
#Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
#rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.

radni_sat = float(input("Unesite broj radnih sati: "))
satnica = float(input("Unesite satnicu: "))

zarada = radni_sat * satnica

#print("Korisnik je zaradio:", zarada, "eura")

def total_euro(radni_sat, satnica):
    ukupna_zarada = radni_sat * satnica
    return ukupna_zarada

rezultat = total_euro(radni_sat, satnica)

print("Ukupna zarada iznosi:", rezultat, "eura")


