def calculate_percentage(obtained,total):
    return (obtained / total) * 100
def status_pass(percentage):
    if percentage >= 40:
        return "Pass"
    return "Fail"