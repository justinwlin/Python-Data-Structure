def flip_and_reverse_it(phrase):
    string = ""
    for word in phrase.split():
        string = word + " " + string
    return string


print(flip_and_reverse_it("Hello my name is sllim shaddy"))