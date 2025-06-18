# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])
        # Dubug: Modified k to keys

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         # Debug: Removed trailing whitespace
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!",
                         # Degug: Modified ' ' to " "
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ('lisa', 'bart', 'homer'))
# Debug: Added brackets around keys

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
