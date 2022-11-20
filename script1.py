def madlib():
    ## Madlib Phase 1 ##
    # String Concatenation
    occasion=input("Enter an occasion: ")
    verb1=input("Enter a verb: ")+"ed"
    body_parts=input("Enter a body part: ")
    adj=input("Enter an adjective: ")
    emotion=input("Enter an emotion: ")
    adj2=input("Enter another adjective: ")
    verb2=input("Enter another verb: ")+"ing"
    verb3=input("Enter another verb: ")+"ed"
    body_part2=input("Enter another body part: ")
    obj=input("Enter an object: ")
    verb4=input("Enter another verb: ")+"ed"
    animal=input("Enter an animal: "+"s")

    madlib=f"\nThere was so much anticipation leading up to our {occasion} first time. Up to that point we had only ever {verb1} each other’s {body_parts}. So when the {adj} night came, we were both {emotion} because we were so {adj2}. We started off {verb2}, but things started to get more {verb3} as we went along. The most memorable part was when you stuck your {body_part2} into my {obj}. I will admit, it {verb4} me greatly. Overall, it was truly a night to remember. We were real {animal} in the sack!"

    print(madlib)
    return(madlib)