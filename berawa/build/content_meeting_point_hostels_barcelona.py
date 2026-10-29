# Contenido de la demo Meeting Point Hostels (Barcelona) (es/ca/en/fr). Hechos de meetingpointhostels.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Dormitorios compartidos','Habitaciones privadas','Grupos de 9 o más'],'ca':['Dormitoris compartits','Habitacions privades','Grups de 9 o més'],'en':['Shared dorms','Private rooms','Groups of 9 or more'],'fr':['Dortoirs partagés','Chambres privées','Groupes de 9 ou plus']}
RD={
'es':['Con baño privado, como todas las habitaciones del albergue. Solo para mayores de 18 años.','También con baño privado; los menores de 18 años pueden alojarse en ellas si van con sus padres.','Las reservas de grupo se gestionan por correo electrónico en hello@meetingpointhostels.com.'],
'ca':['Amb bany privat, com totes les habitacions de l\'alberg. Només per a majors de 18 anys.','També amb bany privat; els menors de 18 anys s\'hi poden allotjar si van amb els pares.','Les reserves de grup es gestionen per correu electrònic a hello@meetingpointhostels.com.'],
'en':['With private bathroom, like every room in the hostel. Only for guests aged 18 and over.','Also with private bathroom; under-18s can stay in them if accompanied by their parents.','Group bookings are handled by email at hello@meetingpointhostels.com.'],
'fr':['Avec salle de bains privée, comme toutes les chambres de l\'auberge. Réservés aux plus de 18 ans.','Également avec salle de bains privée ; les moins de 18 ans peuvent y séjourner accompagnés de leurs parents.','Les réservations de groupe se font par e-mail à hello@meetingpointhostels.com.']}
ART={
'hero':('skyline',3501,['#2b3550','#e48a5f','#f9d19b','#29334d','#1f283d','#141a29']),
'intro':('columns',3502,['#eceff6','#f5f7fb','#b8893e','#2e3f6e','#1b2647']),
'r1':('arches',3511,['#eceff6','#c7cfe2','#8795bd','#2e3f6e','#1b2647']),
'r2':('columns',3512,['#ebeef5','#f4f6fa','#c08c40','#33457a','#1e2a4d']),
'r3':('skyline',3513,['#2f3a58','#e2a160','#f6d59e','#2d3855','#222b42','#161c2c']),
'g1':('hills',3521,['#e6ecd9','#f1e6c4','#f6cf8a','#a9c19e','#80a085','#587767']),
'g2':('arches',3522,['#eceff6','#c4cce0','#8492ba','#2e3f6e','#1b2647']),
'g3':('skyline',3523,['#28324c','#e48a5f','#f9d19b','#26304a','#1d253a','#131827']),
'g4':('columns',3524,['#eceff6','#f5f7fb','#b8893e','#2e3f6e','#1b2647']),
'g5':('hills',3525,['#e3ead6','#f0e5c2','#f4cf8c','#9fbf96','#6f9a72','#4d7550']),
'g6':('arches',3526,['#ebeef5','#c2cadf','#8290b8','#2e3f6e','#1b2647'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Meeting Point Hostels · Albergue moderno junto a la estación de Sants, Barcelona',see_rooms='Ver habitaciones',hero_k='Barcelona · Sants',hero_t='Tu punto de encuentro en Barcelona',hero_s='Un albergue moderno con ambiente amigable e internacional, a solo 3 minutos a pie de la estación de Sants.',
 intro_t='Todas las habitaciones con baño privado',intro_p1='Meeting Point Hostels está en Vallespir 20, cerca de la estación de Sants y de las líneas de metro L1/L3/L5: el centro histórico y la plaza de Cataluña quedan a unos 10 minutos en tren.',
 intro_p2='Ofrece dormitorios compartidos y habitaciones privadas, todas con baño privado. Check-in de 14:00 a 23:00 y teléfono atendido a todas horas.',
 stats=['Junto a Sants','Baño privado en todas','Metro L1/L3/L5','Ambiente internacional'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Cómo se puede alojar en el albergue.',
 svcs=['Baño privado en todas las habitaciones','Consigna de equipaje','Check-in de 14:00 a 23:00','Teléfono a todas horas','Pago con Visa, MasterCard y Maestro','Reservas de grupo','A 3 minutos de Sants','Ambiente amigable e internacional'],
 loc_p='Vallespir 20 · 08014 Barcelona, a 3 minutos a pie de la estación de Sants (tren y metro L1/L3/L5).',
 chips=['¿Qué habitaciones tiene?','¿A qué hora es el check-in?','¿Cómo llego desde el aeropuerto?','¿Cómo se reserva?']),
'ca':dict(title='Meeting Point Hostels · Alberg modern al costat de l\'estació de Sants, Barcelona',see_rooms='Veure habitacions',hero_k='Barcelona · Sants',hero_t='El teu punt de trobada a Barcelona',hero_s='Un alberg modern amb ambient amigable i internacional, a només 3 minuts a peu de l\'estació de Sants.',
 intro_t='Totes les habitacions amb bany privat',intro_p1='Meeting Point Hostels és a Vallespir 20, a prop de l\'estació de Sants i de les línies de metro L1/L3/L5: el centre històric i la plaça de Catalunya queden a uns 10 minuts en tren.',
 intro_p2='Ofereix dormitoris compartits i habitacions privades, totes amb bany privat. Check-in de 14:00 a 23:00 i telèfon atès a totes hores.',
 stats=['Al costat de Sants','Bany privat a totes','Metro L1/L3/L5','Ambient internacional'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Com es pot allotjar a l\'alberg.',
 svcs=['Bany privat a totes les habitacions','Consigna d\'equipatge','Check-in de 14:00 a 23:00','Telèfon a totes hores','Pagament amb Visa, MasterCard i Maestro','Reserves de grup','A 3 minuts de Sants','Ambient amigable i internacional'],
 loc_p='Vallespir 20 · 08014 Barcelona, a 3 minuts a peu de l\'estació de Sants (tren i metro L1/L3/L5).',
 chips=['Quines habitacions té?','A quina hora és el check-in?','Com arribo des de l\'aeroport?','Com es reserva?']),
'en':dict(title='Meeting Point Hostels · Modern hostel next to Sants station, Barcelona',see_rooms='See the rooms',hero_k='Barcelona · Sants',hero_t='Your meeting point in Barcelona',hero_s='A modern hostel with a friendly, international atmosphere, just a 3-minute walk from Sants station.',
 intro_t='Every room with a private bathroom',intro_p1='Meeting Point Hostels is at Vallespir 20, near Sants station and metro lines L1/L3/L5: the historic centre and Plaça de Catalunya are about 10 minutes away by train.',
 intro_p2='It offers shared dorms and private rooms, all with private bathroom. Check-in from 14:00 to 23:00 and a phone answered at all hours.',
 stats=['Next to Sants','Private bathroom in all','Metro L1/L3/L5','International vibe'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='How you can stay at the hostel.',
 svcs=['Private bathroom in every room','Luggage storage','Check-in 14:00 to 23:00','Phone at all hours','Visa, MasterCard and Maestro accepted','Group bookings','3 minutes from Sants','Friendly, international atmosphere'],
 loc_p='Vallespir 20 · 08014 Barcelona, a 3-minute walk from Sants station (train and metro L1/L3/L5).',
 chips=['What rooms does it have?','What time is check-in?','How do I get there from the airport?','How do I book?']),
'fr':dict(title='Meeting Point Hostels · Auberge moderne près de la gare de Sants, Barcelone',see_rooms='Voir les chambres',hero_k='Barcelone · Sants',hero_t='Votre point de rencontre à Barcelone',hero_s='Une auberge moderne à l\'ambiance conviviale et internationale, à 3 minutes à pied de la gare de Sants.',
 intro_t='Toutes les chambres avec salle de bains privée',intro_p1='Meeting Point Hostels se trouve Vallespir 20, près de la gare de Sants et des lignes de métro L1/L3/L5 : le centre historique et la plaça de Catalunya sont à environ 10 minutes en train.',
 intro_p2='Elle propose des dortoirs partagés et des chambres privées, tous avec salle de bains privée. Check-in de 14:00 à 23:00 et téléphone joignable à toute heure.',
 stats=['Près de Sants','Salle de bains privée partout','Métro L1/L3/L5','Ambiance internationale'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Comment séjourner à l\'auberge.',
 svcs=['Salle de bains privée dans chaque chambre','Consigne à bagages','Check-in de 14:00 à 23:00','Téléphone à toute heure','Visa, MasterCard et Maestro acceptées','Réservations de groupe','À 3 minutes de Sants','Ambiance conviviale et internationale'],
 loc_p='Vallespir 20 · 08014 Barcelone, à 3 minutes à pied de la gare de Sants (train et métro L1/L3/L5).',
 chips=['Quelles chambres a-t-il ?','À quelle heure est le check-in ?','Comment venir depuis l\'aéroport ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
R='https://wubook.net/wbkd/wbk/?lcode=1470476499&lang='
BOOK=dict(mode='engine',url={l:R+l for l in ('es','ca','en','fr')})
D=dict(name='Meeting Point Hostels',ac='#2e3f6e',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Vallespir 20 · 08014 Barcelona',phones=['+34 934 097 446'],emails=['hello@meetingpointhostels.com'],maps='Meeting Point Hostels, Carrer de Vallespir 20, Barcelona',t=T)
META=dict(repo='demo-meeting-point-hostels-barcelona',name='Meeting Point Hostels',legal_name='Meeting Point Hostels S.L.',registry_ids=['CIF B65676637','AJ000667'],
 url='https://meetingpointhostels.com/',domain='meetingpointhostels.com',municipality='Barcelona',province='Barcelona',sector='albergue junto a la estación de Sants',
 read_at='2026-10-29T08:25:00+01:00',created_at='2026-10-29T08:30:00+01:00',built_at='2026-10-29T08:30:00+01:00',audit_date='2026-10-29T07:53:00+01:00',
 rating=dict(value=4.3,coincide=['telefono','web'],date='2026-10-29T06:56:16+01:00',url='https://www.google.com/maps/place/Meeting+Point+Hostels/@41.3787101,2.1376915,17z/data=!4m9!3m8!1s0x12a49886ff67b11b:0xc19c565abb02f293!5m2!4m1!1i2!8m2!3d41.3787101!4d2.1376915!16s%2Fg%2F11c5bst0gd?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyMC4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Los botones Reservar van al motor WuBook que enlaza su propia web (wubook.net/wbkd/wbk/?lcode=1470476499), con parametro de idioma. La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿A qué hora es el check-in?','K02'),('¿Tienen consigna de equipaje?','K03'),('¿Cuál es la política de cancelación?','K04'),('¿Qué métodos de pago aceptan?','K05'),('¿Hacen reservas de grupo?','K06'),('¿Aceptan menores de 18 años?','K07'),('¿Dónde está?','K08'),('¿Cómo llego desde el aeropuerto?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una cama libre mañana','K10'),('¿Hay desayuno?','K13'),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('A quina hora és el check-in?','K02'),('Teniu consigna d\'equipatge?','K03'),('Quina és la política de cancel·lació?','K04'),('Quins mètodes de pagament accepteu?','K05'),('Feu reserves de grup?','K06'),('Accepteu menors de 18 anys?','K07'),('On és?','K08'),('Com arribo des de l\'aeroport?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha un llit lliure demà','K10'),('Hi ha esmorzar?','K13'),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What time is check-in?','K02'),('Do you have luggage storage?','K03'),('What is the cancellation policy?','K04'),('What payment methods do you accept?','K05'),('Do you take group bookings?','K06'),('Do you accept under-18s?','K07'),('Where is it?','K08'),('How do I get there from the airport?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free bed tomorrow','K10'),('Is breakfast served?','K13'),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('À quelle heure est le check-in ?','K02'),('Avez-vous une consigne à bagages ?','K03'),('Quelle est la politique d\'annulation ?','K04'),('Quels moyens de paiement acceptez-vous ?','K05'),('Acceptez-vous les groupes ?','K06'),('Acceptez-vous les moins de 18 ans ?','K07'),('Où est-ce ?','K08'),('Comment venir depuis l\'aéroport ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a un lit libre demain','K10'),('Le petit-déjeuner est-il servi ?','K13'),('Y a-t-il une piscine ?',None)]}
