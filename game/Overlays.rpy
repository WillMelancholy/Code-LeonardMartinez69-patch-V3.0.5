screen Leaderboard(data):
    tag leaderboard
    $ print(data.leaderboard)
    vbox style "st_leaderboard_box":
        hbox style "st_leaderboard_box":
            frame style "st_leaderboard_col1":
                background Solid("#353535ff")
                text "Player Name" style "st_leaderboard_header"
            frame style "st_leaderboard_col2":
                background Solid("#353535ff")
                text "Points" style "st_leaderboard_header"
        $ index = 0
        for name, score in data.leaderboard.items():
            python:
                index += 1
                row_color = "#353535bb" if index % 2 == 0 else "#222222c4"
            hbox style "st_leaderboard_box":
                frame style "st_leaderboard_col1":
                    background Solid(row_color)
                    text "[name]" style "st_leaderboard_text"
                frame style "st_leaderboard_col2":
                    background Solid(row_color)
                    text "[score]" style "st_leaderboard_text"
    frame:
        background None
        anchor (1.0, 0.0)
        offset (-10, 10)
        pos (1.0, 0.0)
        vbox:
            xalign 1.0
            spacing 5
            button style "st_leaderboard_button":
                action Function(data.reload_leaderboard)
                text "Reload" style "st_leaderboard_button_text"
            button style "st_leaderboard_button":
                action Return()
                text "Close" style "st_leaderboard_button_text"
        
screen ScoreOverlay():
    tag score_overlay
    frame:
        anchor (0.5, 0.0)
        background Frame("lined_paper.png")  # Use an image of lined paper as background
        offset (0, 10)
        pos (0.5, 0.0)
        xsize 250  # Ensuring the frame is wide enough for centering
        vbox:
            spacing 10  # Increased spacing further to move Points text down
            xalign 0.5  # Ensures child elements are centered
            null height 20  # Moves the Points value down by adding space
            text _("Points") size 28 bold True xalign 0.5
            text "[variables.points]" size 48 bold True xalign 0.5
            textbutton "Leaderboard":
                xalign 0.5
                background Solid("#e2e2e299")
                hover_background Solid("#757575cc")
                xsize 150  # Reduced width
                ysize 40   # Adjusted height
                text_size 22  # Ensures text scales properly within the button
                action ShowMenu("Leaderboard", variables)

style st_leaderboard_text:
    xalign 0.5

style st_leaderboard_header is st_leaderboard_text:
    size int(gui.text_size * 1.4)
    bold True

style st_leaderboard_box:
    align (0.5, 0.5)
    spacing 5

style st_leaderboard_col1:
    xsize 400
    xalign 0.5

style st_leaderboard_col2 is st_leaderboard_col1:
    xsize 200

style st_leaderboard_button:
    background Solid("#ffffff99")
    hover_background Solid("#ffffff66")
    xsize 200

style st_leaderboard_button_text:
    xalign 0.5

screen material_selection(correct_items, all_items):
    modal True
    zorder 200
    default selected = set()

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        
        vbox:
            spacing 20
            label "Select the correct materials:" xalign 0.5
            
            # Display the number of selected items
            text "Selected: [len(selected)]/5" xalign 0.5
            
            vpgrid:
                cols 3
                spacing 40
                for item in all_items:
                    button:
                        # Disable the button if the selection limit is reached and the item is not already selected
                        action If(
                            len(selected) < 5 or item in selected,
                            ToggleSetMembership(selected, item),
                            None
                        )
                        selected_background "#CCFFCC"
                        xfill True
                        xsize 200
                        ysize 200
                        sensitive (len(selected) < 5 or item in selected)  # Disable button if limit is reached
                        vbox:
                            spacing 5
                            add materials[item]:
                                xalign 0.5
                                ysize 150
                                fit "contain"
                            text item:
                                xalign 0.5
                                size 16
            
            textbutton "Submit" action [Return(selected), Hide("material_selection")] xalign 0.5