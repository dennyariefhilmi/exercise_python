def biaya_awal(tipe_kendaraan):
    j = 0
    if tipe_kendaraan in ['mobil', 'Mobil']:
        j = 5000
    elif tipe_kendaraan in ['motor', 'Motor'] :
        j = 2500
    else :
        j = 7500
    return j

def harian(jam_parkir,tipe_kendaraan):
    x = 0
    if tipe_kendaraan in ['mobil', 'Mobil']:
        x = 3000*(jam_parkir-1)
    elif tipe_kendaraan in ['motor', 'Motor'] :
        x = 1500*(jam_parkir-1)
    else :
        x = 5000*(jam_parkir-1)
    return x

def langganan(saldo,tipe_kendaraan):
    y = 0
    if tipe_kendaraan in ['mobil','Mobil']:
        y = saldo-biaya_awal(tipe_kendaraan)
    elif tipe_kendaraan in ['motor','Motor']:
        y = saldo-biaya_awal(tipe_kendaraan)
    else :
        y = saldo-biaya_awal(tipe_kendaraan)
    return y

tipe_kendaraan = input('Tipe Kendaraan Anda : ')         
member = input('Apakah anda memiliki kartu member ? "Ya"/"Tidak" ')
jam_parkir = int(input("Berapa lama anda parkir ?"))
biaya = harian(jam_parkir,tipe_kendaraan)
total_tarif = biaya_awal(tipe_kendaraan)+harian(jam_parkir,tipe_kendaraan)
saldo = 50000

if member in ['tidak','Tidak'] and tipe_kendaraan in ['mobil','Mobil']:
    if jam_parkir <= 1:
        print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
        print("Total tarif parkir {}".format(biaya_awal(tipe_kendaraan)))
    else :
        biaya_tambahan = harian(jam_parkir,tipe_kendaraan)
        if biaya in range (0,50000):
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam, total biaya tambahan : {}".format(jam_parkir,biaya_tambahan))
            print("Total tarif parkir {}".format(total_tarif))
        else :
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam".format(jam_parkir))
            print("Total tarif parkir : 50000")
            
elif member in ['tidak','Tidak'] and tipe_kendaraan in ['motor','Motor']:
    if jam_parkir <= 1:
        print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
        print("Total tarif parkir {}".format(biaya_awal(tipe_kendaraan)))
    else :
        biaya_tambahan = harian(jam_parkir,tipe_kendaraan)
        if biaya in range (0,25000):
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam, total biaya tambahan : {}".format(jam_parkir,biaya_tambahan))
            print("Total tarif parkir {}".format(total_tarif))
        else :
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam".format(jam_parkir))
            print("Total tarif parkir : 25000")
            
elif member in ['tidak','Tidak'] and tipe_kendaraan not in ['motor','Motor','mobil','Mobil'] :
    if jam_parkir <= 1:
        print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
        print("Total tarif parkir {}".format(biaya_awal(tipe_kendaraan)))
    else :
        biaya_tambahan = harian(jam_parkir,tipe_kendaraan)
        if biaya in range (0,75000):
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam, total biaya tambahan : {}".format(jam_parkir,biaya_tambahan))
            print("Total tarif parkir {}".format(total_tarif))
        else :
            print("Tarif jam pertama {}".format(biaya_awal(tipe_kendaraan)))
            print("Anda telah parkir selama {} jam".format(jam_parkir))
            print("Total tarif parkir : 75000")
            
elif member in ['ya','Ya'] and tipe_kendaraan in ['mobil','Mobil'] :
    print("Anda telah parkir selama {} jam".format(jam_parkir))
    print("Total tarif parkir {}, Sisa saldo anda : {}".format(biaya_awal(tipe_kendaraan),langganan(saldo,tipe_kendaraan)))

elif member in ['ya','Ya'] and tipe_kendaraan in ['motor','Motor'] :
    print("Anda telah parkir selama {} jam".format(jam_parkir))
    print("Total tarif parkir {}, Sisa saldo anda : {}".format(biaya_awal(tipe_kendaraan),langganan(saldo,tipe_kendaraan)))

elif member in ['ya','Ya'] and tipe_kendaraan not in ['motor','Motor','mobil','Mobil'] :   
    print("Anda telah parkir selama {} jam".format(jam_parkir))
    print("Total tarif parkir {}, Sisa saldo anda : {}".format(biaya_awal(tipe_kendaraan),langganan(saldo,tipe_kendaraan))) 

else :
    print("Input yang anda masukkan salah!")
