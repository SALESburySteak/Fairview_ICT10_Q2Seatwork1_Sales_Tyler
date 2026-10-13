from pyscript import display, document


def check(e):
    
    members = ["Tyler Sales", "Lance Garcia", "Jilliane Tech", "Therese Reyes", "Bianca Ledres", "Carlos Borromeo"]
    document.getElementById("output").innerHTML = ""

    a = document.getElementById("firstname").value
    b = document.getElementById("lastname").value

    name = (a + " " + b)
    memberchecker = name in members

    status = [
        (f"Sorry, {name}. You are not included in the club."),
        (f"Congratulations {name}! You are included in the club.")
        ]

    document.getElementById("output").innerHTML = status[memberchecker]    
