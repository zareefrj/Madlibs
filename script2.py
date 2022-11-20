def madlib():
    noun1 = input("Add a noun: ")
    adjective1 = input("Add an adjective: ")
    verb1 = input("Add a verb: ")
    plural_noun1 = input("Add a plural noun: ")
    adjective2 = input("Add another adjective: ")
    plural_noun2 = input("Add another plural noun: ")

    message = '''It was a time to be alive in the ''' + noun1 + ''' age. Not many people could tell that the sky
    was littered with ''' + plural_noun1 + '''.''' + ''' But if you could ''' + verb1 + ''' you would ''' + verb1 + ''' it. There they were in the sky, all ''' + adjective1 + ''' and ''' + adjective2 + ''' wrapped up in their uniforms
    and ''' + adjective1 + ' ' + plural_noun2 + '''. You just had to see it.'''

    print(message)
    return(message)