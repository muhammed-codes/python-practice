full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif len(name) == 0:
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"

    elif not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4" 
    elif not strength + intelligence + charisma == 7:
        return "The character should start with 7 points"
    
    else:
        final_result = f"{name}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
        return final_result
    

test = create_character('ren', 4, 2, 1)
print(test)


FULL_DOT = '●'
EMPTY_DOT = '○'
MAX_DOTS = 10
STAT_POOL = 7

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str) or len(name) == 0:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    stats = {"STR": strength, "INT": intelligence, "CHA": charisma}

    if any(not isinstance(v, int) for v in stats.values()):
        return "All stats should be integers"
    if any(v < 1 for v in stats.values()):
        return "All stats should be no less than 1"
    if any(v > 4 for v in stats.values()):
        return "All stats should be no more than 4"
    if sum(stats.values()) != STAT_POOL:
        return "The character should start with 7 points"

    lines = [name] + [
        f"{label} {FULL_DOT * val}{EMPTY_DOT * (MAX_DOTS - val)}"
        for label, val in stats.items()
    ]
    return "\n".join(lines)

