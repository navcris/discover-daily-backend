

KEYWORDS = [
    "harris", "trump", 'russia', 'ukraine', 'digvid', 'relationship', 'health', 'welz', 'ukrainian', 'west bank', 'kidnap'
    'drug', 'riot', 'biden', 'Ukraine', 'Trump', 'Israel', 'loan', 'marriage', 'Ukrainian', 'Biden', '- BBC Sport'
    "walz", "donald", "kamala", 'democrat', 'republican', 'govenor', 'GOP', 'DNC', 'death', 'israel', 'gaza',
    'palestine', 'shot', 'ammo', 'killing', 'attack', 'iraq', 'iran', 'afghanistan', 'troops'
    "politics", "election", "government", "war", "violence", "crime", "drugs", 
    "alcohol", "sex", "scandal", "protest", "terrorism", "abuse", "murder", 
    "assault", "weapon",  "hate", "racism", "discrimination", "gang",  "rape", "kidnap", "extremism", "porn", "nudity", "genocide", 
    "torture", "suicide", "bullying", "harassment", "prostitution", "trafficking", 
    "explosion", "massacre", "hostage", "riot", "anarchy", "dictator", "corruption", 
    "bribery", "fraud", "embezzlement", "money laundering", "homicide", "manslaughter", 
    "arson", "vandalism", "looting", "smuggling", "cybercrime", "hacker", "pedophile", 
    "incest", "molestation", "abduction", "stalking", "domestic violence", "child abuse", 
    "hate speech", "lynching", "extortion", "blackmail", "assassination", "execution", 
    "witchcraft", "satanism", "cult",  "blasphemy", "heresy", 
    "infidelity", "adultery", "fornication", "profanity", "obscenity", "slavery", 
    "human trafficking", "forced labor", "child labor", "exploitation", "terrorist", 
    "militant", "insurgent", "rebel", "guerrilla", "coup", "uprising", "revolution", 
    "civil war", "martial law", "martyr", "radical", "extremist", "fundamentalist", 'trans', 'HIV'
]



def filtered_urls(all_urls):
    filtered_url =[]
    for url in all_urls:
        check = True
        for keyword in KEYWORDS:
            if keyword in url:
                check = False
                break
        if check == True and url not in filtered_url:
            filtered_url.append(url)

    return filtered_url
