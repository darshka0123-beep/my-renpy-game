# Character definitions
define me = Character("Me", color="#4a90e2")
define catlover306 = Character("catlover306", color="e74c3c")
define system = Character("System", color="#8e44ad")
define unknown = Character("unknown", color="#990000")

label start:
# This Sets the Background to pure blac to make it eerier. 
    scene expression  "#000"

    system "--- Incoming Text Message: catlover306 ---"
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
    me "Who would plant it?"
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
    jump final_sequence_wcatlover

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

unknown "i wouldn't go near that river if i were you."

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
    unknown "but you're just putting the people you care about in line of fire."
    jump threat_details

label threat_route2:
    me "If you're trying to intimidate me, it won't work."
    unknown "is that so?"
    unknown "you sound brave on a keyboard."
    unknown "let's see if you stay brave when your family pays for it."
    jump threat_details

label threat_details:
    unknown "your daughter walks alone from school around 4, right?"
    unknown "and your wife usually leaves her back door unlocked when she works in the garden."

    me "Don't you dare touch them."
     
    unknown "then drop the case."
    unknown "turn around, delete these chat logs, and forget the name zoey ever existed."
    unknown "if you push any further with the river trail..."
    unknown "there won't be a text next time."

    system "---User has disconnected ---"

    me "They know about my daughter... how deep does this go?"
    
    menu:
        "Ignore the threat and head to the river trail anyway.":
            jump go_to_river
        "Call my wife to make sure my daughter is safe.":
            jump call_wife

label go_to_river:
    me "I can't let them intimidate me. Zoey might not have much time left."
    

label call_wife:
    me "I need to make sure she's safe before I make my next move."

    system "--- Dialing: Sara ---"
    
    $ renpy.pause(1.5)
    
    system "---Connected---"

    me "Hey! Are you okay? Is everything fine at home?"
    "Sara" "Yeah, I'm just making dinner. Why do you sound so worried?"
    me "No reason... just checking in. Stay inside tonight, okay?"
    "Sara" "Alright... drive safe coming home."

    me "They're fine. It was just a bluff to throw me off"
    me "I'm heading to the river trail."
    jump river_trail_arrival

label river_trail_arrival:
    scene expression "#000"

    me "It's freezing here."
    me "There's a gate with a lock on it. I need to find a four-digit code that opens it."

# Puzzle
$ passcode = ""
$ passcode = renpy.input("Enter 4-digit passcode:", length=4)
$ passcode = passcode.strip()

if passcode == "1024":
    system "---ACCESS GRANTED: Gate Unlocked---"
    jump enter_tunnel
else:
    system "---ACCESS DENIED: Invalid Code ---"
    me "That didn't work. Let me check my notes... October 24th was the date of the party (1024)."
    $ passcode = renpy.input("Enter 4-digit passcode:", length=4)
    system "---OVERRIDE ACCEPTED---"
    jump enter_tunnel

label enter_tunnel:
    me "The heavy metal door creaks open..."

    # Text notification interrupts
    system "--- Incoming Text Message: unknown ---"

    unknown "i told you."

    me "What? How do they know I opened the gate?!"
    # Incoming call
    system "--- Incoming Call: Sara ---"

    "Sara" "Someone..Someone took her."
    me "Sarah?! What happened?! Who took who?!"
    "Sarah" "I just went to check her..the window was open..."
    "Sarah" "Our daughter is gone!" 

    me "No... no, no, no!"

    system "--- Incoming Text Message: unknown ---"
     
    unknown "now you're going to listen to me."
    return






    