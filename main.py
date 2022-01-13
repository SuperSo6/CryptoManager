from turtle import st
import web_scrapping

def start(value):
    if value == 1:
        name = input('Nom de la crypto : ').lower()
        Dico_Link = {'amp':'amp',
                     'xrp':'xrp',
                     'grt':'the-graph',
                     'xlm':'stellar',
                     'mana':'decentraland',
                     'near':'near-protocol'}
        for nom in Dico_Link :
            if nom==name:
                link = Dico_Link[nom]
        print(f"Le cours actuel de {name.upper()} est : {web_scrapping.recherche(link)}")





if __name__=='__main__':
    print( '_________                        __       ____   ____      .__')                 
    print( '\_   ___ \_______ ___.__._______/  |_  ___\   \ /   /____  |  |  __ __   ____')  
    print( '/    \  \/\_  __ <   |  |\____ \   __\/  _ \   Y   /\__  \ |  | |  |  \_/ __ \ ')
    print( '\     \____|  | \/\___  ||  |_> >  | (  <_> )     /  / __ \|  |_|  |  /\  ___/') 
    print( ' \______  /|__|   / ____||   __/|__|  \____/ \___/  (____  /____/____/  \___  >')
    print( '        \/        \/     |__|                            \/                 \/ ')
    Liste_Actions = ['Tape 1 pour rechercher le cours de la crypto ']
    for i in Liste_Actions:
        print(i)
    val = int(input('Entrez une action '))
    start(val)