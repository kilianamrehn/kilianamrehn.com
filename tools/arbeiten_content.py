# Inhalte der Arbeiten (Kampagnen + freie Strecken). Erzeugt tools/arbeiten_content.json.
# Bildnamen (w-<slug>-<n>) entsprechen public/img/<name>-<breite>.webp, Videos public/media/video/<name>.mp4
import json, os
H=os.path.dirname(os.path.abspath(__file__))
P=[]
def p(slug,title,kind,kindEn,year,client,sections,credits=(),textDe='',textEn='',top=None,color=None,edge=('KAMPAGNENFOTOGRAFIE','MODEFOTOGRAFIE')):
    P.append(dict(slug=slug,title=title,kind=kind,kindEn=kindEn,year=year,client=client,sections=sections,credits=list(credits),textDe=textDe,textEn=textEn,top=top,color=color,edge=list(edge)))
def S(label,labelEn,items,note=None,noteEn=None): return dict(label=label,labelEn=labelEn,items=items,note=note,noteEn=noteEn)
# Abspann in Kapiteln, wenn eine Arbeit mehrere Shootings zusammenfasst (Titel wie der Bogen auf der Seite).
# credits = was für alle gilt, CH[slug] = je Shooting nur, was belegt ist (alte Seite, Instagram). Ohne Belege kein Kapitel.
CH={}
def C(t,tEn,rows): return dict(t=t,tEn=tEn,rows=rows)
r=lambda s,a,b: [f'w-{s}-{i}' for i in range(a,b+1)]
p('rock-fairyland','Rock Fairyland','Freie Strecke · Editorial','Personal series · Editorial','2021',"First Magazine, New Icons' Club",
  [S('','',r('rock-fairyland',1,10))],
  [('Produktion','Kilian Amrehn'),('Styling','Jacqueline Tamm'),('Models','Marie Wehder, Louis Joerissen'),('Hair & Make-up','Kathrin Hupertz'),('Veröffentlicht',"First Magazine, New Icons' Club Magazine")],
  edge=('FREIE STRECKE','EDITORIAL'))
p('ozean-der-stille','Ozean der Stille','Freie Strecke · Mode','Personal series · Fashion','2026','',
  [S('','',r('ozean-der-stille',1,11))],[('Design','Jonas Braun · Pulpo Productions'),('Foto','Kilian Amrehn'),('Video','Lukas Beilenhoff'),('Video-Assistenz','Dopia Films'),('Assistenz','Alexandra Neufeld, Gereon Schultes, David Heinrichs')],top='ozean-der-stille',edge=('FREIE STRECKE','MODEFOTOGRAFIE'))
p('scholl-iconic','Scholl','Kampagne','Campaign','2021 bis 2023','The Wants Social',
  [S('Scholl Comfort · Weihnachten','Scholl Comfort · Christmas',r('scholl',33,35)),
   S('Scholl Comfort · Ägypten','Scholl Comfort · Egypt',r('scholl',21,28)),
   S('Scholl iconic · Belinda und Anna','Scholl iconic · Belinda and Anna',r('scholl',36,41)),
   S('Scholl Comfort · Julie und Emma','Scholl Comfort · Julie and Emma',r('scholl',12,20)),
   S('Scholl iconic · Alua und Linde','Scholl iconic · Alua and Linde',r('scholl',7,11)),
   S('Scholl iconic · Fuerteventura','Scholl iconic · Fuerteventura',r('scholl',1,6))],
  [('Agentur','The Wants Social'),('Foto','Kilian Amrehn')])
CH['scholl-iconic']=[
  C('Scholl Comfort · Weihnachten','Scholl Comfort · Christmas',[('Produktion','Anna Siepenkötter'),('Produktionsassistenz','Nataliya Kaiser'),('Styling','Stella Lukaschewski'),('Model','Mona M.'),('Hair & Make-up','Hanna Fuchs'),('Fotoassistenz','Eno de Witt')]),
  C('Scholl Comfort · Ägypten','Scholl Comfort · Egypt',[('Creative Direction','Wiebke Horst, Anna Siepenkötter'),('Film','YOVEGO'),('Styling','Stella Lukaschewski, Catarina Brockhoff-Lingke'),('Hair & Make-up','Melanie Bulu'),('Stills','Eno de Witt'),('Fotoassistenz','Fabian Podzuweit'),('Talents','Cristina, Salwa, Alexandra, Mathilde')]),
  C('Scholl iconic · Belinda und Anna','Scholl iconic · Belinda and Anna',[('Produktion','Anna Siepenkötter'),('Styling','Stella Lukaschewski, Johanna Löer'),('Models','Belinda, Anna'),('Hair & Make-up','Nadine Thoma'),('Video','Norman Keutgen'),('Video, BTS, Reels','Wiebke Horst, Wiebke Hennig, Lara Hartmann'),('Stills','Nina Schörner')]),
  C('Scholl Comfort · Julie und Emma','Scholl Comfort · Julie and Emma',[('Produktion','Anna Siepenkötter'),('Creative Direction','Wiebke Hennig'),('Styling','Henni Schaefer, Johanna Löer, Stella Lukaschewski'),('Models','Julie March, Emma Loughran'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Eno de Witt')]),
  C('Scholl iconic · Alua und Linde','Scholl iconic · Alua and Linde',[('Produktion','Anna Siepenkötter, Wiebke Hennig'),('Styling','Henrike Schaefer, Alexa Drepper'),('Models','Alua, Linde Derickx'),('Hair & Make-up','Nadine Thoma'),('Video','Nico Pékar, Kevin Bressler'),('Reels','Cata Lingke, Johanna Löer'),('BTS','Kathrin Giblian'),('Fotoassistenz','Fabian Podzuweit')]),
  C('Scholl iconic · Fuerteventura','Scholl iconic · Fuerteventura',[('Creative Direction','Anna Siepenkötter, Wiebke Hennig'),('Styling','Johanna Löer, Henni Schaefer'),('Models','Amy Gambini, Sanne'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Fabian Podzuweit')])]
p('copenhagen-studios','Copenhagen Studios','Kampagne','Campaign','2021 bis 2022','The Wants Social',
  [S('Margot und Jason','Margot and Jason',r('copenhagen-studios',8,13)+['cph-schal-loop']),S('Linde','Linde',r('copenhagen-studios',4,7)),S('Djerra','Djerra',r('copenhagen-studios',1,3))],
  [('Agentur','The Wants Social'),('Foto','Kilian Amrehn')])
CH['copenhagen-studios']=[
  C('Margot und Jason','Margot and Jason',[('Creative Direction','Karla Jenders'),('Models','Margot Davy, Jason Grotjahn'),('Hair & Make-up','Melanie Bulu'),('Styling','Johanna Löer'),('Fotoassistenz','Eno de Witt')]),
  C('Linde','Linde',[('Produktion','Karla Jenders'),('Co-Produktion','Gina Walser'),('Styling','Henrike Schaefer, Vicky Krampen'),('Model','Linde Torenvlied'),('Hair & Make-up','Melanie Bulu'),('BTS','Vicky Krampen')]),
  C('Djerra','Djerra',[('Model','Djerra'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Fabian Podzuweit')])]
p('peek-cloppenburg-x-ellesse','Peek & Cloppenburg x Ellesse','Kampagne','Campaign','2022','Feelming',
  [S('','',r('peek-cloppenburg-x-ellesse',1,7))],
  [('Produktion','Feelming'),('Regie','Mario Bürger'),('1st AD','Nico Pékar'),('DOP','Pasindu Goldmann'),('Styling','Peninah Amanda'),('Hair & Make-up','Kristin Belger'),('Movement','Tim Schmitz'),('Talents','Nora Nova, Rowdy Eyez, Mecnun'),('Foto','Kilian Amrehn')])
p('synergy','Untamed','Freie Strecke · Editorial','Personal series · Editorial','2024','',
  [S('','',r('synergy',1,5),'Ein Model, ein Rabe namens Hitchcock, ein Hahn namens Michelangelo, ein Studio. Genau so fotografiert.','A model, a raven called Hitchcock, a cockerel called Michelangelo, a studio. Photographed exactly as you see it.'),
   S('KI-animiert aus diesen Fotos','AI-animated from these photos',['untamed-ki-1','untamed-ki-3'])],
  [('Art Direction, Foto','Kilian Amrehn'),('Produktion','Pia Unterstell'),('Model','Jóna Gudmundsdóttir · MIRRRS Models'),('Tiertrainerin','Fränze Lüttich'),('Hair & Make-up','Tini Sager'),('Kollektiv','Artistpool')],
  edge=('FREIE STRECKE','EDITORIAL'))
p('silent-escape','Silent Escape','Kampagne','Campaign','2024','JEREMIAH',
  [S('','',r('silent-escape',1,5)),S('KI-animiert aus diesen Fotos','AI-animated from these photos',['jeremiah-ki-1','jeremiah-ki-3']),S('Behind the Scenes','Behind the scenes',['silent-escape-bts'])],
  [('Design','JEREMIAH'),('Produktion','Kilian Amrehn'),('Models','Marie Lange, Ricardo Alverez'),('Hair & Make-up','Natalie Arslan')],
  'Eine Wüste unter vollem Mond, zwei Menschen stehen still. Sie trägt die Erwartungen der anderen, er die Unsichtbarkeit. Für einen Moment sind beide nicht mehr gefangen. Sie stehen still und sind doch längst unterwegs.',
  'A desert under a full moon, two people standing still. She carries other people’s expectations, he carries being unseen. For a moment, neither of them is trapped. They stand still, and yet they are already on their way.',
  edge=('KAMPAGNE','MODEFOTOGRAFIE'))
p('trish-reflections-of-identity','Reflections of Identity','Freie Strecke · Porträt','Personal series · Portrait','2024','Studio Zehn70',
  [S('','',r('trish-reflections-of-identity',1,7))],
  [('Art Direction, Foto','Kilian Amrehn'),('Produktion','Pia Unterstell'),('Model','Trish · PARS Management'),('Hair & Make-up','Serife Cigdem Güney')],
  'Vier Szenen, eine Person. Stark in der Mode, weich in der Beauty, fremd vor einem offenen Kühlschrank, nackt im Schwarzweiß.',
  'Four scenes, one person. Strong in fashion, soft in beauty, out of place in front of an open fridge, bare in black and white.',
  edge=('FREIE STRECKE','GERICHTETES LICHT'))
p('niewiederleise','#niewiederleise','Kampagne','Campaign','2024','',[S('','',r('niewiederleise',1,9))],[('Foto','Kilian Amrehn')],top='niewiederleise-kampagne',edge=('KAMPAGNE','#NIEWIEDERLEISE'))
p('phiala','Phiala','Kampagne','Campaign','2024','Phiala',[S('','',r('phiala',1,9))],
  [('Produktion','Ischtar Isik'),('Creative Direction','Ischtar Isik'),('Models','Lael Schunter, Nicole Handy'),('Hair & Make-up','Sara Cassel'),('Styling','Henni Schaefer'),('Foto','Kilian Amrehn')],edge=('KAMPAGNE','DESSOUSFOTOGRAFIE'))
p('monano-schmuck','Monano Schmuckmanufaktur','Kampagne','Campaign','2024','Monano',[S('','',r('monano-schmuck',1,6))],
  [('Produktion','Kilian Amrehn'),('Styling','Jacqueline Tamm'),('Hair & Make-up','Hanna Fuchs'),('Models','Ronja Stevens, Hella Kornatzki'),('Fotoassistenz','Eno de Witt')],edge=('SCHMUCKFOTOGRAFIE','KAMPAGNE'))
p('new-icons-club-magazine',"New Icons' Club Magazine",'Editorial · Magazin','Editorial · Magazine','2023 bis 2024',"New Icons' Club",
  [S('2nd Hand','2nd Hand',r('new-icons-club-magazine-2',1,10)),S('Ausgabe 1','Issue 1',[x for x in r('new-icons-club-magazine',1,13) if x not in ('w-new-icons-club-magazine-4','w-new-icons-club-magazine-2')])],
  [('Produktion','Kilian Amrehn'),('Creative Direction','Ann-Kathrin Templin'),('Styling','Jacqueline Tamm'),('Fotoassistenz','Fabian Podzuweit'),('Second Hand','Kleiderei, MatchYourStyle'),('Foto','Kilian Amrehn')],edge=('EDITORIAL','MAGAZIN'))
CH['new-icons-club-magazine']=[
  C('2nd Hand','2nd Hand',[('Hair & Make-up','Hanna Fuchs'),('Models','Linda, Nika, Lasse')]),
  C('Ausgabe 1','Issue 1',[('Hair & Make-up','Serife Cigdem Güney'),('Models','Marie, Louis, Lia, Paulus, Elisabeth')])]
p('pnts','PNTS','Kampagne','Campaign','2022 bis 2023','The Wants Social',
  [S('Noordwijk','Noordwijk',r('pnts',8,16)),S('Studio','Studio',r('pnts',1,7))],
  [('Agentur','The Wants Social'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Eno de Witt'),('Foto','Kilian Amrehn')],color='#1c1b1a')
CH['pnts']=[
  C('Noordwijk','Noordwijk',[('Creative Direction','Wiebke Hennig, Vera Evers'),('Styling','Catarina Brockhoff-Lingke, Ricarda Saemann'),('DOP','Christian Hülsmeyer, Paul Mess'),('Talents','Chelsey Weimar, Amelie Fiebach')]),
  C('Studio','Studio',[('Creative Direction','Wiebke Hennig, Anna Siepenkötter'),('Styling','Johanna Löer, Catarina Brockhoff-Lingke'),('BTS & Social','Vera Evers, Marvin Schmidt'),('Talents','Chelsey Weimar, Aline Gomes')])]
p('appelrathcuepper','AppelrathCüpper','Kampagne','Campaign','2022','AppelrathCüpper',[S('','',r('appelrathcuepper',1,9))],
  [('Produktion','Mariann Reitz'),('Creative Direction','Alexandra Specht'),('Fotoassistenz','Jonas Boltze'),('Styling','Lisa Bräuer'),('Models','Maren Thelen, Signe'),('Hair & Make-up','Patricia Irsinger'),('Foto','Kilian Amrehn')],
  'Spiel mit Spiegeln.','Playing with mirrors.')
p('marie-dahmen','Marie','Freie Strecke · Porträt','Personal series · Portrait','2022','',[S('','',[x for x in r('marie-dahmen',1,10) if x!='w-marie-dahmen-3'])],
  [('Produktion','Kilian Amrehn'),('Model','Marie Dahmen'),('Styling','Jacqueline Tamm'),('Hair & Make-up','Ilknur Gelme'),('Fotoassistenz','Fabian Podzuweit')],edge=('FREIE STRECKE','ANALOG UND DIGITAL'))
p('the-wants','The Wants','Kampagne','Campaign','2020','The Wants Social',[S('','',r('the-wants',1,10))],
  [('Agentur','The Wants Social'),('Produktion','Anna Siepenkötter'),('Creative Direction','Karla Jenders'),('Model','Mona Lillian'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Fabian Podzuweit'),('Foto','Kilian Amrehn')])
p('bundesliga','Bundesliga','Sport · Bundesliga','Sport · Bundesliga','2023 bis 2025','DFL',[S('','',[x for x in r('bundesliga',1,29) if x!='w-bundesliga-26'])],[('Auftrag','DFL'),('Foto','Kilian Amrehn')],
  'Für die DFL in den Stadien, direkt am Spielfeldrand. Beeindruckende Orte. Und der Sport erst, so nah dran.',
  'For the DFL in the stadiums, right on the touchline. Impressive places. And the football even more so, this close up.',
  edge=('SPORTFOTOGRAFIE','BUNDESLIGA'))

# Farbe des Bands (mit Farbpipette aus den Bildern der Arbeit genommen) und Bild(er) beim Aufklappen.
# Reihenfolge so, dass nie zwei ähnliche Farben nebeneinander stehen.
BAND=[('rock-fairyland','#95c5b9',[1,4,2]),
 ('copenhagen-studios','#e8603e',[11,'vid:cph-schal-loop',12]),
 ('peek-cloppenburg-x-ellesse','#99b4bc',[1]),
 ('trish-reflections-of-identity','#0a8389',[6]),
 ('ozean-der-stille','#5a1f1b',[11]),
 ('synergy','#2f6f58',[1,2,'vid:untamed-ki-1']),
 ('appelrathcuepper','#0d3a78',[2]),
 ('niewiederleise','#6f6f41',['vid:niewiederleise-kampagne']),
 ('new-icons-club-magazine','#c8182e',['new-icons-club-magazine-12','new-icons-club-magazine-9','new-icons-club-magazine-2-9']),
 ('silent-escape','#2e4f56',[5,1,'vid:jeremiah-ki-3']),
 ('phiala','#ceb57d',[8,4,2]),
 ('scholl-iconic','#d0592b',['scholl-3','scholl-5','scholl-9']),
 ('pnts','#2f5878',[3,10,4]),
 ('the-wants','#af7a56',[3,5,8]),
 ('monano-schmuck','#9eccd4',[5]),
 ('bundesliga','#3a3a38',[13,7,18]),
 ('marie-dahmen','#9a5530',[5,10])]
for i,x in enumerate(P): x['seed']=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17][i]  # alte Position, damit die Bögen gleich bleiben
byslug={x['slug']:x for x in P}
assert len(BAND)==len(P), (len(BAND),len(P))
P=[]
for slug,col,ims in BAND:
    x=byslug[slug]; x['band']=col; x['color']=col  # Hintergrund der Arbeit = Bandfarbe
    x['bandImgs']=[(i if isinstance(i,str) and i.startswith('vid:') else 'w-'+i if isinstance(i,str) else f'w-{slug}-{i}') for i in ims]
    P.append(x)

# Zusätzlich auf der Arbeiten-Übersicht (nach der Bandwahl, Kilian 12.10.)
EXTRA={'peek-cloppenburg-x-ellesse':['w-peek-cloppenburg-x-ellesse-4'],'trish-reflections-of-identity':['w-trish-reflections-of-identity-1'],
 'ozean-der-stille':['w-ozean-der-stille-4','w-ozean-der-stille-1'],'appelrathcuepper':['w-appelrathcuepper-8'],'niewiederleise':['w-niewiederleise-9'],
 'monano-schmuck':['w-monano-schmuck-1'],'bundesliga':['w-bundesliga-20']}
for x in P: x['overviewExtra']=EXTRA.get(x['slug'],[]); x['chapters']=CH.get(x['slug'],[])
json.dump(P,open(os.path.join(H,'arbeiten_content.json'),'w'),ensure_ascii=False,indent=1)
print(len(P))
