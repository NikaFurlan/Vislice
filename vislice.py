import bottle
import model

SKRIVNOST = 'moja_prva_skrivnost'
DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

vislice = model.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_Z_BESEDAMI)
vislice.nalozi_igre_iz_datoteke()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect(f'/igra/{id_igre}/')


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('datoteke/views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)


@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    #dobim crko 
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)

    bottle.redirect(f'/igra/{id_igre}/')
    
@bottle.get('/statistika/')
def pokazi_statistiko():
    slovar_statistik = model.statistika(DATOTEKA_S_STANJEM)
    return bottle.template('statistika.tpl',
                           slovar_statistik=slovar_statistik)


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)


#hh