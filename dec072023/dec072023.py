from collections import Counter
import pandas as pd


df = pd.read_csv("data.txt", sep=" ", names=["hands", "bid"])

def replaceJ(hand):
    if 'J' in hand:
        without_J = hand.replace('J', '')
        if without_J: 
            most_frequent_char = max(set(without_J), key=without_J.count)
            val = hand.replace('J', most_frequent_char)
            if hand == "KTJJT":
                print(hand, val, most_frequent_char)
            return val
    return hand

df['newHands'] = df['hands'].apply(replaceJ)

print(df)

fiveOfKind = []
fourOfKind = []
fullHouseOfKind = []
threeOfKind = []
twoPairOfKind = []
onePairOfKind = []
highCardOfKind = []

# for index, row in df.iterrows():
#     if row["hands"].nunique() == 1:
#         fiveOfKind.append(row["hands"])

# 198209546

fiveOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 1)]

fourOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 2 and any(x.count(char) == 4 for char in set(x)))]

fullHouseOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 2 and any(x.count(char) == 3 for char in set(x)))]

threeOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 3 and  any(x.count(char) == 3 for char in set(x)))]
# threeOfKind = threeOfKind[threeOfKind['newHands'].apply(lambda x: any(x.count(char) == 2 for char in set(x)))]

twoPairOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 3 and any(x.count(char) == 2 for char in set(x)))]

onePairOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 4 and any(x.count(char) == 2 for char in set(x)))]

highCardOfKind = df[df['newHands'].apply(lambda x: len(set(x)) == 5)]

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
priorities = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}

def assignPriority(hand):
    output = [priorities[card] for card in hand]
    return output

fiveOfKindPrioritized = fiveOfKind.sort_values(by='hands', key = lambda x: x.map(assignPriority))
fourOfKindPrioritized = fourOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))
fullHouseOfKindPrioritized = fullHouseOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))
threeOfKindPrioritized = threeOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))
twoPairOfKindPrioritized = twoPairOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))
onePairOfKindPrioritized = onePairOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))
highCardOfKindPrioritized = highCardOfKind.sort_values(by='hands', key=lambda x: x.map(assignPriority))


print(fiveOfKindPrioritized, ".")
print("*"*100)
print(fourOfKindPrioritized, ".")
print("*"*100)
print(threeOfKindPrioritized, ".")
print("*"*100)
print(twoPairOfKindPrioritized, ".")
print("*"*100)
print(onePairOfKindPrioritized, ".")
print("*"*100)
print(highCardOfKindPrioritized, ".")
print("*"*100)


rank = 1
kinds = [highCardOfKindPrioritized, onePairOfKindPrioritized, twoPairOfKindPrioritized, threeOfKindPrioritized, fullHouseOfKindPrioritized,  fourOfKindPrioritized, fiveOfKindPrioritized]
output = None

for kind in kinds:
    for index, row in kind.iterrows():
        bidVal = int(row["bid"])
        if not output:
            output = bidVal
        else:
            output += bidVal * rank
        rank += 1

print(output)