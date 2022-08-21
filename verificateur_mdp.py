mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    if len(mdp) != 0 and len(mdp) < 8:
        mdp_trop_court = mdp_trop_court.capitalize()
        print(mdp_trop_court)
    elif len(mdp) == 0:
        mdp_trop_court = mdp_trop_court.upper()
        print(mdp_trop_court)
    else:
        print("Inscription terminée.")
