import math 
file='bigger_example.txt'
def read_file(file):
    with open(file) as f:
        contents=f.read()
    contents=contents.split('\n\n')
    villagers,songs,parties=contents[0].split('\n'),contents[1].split('\n'),contents[2].split('\n')
    villagers.remove('VILLAGERS')
    songs.remove('SONGS')
    parties.remove('PARTIES')
    parties.remove('')
    return villagers,songs,parties

def data_structure():
    villagers,songs,parties=read_file(file)
    list_villagers,list_songs,bards=[],[],[]
    for villager in villagers:
        if villager[-1] !=  '*':
           v={villager:set()}
           list_villagers.append(v)
        else:
             bards.append(villager)
    for song in songs:
           s={song:set()}
           list_songs.append(s)
    return list_villagers,list_songs,villagers,songs,parties,bards
#def learn():
    
"""def sing():
    villagers,songs,parties,bards=data_structure()
    #for i in range(len(parties)):"""
def hold_party():
    list_villagers,list_songs,villagers,songs,parties,bards=data_structure()
    songs.sort()
    bards_new=[]
    #print(villagers)
    for b in bards:
        bar=b.strip('*')
        bards_new.append(bar)
        #rint(bards_new)
    bards_set=set(bards_new)
    new=set()
    counter=0
    coop=0
    el=set()
    thresh=5
    attendees=[]
    for i in parties:
        party=i.split(',')
        party=set(party)
        #print("p set",list_villagers)
        #print("bard",bards_set)
        co=party&bards_set
        x=len(party)
        attendees.append(x)
        print(x)
        coop=+0
        #print(co)
        if len(co) != 0:
            counter+=1
            #print(counter,songs)
            new_song=songs.pop(0)
            for val in list_villagers:
                #print(val)
                for key,vali in val.items():
                    if key in party:
                        vali.add(new_song)
                        for  soo in list_songs:
                            for  sk, sv in soo.items():
                                if sk == new_song:
                                        sv.add(key)
                            
                        nos=len(vali)
                        if nos >= thresh:
                             #print(coop,key,"ch")
                             #temp_bard=villagers.rem(vali)
                             bards_set.add(key)
                            
             
        else:
            #print(party|bards_set))
            for village in list_villagers:
                #print(val)
                for keyy,vall in village.items():
                    if keyy in party:
                        #print(keyy,vall)
                        for i in vall:
                            #print(i)
                            el.add(i)
                        vall.update(el)
                        for  soo in list_songs:
                            for  sk, sv in soo.items():
                                if sk == i:
                                        sv.add(key)
                        #el.append(vall)
                        #print(keyy,vall
                        #print(el)
                    #print(keyy,vall)
        #print(list_songs)
    unheard=set()
    best={}
    for a in  list_songs:
            for x,y in a.items():
                best[x]=len(y)
                #best.update(tup)
                #print(x,len(y))
                if len(y)==0:
                        unheard.add(x)
    #print(best)
    so=sorted(best.items(),key=lambda x:x[1],reverse=True)
    print(so)
    print(bards_set,len(bards_set),len(villagers),"bset")
    avarage=math.ceil(sum(attendees)/len(attendees))
    print(avarage)
hold_party()
