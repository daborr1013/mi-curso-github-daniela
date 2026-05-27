# Activite Ren'Py - Unite 4 : Tu ou vous ?

define prof = Character("Professeur")
define appr = Character("Apprenant")

image bg paris = "paris.jpg"
image bg famille = "familia.jpg"
image bg reunion = "reunion.jpg"
image bg village = "pueblo.jpg"

default score = 0

label start:

    $ score = 0

    scene bg paris
    with fade

    prof "Bienvenue dans l'activite de l'unite 4."
    prof "Tu vas choisir le registre adapte a chaque situation : formel ou informel."
    appr "Je dois faire attention au contexte, a la politesse et au choix entre tu et vous."

    scene bg reunion
    with dissolve

    prof "Situation 1. Tu arrives a l'accueil d'un hotel et tu demandes de l'aide."

    menu:
        "Salut, tu peux m'aider ?":
            prof "Trop informel. A l'accueil d'un hotel, il vaut mieux utiliser 'vous'."
        "Bonjour, pourriez-vous m'aider ?":
            $ score += 1
            prof "Tres bien. C'est une formule polie et formelle."

    scene bg famille
    with dissolve

    prof "Situation 2. Tu parles avec un ami."

    menu:
        "Salut, tu vas bien ?":
            $ score += 1
            prof "Exact. Avec un ami, le registre informel est naturel."
        "Bonjour Monsieur, comment allez-vous ?":
            prof "Cette phrase est correcte, mais trop formelle pour un ami."

    scene bg reunion
    with dissolve

    prof "Situation 3. Tu parles avec ton professeur."

    menu:
        "Vous pouvez repeter, s'il vous plait ?":
            $ score += 1
            prof "Parfait. Avec un professeur, le vouvoiement est conseille."
        "Repete, s'il te plait.":
            prof "Cette phrase est trop directe dans ce contexte."

    scene bg paris
    with dissolve

    prof "Situation 4. Tu demandes ton chemin a une personne inconnue dans la rue."

    menu:
        "Excusez-moi, pourriez-vous m'indiquer la gare ?":
            $ score += 1
            prof "Tres bien. Avec une personne inconnue, on utilise une formule de politesse."
        "Dis, tu sais ou est la gare ?":
            prof "C'est trop familier pour parler a une personne inconnue."

    scene bg village
    with dissolve

    prof "Situation 5. Tu compares la ville et la campagne. Choisis la phrase la plus adaptee."

    menu:
        "La ville a un rythme plus rapide, la campagne est souvent plus calme.":
            $ score += 1
            prof "Exact. Cette phrase reprend bien le contenu culturel de l'unite."
        "En France, personne ne dit bonjour avant de parler.":
            prof "Non. Dans l'unite, on insiste au contraire sur l'importance de dire bonjour."

    scene bg paris
    with fade

    prof "Ton score est de [score] sur 5."

    if score == 5:
        prof "Excellent. Tu sais adapter ton langage selon la situation."
    elif score >= 3:
        prof "Bien joue. Continue a faire attention au contexte social."
    else:
        prof "Revise les differences entre registre formel et registre informel."

    prof "Fin de l'activite."

    return
