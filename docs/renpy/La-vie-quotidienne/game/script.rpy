# Activite Ren'Py - Unite 2 : La vie quotidienne

define prof = Character("Professeur")
define eleve = Character("Eleve")

image bg routine = "rutina.jpg"
image bg temps = "reloj-arena.jpg"

default score = 0

label start:

    $ score = 0

    scene bg routine
    with fade

    prof "Bienvenue dans l'activite de l'unite 2."
    prof "Aujourd'hui, tu vas distinguer l'imparfait et le passe compose dans une routine passee."
    eleve "Je dois choisir entre une habitude, une description ou une action ponctuelle."

    scene bg temps
    with dissolve

    prof "Question 1. Complete la phrase : Quand j'etais petit, je ___ toujours a huit heures."

    menu:
        "me levais":
            $ score += 1
            prof "Tres bien. 'Toujours' indique une habitude dans le passe : on utilise l'imparfait."
        "me suis leve":
            prof "Pas ici. Pour une habitude repetee dans le passe, on utilise l'imparfait."

    prof "Question 2. Complete la phrase : Hier soir, je regardais la television quand tu ___."

    menu:
        "appelais":
            prof "Attention. L'appel est une action ponctuelle qui interrompt l'action en cours."
        "as appele":
            $ score += 1
            prof "Exact. L'action ponctuelle se met au passe compose."

    scene bg routine
    with dissolve

    prof "Question 3. Choisis la phrase correcte."

    menu:
        "Il faisait froid quand je suis sorti.":
            $ score += 1
            prof "Parfait. 'Il faisait froid' decrit le contexte, et 'je suis sorti' est l'action ponctuelle."
        "Il a fait froid quand je sortais.":
            prof "Cette phrase ne correspond pas bien au contraste contexte / action ponctuelle."

    prof "Question 4. Complete la phrase : Tous les samedis, nous ___ les courses."

    menu:
        "avons fait":
            prof "Pas exactement. 'Tous les samedis' exprime une repetition."
        "faisions":
            $ score += 1
            prof "Oui. Une action repetee dans le passe se met a l'imparfait."

    prof "Question 5. Complete la phrase : Soudain, le telephone ___."

    menu:
        "sonnait":
            prof "Ici, 'soudain' annonce une action ponctuelle."
        "a sonne":
            $ score += 1
            prof "Tres bien. Une action soudaine utilise le passe compose."

    scene bg temps
    with fade

    prof "Ton score est de [score] sur 5."

    if score == 5:
        prof "Excellent. Tu sais tres bien distinguer imparfait et passe compose."
    elif score >= 3:
        prof "Bien joue. Revise surtout les indices de temps comme 'toujours', 'tous les samedis' et 'soudain'."
    else:
        prof "Continue a t'entrainer. Retiens ceci : l'imparfait decrit ou repete, le passe compose raconte une action ponctuelle."

    prof "Fin de l'activite."

    return
