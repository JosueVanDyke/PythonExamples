countKang = 2
countThomas = 4
countNowlin = 4
countHobbs = 2
countLuke = 4
countStonks = 0

quotesKang = \
    ["Hello!",
     "You are a lucky lady.",
     "You are a poor fella."]

quotesThomas = \
    ["Hello.",
     "You need more comments in that code there.",
     "Pay no attention to that professor behind the curtain!,",
     "More Foot = More Go. Less foot = Less Go.",
     "I just think this is WAY cool."]

quotesNowlin = \
    ["Howdy!",
     "Shout it out!",
     "It is your job to entertain me!",
     "Talk to me.",
     "I'm not your dad. You're not even in this class."]

quotesHobbs = \
    ["Hi!",
     "football",
     "The Steelers stink."]

quotesLuke = \
    ["Look at the results of the 2010 levy!!",
     "gonna be honest, I don’t know anything about the 2010 levy.",
     "Let's goooooo",
     "soccer.",
     "NO! Don't do it to 'em!!"]

quotesStonks = \
    ["Stonks"]

class CseQuotes:


    def __init__(self):
        print("Instantiated")


def action_Luke():

    global countLuke
    global quotesLuke

    print(quotesLuke[countLuke])
    if countLuke > 0:
        countLuke = countLuke - 1
    else:
        countLuke = len(quotesLuke) - 1

def action_Hobbs():

    global countHobbs
    global quotesHobbs

    print(quotesHobbs[countHobbs])
    if countHobbs > 0:
        countHobbs = countHobbs - 1
    else:
        countHobbs = len(quotesHobbs) - 1

def action_Nowlin():

    global countNowlin
    global quotesNowlin

    print(quotesNowlin[countNowlin])
    if countNowlin > 0:
        countNowlin = countNowlin - 1
    else:
        countNowlin = len(quotesNowlin) - 1

def action_Stonks():

    global countStonks
    global quotesStonks

    print(quotesStonks[countStonks])
    if countStonks > 0:
        countStonks = countStonks -1
    else:
        countStonks = len(quotesStonks) - 1

def action_Thomas():

    global countThomas
    global quotesThomas

    print(quotesThomas[countThomas])
    if countThomas > 0:
        countThomas = countThomas - 1
    else:
        countThomas = len(quotesThomas) - 1

def action_Kang():

    global countKang
    global quotesKang

    print(quotesKang[countKang])
    if countKang > 0:
        countKang = countKang - 1
    else:
        countKang = len(quotesKang) - 1