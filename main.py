from pyscript import document

def compute_average(event):
    #Get the Input Values and convert to Float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    
    #Compute for the average
    average = (score1 + score2) / 2

    #Determine if pass/fail
    if average >= 75:
        result = "Passed !"
    else:
        result = "Failed."

    #Display the Result
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result