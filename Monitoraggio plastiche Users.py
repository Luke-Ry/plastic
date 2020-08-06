tweets = []
with open('Tweet hydrated/plasticpollution hydrated.jl', 'rb') as f:
    for item in json_lines.reader(f):
        tweets.append(item)
print(len(tweets))


#estraggo gli utenti
prova = []
utenti = []
pp=0
for wl in tweets:
    pp+=1
    if wl["user"]["id_str"] not in utenti:
        new = {}
        new["id"] = wl["user"]["id_str"]
        new["screen_name"] = wl["user"]["screen_name"]
        new["followers"] = wl["user"]["followers_count"]
        new["friends"] = wl["user"]["friends_count"]
        prova.append(new)
        utenti.append(wl["user"]["id_str"])
    print(pp)
print(len(prova))



#conto il numero di tweet per utente e il numero di retweet
pp = 0
for i in prova:
    pp+=1
    numero_tweet = 0
    numero_retweet = 0
    for t in tweets:
        if t["user"]["id_str"] == i["id"]:
            numero_tweet += 1
            numero_retweet += t["retweet_count"]
    i["tweet_count"] = numero_tweet
    i["retweet_count"] = numero_retweet
    print(pp)



#controllo che il conteggio sia giusto
s=0
for i in prova:
    s+=i["tweet_count"]
print(s)