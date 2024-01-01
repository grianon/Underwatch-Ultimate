regionKeysByDetectableTypes = {
    "popups": [
        "Elimination",
        "Assist",
        "Saved",
    ],
    "playerSpecificStates": [
        "Give Harmony Orb",
        "Give Discord Orb",
        "Give Mercy Boost",
        "Give Mercy Heal",
        "Give Moira Heal",
        "Give Moira Ult",
        "Give Orisa Ult",
    ],
    "healRecieveStates": [
        "Receive Zen Heal",
        "Receive Mercy Boost",
        "Receive Mercy Heal",
    ],
    "playerStatus": [
        "Receive Hack",
        "Receive Discord Orb",
        "Receive Anti-Heal",
        "Receive Heal Boost",
        "Receive Immortality",
    ],
}


regions = {
    # Is the kill cam or potg playing?
    "KillcamOrPOTG": {"Rect": [118.0, 167.0, 2868.0, 3394.0], "MaxMatches": 1},
    # Popups are where elims, assists, saved, etc. are rendered
    "Popup1": {"Rect": [999.0, 1041.0, 1563.0, 1875.0], "MaxMatches": 1},
    "Popup2": {"Rect": [1045.0, 1085.0, 1591.0, 1847.0], "MaxMatches": 1},
    "Popup3": {"Rect": [1092.0, 1132.0, 1634.0, 1804.0], "MaxMatches": 1},
    # players status
    "Receive Heal": {"Rect": [980.0, 1122.0, 570.0, 721.0], "MaxMatches": 2},
    "Receive Status Effect": {
        "Rect": [1129.0, 1192.0, 209.0, 497.0],
        "MaxMatches": 3,
    },
    # Character specific states
    "Give Harmony Orb": {
        "Rect": [1273.0, 1315.0, 1416.0, 1461.0],
        "MaxMatches": 1,
    },
    "Give Discord Orb": {
        "Rect": [1270.0, 1316.0, 1975.0, 2021.0],
        "MaxMatches": 1,
    },
    "Give Mercy Heal": {
        "Rect": [886.0, 951.0, 1505.0, 1570.0],
        "MaxMatches": 1,
    },
    "Give Mercy Boost": {
        "Rect": [886.0, 950.0, 1869.0, 1933.0],
        "MaxMatches": 1,
    },
    "Give Moira Heal": {
        "Rect": [981.0, 1063.0, 1247.0, 1345.0],
        "MaxMatches": 1,
    },
    "Give Moira Ult": {
        "Rect": [1119.0, 1236.0, 1150.0, 1381.0],
        "MaxMatches": 1,
    },
    "Give Orisa Ult": {
        "Rect": [838.0, 888.0, 1662.0, 1780.0],
        "MaxMatches": 1,
    },
}

detectables = {
    # Is the kill cam or potg playing?
    "KillcamOrPOTG": {"Filename": "killcam_potg_sobel.png", "Threshold": 1.1},
    # The following states are rendered in the "popup" regions
    "Elimination": {
        "Filename": "elimination.png",
        "Threshold": 0.9,
        "Points": 25,
        "Type": 2,
        "Duration": 2.5,
    },
    "Assist": {
        "Filename": "assist.png",
        "Threshold": 2,
        "Points": 20,
        "Type": 2,
        "Duration": 2.5,
    },
    "Saved": {
        "Filename": "saved.png",
        "Threshold": 1.2,
        "Points": 30,
        "Type": 2,
        "Duration": 2.5,
    },
    "Eliminated": {
        "Filename": "you_were_eliminated.png",
        "Threshold": 0.8,
        "Points": 0,
        "Type": 2,
        "Duration": 2.5,
    },
    # Character specific states
    "Give Harmony Orb": {
        "Filename": "apply_harmony.png",
        "Threshold": 0.6,
        "Points": 10,
        "Type": 0,
        "Duration": 1,
    },
    "Give Discord Orb": {
        "Filename": "apply_discord.png",
        "Threshold": 0.6,
        "Points": 20,
        "Type": 0,
        "Duration": 1,
    },
    "Give Mercy Heal": {
        "Filename": "apply_mercy_heal.png",
        "Threshold": 0.6,
        "Points": 5,
        "Type": 0,
        "Duration": 1,
    },
    "Give Mercy Boost": {
        "Filename": "apply_mercy_boost.png",
        "Threshold": 0.6,
        "Points": 20,
        "Type": 0,
        "Duration": 1,
    },
    "Give Moira Heal": {
        "Filename": "apply_moira_heal.png",
        "Threshold": 1,
        "Points": 5,
        "Type": 0,
        "Duration": 1,
    },
    "Give Orisa Ult": {
        "Filename": "apply_orisa_ult.png",
        "Threshold": 0.9,
        "Points": 100,
        "Type": 0,
        "Duration": 1,
    },
    "Give Moira Ult": {
        "Filename": "apply_moira_ult.png",
        "Threshold": 1.1,
        "Points": 100,
        "Type": 0,
        "Duration": 1,
    },
    # players status
    "Receive Zen Heal": {
        "Filename": "receive_zen_heal.png",
        "Threshold": 0.85,
        "Points": 10,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Mercy Heal": {
        "Filename": "receive_mercy_heal.png",
        "Threshold": 0.8,
        "Points": 15,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Mercy Boost": {
        "Filename": "receive_mercy_boost.png",
        "Threshold": 0.9,
        "Points": 25,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Hack": {
        "Filename": "receive_hack_icon.png",
        "Threshold": 0.9,
        "Points": 100,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Discord Orb": {
        "Filename": "receive_discord.png",
        "Threshold": 1,
        "Points": -20,
        "Type": 1,
        "Duration": 1,
    },
    "Receive Anti-Heal": {
        "Filename": "receive_purple_pot.png",
        "Threshold": 0.9,
        "Points": -50,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Heal Boost": {
        "Filename": "receive_yellow_pot.png",
        "Threshold": 0.8,
        "Points": 20,
        "Type": 0,
        "Duration": 1,
    },
    "Receive Immortality": {
        "Filename": "receive_immortality.png",
        "Threshold": 0.8,
        "Points": 20,
        "Type": 0,
        "Duration": 1,
    },
}
