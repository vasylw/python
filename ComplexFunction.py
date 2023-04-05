def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    #return new_replacement

    def new_replacement2(text):
        return text.replace('e', replacement)
    #return new_replacement
    return new_replacement2


stars = replace_spaces("xxx")
print(stars("And Now for Something Completely Different"))