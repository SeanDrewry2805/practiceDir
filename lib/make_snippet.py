def make_snippet(text):
    List = text.split(" ")
    if len(List) > 5:
        first_five = List[:5]
        sentence = " ".join(first_five)
        return sentence + "..."
    else:
        return text
