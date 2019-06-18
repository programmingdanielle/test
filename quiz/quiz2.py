import question from Question

question_prompts = {
    "What element do you prefer?\n(a) Fire \n (b)Water \n (c)Earth\n\n",
    "What color?\n(a) Orange \n (b)Blue \n (c)Green\n\n",
    "What best describes you?\n (a)Aggressive \n (b) Go with the flow \n\n (c)Stubborn",
}

questions = {
    Question(question_prompts[0], "a", "b", "c"),
    Question(question_prompts[1], "a", "b", "c"),
    Question(question_prompts[2], "a", "b", "c"),
}

def run_test(questions):
    score = ""
    for question in questions:
        answer = input(question.prompt)
    if answer