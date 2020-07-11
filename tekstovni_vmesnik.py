import vislice.model

def izpis_igre(igra):
    tekst = (
        "Stevilo preostalih preizkusov: {stevilo_preostalih_poskusov} \n\n"
        "   {pravilni_del_gesla}\n\n"
        "Neuspeli poskusi: {neuspeli_poskusi}\n\n"
    ).format(
        stevilo_preostalih_poskusov = vislice.model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        neuspeli_poskusi = igra.nepravilni_ugibi()
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        "Wipiii, zmaga!!! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo=igra.geslo
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        "Booo, poraz! Geslo je bilo: {geslo} \n\n"
    ).format(
        geslo=igra.geslo
    )
    return tekst

def zahtevaj_vnos():
    return input 