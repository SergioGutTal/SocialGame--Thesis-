'''
Created on Jun 10, 2012

@author: drazic_1
'''

import os
import simplejson as json
import urllib
import urllib2
import webbrowser
import nltk
from cgi import escape
import sqlite3

json_output = {
    "id": "WORDS",
    "data": {
        "$dim": 1,
        "$color": "#001eff"
    },
    "children": [
        {
            "id": "think",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 35,
                    "name": "i sure dont think these facts are lies."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 39,
                    "name": "in what fairytale land does priebus thinks we are at?!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 94,
                    "name": "i used to think the democratic party was a party of ideas. a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 113,
                    "name": "still for obama.. great discoveries we made with him ! i thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "think"
        },
        {
            "id": "love",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 91,
                    "name": "i love this!!!  obama 2012!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 154,
                    "name": "lovely couple."
                }
            ],
            "name": "love"
        },
        {
            "id": "help",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "help"
        },
        {
            "id": "ron",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 83,
                    "name": "here a troll there a troll everywhere a troll...why are you "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 135,
                    "name": "i believe james piedad is fucking moron.:)"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                }
            ],
            "name": "ron"
        },
        {
            "id": "give",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 146,
                    "name": "women have the right to go buy birth control. they do not ha"
                }
            ],
            "name": "give"
        },
        {
            "id": "money",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                }
            ],
            "name": "money"
        },
        {
            "id": "romney",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 136,
                    "name": "romney is a idiot in every sense of the word. he's make a te"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 137,
                    "name": "romney's an idiot!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 153,
                    "name": "ryan as vp for romney @_@ bunch of jokers!!! obama all the w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                }
            ],
            "name": "romney"
        },
        {
            "id": "back",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 68,
                    "name": "ivan, isn't your thought process a little backwards???"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 85,
                    "name": "trolls you turned left...please go back to your own page!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 155,
                    "name": "send these foul men back to the abyss"
                }
            ],
            "name": "back"
        },
        {
            "id": "one",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 3,
                    "name": "one of these charts is a lie. i wonder which?"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 12,
                    "name": "please notice that the 2 charts do not  measure the same thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 14,
                    "name": "funny when the chart here and the one posted by james piedad"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 23,
                    "name": "when the people who are no longer in the labor force (they a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 34,
                    "name": "seriously? do they realize we have it on video? in printed t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 38,
                    "name": "reince priebus?  isn't that the name of one of those old lux"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 45,
                    "name": "their attacks have been proven....the attack on religion is "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 76,
                    "name": "stfu eric, no one wants to hear your slanted refucklican bul"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 92,
                    "name": "i find it interesting that you only wish to hear criticism w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 122,
                    "name": "@adam ..... okay, you get out there and tell em how it's don"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 139,
                    "name": "they're not the only ones...."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 140,
                    "name": "this is the one place where i drop the line.  every baby has"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                }
            ],
            "name": "one"
        },
        {
            "id": "go",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 2,
                    "name": "look at this chart from the dept of labor statistics. http:/"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 23,
                    "name": "when the people who are no longer in the labor force (they a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 30,
                    "name": "anything said by any gop member is utter nonsense -"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 32,
                    "name": "lol @ jon stafford.  i just got finished asking myself the s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 34,
                    "name": "seriously? do they realize we have it on video? in printed t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 47,
                    "name": "i have no problem seeing planned parenthood go to it's grave"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 53,
                    "name": "car pooled eight people today to the county courthouse...all"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 65,
                    "name": "chaney, goodman, schwerner, liuozzo."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 85,
                    "name": "trolls you turned left...please go back to your own page!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 87,
                    "name": "oh yeah, i'm fired up and ready to go!!!!! obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 105,
                    "name": "exactly!  what kind of economy are you going to have with un"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 116,
                    "name": "gobama!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 146,
                    "name": "women have the right to go buy birth control. they do not ha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 152,
                    "name": "brent, you're doing good stuff. keep up the great work!"
                }
            ],
            "name": "go"
        },
        {
            "id": "see",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 1,
                    "name": "hey richard!!!!!!! did you see this?"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 47,
                    "name": "i have no problem seeing planned parenthood go to it's grave"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 128,
                    "name": "they seem to prefer dick sanitorom'splatform much better...?"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                }
            ],
            "name": "see"
        },
        {
            "id": "good",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 65,
                    "name": "chaney, goodman, schwerner, liuozzo."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 152,
                    "name": "brent, you're doing good stuff. keep up the great work!"
                }
            ],
            "name": "good"
        },
        {
            "id": "right",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 17,
                    "name": "right on eric waterman!! obama 2012!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 48,
                    "name": "<<<--for woman's rights......obama/biden 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 70,
                    "name": "felons don't have the right to vote.  more and more republic"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 130,
                    "name": "women's rights, and gay rights, should be a central focus in"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 133,
                    "name": "equal rights for all!!!:) vote dem 2012!!:)"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 140,
                    "name": "this is the one place where i drop the line.  every baby has"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 145,
                    "name": "or your supposed rights"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 146,
                    "name": "women have the right to go buy birth control. they do not ha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "right"
        },
        {
            "id": "democrats",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 61,
                    "name": "today, democrats, in pursuit of their socialist agenda, are "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 90,
                    "name": "obama 2012!!!! and allother democrats!!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                }
            ],
            "name": "democrats"
        },
        {
            "id": "another",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 81,
                    "name": "another term, yes he can!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                }
            ],
            "name": "another"
        },
        {
            "id": "need",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 23,
                    "name": "when the people who are no longer in the labor force (they a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 105,
                    "name": "exactly!  what kind of economy are you going to have with un"
                }
            ],
            "name": "need"
        },
        {
            "id": "still",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 69,
                    "name": "how sad this still happens in the year 2012. i was lucky eno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 113,
                    "name": "still for obama.. great discoveries we made with him ! i thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                }
            ],
            "name": "still"
        },
        {
            "id": "insurance",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "insurance"
        },
        {
            "id": "really",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 159,
                    "name": "the plutocrats really do have everything bass-akwards!  ...a"
                }
            ],
            "name": "really"
        },
        {
            "id": "even",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                }
            ],
            "name": "even"
        },
        {
            "id": "doesn't",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                }
            ],
            "name": "doesn't"
        },
        {
            "id": "republican",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 9,
                    "name": "if a republican accomplished half as much, they'd be screami"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 11,
                    "name": "so we are digging out of the hole left by republican traitor"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 51,
                    "name": "mlk was a model republican"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 60,
                    "name": "mlk was a republican..fyi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 70,
                    "name": "felons don't have the right to vote.  more and more republic"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 73,
                    "name": "http://www.politifact.com/rhode-island/statements/2012/jan/2"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 74,
                    "name": "yes, and vote like dr. king.  he was a registered republican"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 103,
                    "name": "republican healthcare plan: don't get sick."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "republican"
        },
        {
            "id": "want",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 33,
                    "name": "people will believe any lie they want"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 76,
                    "name": "stfu eric, no one wants to hear your slanted refucklican bul"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 97,
                    "name": "@ bella: owebama has two full years to pass everything he wa"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 110,
                    "name": "lol, the machine wants you to fight about parties... thats w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "want"
        },
        {
            "id": "he's",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 136,
                    "name": "romney is a idiot in every sense of the word. he's make a te"
                }
            ],
            "name": "he's"
        },
        {
            "id": "pay",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "pay"
        },
        {
            "id": "make",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 136,
                    "name": "romney is a idiot in every sense of the word. he's make a te"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                }
            ],
            "name": "make"
        },
        {
            "id": "don't",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 12,
                    "name": "please notice that the 2 charts do not  measure the same thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 70,
                    "name": "felons don't have the right to vote.  more and more republic"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 82,
                    "name": "@robert, maybe you should read marx before using your voice "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 103,
                    "name": "republican healthcare plan: don't get sick."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 123,
                    "name": "oh adam, don't hate! celebrate!!  your president is amazing!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "don't"
        },
        {
            "id": "-",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 24,
                    "name": "sounds like diana is talking t-bagger hate speech facts r th"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 30,
                    "name": "anything said by any gop member is utter nonsense -"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 48,
                    "name": "<<<--for woman's rights......obama/biden 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 73,
                    "name": "http://www.politifact.com/rhode-island/statements/2012/jan/2"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 84,
                    "name": "you marketed yourself as anti-establishment. you're no diffe"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 132,
                    "name": "yup - chicks will believe anything."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 147,
                    "name": "totally untrue - typical democratic socialist party drivel"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 148,
                    "name": "hey piedad - obviously you are a less than intelligent male."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 159,
                    "name": "the plutocrats really do have everything bass-akwards!  ...a"
                }
            ],
            "name": "-"
        },
        {
            "id": ",",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 4,
                    "name": "probably yours piedad, but you already knew that didn't you"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 7,
                    "name": "88 million people have dropped out of the work force, so the"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 9,
                    "name": "if a republican accomplished half as much, they'd be screami"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 15,
                    "name": "amen, jim."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 23,
                    "name": "when the people who are no longer in the labor force (they a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 32,
                    "name": "lol @ jon stafford.  i just got finished asking myself the s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 34,
                    "name": "seriously? do they realize we have it on video? in printed t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 43,
                    "name": "no, the priebus is a hybrid from honda, or is it toyota?"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 46,
                    "name": "mitt promises not only to defund planned parenthood, but to "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 55,
                    "name": "in the spirit of dr. king, find an occupy group near you and"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 61,
                    "name": "today, democrats, in pursuit of their socialist agenda, are "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 65,
                    "name": "chaney, goodman, schwerner, liuozzo."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 68,
                    "name": "ivan, isn't your thought process a little backwards???"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 74,
                    "name": "yes, and vote like dr. king.  he was a registered republican"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 76,
                    "name": "stfu eric, no one wants to hear your slanted refucklican bul"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 78,
                    "name": "and my voice says, \"buh bye, marxist, barry owebama...\""
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 81,
                    "name": "another term, yes he can!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 82,
                    "name": "@robert, maybe you should read marx before using your voice "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 83,
                    "name": "here a troll there a troll everywhere a troll...why are you "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 87,
                    "name": "oh yeah, i'm fired up and ready to go!!!!! obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 92,
                    "name": "i find it interesting that you only wish to hear criticism w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 98,
                    "name": "remember, for every voice that changes the world there are m"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 99,
                    "name": "oh puleeze, robert.  never heard of a filibuster???? never h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 105,
                    "name": "exactly!  what kind of economy are you going to have with un"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 106,
                    "name": "4 more years, then it is hillary's turn!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 110,
                    "name": "lol, the machine wants you to fight about parties... thats w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 121,
                    "name": "ah, professional troll william j. green is here, now we can "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 122,
                    "name": "@adam ..... okay, you get out there and tell em how it's don"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 123,
                    "name": "oh adam, don't hate! celebrate!!  your president is amazing!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 127,
                    "name": "yes, yes keep it up, so that santorum can beat your ass"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 130,
                    "name": "women's rights, and gay rights, should be a central focus in"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 140,
                    "name": "this is the one place where i drop the line.  every baby has"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 152,
                    "name": "brent, you're doing good stuff. keep up the great work!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 156,
                    "name": "repubs mean bankruptcy, unemployment, corruption, discrimina"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 159,
                    "name": "the plutocrats really do have everything bass-akwards!  ...a"
                }
            ],
            "name": ","
        },
        {
            "id": "vote",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 34,
                    "name": "seriously? do they realize we have it on video? in printed t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 58,
                    "name": "voter safety is always of critical importance"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 70,
                    "name": "felons don't have the right to vote.  more and more republic"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 74,
                    "name": "yes, and vote like dr. king.  he was a registered republican"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 118,
                    "name": "you can't fix stupity you vote it out president obama landsl"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 133,
                    "name": "equal rights for all!!!:) vote dem 2012!!:)"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "vote"
        },
        {
            "id": "also",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                }
            ],
            "name": "also"
        },
        {
            "id": "much",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 9,
                    "name": "if a republican accomplished half as much, they'd be screami"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 128,
                    "name": "they seem to prefer dick sanitorom'splatform much better...?"
                }
            ],
            "name": "much"
        },
        {
            "id": "health",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 103,
                    "name": "republican healthcare plan: don't get sick."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "health"
        },
        {
            "id": "take",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 92,
                    "name": "i find it interesting that you only wish to hear criticism w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                }
            ],
            "name": "take"
        },
        {
            "id": "way",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 26,
                    "name": "what the hell kind of name is \"reince priebus\" anyway?  it p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 58,
                    "name": "voter safety is always of critical importance"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 64,
                    "name": "a memory always present!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 153,
                    "name": "ryan as vp for romney @_@ bunch of jokers!!! obama all the w"
                }
            ],
            "name": "way"
        },
        {
            "id": "new",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 4,
                    "name": "probably yours piedad, but you already knew that didn't you"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "new"
        },
        {
            "id": "get",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 46,
                    "name": "mitt promises not only to defund planned parenthood, but to "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 63,
                    "name": "greatness isn't  mean do great things but by doing simple th"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 103,
                    "name": "republican healthcare plan: don't get sick."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 121,
                    "name": "ah, professional troll william j. green is here, now we can "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 122,
                    "name": "@adam ..... okay, you get out there and tell em how it's don"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "get"
        },
        {
            "id": "many",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "many"
        },
        {
            "id": "gop",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 30,
                    "name": "anything said by any gop member is utter nonsense -"
                }
            ],
            "name": "gop"
        },
        {
            "id": "2012",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 17,
                    "name": "right on eric waterman!! obama 2012!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 48,
                    "name": "<<<--for woman's rights......obama/biden 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 57,
                    "name": "great work beverly !!  obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 69,
                    "name": "how sad this still happens in the year 2012. i was lucky eno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 73,
                    "name": "http://www.politifact.com/rhode-island/statements/2012/jan/2"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 87,
                    "name": "oh yeah, i'm fired up and ready to go!!!!! obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 90,
                    "name": "obama 2012!!!! and allother democrats!!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 91,
                    "name": "i love this!!!  obama 2012!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 107,
                    "name": "yes we will!\n\nobama2012!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 109,
                    "name": "the campaign has \"officially\" started today !!!.....obama 20"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 118,
                    "name": "you can't fix stupity you vote it out president obama landsl"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 133,
                    "name": "equal rights for all!!!:) vote dem 2012!!:)"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 134,
                    "name": "obama2012!!!!!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 156,
                    "name": "repubs mean bankruptcy, unemployment, corruption, discrimina"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                }
            ],
            "name": "2012"
        },
        {
            "id": "it.",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 6,
                    "name": "86 and 87 when \"free checking\" came along. not that it matte"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 46,
                    "name": "mitt promises not only to defund planned parenthood, but to "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 95,
                    "name": "@ mike your so full of shit... just saying"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "it."
        },
        {
            "id": "obama",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 17,
                    "name": "right on eric waterman!! obama 2012!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 48,
                    "name": "<<<--for woman's rights......obama/biden 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 57,
                    "name": "great work beverly !!  obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 84,
                    "name": "you marketed yourself as anti-establishment. you're no diffe"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 87,
                    "name": "oh yeah, i'm fired up and ready to go!!!!! obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 90,
                    "name": "obama 2012!!!! and allother democrats!!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 91,
                    "name": "i love this!!!  obama 2012!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 107,
                    "name": "yes we will!\n\nobama2012!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 109,
                    "name": "the campaign has \"officially\" started today !!!.....obama 20"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 113,
                    "name": "still for obama.. great discoveries we made with him ! i thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 116,
                    "name": "gobama!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 118,
                    "name": "you can't fix stupity you vote it out president obama landsl"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 134,
                    "name": "obama2012!!!!!!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 153,
                    "name": "ryan as vp for romney @_@ bunch of jokers!!! obama all the w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 156,
                    "name": "repubs mean bankruptcy, unemployment, corruption, discrimina"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 100,
                    "name": "obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 28,
                    "name": "obama 2012"
                }
            ],
            "name": "obama"
        },
        {
            "id": "republicans",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "republicans"
        },
        {
            "id": "jobs",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 12,
                    "name": "please notice that the 2 charts do not  measure the same thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 156,
                    "name": "repubs mean bankruptcy, unemployment, corruption, discrimina"
                }
            ],
            "name": "jobs"
        },
        {
            "id": "government",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 146,
                    "name": "women have the right to go buy birth control. they do not ha"
                }
            ],
            "name": "government"
        },
        {
            "id": "it's",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 46,
                    "name": "mitt promises not only to defund planned parenthood, but to "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 47,
                    "name": "i have no problem seeing planned parenthood go to it's grave"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 82,
                    "name": "@robert, maybe you should read marx before using your voice "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 97,
                    "name": "@ bella: owebama has two full years to pass everything he wa"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 98,
                    "name": "remember, for every voice that changes the world there are m"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 122,
                    "name": "@adam ..... okay, you get out there and tell em how it's don"
                }
            ],
            "name": "it's"
        },
        {
            "id": "mitt",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 46,
                    "name": "mitt promises not only to defund planned parenthood, but to "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "mitt"
        },
        {
            "id": "never",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 6,
                    "name": "86 and 87 when \"free checking\" came along. not that it matte"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 98,
                    "name": "remember, for every voice that changes the world there are m"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 99,
                    "name": "oh puleeze, robert.  never heard of a filibuster???? never h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                }
            ],
            "name": "never"
        },
        {
            "id": "like",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 24,
                    "name": "sounds like diana is talking t-bagger hate speech facts r th"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 38,
                    "name": "reince priebus?  isn't that the name of one of those old lux"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 49,
                    "name": "reince priebus sound like a disease"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 50,
                    "name": "boy could we use him today!!!  and about 10 more just like h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 74,
                    "name": "yes, and vote like dr. king.  he was a registered republican"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 77,
                    "name": "hello! this is an experiment, an experiment to show the supp"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 143,
                    "name": "i didn't vote for him when he ran for governor in mass.  nev"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "like"
        },
        {
            "id": "every",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 83,
                    "name": "here a troll there a troll everywhere a troll...why are you "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 88,
                    "name": "have any of you watched the c-span in the last 4 years?  our"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 97,
                    "name": "@ bella: owebama has two full years to pass everything he wa"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 98,
                    "name": "remember, for every voice that changes the world there are m"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 136,
                    "name": "romney is a idiot in every sense of the word. he's make a te"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 140,
                    "name": "this is the one place where i drop the line.  every baby has"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 159,
                    "name": "the plutocrats really do have everything bass-akwards!  ...a"
                }
            ],
            "name": "every"
        },
        {
            "id": "know",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 12,
                    "name": "please notice that the 2 charts do not  measure the same thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "know"
        },
        {
            "id": "party",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 83,
                    "name": "here a troll there a troll everywhere a troll...why are you "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 94,
                    "name": "i used to think the democratic party was a party of ideas. a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 147,
                    "name": "totally untrue - typical democratic socialist party drivel"
                }
            ],
            "name": "party"
        },
        {
            "id": "president",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 118,
                    "name": "you can't fix stupity you vote it out president obama landsl"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 123,
                    "name": "oh adam, don't hate! celebrate!!  your president is amazing!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 136,
                    "name": "romney is a idiot in every sense of the word. he's make a te"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "president"
        },
        {
            "id": "believe",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 33,
                    "name": "people will believe any lie they want"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 112,
                    "name": "another propaganda speech by president algae aka president p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 132,
                    "name": "yup - chicks will believe anything."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 135,
                    "name": "i believe james piedad is fucking moron.:)"
                }
            ],
            "name": "believe"
        },
        {
            "id": "people",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 7,
                    "name": "88 million people have dropped out of the work force, so the"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 23,
                    "name": "when the people who are no longer in the labor force (they a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 33,
                    "name": "people will believe any lie they want"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 53,
                    "name": "car pooled eight people today to the county courthouse...all"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 99,
                    "name": "oh puleeze, robert.  never heard of a filibuster???? never h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "people"
        },
        {
            "id": "must",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                }
            ],
            "name": "must"
        },
        {
            "id": "going",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 105,
                    "name": "exactly!  what kind of economy are you going to have with un"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                }
            ],
            "name": "going"
        },
        {
            "id": "great",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 57,
                    "name": "great work beverly !!  obama 2012"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 63,
                    "name": "greatness isn't  mean do great things but by doing simple th"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 113,
                    "name": "still for obama.. great discoveries we made with him ! i thi"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 152,
                    "name": "brent, you're doing good stuff. keep up the great work!"
                }
            ],
            "name": "great"
        },
        {
            "id": "would",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 29,
                    "name": "maybe he wouldn't be such a dick if his name wasn't \"reince "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 89,
                    "name": "i wouldn't have turned left if things hadn't continued to tu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "would"
        },
        {
            "id": "country",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 42,
                    "name": "people born with a silver spoon get names like that, you kno"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 89,
                    "name": "i wouldn't have turned left if things hadn't continued to tu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 97,
                    "name": "@ bella: owebama has two full years to pass everything he wa"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 130,
                    "name": "women's rights, and gay rights, should be a central focus in"
                }
            ],
            "name": "country"
        },
        {
            "id": "could",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 37,
                    "name": "he was 15 before he could spell his name."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 50,
                    "name": "boy could we use him today!!!  and about 10 more just like h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 67,
                    "name": "i was shocked by his death, but not surprised.  mlk was too "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 119,
                    "name": "couldn't agree more!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 141,
                    "name": "all romney is doing is trying to copy santorum's strategy to"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                }
            ],
            "name": "could"
        },
        {
            "id": "well",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 75,
                    "name": "well.. that's bullshit"
                }
            ],
            "name": "well"
        },
        {
            "id": "say",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 7,
                    "name": "88 million people have dropped out of the work force, so the"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 73,
                    "name": "http://www.politifact.com/rhode-island/statements/2012/jan/2"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 78,
                    "name": "and my voice says, \"buh bye, marxist, barry owebama...\""
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 95,
                    "name": "@ mike your so full of shit... just saying"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 129,
                    "name": "if you're a woman and support the republican party, you're b"
                }
            ],
            "name": "say"
        },
        {
            "id": "us",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 6,
                    "name": "86 and 87 when \"free checking\" came along. not that it matte"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 8,
                    "name": "james, if i read your chart right, there's only a 3 1/2%  di"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 9,
                    "name": "if a republican accomplished half as much, they'd be screami"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 16,
                    "name": "data is data and is used to spin positions.  1 chart reflect"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 26,
                    "name": "what the hell kind of name is \"reince priebus\" anyway?  it p"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 29,
                    "name": "maybe he wouldn't be such a dick if his name wasn't \"reince "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 32,
                    "name": "lol @ jon stafford.  i just got finished asking myself the s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 34,
                    "name": "seriously? do they realize we have it on video? in printed t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 38,
                    "name": "reince priebus?  isn't that the name of one of those old lux"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 39,
                    "name": "in what fairytale land does priebus thinks we are at?!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 40,
                    "name": "reince priebus lies!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 43,
                    "name": "no, the priebus is a hybrid from honda, or is it toyota?"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 49,
                    "name": "reince priebus sound like a disease"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 50,
                    "name": "boy could we use him today!!!  and about 10 more just like h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 53,
                    "name": "car pooled eight people today to the county courthouse...all"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 56,
                    "name": "mlk jr. is the only man who died long before i was even born"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 61,
                    "name": "today, democrats, in pursuit of their socialist agenda, are "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 62,
                    "name": "and yet atlanta just named street after him"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 66,
                    "name": "finally a real post from the democrats. dr. king was a repub"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 79,
                    "name": "my voice, my vote, and my love of/for country will fire the "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 82,
                    "name": "@robert, maybe you should read marx before using your voice "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 84,
                    "name": "you marketed yourself as anti-establishment. you're no diffe"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 94,
                    "name": "i used to think the democratic party was a party of ideas. a"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 95,
                    "name": "@ mike your so full of shit... just saying"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 96,
                    "name": "@ ana: i have read marx. i've also read another of owebama's"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 99,
                    "name": "oh puleeze, robert.  never heard of a filibuster???? never h"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 108,
                    "name": "amazing speech, amazing president! paul ryan wishes he could"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 111,
                    "name": "president barack hussein obama continues to gamble on green "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 124,
                    "name": "the republicans have been out of touch therefore we must re-"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 130,
                    "name": "women's rights, and gay rights, should be a central focus in"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 144,
                    "name": "dont quite understand your hatred toward men... but either w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 148,
                    "name": "hey piedad - obviously you are a less than intelligent male."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 157,
                    "name": "ha, i was just exposed to republican blathering on a website"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "us"
        },
        {
            "id": "keep",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 21,
                    "name": "look at the sources of both charts,please.  both are bls cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 61,
                    "name": "today, democrats, in pursuit of their socialist agenda, are "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 127,
                    "name": "yes, yes keep it up, so that santorum can beat your ass"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 142,
                    "name": "i like how we keep pretending the presidential election is s"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 152,
                    "name": "brent, you're doing good stuff. keep up the great work!"
                }
            ],
            "name": "keep"
        },
        {
            "id": "women",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 27,
                    "name": "can republicans be criminalized? they do more harm to freedo"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 130,
                    "name": "women's rights, and gay rights, should be a central focus in"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 146,
                    "name": "women have the right to go buy birth control. they do not ha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 156,
                    "name": "repubs mean bankruptcy, unemployment, corruption, discrimina"
                }
            ],
            "name": "women"
        },
        {
            "id": "can't",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 92,
                    "name": "i find it interesting that you only wish to hear criticism w"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 118,
                    "name": "you can't fix stupity you vote it out president obama landsl"
                }
            ],
            "name": "can't"
        },
        {
            "id": "time",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 2,
                    "name": "look at this chart from the dept of labor statistics. http:/"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 13,
                    "name": "mr piedad have you ever had an economics class? the usdl cha"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 97,
                    "name": "@ bella: owebama has two full years to pass everything he wa"
                }
            ],
            "name": "time"
        },
        {
            "id": "let",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 72,
                    "name": "no, renee pera...he was a republican!!!!  do you all like ch"
                }
            ],
            "name": "let"
        },
        {
            "id": "i'm",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 0,
                    "name": "wow, that obama, what a son of a bitch for creating jobs. by"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 6,
                    "name": "86 and 87 when \"free checking\" came along. not that it matte"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 87,
                    "name": "oh yeah, i'm fired up and ready to go!!!!! obama 2012!!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 110,
                    "name": "lol, the machine wants you to fight about parties... thats w"
                }
            ],
            "name": "i'm"
        },
        {
            "id": "page",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 83,
                    "name": "here a troll there a troll everywhere a troll...why are you "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 85,
                    "name": "trolls you turned left...please go back to your own page!"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 120,
                    "name": "do people like this page just to make rude comments? o_o\n(ob"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 150,
                    "name": "republicans just don't get the issues.  their ideology is fu"
                }
            ],
            "name": "page"
        },
        {
            "id": "care",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 10,
                    "name": "what's next a heath care plan that helps million, or a push "
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 20,
                    "name": "also: help get unemployment down faster! if you're unemploye"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 22,
                    "name": "if you want to know how well job creation is really going, g"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 31,
                    "name": "women's health? is that what we call it now, because it soun"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 41,
                    "name": "the truth is somewhere in the middle.  there is no constitut"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 44,
                    "name": "do republicans realize that women constitute the majority of"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 103,
                    "name": "republican healthcare plan: don't get sick."
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FF0000"
                    },
                    "id": 114,
                    "name": "president pondscum and the democrats healthcare policy, give"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#FFA500"
                    },
                    "id": 151,
                    "name": "i know this is a long question, but\u2026healthcare reform mandat"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 158,
                    "name": "thanks to these two a lot of americans will be seriously har"
                }
            ],
            "name": "care"
        },
        {
            "id": "that's",
            "data": {
                "$dim": 1,
                "$color": "#001eff"
            },
            "children": [
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 18,
                    "name": "lol. the gop has completely ignored this data for at least t"
                },
                {
                    "data": {
                        "$dim": 1,
                        "$color": "#00FF00"
                    },
                    "id": 75,
                    "name": "well.. that's bullshit"
                }
            ],
            "name": "that's"
        }
    ],
    "name": "SENTIMIENTO DE LAS PALABRAS"
}

mensajes = {}
for posts in json_output['children']:
    for post in posts['children']:
        if not mensajes.has_key(post["id"]):
            #mensajes[post["id"]].append(post['data']['$color'])
            mensajes[post["id"]] = [post['data']['$color'],post["name"]]  
        #else:
         #   mensajes[post["id"]] = [post['data']['$color']]
sentimiento = {'neutral':0,'positivo':0,'negativo':0}
for mensaje in mensajes.items():
    print mensaje
    if '#FFA500' in mensaje[1]:
        sentimiento['neutral']+=1
    elif '#00FF00' in mensaje[1]:
        sentimiento['positivo']+=1
    elif '#FF0000' in mensaje[1]:
        sentimiento['negativo']+=1    
print sentimiento
    
#print post["id"], post['data']['$color']