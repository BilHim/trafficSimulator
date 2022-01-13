def autoSearch(word_to_check):
    list_to_check = ["Automation Engineer", "QA", "Auto", "Desc automation", "AutomatIon manager"]
    counter = 0
    for job in list_to_check:
        job_lower = job.lower()
        word_to_check = str(word_to_check).lower()
        if word_to_check in job_lower:
            counter = counter + 1
    print(counter)
    return counter

autoSearch("automation")