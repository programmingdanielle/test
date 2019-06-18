questions = {
    "How would you describe yourself? \na) brave \nb) studious \nc) loyal \nd) ambitious\n",
    "What is your preference? \na) outside \nb) inside \nc) darkness \nd) other\n",
    "How would you describe yourself? \na) brave \nb) studious \nc) loyal \nd) ambitious\n",
}


def run_test(questions):
    firedrake = 0
    waterdrake = 0
    earthdrake = 0
    unknown_origin = 0
    for question in questions:
        if questions == "a":
            firedrake += 1
        elif questions == "b":
            waterdrake += 1
        elif questions == "c":
            earthdrake += 1
        elif unknown_origin == "d":
            unknown_origin += 1

print(run_test(questions))