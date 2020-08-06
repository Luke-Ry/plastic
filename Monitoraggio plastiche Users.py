tweets = []
with open('Tweet hydrated/plasticpollution hydrated.jl', 'rb') as f:
    for item in json_lines.reader(f):
        tweets.append(item)
print(len(tweets))


#estraggo gli utenti
utenti = {} 
pp=0
for wl in tweets:
    pp+=1
    ids = wl["user"]["id_str"]
    if ids not in utenti:
        utenti[ids] = {}
        utenti[ids]["screen_name"] = wl["user"]["screen_name"]
        utenti[ids]["followers"] = wl["user"]["followers_count"]
        utenti[ids]["friends"] = wl["user"]["friends_count"]
        utenti[ids]["numero_tweet"] = 1
        utenti[ids]["numero_retweet"] = wl["retweet_count"]
    else:
        utenti[ids]["numero_tweet"] += 1
        utenti[ids]["numero_retweet"] += wl["retweet_count"] 
    print(pp)
print(len(prova))

#controllo che il conteggio sia giusto
s=0
for i in prova:
    s+=i["tweet_count"]
print(s)
