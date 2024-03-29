from forward_chaining import relations

def delegate_question(question):
    keysAndRleations = question.split(" ")
    result = relations[keysAndRleations[0]](keysAndRleations[1]) \
        if len(keysAndRleations) < 3 \
        else relations[keysAndRleations[1]](keysAndRleations[0], keysAndRleations[2])


delegate_question("henryfitzroy bastard henryVIII")
delegate_question("lover isabelblount")
delegate_question("claim edwardVI")
delegate_question("granchild maryI")
