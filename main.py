from pyscript import display, document

members = ["Tyler Sales", "Lance Garcia", "Jilliane Tech", "Therese Reyes", "Bianca Ledres", "Carlos Borromeo"]


def check(e):
    document.getElementById("output").innerHTML = ""
    a = document.getElementById("firstname").innerHTML 
    b = document.getElementById("lastname").innerHTML
    display("Your name is " + str(a) + str(b), target = "output")