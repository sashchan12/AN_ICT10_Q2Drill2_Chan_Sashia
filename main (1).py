from pyscript import display, document

# ---------- Predefined club sets ----------
varsity = {"Joe Kerr", "Sheldon Cooper", "Billy Sparks"}
science_club = {"Alice Blue", "Anita Bath", "Ella Vator", "Eileen Dover"}
computer_club = {"Tam Nguyen", "Juanito Lakarin", "Francisco Portero",
                 "Justin Case"}
math_club = {"Ligaya Anonuevo", "Restituto Fruto", "Paige Turner"}


def show_clubs():
    """Show each club's members inside its card on the page."""
    pass


def add_member(event):
    """Runs when the button is clicked (py-click)"""

    first = document.querySelector("#first-name").value
    last = document.querySelector("#last-name").value
    club = document.querySelector('input[name="club"]:checked').value
    # club is "varsity", "science", "computer", or "math"
    pass

# Show the club lists when the page first loads
show_clubs()
