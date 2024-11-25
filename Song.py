thick_of_it = """
I'm in the {adjective1} of it, everybody knows
They know me where it {verb1}, I {verb2} in and they froze
I don't know no nothin' 'bout no {noun1}, I'm just {noun2}
Forty somethin' milli' {noun3} or so, I've been told
I'm in my prime and this ain't even final form
They {verb3} me down, but still, my {noun4}, they find the {noun5}
I went from {noun6} straight out to sold-out tours
Life's a fight, but trust, I'm ready for the {noun7}
"""

auth = """
Yeah, yeah
Forfeit the {noun1}
Before somebody else
{verb1} you out of the {noun2}
And puts your {noun3} to {adjective1}
Cover up your {noun4}
You can't {verb2} the {noun5}
The {noun6} is too {adjective2}
You just won't {verb3} ({verb3}, {verb3}, {verb3})
You love the way I {verb4} at you
While taking pleasure in the awful {noun7} you {verb5} me through
You {verb6} away if I give in
My {noun8}
My {noun9} is {verb6}ed
"""

duality = """I {verb1} my {noun1} into my {noun2}
It's the only thing that slowly {verb2}s the {noun3}
But it's made of all the {noun4}s, I have to {verb3} the
{noun5}, it never ends, it {verb4} it's way inside
If the {noun6} {verb5}s on
I have {verb6} until my {noun7}s {verb7}ed
I've {verb8} as my {noun8}s elapsed
Now, all I do is {verb9} with so much hate
I've {verb10}ed for this, I've bitched at that
I've left behind this little {noun9}"""

def get_user_inputs(placeholders):
    inputs = {}
    print("Enter whatever brainrot terms you like following the instruction word, for e.g if it asks for a verb: goon. Feel free to get creative, reuse verbs if you'd like")
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}: ")
        inputs[placeholder] = user_input
    return inputs

placeholders_thick_of_it = [
    "adjective1", "verb1", "verb2", "noun1", "noun2",
    "noun3", "verb3", "noun4", "noun5", "noun6", "noun7"
]

placeholders_auth = [
    "noun1", "verb1", "noun2", "noun3", "adjective1", 
    "noun4", "verb2", "noun5", "noun6", "adjective2", 
    "verb3", "verb4", "noun7", "verb5", "verb6", 
    "noun8", "noun9"
]
placeholders_duality = [
    "verb1", "noun1", "noun2", "verb2", "noun3","noun4", "verb3", "noun5", "verb4", "noun6", "verb5", "verb6", "noun7", "verb7", "verb8", "noun8","verb9", "verb10", "noun9"
]

choice = input("Which song would you like to customize? Enter '1' for Thick of It, '2' for Points of authority, '3' for duality: ")

if choice == "1":
    user_inputs = get_user_inputs(placeholders_thick_of_it)
    final_song = thick_of_it.format(**user_inputs)
    print("\nHere is your custom version of Thick of It:")
    print(final_song)
elif choice == "2":
    user_inputs = get_user_inputs(placeholders_auth)
    final_song = auth.format(**user_inputs)
    print("\nHere is your custom version of Points of authority:")
    print(final_song)

elif choice == '3':
    user_inputs = get_user_inputs(placeholders_duality)
    final_song = duality.format(**user_inputs)
    print("\nHere is your custom version of Duality:")
    print(final_song)

    
else:
    print("Invalid choice.")
