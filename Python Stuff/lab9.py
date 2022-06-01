def make_dictionary(n, s):
    score_dict = {}
    for i in range(len(n)):
        score_dict[n[i]] = s[i]
    return score_dict
def get_score(n, d):
    try:
        return d[n]
    except:
        return -1
def morse():
    morse_dictionary={' ': '/','A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'}
    text = input("Enter a message: ")
    text = text.upper()
    text2 = ''
    for letter in text:
        text2 += morse_dictionary[letter]
    return text2

def rank_suit_count(cards):
    r_dict = {}
    s_dict = {}
    for i in cards:
        rank = i[0]
        suit = i[1]
        if suit not in s_dict:
            s_dict[suit] = 1
        else:
            s_dict[suit] +=1
        if rank not in r_dict:
            r_dict[rank] = 1
        else:
            r_dict[rank] +=1  
    return r_dict, s_dict
        
def poker_hand(cards):
    t = rank_suit_count(cards)
    num = len(t[0])
    if nun == 5:
        
    if num == 4:
    if num == 3:
        count = 0
        for i in t[0]:
            
    if num == 2:
        count = 0
        for i in t[0].values():
            if i == 4:
                count+=1
        if count == 1:
            return "Four-of-a-kind"
        else:
            return "full-house"
        


    
