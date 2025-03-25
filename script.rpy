init: 
    # Background images
    image bg laboratory = "images/Laboratory.png"
    image bg laboratory_table = "images/Laboratory.png"
    image bg classroom = "images/classroom.png"
    image bg classroom_pov = "images/classroom_pov.png"
    image bg menu = "images/MenuBG.png"
    image bg hallway = "images/Hallway1.png"

    # Irene images
    image irene speaking:
        "images/Irene_Speak.png"
        zoom 0.5
    image irene speak2:
        "images/Irene_Speak2.png"
        zoom 0.5
    image irene default:
        "images/Irene_Default.png"
        zoom 0.5

    # Titania images
    image titania speaking:
        "images/Titania_Speak.png"
        zoom 0.5
    image titania smile:
        "images/Titania_Smile.png"
        zoom 0.5
    image titania idle:
        "images/Titania_Idle.png"
        zoom 0.5

    # Chlory images
    image chlory speaking:
        "images/Chlory_Speak.png"
        zoom 0.525
        yalign -0.2
    image chlory confused:
        "images/Chlory_Confused.png"
        zoom 0.5
    image chlory idle:
        "images/Chlory_Idle.png"
        zoom 0.5
        yanchor 0.95
    image chlory happy:
        "images/Chlory_Happy.png"
        zoom 0.5
        yanchor 0.95

    # Yuranno images
    image yuranno speaking:
        "images/Yuranno_Speak.png"
        zoom 0.5
    image yuranno confused:
        "images/Yuranno_Confused.png"
        zoom 0.5
    image yuranno default:
        "images/Yuranno_Default.png"
        zoom 0.5

    # Additional character images
    image characA idle1:
        "images/characA_IDLE1.png"
        zoom 0.5
    image characA greet:
        "images/characAGREET.png"
        zoom 0.5

    # Icon placeholder
    image icon placeholder:
        "images/ICON_PLACEHOLDER.png"
        zoom 0.5

define e = Character("Eileen")
define player = Character("Player")
define A = Character("Irene")
define B = Character("Titania")
define C = Character("Chlory")
define D = Character("Yuranno")
define teacher = Character("Teacher")

define correct = "You got the right answer!"
define wrong = "You got the wrong answer!"

default materials = {
    "Wire": "images/wire.png",
    "Tongs": "images/tongs.png",
    "Bunsen Burner": "images/bunsen_burner.png",
    "Evaporating Dish": "images/evaporating_dish.png",
    "Magnesium": "images/magnesium.png",
    "Test Tubes": "images/test_tubes.png",
    "Test Tube Holder": "images/test_tube_holder.png",
    "Matches": "images/matches.png",
    "Copper (II) Carbonate (CuCO3)": "images/copper_carbonate.png",
    "5mL of 3M Hydrochloric Acid (HCl)": "images/hydrochloric_acid.png",
    "Zinc Metal (Zn)": "images/zinc_metal.png",
    "Wood Splint": "images/wood_splint.png",
    "5mL of 1M Copper (II) Sulfate (CuSO4)": "images/copper_sulfate.png",

}

label before_main_menu:
    $ preferences.set_volume("music", 0.2)  # set default main music
    return

label start:
    call variables  
    show screen ScoreOverlay  

    play music "audio/classroom.ogg" fadein 1.0

    scene bg classroom_pov
    with fade

    show irene speaking at left
    A "Hi! I'm [A]! Nice to meet you!"
    hide irene speaking

    show titania speaking at left
    B "Hello! I'm [B]. Let's split up the parts, I'll do the second experiment!"
    hide titania speaking

    show chlory speaking
    C "Then the third should be mine! [C] by the way, nice to meet you!"
    hide chlory speaking

    show yuranno speaking at right
    D "I guess the last one's mine then. The name's [D]."
    hide yuranno speaking

    show titania smile
    B "You should help everyone, [player]!"
    hide titania smile

    player "Sure!"

    show irene speaking at left
    A "Let's do mine first!"
    hide irene speaking
    
    jump scene_2

label scene_2:

    scene bg laboratory_table
    with fade
    
    show irene speaking at left
    A "I'll read out the process in the book, then you keep it in mind."
    hide irene speaking
    
    player "*nods*"
    
    show irene speaking at left
    A "Here I go! It says that we should-"
    A "Note the appearance of the wire."
    A "Using the tongs..."
    A "We must hold the wire in the hottest part of a burner flame for 1 to 2 minutes."
    A "But first, to do that, we need to fix the Bunsen burner. Put the end of the tube into the yellow faucet, and the other end to the Bunsen burner."
    A "Then, we place the evaporating dish near the base of the burner."
    A "After that, we get a piece of magnesium from the laboratory coordinator. Using crucible tongs, hold the sample in the burner flame until the magnesium starts to burn. REMEMBER, DO NOT LOOK DIRECTLY AT THE FLAME."
    A "When the ribbon stops burning, put the remains in the evaporating dish. Then we examine all that!"
    A "Did you get all that?"
    hide irene speaking
    
    player "*nods*"
    
    show irene speaking at left
    A "Great! Let's start!"
    hide irene speaking
    
    jump scene_3

label scene_3:
    show irene speaking at left
    A "What are the materials we need?"
    hide irene speaking

    # Define correct materials and all items
    $ correct_materials = {"Wire", "Tongs", "Bunsen Burner", "Evaporating Dish", "Magnesium"}
    $ all_items = list(materials.keys())

    # Ensure correct materials are included
    $ remaining_items = [item for item in all_items if item not in correct_materials]

    # Randomly select enough items to make a total of 6
    $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

    # Combine correct materials and additional items
    $ all_items = list(correct_materials) + additional_items
    $ renpy.random.shuffle(all_items)

    call screen material_selection(correct_materials, all_items)

    # Evaluate selection
    $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
    $ points_earned = len(correct_selected)  # 1 point for each correct item

    $ variables.points += points_earned  # Update the score

    show irene speaking at left
    if _return == correct_materials:
        A "[correct] You selected all the right materials!"
    else:
        $ missing_items = correct_materials - _return
        if missing_items:
            A "[wrong] You missed the following items: [', '.join(missing_items)]."
        else:
            A "[wrong] You selected incorrect items."
    hide irene speaking

    show irene speaking at left
    A "What do we do with this?"
    hide irene speaking

    menu:
        "Hold the sample in the burner flame until the magnesium starts to burn":
            $ variables.points += 5
            show irene speaking at left
            A "Right! I remember now! DON'T LOOK AT IT DIRECTLY!"
            hide irene speaking
        "Put aside":
            $ variables.points -= 1
            show irene speaking at left
            A "[wrong]"
            hide irene speaking
        "Hold the sample beside the burner flame for 2 to 3 minutes":
            $ variables.points -= 1
            show irene speaking at left
            A "[wrong]"
            hide irene speaking
        "dgsgsdsg":
            $ variables.points -= 1
            show irene speaking at left
            A "[wrong]"
            hide irene speaking
    
    jump scene_4

label scene_4:
    if variables.points >= 3:
        show irene speaking at left
        A "We're finally done!"
        hide irene speaking
        
        show teacher at left
        teacher "Great Job!"
        hide teacher
    else:
        show teacher at left
        teacher "That is wrong! Re-do it right now!"
        hide teacher
        jump scene_2

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_5

label scene_5:
    scene bg laboratory_table
    with fade
    
    show titania speaking at left
    B "Oh! Great, you've finished the first experiment. Let's move on to mine next. It says here in the book that-"
    
    B "Place 2 heaping micro spatulas of copper (II) carbonate (CuCO3) in a clean, dry test tube. Note the appearance of the sample."
    
    B "Watch the appearance closely—it's a light green powder."
    
    B "Next, we'll heat it for about 3 minutes. Use the test tube holder like this. Make sure you hold it at the top, and don't touch the bottom."
    
    B "After heating, we insert a burning wood splint into the test tube. If carbon dioxide (CO2) is present, it will extinguish the flame. Make sure you observe any changes in the residue inside the test tube."
    
    B "Did you get all that?"
    hide titania speaking
    
    show player at left
    player "*nods*"
    hide player
    
    show titania speaking at left
    B "Great! Let's start!"
    hide titania speaking
    
    jump scene_6

label scene_6:
    show titania speaking at left
    B "What are the materials we need?"
    hide titania speaking
    
    # Define correct materials and all items
    $ correct_materials = {"Test Tube Holder", "Test Tubes", "Matches", "Copper (II) Carbonate (CuCO3)", "Bunsen Burner"}
    $ all_items = list(materials.keys())

    # Ensure correct materials are included
    $ remaining_items = [item for item in all_items if item not in correct_materials]

    # Randomly select enough items to make a total of 6
    $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

    # Combine correct materials and additional items
    $ all_items = list(correct_materials) + additional_items
    $ renpy.random.shuffle(all_items)

    call screen material_selection(correct_materials, all_items)

    # Evaluate selection
    $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
    $ points_earned = len(correct_selected)  # 1 point for each correct item

    $ variables.points += points_earned  # Update the score

    show titania speaking at left
    if _return == correct_materials:
        B "[correct] You selected all the right materials!"
    else:
        $ missing_items = correct_materials - _return
        if missing_items:
            B "[wrong] You missed the following items: [', '.join(missing_items)]."
        else:
            B "[wrong] You selected incorrect items."
    hide titania speaking

    show titania speaking at left
    B "Great! Next, what will we put in the clean, dry test tube?"
    hide titania speaking
    
    menu:
        "2 heaping micro spatulas of copper (II) carbonate (CuCO3)":
            $ variables.points += 5
            show titania speaking at left
            B "That's amazing!"
            hide titania speaking
        "3 heaping micro spatulas of copper (II) carbonate (CuCO3)":
            $ variables.points -= 1
            show titania speaking at left
            B "Haha! I see you got confused. Here's the right one."
            hide titania speaking
        "2 heaping micro spatulas of Copper (II) carbonate (CuCO4)":
            $ variables.points -= 1
            show titania speaking at left
            B "Haha! I see you got confused. Here's the right one."
            hide titania speaking
        "3 heaping micro spatulas of Copper (II) carbonate (CuCO2)":
            $ variables.points -= 1
            show titania speaking at left
            B "Haha! I see you got confused. Here's the right one."
            hide titania speaking
    
    show titania speaking at left
    B "Now, let's heat it for 3 minutes. Do you have the test tube holder ready?"
    hide titania speaking
    
    menu:
        "Hold the top of the test tube firmly":
            $ variables.points += 5
            show titania speaking at left
            B "Wow, that's great!"
            hide titania speaking
        "Hold the middle half of the test tube firmly":
            $ variables.points -= 1
            show titania speaking at left
            B "Oh no! Be careful with that. You need to hold the test tube like this—"
            hide titania speaking
    
    show titania speaking at left
    B "How long will we heat this up?"
    hide titania speaking
    
    menu:
        "3 minutes":
            $ variables.points += 5
            show titania speaking at left
            B "Wow, you have good memory!"
            hide titania speaking
        "2 minutes":
            $ variables.points -= 1
            show titania speaking at left
            B "Oh you got it wrong. Here look at the textbook again."
            hide titania speaking
        "20 seconds":
            $ variables.points -= 1
            show titania speaking at left
            B "Oh you got it wrong. Here look at the textbook again."
            hide titania speaking
        "1 minute":
            $ variables.points -= 1
            show titania speaking at left
            B "Oh you got it wrong. Here look at the textbook again."
            hide titania speaking
    
    show titania speaking at left
    B "It's almost 3 minutes, what do we put inside the test tube?"
    hide titania speaking
    
    menu:
        "Burning wood splint":
            $ variables.points += 5
            show titania speaking at left
            B "Wow, that's great!"
            hide titania speaking
        "Copper (II)":
            $ variables.points -= 1
            show titania speaking at left
            B "No! Put this instead."
            hide titania speaking
    
    show titania speaking at left
    B "Oh shoot! I forgot, what's present if the flame of the burning wood splint inside the test tube gets put out?"
    hide titania speaking
    
    menu:
        "Carbon dioxide gas (CO2) is present":
            $ variables.points += 5
            show titania speaking at left
            B "Okay, thanks!"
            hide titania speaking
        "Copper (II) carbonate (CuCO3) is present":
            $ variables.points -= 1
            show titania speaking at left
            B "Hmm, are you sure?"
            hide titania speaking
    
    show titania speaking at left
    B "Okay, are we finished?"
    hide titania speaking
    
    menu:
        "No, we have to take note of the appearance of the residue in the test tube":
            $ variables.points += 5
            show titania speaking at left
            B "Oh, right!"
            hide titania speaking
        "Yes, let's move on to the next experiment":
            $ variables.points -= 1
            show titania speaking at left
            B "Oh no, did you take note of the appearance of the residue? Hmm, that's okay, I did!"
            hide titania speaking
    
    jump scene_7

label scene_7:
    if variables.points >= 30:
        show titania speaking at left
        B "We're finally done!"
        hide titania speaking
        show teacher speaking at right
        teacher "Great Job!"
        hide teacher speaking
    else:
        show teacher speaking at right
        teacher "That is wrong! Re-do it right now!"
        hide teacher speaking
        jump scene_5

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_8

label scene_8:
    scene bg laboratory_table
    with fade
    
    show chlory happy
    C "Congratulations! You've made it to the third experiment, substitution! I'm eager to explain what the book says here. So listen carefully!"
    hide chlory happy
    
    player "*nods*"
    
    label substitution_book:

    show chlory speaking
    C "CAUTION. IT IS IMPORTANT TO WEAR PROPER ATTIRE INSIDE THE LABORATORY EXPERIMENT SUCH AS: LABORATORY GOWN, SAFETY GOGGLES, FACE MASK, AND DISPOSABLE GLOVES."
    
    C "Let's start! First, stand a clean, dry test tube in the test tube rack."
    
    C "Add about 5 mL of 3 M hydrochloric acid (HCl) to the tube."
    
    C "Then, carefully drop a small piece of zinc metal (Zn) into the acid in the test tube. Observe and record what happens."
    
    C "Using a test tube holder, invert a second test tube over the mouth of the test tube in which the reaction is taking place. Then, remove the inverted tube after 30 seconds and quickly insert a burning wood splint into the mouth of the tube. A 'pop' indicates the presence of hydrogen gas."
    
    C "Take note of the appearance of the substance in the reaction test tube."
    
    C "Now, for the second part: Add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution to a clean, dry test tube. Place a small amount of zinc metal in the solution. Observe the solution and the zinc before and after the reaction."
    
    C "Did you get all that?"

    player "*nods*"
    
    hide chlory speaking
    show chlory happy
    C "Great! Let's start!"
    
    jump scene_9
    
label scene_9:
    show chlory speaking
    C "Alright, to check your knowledge, it's time for a quiz!"
    C "What are the materials we need?"
    # Define correct materials and all items
    $ correct_materials = {"5mL of 3M Hydrochloric Acid (HCl)", "Zinc Metal (Zn)", "Wood Splint", "5mL of 1M Copper (II) Sulfate (CuSO4)", "Test Tubes"}
    $ all_items = list(materials.keys())

    # Ensure correct materials are included
    $ remaining_items = [item for item in all_items if item not in correct_materials]

    # Randomly select enough items to make a total of 6
    $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

    # Combine correct materials and additional items
    $ all_items = list(correct_materials) + additional_items
    $ renpy.random.shuffle(all_items)

    call screen material_selection(correct_materials, all_items)

    # Evaluate selection
    $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
    $ points_earned = len(correct_selected)  # 1 point for each correct item

    $ variables.points += points_earned  # Update the score

    if _return == correct_materials:
        C "[correct] You selected all the right materials!"
    else:
        $ missing_items = correct_materials - _return
        if missing_items:
            C "[wrong] You missed the following items: [', '.join(missing_items)]."
        else:
            C "[wrong] You selected incorrect items."
    
    C "Why should you be careful when handling hydrochloric acid (HCl)?"
    menu:
        "A. It can cause fire":
            $ variables.points -= 1
            C "Oh no! You did not pay attention to the caution."
        "B. It can cause painful burns":
            $ variables.points += 5
            C "That's right! It is important to handle acids with care."
        "C. It can stain your clothes":
            $ variables.points -= 1
            C "Oh no! You did not pay attention to the caution."
    
    C "What is the next step after inverting the test tube for 30 seconds?"
    menu:
        "A. Immediately add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution":
            $ variables.points -= 1
            C "Oh no! Let me read the book again for you."
            jump substitution_book
        "B. Remove the inverted test tube and quickly insert burning wood splint into the mouth of the tube":
            $ variables.points += 5
            C "Very good! You have remembered the procedure."
        "C. Smell the test tube and wait for another 1 minute":
            $ variables.points -= 1
            C "Oh no! Let me read the book again for you."
            jump substitution_book
    
    hide chlory speaking
    jump scene_10
    
label scene_10:
    if variables.points >= 40:
        show chlory idle
        C "We're finally done!"
        hide chlory idle
        teacher "Great Job!"
    else:
        teacher "That is wrong! Re-do it right now!"
        jump scene_8

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_11

label scene_11:

    scene bg laboratory_table
    with fade

    show yuranno speaking
    
    D "Good morning! Are you ready for our last experiment? This one is called metathesis! I'm excited to walk you through it, so pay close attention!"

    hide yuranno speaking
    show yuranno default
    
    D "First, we'll start by adding about 2 mL of 0.1 M Lead Nitrate Pb (NO3)2 to a clean, dry test tube."
    
    D "Next, we'll add 2 mL of 0.1 M Potassium Iodide (KI) to the test tube. Watch closely!"
    
    D "Look at that! Observe the reaction and note any changes in the mixture."
    
    D "Next, we need to prepare three solutions. For Beaker A, add 5 drops of alcohol and 5 drops of phenolphthalein."
    
    D "For Beaker B, we'll prepare a saturated lead nitrate solution. That means adding 30g of lead nitrate to 10 mL of H2O."
    
    D "And for Beaker C, we'll add 15g of copper sulfate to 100 mL of H2O."
    
    D "Now, let's fill an Erlenmeyer flask with 1M ammonium hydroxide (NH4OH). We'll dissolve 3.5 g in 100 mL of H2O."
    
    D "Now comes the fun part! We'll fill each beaker with the ammonium hydroxide solution to produce red, white, and blue solutions."
    
    D "Make sure to observe the colors that develop!"
    
    jump scene_12

label scene_12:

    D "Did you follow all of that? Let's do a quick quiz to check your understanding!"
    
    D "What should we add to the first test tube to start our reaction?"
    menu:
        "A. 2 mL of sodium chloride (NaCl)":
            hide yuranno speaking
            show yuranno confused
            $ variables.points -= 1
            D "Not quite! It should be potassium iodide. Let's remember that for next time!"
            hide yuranno confused
            show yuranno speaking
        "B. 2 mL of potassium iodide (KI)":
            $ variables.points += 5
            D "Exactly! Potassium iodide is correct!"
    
    D "What color did the mixture turn after adding the potassium iodide?"
    menu:
        "A. Blue":
            hide yuranno speaking
            show yuranno confused
            $ variables.points -= 1
            D "Nope! It was yellow. Let's keep an eye out for that!"
            hide yuranno confused
            show yuranno speaking
        "B. Yellow":
            $ variables.points += 5
            D "Right! It turned bright yellow!"
    
    D "What do we need to observe in the beakers after adding the ammonium hydroxide solution?"
    menu:
        "A. The color changes in the solutions":
            $ variables.points += 5
            D "Correct! We need to observe the color changes!"
        "B. The temperature of the solutions":
            hide yuranno speaking
            show yuranno confused
            $ variables.points -= 1
            D "That's not it! We're looking for color changes, not temperature."
            hide yuranno confused
            show yuranno speaking
    
    jump scene_13

label scene_13:
    if variables.points >= 50:
        D "We did it! Great job!"
        hide yuranno speaking
    else:
        teacher "That is wrong! You need to re-do it!"
        jump scene_14
    
    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."
    
    jump scene_14

label scene_14:

    scene bg classroom
    with fade

    show irene speaking at left
    A "Good morning, everyone! We are here today to present our findings on four interesting chemistry experiments: Synthesis, Analysis, Substitution, and Metathesis."
    hide irene speaking

    show titania speaking at right
    B "Let's begin with the Synthesis experiment, where we observed the reaction of magnesium with a Bunsen burner flame."
    hide titania speaking

    show irene speaking at left
    A "We noted the appearance of the wire before heating and then heated it in the hottest part of the flame for 1-2 minutes. The key thing was to observe the changes."
    hide irene speaking

    show chlory speaking
    C "Next, the Analysis experiment. We heated copper(II) carbonate and observed its color change and the emission of carbon dioxide."
    hide chlory speaking

    show yuranno speaking at left
    D "The Substitution experiment involved the reaction of zinc with hydrochloric acid and copper(II) sulfate. Safety precautions were very important, as we worked with acids."
    hide yuranno speaking

    show irene speaking at right
    A "Finally, the Metathesis experiment. We mixed lead nitrate with potassium iodide and observed the precipitate formation."
    hide irene speaking

    show titania speaking at left
    B "Now, let's test your knowledge with a quiz!"
    hide titania speaking

    jump quiz

label quiz:
    
    show titania speaking at left
    B "Question 1: What important observation must be made in the Synthesis experiment before heating the wire?"
    hide titania speaking

    menu:
        "A. The color of the flame":
            $ variables.points -= 1
            show chlory speaking
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
            hide chlory speaking
        "B. The length of the wire":
            $ variables.points -= 1
            show chlory speaking
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
            hide chlory speaking
        "C. The appearance of the wire":
            $ variables.points += 5
            show titania speaking at left
            B "That's right! Observing the wire before heating is crucial. You get 1 point!"
            hide titania speaking
        "D. The temperature of the burner":
            $ variables.points -= 1
            show chlory speaking
            C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
            hide chlory speaking

    show chlory speaking
    C "Question 2: In the Analysis experiment, what gas was tested using the burning splint method?"
    hide chlory speaking

    menu:
        "A. Hydrogen":
            $ variables.points -= 1
            show irene speaking at left
            A "Oops, incorrect! We tested for carbon dioxide."
            hide irene speaking
        "B. Oxygen":
            $ variables.points -= 1
            show irene speaking at left
            A "Oops, incorrect! We tested for carbon dioxide."
            hide irene speaking
        "C. Carbon dioxide":
            $ variables.points += 5
            show yuranno speaking at right
            D "That is correct! Carbon dioxide extinguished the flame."
            hide yuranno speaking
        "D. Nitrogen":
            $ variables.points -= 1
            show irene speaking at left
            A "Oops, incorrect! We tested for carbon dioxide."
            hide irene speaking

    show yuranno speaking at right
    D "Question 3: In the Substitution experiment, what safety precaution is most important when handling hydrochloric acid?"
    hide yuranno speaking

    menu:
        "A. Wear gloves":
            $ variables.points -= 1
            show titania speaking at left
            B "Not quite, though gloves are important!"
            hide titania speaking
        "B. Wear a lab coat":
            $ variables.points -= 1
            show titania speaking at left
            B "Not quite, though protective clothing is needed!"
            hide titania speaking
        "C. Don't inhale fumes":
            $ variables.points -= 1
            show titania speaking at left
            B "Important, but there's more to consider."
            hide titania speaking
        "D. All of the above":
            $ variables.points += 5
            show yuranno speaking at right
            D "Correct! Safety first in all cases!"
            hide yuranno speaking

    show irene speaking at left
    A "Question 4: What was the noticeable observation when lead nitrate reacted with potassium iodide in a Metathesis reaction?"
    hide irene speaking

    menu:
        "A. Temperature change":
            $ variables.points -= 1
            show chlory speaking
            C "No, we were expecting a color change due to a precipitate forming."
            hide chlory speaking
        "B. Color change":
            $ variables.points += 5
            show chlory happy
            C "That's correct! A precipitate formed, causing a color change."
            hide chlory happy
        "C. Gas production":
            $ variables.points -= 1
            show chlory speaking
            C "No, we were expecting a color change due to a precipitate forming."
            hide chlory speaking
        "D. No change":
            $ variables.points -= 1
            show chlory speaking
            C "No, we were expecting a color change due to a precipitate forming."
            hide chlory speaking

    python:
        player_name = renpy.input("Enter your name for the leaderboard:")
        variables.leaderboard.update({player_name: variables.points})
        variables.save_leaderboard()

    jump results

label results:
    if variables.points >= 40:
        "You have [variables.points] points."
        "In total, you made [variables.mistakes] wrong choices."
        B "Well done! You certainly listened well. As a reward—an extra credit point!"
        D "Congratulations! Here's a chemistry-themed sticker!"
    else:
        A "Looks like you're a bit of practice away. Don't worry!"
        C "You need to retake the quiz to improve your score. Let's go over the main observations again."
        D "Reloading the slideshow for review."
        jump quiz

    B "We hope you learned something new about these experiments. Thanks for trying it out!"
        
    call screen Leaderboard(variables)

    menu leaderboard_menu:
        "Retry from the beginning":
            hide screen Leaderboard
            jump start
        "Exit":
            return
    
    hide screen ScoreOverlay

label rightchoice:
    e "This is the right choice"

    return

label variables:
    python:
        variables = Variables()  
    return

label addtional_options:
    
    if variables.retry_option and not variables.continue_anyway:
        menu too_many_mistakes_menu:
            "You made too many mistakes."
            "Continue anyway!":
                $ variables.continue_anyway = True
            "Retry from the beginning!":
                jump start
        return


#    if variables.retry_option == True and variables.continue_anyway == False:
#        menu too_many_mistakes_menu:
#            "You made too many mistakes."
#            "Continue anyway!":

#                $ variables.continue_anyway = True
#                pass
#            "Retry from the beginning!":
#                jump start
#    return
#    menu:
#        "You made too many mistakes."
#        "Continue anyway!":
#            pass
#        "Retry from the beginning":
#            return