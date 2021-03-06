import requests

# Busca de restaurantes da promoção
# https://www.apoieumrestaurante.com.br/home.html#restaurantes

RESTAURANTS = [
    "Lá Carioca Cevicheria en La Playa",
    "1$ushi Lounge Bar",
    "4&5 bar",
    "4kamaradas",
    "A Melhor Costelinha do Mundo",
    "A Melhor Costelinha do Mundo - Uptown",
    "AMENDOLA SALUMERIA",
    "ANGU DO GOMES",
    "AZZURRA",
    "Academia da Cachaça",
    "Aconchego Carioca - Praça da Bandeira",
    "Aconchego Carioca - Shopping Village Mall",
    "Adega Santiago Barra da Tijuca",
    "Afro Gourmet",
    "Alla Zingara",
    "Amazônia Soul",
    "Artesan - Planetário da Gávea",
    "Atlântico Beach Lounge",
    "Azteka",
    "Azur",
    "B de Burger (Jardim Botânico)",
    "B&B Boards and Burgers",
    "BAR DO ADÃO GRAJAÚ",
    "BARTIU",
    "BARÓDROMO",
    "BUTECO ORIGINAL",
    "Balada Mix Arpoador",
    "Balada Mix Downtown",
    "Bar Astor RJ",
    "Bar Lagoa",
    "Bar Tio Ruy",
    "Bar da Frente",
    "Bar do Gil",
    "Bar do Honô",
    "Bar do Urso",
    "Bar399",
    "BarTínez",
    "Barril 8000 Valqueire",
    "Beco",
    "Beduino",
    "Benevenuto",
    "Berê Burger",
    "Biroska Espeto & Beer",
    "Bistrô Rio’s",
    "Bistrô das Artes",
    "Blend Lab",
    "Bobô",
    "Boralá",
    "Bota Restaurante",
    "Boteco Cevada",
    "Boteco Colarinho",
    "Boteco do Seu João Hamburgueria",
    "Botequim Restaurante",
    "Botequim Rio Antigo",
    "Botero Bar",
    "Brasas Show Galeteria",
    "Braseiro da Praia",
    "Braz Rio",
    "Brewteco",
    "Brows Casual Food",
    "Bucaneiros",
    "Buena Vida Social Clube",
    "Buenos Aires",
    "Burgers",
    "Burguer Joint Bossa Nova",
    "Burguer Joint RJ",
    "Buteco 21",
    "CANAL 6",
    "CANTINA E PIZZARIA MANJERONA EIRELI",
    "CARIOCA BAR E BOTEQUIM",
    "CASA CAMOLESE",
    "CASA URICH",
    "CEVADAS S.A.",
    "Cafe Musical carioca da Gema",
    "Cafofo Pub",
    "Caju",
    "Calabrezza Pizzaria",
    "Cam On Thai Food",
    "Cantina da Praça",
    "Capelinha",
    "Capricciosa - Ipanema",
    "Capricciosa - Lagoa",
    "Carmelo Restaurante",
    "Casa de Arte e Cultura Julieta de Serpa",
    "Caverna",
    "Cedro do Líbano",
    "Ceviche RJ",
    "Chef dos Sabores",
    "Choperia Barril 8000 - Méier",
    "Choperia Barril 8000 - Piedade",
    "Choperia Brahma Número 1",
    "CoLAB",
    "Coco Verde",
    "Coisa de Carioca",
    "Costelas",
    "Costello",
    "Costelão do Cadeg",
    "Cozi Bistrô + Bar",
    "Cozinha",
    "Curadoria",
    "D-vino",
    "DE SEMPRE BAR",
    "DOC Ristorante",
    "DOMENICA PIZZA ARTESANAL",
    "DOMENICA PIZZARIA",
    "Da Gema",
    "Da Silva",
    "Dale! Mexicano - Aerotown",
    "Deck Zero Nove",
    "Degustte",
    "Delação Premiada",
    "Deliciando Quitanda Gourmet",
    "Delirium Café",
    "Demi-Glace Premium Grill - Gonçalves Dias",
    "Demi-Glace Premium Grill - Mairink Veiga",
    "Demi-Glace Restaurante - Rua México",
    "Demi-Glace Restaurante - Rua do Lavradio",
    "Descolado Burger & Beer",
    "Destilado Bar",
    "Dezenove Restaurante",
    "Didier Restaurante",
    "Doc Bistro",
    "Dom Barcelos",
    "Dom Marvim",
    "Donninha",
    "Du Dudud Kilo Grill",
    "El Chaco Parrilla",
    "El Peruano",
    "Ella",
    "Empório Jardim - Instituto Moreira Salles",
    "Empório Jardim - Ipanema",
    "Enchendo Linguiça",
    "Espaço A",
    "Eventual Carioca",
    "FAZENDOLA IPANEMA",
    "Fazenda Culinária",
    "Ferrari Praia Bar e Lanchonete Ltda.",
    "Ferro e Farinha",
    "Ferro e Farinha",
    "Figs&Co",
    "Flor do Caribe",
    "Flórida Bar Ltda",
    "Formato Vino & Forneria",
    "Forneria Tropical",
    "Fresh & Good Restaurante",
    "Fábrica Nômade",
    "GRATTO BISTRÔ",
    "GRAVIOLA COMERCIO DE ALIMENTOS E BEBIDAS",
    "GRAVIOLA LEBLON COMERCIO DE ALIMENTOS E BEBIDAS LTDA",
    "Gabbiano Ristorante",
    "Galeto Monte Gordo",
    "Galeto Otto",
    "Garota da tijuca",
    "Gela Goela",
    "Gioia Cucina Italiana",
    "Glicerina",
    "Globar restaurante e pizzaria",
    "Gran Parrilla",
    "Gruta do bacalhau",
    "Guimas",
    "Gusto Cucina Bar",
    "Gutessen",
    "HARU SUSHI",
    "Hamburgueria da Alfândega - Centro",
    "Hamburgueria da Alfândega - Ipanema",
    "Hamburgueria da Alfândega - Lapa",
    "Hamburgueria do Barba",
    "Hansl restaurante",
    "Heaven Cucina",
    "Hell's Burguer - Barra da Tijuca",
    "Hell's Burguer - Botafogo",
    "Hocus Pocus DNA",
    "Honesto",
    "Hop Lab Pub",
    "Hula Hula Beach Bar",
    "IRAJÁ",
    "In House Café-Bistrô",
    "Itahy",
    "Jac café",
    "Japinha Carioca Méier",
    "Joaquina - Humaitá",
    "Joaquina - Leme",
    "Juanna’s",
    "Jungle Garden Pub",
    "KENTARO CULINÁRIA JAPONESA",
    "KILOGRAMA CHURRASCARIA",
    "Karibune Nova América",
    "Ki Culinária Japonesa",
    "Kilograma Restaurante",
    "Kinoa - Saudável to go",
    "Kioske leal e Almeida",
    "Kioske leal e Almeida",
    "Ko Ba Izakaya",
    "Kobudai",
    "Kostão",
    "LA VILLA BOTAQFOGO",
    "LASBRUTAS E VIVANT",
    "La Bicyclette",
    "La Bocca Bar & Trattoria",
    "La Carioca Cevicheria",
    "La Carioca Cevicheria Jardim Botanico",
    "La Empanada Ipanema",
    "La Nostra TRATTORIA",
    "La Parrilla del Mercado",
    "La Pizzateca",
    "La Plancha - Casa Shopping",
    "Labuta",
    "Laca Praia",
    "Lanches Alla Zingara",
    "Le Boucher - Leblon",
    "LeBonTon Shopping Tijuca",
    "LeBonton - Shopping Metropolitano",
    "Lilia",
    "Lilia Café",
    "Los Frick Mexican Restaurant",
    "Lulivo Cucina e Vini",
    "MALTA JARDIM BOTANICO",
    "MALTA LEBLON",
    "MANÉ FLAMENGO",
    "MARGUTTA CITTA",
    "MITSUBA",
    "MOZA street bar",
    "Mais japa",
    "Make a Cake",
    "Mamma Rosa Ristorante",
    "Mangue Seco",
    "Maracuyá da Ilha",
    "Maria e o Boi",
    "Marzipan Restaurante",
    "Marín Bistrô",
    "Massa",
    "Mazzo ristorante & pizzeria artegianale",
    "Mensateria Portucale",
    "Mercearia da Praça",
    "Mestre Oyama Sushi Bar e Restaurante LTDA",
    "Meza Bar - Botafogo",
    "Miam Miam",
    "Minimok - Leblon",
    "Minimok Ipanema",
    "Miraflores Comida Peruana",
    "Mizu",
    "Morena",
    "Moreno",
    "Mr. Maki - Shopping Millennium",
    "Mãe Joana",
    "NONNA per Heaven",
    "Naa! Sushi Bar",
    "Nagara Sushi - Galeria 1079",
    "Nagara Sushi - Galeria 566",
    "Nam Thai",
    "Nanquim",
    "Narumi Botafogo",
    "Narumi Culinária Japonesa",
    "Noo Cachaçaria",
    "Nossa Bahia",
    "O Bom Galeto",
    "O Templo",
    "O Viajante",
    "Oka Vista Bar LTDA",
    "Olympe",
    "Os Imortais",
    "PAPA JACK LEBLON",
    "PAPPA JACK COPACABANA",
    "PARRILLA TORO NEGRO",
    "PIZZA GRILL GAMBINO",
    "PORTELLA BAR",
    "Paraíso Beach Club",
    "Parrilla Uruguai - Tijuca",
    "Pizza Hut",
    "Pizzaria Camelo",
    "Pobre Juan - Barra da Tijuca",
    "Ponto de Encontro",
    "Porco Amigo Bar",
    "Porto das Carnes",
    "Praia Skol - Posto 04",
    "Praia Skol - Posto 04",
    "Praiô Beach Point",
    "Praticita",
    "Prima Osteria e Bruschetteria",
    "Prize Burger",
    "Puro",
    "Puro Restaurante",
    "Puxadinho Pub",
    "Pátio Restaurante",
    "QUIOSQUE TERRA VISTA",
    "Quase Nove",
    "Quiosque Barra 1",
    "Quiosque Chopp Brahma - Na Altura da R. Fernando Mendez",
    "Quiosque Chopp Brahma - Na altura da R. Djalma Urich",
    "Quiosque Chopp Brahma - Na altura da R. República do Peru",
    "Quiosque Chopp Brahma Na altura da R. Almirante Gonçalves",
    "Quiosque Chopp Brahma Na altura da R. Figueiredo de Magalhães",
    "Quiosque Du Leblon",
    "Quiosque Espetto Carioca",
    "Quiosque Samba social clube",
    "Quiosque Santa Clara",
    "Quiosque do Gaucho",
    "REGAJO BISTRÔ",
    "RESTAURANTE TIA PENHA",
    "Rainbow",
    "Reduto",
    "Refeitório Rj",
    "Rei do Bacalhau",
    "Restaurante Be Vegan",
    "Restaurante Estação Largo do Machado 184",
    "Restaurante OJO",
    "Restaurante Pobre Juan - Barra da Tijuca",
    "Restaurante Porto Carioca",
    "Restaurante Terra Brasilis",
    "Rio Point",
    "Rio Scenarium",
    "Royal Grill",
    "SABOR D.O.C",
    "SABORES DE GABRIELA",
    "Sabor de Café",
    "Sabor do Valqueire",
    "San Benito",
    "Santo Scenarium",
    "Santé Bistrô",
    "Satyricon",
    "Saíra Restaurante",
    "Sheesh!",
    "Shirley",
    "Soul Prainha Rio",
    "South Ferro",
    "Spud Club",
    "Sr hashi",
    "Strada restaurante",
    "SuSHiTeN",
    "Sud, O Passaro Verde",
    "Surreal Bar & Realidade Virtual",
    "Sushi Leblon",
    "Sushinharia",
    "Taboo Japa Food",
    "Tasca Filho d'Mãe",
    "The Drunk Trunk - Centro",
    "The Drunk Trunk - Shopping Nova América",
    "The Drunk Trunk - Tijuca",
    "The House of Rock and Roll",
    "Toca do Candiru",
    "Tragga - Barra da Tijuca",
    "Tragga - FashionMall",
    "Tragga - Humaitá",
    "Tulipa bistrô",
    "UP Candelária",
    "URBANITO BAR",
    "Up Burger's Ipanema",
    "Up do Sabor",
    "VENGA!",
    "VERANO RESTAURANTE",
    "Varandinha bar restaurante",
    "Venne Gastronomia Mediterrânea",
    "Verso Café",
    "Vezpa Barra",
    "Vezpa Gavea",
    "Vezpa Lapa",
    "Vezpa Largo do Machado",
    "Vezpa Leme",
    "Vezpa Novo Leblon",
    "Vezpa Pizzas - Centro",
    "Vezpa Pizzas - Leblon",
    "Vezpa Pizzas - Shopping Tijuca",
    "Via 11",
    "Via Farani",
    "Villar Formoso",
    "VinciRio Bistrô",
    "Vizinhando Crystal Mall",
    "Vizinhando Uptown",
    "Vizinho Gastrobar",
    "Vokos Grego - Leblon",
    "Yosuki",
    "Yámã Burger Vibration",
    "ZAZÁ CAFÉ",
    "ZUKA",
    "Zazá Bistrô Tropical",
    "Zb restaurante",
    "Zona Zen",
    "casa da feijoada",
    "k 08 club",
    "quartinho bar",
    "sult",
    "Êtta"
]

URL = "https://www.google.com/search"
LOCAL = 'barra da tijuca'
print(f"Opções em \"{LOCAL}\":")
LOCAL_RESTAURANTS = list()

for restaurant in RESTAURANTS:
    params = {'q': f'{restaurant} Rio de Janeiro'}
    response = requests.get(URL, params=params)
    # import pdb; pdb.set_trace()
    if not response.ok:
        print(response)

    if LOCAL in response.text.lower() and restaurant not in LOCAL_RESTAURANTS:
        print("\t", restaurant)
        LOCAL_RESTAURANTS.append(restaurant)

# vabarros@hunb518:~/Documents/python-notes$ python3 crawler.py
# Opções em "barra da tijuca":
#          4&5 bar
#          AZZURRA
#          Aconchego Carioca - Shopping Village Mall
#          Adega Santiago Barra da Tijuca
#          B de Burger (Jardim Botânico)
#          BAR DO ADÃO GRAJAÚ
#          BUTECO ORIGINAL
#          Balada Mix Arpoador
#          Balada Mix Downtown
#          Bar Tio Ruy
#          Bar do Gil
#          Bar399
#          Barril 8000 Valqueire
#          Benevenuto
#          Berê Burger
#          Bistrô Rio’s
#          Boteco do Seu João Hamburgueria
#          Braseiro da Praia
#          Braz Rio
#          Brewteco
#          Brows Casual Food
#          Buena Vida Social Clube
#          Burgers
#          CARIOCA BAR E BOTEQUIM
#          CASA URICH
#          Cam On Thai Food
#          Capelinha
#          Chef dos Sabores
#          Choperia Brahma Número 1
#          Costelas
#          Cozi Bistrô + Bar
#          Curadoria
#          DE SEMPRE BAR
#          DOC Ristorante
#          Da Silva
#          Dale! Mexicano - Aerotown
#          Doc Bistro
#          Dom Marvim
#          Ella
#          Espaço A
#          Fazenda Culinária
#          Ferrari Praia Bar e Lanchonete Ltda.
#          Figs&Co
#          Forneria Tropical
#          Fresh & Good Restaurante
#          GRAVIOLA COMERCIO DE ALIMENTOS E BEBIDAS
#          Gabbiano Ristorante
#          Gela Goela
#          Gioia Cucina Italiana
#          Gran Parrilla
#          Gruta do bacalhau
#          Hansl restaurante
#          Heaven Cucina
#          Hell's Burguer - Barra da Tijuca
#          Hula Hula Beach Bar
#          In House Café-Bistrô
#          Ki Culinária Japonesa
#          Kioske leal e Almeida
#          La Nostra TRATTORIA
#          La Parrilla del Mercado
#          La Plancha - Casa Shopping
#          Le Boucher - Leblon
#          LeBonTon Shopping Tijuca
#          Los Frick Mexican Restaurant
#          Mais japa
#          Make a Cake
#          Maracuyá da Ilha
#          Massa
#          Mensateria Portucale
#          Minimok Ipanema
#          Moreno
#          Mr. Maki - Shopping Millennium
#          NONNA per Heaven
#          O Templo
#          PAPPA JACK COPACABANA
#          Paraíso Beach Club
#          Parrilla Uruguai - Tijuca
#          Pobre Juan - Barra da Tijuca
#          Praiô Beach Point
#          Praticita
#          Prize Burger
#          Quiosque Barra 1
#          Quiosque Samba social clube
#          Quiosque do Gaucho
#          Rainbow
#          Rei do Bacalhau
#          Restaurante Be Vegan
#          Restaurante Pobre Juan - Barra da Tijuca
#          Rio Point
#          Royal Grill
#          Sabor de Café
#          Spud Club
#          SuSHiTeN
#          Tasca Filho d'Mãe
#          Tragga - Barra da Tijuca
#          Tragga - FashionMall
#          Tragga - Humaitá
#          Up do Sabor
#          Venne Gastronomia Mediterrânea
#          Vezpa Barra
#          Vezpa Novo Leblon
#          Via 11
#          Vizinhando Crystal Mall
#          Vizinhando Uptown
#          Vizinho Gastrobar
#          Yámã Burger Vibration
#          k 08 club
