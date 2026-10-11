# Inhalte der Arbeiten (Kampagnen + freie Strecken). Erzeugt tools/arbeiten_content.json.
# Bildnamen (w-<slug>-<n>) entsprechen public/img/<name>-<breite>.webp, Videos public/media/video/<name>.mp4
import json, os
H=os.path.dirname(os.path.abspath(__file__))
P=[]
def p(slug,title,kind,kindEn,year,client,sections,credits=(),textDe='',textEn='',top=None,color=None,edge=('KAMPAGNENFOTOGRAFIE','MODEFOTOGRAFIE')):
    P.append(dict(slug=slug,title=title,kind=kind,kindEn=kindEn,year=year,client=client,sections=sections,credits=list(credits),textDe=textDe,textEn=textEn,top=top,color=color,edge=list(edge)))
def S(label,labelEn,items,note=None,noteEn=None): return dict(label=label,labelEn=labelEn,items=items,note=note,noteEn=noteEn)
r=lambda s,a,b: [f'w-{s}-{i}' for i in range(a,b+1)]
p('rock-fairyland','Rock Fairyland','Freie Strecke · Editorial','Personal series · Editorial','2021',"First Magazine, New Icons' Club",
  [S('','',r('rock-fairyland',1,10))],
  [('Produktion','Kilian Amrehn'),('Styling','Jacqueline Tamm'),('Models','Marie Wehder, Louis Joerissen'),('Hair & Make-up','Kathrin Hupertz'),('Veröffentlicht',"First Magazine, New Icons' Club Magazine")],
  edge=('FREIE STRECKE','EDITORIAL'))
p('ozean-der-stille','Ozean der Stille','Freie Strecke · Mode','Personal series · Fashion','2026','',
  [S('','',r('ozean-der-stille',1,11))],[('Foto','Kilian Amrehn')],top='ozean-der-stille',edge=('FREIE STRECKE','MODEFOTOGRAFIE'))
p('scholl-iconic','Scholl','Kampagnen','Campaigns','2021 bis 2023','The Wants Social',
  [S('Scholl iconic · Fuerteventura 2021','Scholl iconic · Fuerteventura 2021',r('scholl',1,6)),
   S('Scholl iconic · Oktober 2021','Scholl iconic · October 2021',r('scholl',7,11)),
   S('Scholl Comfort · Studio, Juli 2022','Scholl Comfort · Studio, July 2022',r('scholl',12,20)),
   S('Scholl Comfort · Ägypten 2023','Scholl Comfort · Egypt 2023',r('scholl',21,28)),
   S('Scholl iconic · Februar 2023','Scholl iconic · February 2023',r('scholl',36,41)),
   S('Scholl iconic · Sizilien 2023','Scholl iconic · Sicily 2023',r('scholl',29,32)),
   S('Scholl Comfort · Weihnachten 2023','Scholl Comfort · Christmas 2023',r('scholl',33,35))],
  [('Produktion','The Wants Social'),('Creative Direction','Anna Siepenkötter, Wiebke Hennig'),('Styling','Johanna Löer, Stella Lukaschewski, Catarina Brockhoff-Lingke'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Fabian Podzuweit, Eno de Witt'),('Film','YOVEGO'),('Foto','Kilian Amrehn')])
p('copenhagen-studios','Copenhagen Studios','Kampagnen','Campaigns','2021 bis 2022','The Wants Social',
  [S('Februar 2021','February 2021',r('copenhagen-studios',1,3)),S('Juni 2021','June 2021',r('copenhagen-studios',4,7)),S('Oktober 2022','October 2022',r('copenhagen-studios',8,13)+['cph-schal-loop'])],
  [('Produktion','The Wants Social'),('Creative Director','Karla Jenders'),('Models','Margot Davy, Jason Grotjahn'),('Hair & Make-up','Melanie Bulu'),('Styling','Johanna Löer'),('Fotoassistenz','Eno de Witt'),('Foto','Kilian Amrehn')])
p('peek-cloppenburg-x-ellesse','Peek & Cloppenburg x Ellesse','Kampagne','Campaign','2022','Feelming',
  [S('','',r('peek-cloppenburg-x-ellesse',1,7))],
  [('Produktion','Feelming'),('Regie','Mario Bürger'),('1st AD','Nico Pékar'),('DOP','Pasindu Goldmann'),('Styling','Peninah Amanda'),('Hair & Make-up','Kristin Belger'),('Movement','Tim Schmitz'),('Talents','Nora Nova, Rowdy Eyez, Mecnun'),('Foto','Kilian Amrehn')])
p('synergy','Untamed','Freie Strecke · Editorial','Personal series · Editorial','2024','',
  [S('','',r('synergy',1,5),'Kein KI-Bild. Ein Model, ein Rabe namens Hitchcock, ein Hahn namens Michelangelo und ein Studio. Genau so fotografiert.','Not an AI image. A model, a raven called Hitchcock, a rooster called Michelangelo and a studio. Photographed exactly like this.'),
   S('KI-animiert aus diesen Fotos','AI-animated from these photos',['untamed-ki-1','untamed-ki-2','untamed-ki-3','untamed-ki-4'])],
  [('Art Direction, Foto','Kilian Amrehn'),('Produktion','Pia Unterstell'),('Model','Jóna Gudmundsdóttir · MIRRRS Models'),('Tiertrainerin','Fränze Lüttich'),('Hair & Make-up','Tini Sager'),('Kollektiv','Artistpool')],
  edge=('FREIE STRECKE','KEIN KI-BILD'))
p('silent-escape','Silent Escape','Kampagne · JEREMIAH','Campaign · JEREMIAH','2024','JEREMIAH',
  [S('','',r('silent-escape',1,5)),S('KI-animiert aus diesen Fotos','AI-animated from these photos',['jeremiah-ki-1','jeremiah-ki-2','jeremiah-ki-3']),S('Behind the Scenes','Behind the scenes',['silent-escape-bts'])],
  [('Design','JEREMIAH'),('Produktion','Kilian Amrehn'),('Models','Marie Lange, Ricardo Alverez'),('Hair & Make-up','Natalie Arslan')],
  'Eine Wüste unter vollem Mond, zwei Menschen stehen still. Sie trägt die Erwartungen der anderen, er die Unsichtbarkeit. Für einen Moment sind beide nicht mehr gefangen. Sie stehen still, und sind doch längst unterwegs.',
  'A desert under a full moon, two people standing still. She carries the expectations of others, he carries invisibility. For a moment, neither of them is trapped. They stand still, yet their spirits are already running free.',
  edge=('SCHMUCKFOTOGRAFIE','KAMPAGNE'))
p('trish-reflections-of-identity','Reflections of Identity','Freie Strecke · Porträt','Personal series · Portrait','2024','Studio Zehn70',
  [S('','',r('trish-reflections-of-identity',1,7))],
  [('Art Direction, Foto','Kilian Amrehn'),('Produktion','Pia Unterstell'),('Model','Trish · PARS Management'),('Hair & Make-up','Serife Cigdem Güney')],
  'Vier Szenen, eine Person. Stark in der Mode, weich in der Beauty, fremd vor einem offenen Kühlschrank, nackt im Schwarzweiß.',
  'Four scenes, one person. Strong in fashion, soft in beauty, strange in front of an open fridge, bare in black and white.',
  edge=('FREIE STRECKE','GERICHTETES LICHT'))
p('niewiederleise','#niewiederleise','Kampagne','Campaign','2024','',[S('','',r('niewiederleise',1,9))],[('Foto','Kilian Amrehn')],top='niewiederleise-kampagne',edge=('KAMPAGNE','#NIEWIEDERLEISE'))
p('phiala','Phiala','Kampagne','Campaign','2024','Phiala',[S('','',r('phiala',1,9))],
  [('Produktion','Ischtar Isik'),('Creative Director','Ischtar Isik'),('Models','Lael Schunter, Nicole Handy'),('Hair & Make-up','Sara Cassel'),('Styling','Henni Schaefer'),('Foto','Kilian Amrehn')],edge=('KAMPAGNE','SCHMUCKFOTOGRAFIE'))
p('monano-schmuck','Monano Schmuckmanufaktur','Kampagne','Campaign','2024','Monano',[S('','',r('monano-schmuck',1,6))],
  [('Produktion','Kilian Amrehn'),('Styling','Jacqueline Tamm'),('Hair & Make-up','Hanna Fuchs'),('Models','Ronja Stevens, Hella Kornatzki'),('Fotoassistenz','Eno de Witt')],edge=('SCHMUCKFOTOGRAFIE','KAMPAGNE'))
p('new-icons-club-magazine',"New Icons' Club Magazine",'Editorial · Magazin','Editorial · Magazine','2023 bis 2024',"New Icons' Club",
  [S('Ausgabe 1 · 2023','Issue 1 · 2023',r('new-icons-club-magazine',1,13)),S('2nd Hand · 2024','2nd Hand · 2024',r('new-icons-club-magazine-2',1,10))],
  [('Second Hand','Kleiderei, MatchYourStyle'),('Produktion','Kilian Amrehn'),('Creative Director','Ann-Kathrin Templin'),('Styling','Jacqueline Tamm'),('Hair & Make-up','Serife Maria Rosewood, Hanna Fuchs'),('Models','Marie, Louis, Lia, Paulus, Elisabeth, Linda, Nika, Lasse'),('Fotoassistenz','Fabian Podzuweit')],edge=('EDITORIAL','MAGAZIN'))
p('pnts','PNTS','Kampagnen','Campaigns','2022 bis 2023','The Wants Social',
  [S('2022','2022',r('pnts',1,7)),S('Noordwijk 2023','Noordwijk 2023',r('pnts',8,16))],
  [('Produktion','The Wants Social'),('Creative Direction','Wiebke Hennig, Anna Siepenkötter, Vera Evers'),('Styling','Johanna Löer, Catarina Brockhoff-Lingke, Ricarda Saemann'),('Hair & Make-up','Melanie Bulu'),('DOP','Christian Hülsmeyer, Paul Mess'),('Fotoassistenz','Eno de Witt'),('Talents','Chelsey Weimar, Aline Gomes, Amelie Fiebach'),('Foto','Kilian Amrehn')],color='#1c1b1a')
p('appelrathcuepper','AppelrathCüpper','Kampagne','Campaign','2022','AppelrathCüpper',[S('','',r('appelrathcuepper',1,9))],
  [('Produktion','Mariann Reitz'),('Creative Director','Alexandra Specht'),('Fotoassistenz','Jonas Boltze'),('Styling','Lisa Bräuer'),('Models','Maren Thelen, Signe'),('Hair & Make-up','Patricia Irsinger'),('Foto','Kilian Amrehn')],
  'Spiel mit Spiegeln.','Playing with mirrors.')
p('marie-dahmen','Marie','Freie Strecke · Porträt','Personal series · Portrait','2022','',[S('','',r('marie-dahmen',1,9))],
  [('Produktion','Kilian Amrehn'),('Model','Marie Dahmen'),('Styling','Jacqueline Tamm'),('Hair & Make-up','Ilknur Gelme'),('Fotoassistenz','Fabian Podzuweit')],edge=('FREIE STRECKE','ANALOG UND DIGITAL'))
p('the-wants','The Wants','Kampagne','Campaign','2020','The Wants Social',[S('','',r('the-wants',1,10))],
  [('Agentur','The Wants Social'),('Produktion','Anna Siepenkötter'),('Creative Director','Karla Jenders'),('Model','Mona Lillian'),('Hair & Make-up','Melanie Bulu'),('Fotoassistenz','Fabian Podzuweit'),('Foto','Kilian Amrehn')])
p('bundesliga','Bundesliga','Sport · DFL','Sport · DFL','2023 bis 2025','DFL',[S('','',r('bundesliga',1,29))],[('Auftrag','DFL'),('Foto','Kilian Amrehn')],
  'Für die DFL war ich in vielen Stadien und durfte Spiele direkt vom Spielfeldrand erleben. Stadien sind beeindruckende Orte. Der Sport auch, vor allem so nah dran.',
  'Working for the DFL has taken me to many stadiums, where I had the chance to experience matches right from the sidelines. Stadiums are impressive places, and so is the sport itself, especially when you are that close to the action.',
  edge=('SPORTFOTOGRAFIE','BUNDESLIGA'))

# Farbe des Bands (mit Farbpipette aus den Bildern der Arbeit genommen) und Bild(er) beim Aufklappen.
# Reihenfolge so, dass nie zwei ähnliche Farben nebeneinander stehen.
BAND=[('rock-fairyland','#6a1a44',[7]),('trish-reflections-of-identity','#0a8389',[6]),('scholl-iconic','#d0592b',['scholl-6']),
 ('pnts','#2f5878',[15]),('phiala','#ceb57d',[6,8,9]),('the-wants','#562b38',[4]),('peek-cloppenburg-x-ellesse','#99b4bc',[6]),
 ('ozean-der-stille','#5a1f1b',[11]),('monano-schmuck','#9eccd4',[5]),('niewiederleise','#6f6f41',[4,5,8]),('copenhagen-studios','#f09a9e',[2,12,9]),
 ('silent-escape','#2e4f56',[1,2,5]),('bundesliga','#d9b42c',[23]),('appelrathcuepper','#0d3a78',[2]),('marie-dahmen','#9a5530',[5]),
 ('synergy','#2f6f58',[1,2,3]),('new-icons-club-magazine','#c8182e',['new-icons-club-magazine-2-3','new-icons-club-magazine-6','new-icons-club-magazine-2-7'])]
for i,x in enumerate(P): x['seed']=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17][i]  # alte Position, damit die Bögen gleich bleiben
byslug={x['slug']:x for x in P}
assert len(BAND)==len(P), (len(BAND),len(P))
P=[]
for slug,col,ims in BAND:
    x=byslug[slug]; x['band']=col
    x['bandImgs']=[('w-'+i if isinstance(i,str) else f'w-{slug}-{i}') for i in ims]
    P.append(x)
json.dump(P,open(os.path.join(H,'arbeiten_content.json'),'w'),ensure_ascii=False,indent=1)
print(len(P))
