# Character definitions
define me = Character("Me", color="#4a90e2")
define catlover306 = Character("catlover306", color="e74c3c")
define system = Character("System", color="#8e44ad")
define unknown = Character("unknown", color="#990000")

label start:
    scene expression  "#000"

    system "--- Incoming Text Message: catlover306 Number ---"
    catlover306 "Is this the detective handling the Elmwood case?"

    menu:
        "Who is asking?":
            jump branch_who
        "Yes. State your business.":
            jump branch_business
        "Wrong number.":
            jump branch_wrong

label branch_who:
    me "Who is asking?"
    catlover306 "That doens't matter right now."
    catlover306 "What matters is Zoey. You're looking for her, right?"
    me "I am. What do you know about her disappearance?"
    catlover306 "I know she never left the party on foot."
    catlover306 "Check the traffic cameras near the highway intersection."
    jump continuation_1

label branch_business:
    me "Yes. State your business."
    catlover306 "Straight to the point. I like it."
    catlover306 "I have the footage from the night Zoey went missing."
    me "Footage? Where did you get that?"
    catlover306 "Let's just say I have access to things the local police missed."
    jump continuation_1

label branch_wrong:
    me "Wrong number."
    catlover306 "Don't play games with me."
    catlover306 "I know you picked up Zoey's case file this morning."
    me "Fine. What do you want?"
    catlover306 "I want to make sure the right person finds her before it's too late."
    jump continuation_1

label continuation_1:
    catlover306 "Listen carefully. She didn't drop her phone by accident."
    me "Are you saying it was planted?"
    catlover306 "Exactly. Someone wanted you to find that specific chat log."

    menu:
        "Who would plant it?":
            jump branch_plant
        "Where is Zoey right now?":
            jump branch_location

label branch_plant:
    me "Who plant it?"
    catlover306 "Someone inside the group from the party."
    catlover306 "They're trying to frame the host."
    jump continuation_2

label branch_location:
    me "Where is Zoey right now?"
    catlover306 "I can't give you the exact coordinates over an unsecured line."
    catlover306 "But I can tell you where to start looking. The old trail entrance near the river."
    jump continuation_2

label continuation_2:
    catlover306 "I'm sending you an encrypted file."
    system "--- Downloading attachment: audio_log_04.wav ---"

    menu:
        "Try 1024":
            jump code_correct
        "Try 1101":
            jump code_wrong

label code_correct:
    system "--- Access Granted ---"
    catlover306 "Good. Listen to the Background noise in that recording."
    me "It sounds like running water... and echo?"
    catlover306 "She was taken near the tunnel under the ridge."
    jump final_sequence

label code_wrong:
    system "---Access Denied: 2 Attempts Remaining ---"
    catlover306 "Wrong Code. Don't lock the file, or we lose our one and only lead."
    me "Wait, let me try October 24th."
    system "---Access Granted---"
    catlover306 "Watch your step next time."
    jump final_sequence_wcatlover

label final_sequence_wcatlover:
    catlover306 "I have to clear this channel now..."
    me "Wait! Tell me who you are!"
    catlover306 "Find Zoey first. Then we'll talk."
    system "---User has disconnected---"
    
    me "Looks like I'm heading to the river trail..."

$ renpy.pause(3)

system "--- Incoming Text Message: Unknown Number ---"

unknown "I wouldn't go near that river if i were you."

me "Who is this? Is that you catlover?"

unknown "doesn't matter who i am."
unknown "what matters is that i know who you are."

menu:
    "How did you get this number?":
        jump threat_route1
    "If you're trying to intimidate me, it won't work.":
        jump threat_route2

label threat_route1:
    me "How did you get this number?"
    unknown "the same way i got your address."
    unknown "you think you're playing detective on zoey's case."
    unknown ""



    