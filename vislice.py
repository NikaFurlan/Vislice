import bottle

import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('datoteke/views/index.tpl')

@bottle.post('/igra/')
#model Vislice naredi novo igro in vrene id
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    #naredi se nam nova igra, sedaj želimo novo igro igrati, želimo da nas direktno pošlje na igranje
    bottle.redirect(f'/igra/{id_nove_igre}/')


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

bottle.run(reloader=True, debug=True)