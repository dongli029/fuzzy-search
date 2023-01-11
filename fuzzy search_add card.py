import re
import json
from fuzzywuzzy import process, fuzz

with open('support bank.json', encoding="utf-8") as f:
    bank_card = json.load(f)

# print(bank_card)
pattern = r'[A-Za-z]'

# text_arrange
def text_arrange(input_name):
    for i in input_name:
        if not '\u4e00' <= i <= '\u9fa5':
            for T in re.findall(pattern, input_name):
                t = T.lower()
                input_name = input_name.replace(T, t)
                after_name = input_name
            return after_name
    else:
        after_name = input_name
        return after_name

# bank list
b_name = []
for j in bank_card.keys():
    b_name.append(j)
print("bank list =", b_name)
while True:
    try:
        input_name = input('please input bank name: ')
        # print(input_name, type(input_name))
        if len(input_name) < 2:
            print('wrong!,please enter 2 text at least')
            continue
        else:
            input_name = input_name.replace(' ', '')
            bank_name = text_arrange(input_name)
            print("input bank name=", bank_name)
            # maybe_bank
            maybe_bank = process.extract(bank_name, b_name, limit=3, scorer=fuzz.token_sort_ratio)
            # print(("maybe_bank=", maybe_bank))
            bank = []
            for i in maybe_bank:
                if i[1] >= 60:
                    bank.append(i[0])
            # print(bank)
            if len(bank) == 0:
                continue
            elif len(bank) == 1:
                print("Bank that you want to add card:", bank[0])
                pick_bank = bank[0]
            else:
                print("maybe bank =", bank)
                while True:
                    again = input("pls refer to the list & enter full bank name:")
                    if again in bank:
                        pick_bank = again
                        print("Bank that you want to add card:", pick_bank)
                        break
                    else:
                        continue
            # print(pick_bank)
            while True:
                try:
                    cd_name = []
                    for k in bank_card[pick_bank]:
                        cd_name.append(k)
                    print("Cards that",pick_bank,"offered =", cd_name)
                    input_card = input('pls input card\'s name that you want to add :')
                    input_card = input_card.replace(' ', '')
                    card_name = text_arrange(input_card)
                    print("card\'s name that you enter =", card_name)
                    maybe_card = process.extract(card_name, cd_name, limit=3, scorer=fuzz.partial_ratio)
                    # print(("maybe_card=", maybe_card))
                    card = []
                    for i in maybe_card:
                        if i[1] >= 80:
                            card.append(i[0])
                    # print(card)
                    if len(card) == 0:
                        continue
                    elif len(card) == 1:
                        print("card that you want to add:", card[0])
                        break
                    else:
                        print("Cards that you may want to add =", card)
                        while True:
                            card_again = input("pls refer to the list & enter full card name:")
                            if card_again in card:
                                pick_card = card_again
                                print("card that you want to add:", pick_card)
                                break
                            else:
                                continue
                    break
                except UnboundLocalError as error_name:
                    # print(error_name)
                    print("wrong text, pls enter again")
            break
    except UnboundLocalError as error_name:
        # print(error_name)
        print("wrong text, pls enter again")
        continue