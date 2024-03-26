define y = Character("You")
define a = Character("Fish-Finder")

define cen = Character(None, what_xalign=0.5, what_text_align=0.5)

label bad_end:
    y "I'm too tired for this."
    "You slap your phone on the table and throw your head onto your pillow."
    "BAD(?) ENDING"
    return

label start:

    $ FinnDone = False
    $ IsoDone = False
    $ CohoDone = False
    $ ScuttleDone = False
    $ DollyDone = False
    $ CallymariDone = False

    scene bg room

    y "It's been a long day."

    y "Work has been overwhelming, and the wages are cut slim."

    y "I always know what cheers me up!"

    y "The app store on my unnamed proprietary phone!"

    "You open the app store, and see something quite peculiar..."

    y "FishFinder? What the fuck is that?"

    "The icon is an aqua blue fish, with a clipart love heart adjacent."

menu:
    "What should I do?"

    "Install FishFinder":
        y "Man, why am I doing this?"

    "Who do you think I am?":
        jump bad_end

label after_menu:

    "You wait until the app downloads."
    "It only takes a minute, despite your shitty data plan."
    y "Let's see what this is all about."
    "You open the app to a splash screen and a sign-in page."
    $ player_name = renpy.input("My name? (Default is Angler)")
    if player_name == "":
        $ player_name = "Angler"

    a "Hello, %(player_name)s!"
    a "Welcome to Fish-Finder!"
    a "Where all your fish-finding fantasies finally fall flat into reality!"
    y "How many 'f's can they fit into a sentence? Who wrote this, Mike Tyson?"
    a "Find a fishy partner here! There's no catch involved!"
    y "Ok, this is just getting unfunny."
    a "Nothing fishy about thi-"
    y "CUT TO IT ALREADY"
    a "We've used your GPS position to find a couple amazing canidates! Check them out!"
    jump choice

label choice:

menu:
        "Finn":
            if FinnDone == False:
                a"Finn; Species: Shark, Personality: Brash, Ill-tempered"
                show finn_neutral with easeinleft
                a "User's Bio:\n
                hi. im finn, my parents named me after that thing on my back haha"
                a "don't know what else to put here tho."
                a "i like sport and hunting"
            else:
                a"You have already been through that."
        "Iso":
            if IsoDone == False:
                a"Iso; Species: Isopod, Personality: Defensive, Oblivious."
            else:
                a"You have already been through that."
        "Coho":
            if CohoDone == False:
                a"Coho; Species: Salmon, Personality: Moron, Stupid, Joyful."
            else:
                a"You have already been through that."
        "Scuttle":
            if ScuttleDone == False:
                a"Scuttle; Species: Octopus, Personality: Curious, Doubtful."
            else:
                a"You have already been through that."
        "Dolly":
            if DollyDone == False:
                a"Dolly; Species: Dolphin, Personality: Trustworthy, Loyal, Kind (User found on 3 registers in this state)"
            else:
                a"You have already been through that."
        "Callymari":
            if CallymariDone == False:
                a"Callymari; Species: Squid, Personality: Serious, Professional."
            else:
                a"You have already been through that."