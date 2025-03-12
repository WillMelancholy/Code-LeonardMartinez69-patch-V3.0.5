#default e = Character("Eileen")
#default mistakes = 0
#default points = 0

#label start:
#    menu choice_menu:
#        "Right choice":
#            call right_choice
#        "Wrong choice":
            
#            call wrong_choice("choice_menu")
#        e "We end up here, when the played finally picked the correct choice."
#        e "The score is [points] points."
#        e "In total, there were [mistakes] wrong choices made so far."
#    return

#label right_choice:

#    $ points += 5

    
#    e "You made the right choice."

#    return

#label wrong_choice(menu_label):
#    $ points -= 1
#    $ mistakes += 1

#    e "You made the wrong choice."

#    call expression menu_label

#    return