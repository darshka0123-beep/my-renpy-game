# Character definitions
define me = Character("Me", color="#4a90e2")
define unkown = Character("Unkown Number", color="e74c3c")
define system = Character("System", color="#8e44ad")

label start:
    scene bg black

    system "--- Incoming Text Message: Unkown Number ---"
    unknown "Is this the detective handling the Elmwood case?"

    menu:
        "Who is asking?":
            jump branch_who
        "Yes. State your business.":
            jump branch_business
        "Wrong number.":
            jump branch_wrong

label branch_who:
    me "Who is asking?"
    unknown "That doens't matter right now."
    unkown "What matters is Zoey. You're looking for her, right?"
    me "I am. What do you know about her disappearance?"
    unknown "I know she never left the party on foot."
    unkown "Check the traffic cameras near the highway intersection."
    jump continuation_1

label branch_business:
    me "Yes. State your business."
    unkown "Straight to the point. I like it."
    unkown "I have the footage from the night Zoey went missing."
    me "Footage? Where did you get that?"
    unknown "Let's just say I have access to things the local police missed."
    jump continuation_1

label branch_wrong:
    me "Wrong number."
    unknown "Don't play games with me."
    unknown "I know you picked up Zoey's case file this morning."
    me "Fine. What do you want?"
    unknown "I want to make sure the right person finds her before it's too late."
    jump continuation_1

label branch_wrong:
    unknown "Listen carefully. She didn't drop her phone by accident."
    me "Are you saying it was planted?"
    unknown "Exactly. Someone wanted you to find that specific chat log."

    menu:
        "Who would plant it?":
            jump branch_plant
        "Where is Zoey right now?":
            jump branch_location

label branch_plant:
    me "Who plant it?"
    unknown "Someone inside the group from the party."
    unknown "They're trying to frame the host."
    jump continuation_2

label branch_location:
    me "Where is Zoey right now?"
    unknown "I can't give you the exact coordinates over an unsecured line."
    unknown "But I can tell you where to start looking. The old trail entrance near the river."
    jump continuation_2

label continuation_2:
    unkown "I'm sending you an encrypted file."
    system "--- Downloading attachment: audio_log_04.wav ---"

    menu:
        "Try 1024":
            jump code_correct
        "Try 1101":
            jump code_incorrect
    