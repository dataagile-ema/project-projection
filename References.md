# Skapa miljö
conda create --name pp_app python=3.9
conda activate pp_app
pip3 install streamlit

# Vidareutveckling
- ha engelsk text
- välja enhet (timmar, dagar, story points)
- välja tid per vecka för att få kalendertid.
- varaiant: gör om till att mata in antal user stories eller story point per vecka eller annan period istället. Skulle passa bättre för projek styrda av ledtider och projekt som jobbar med kanban/agile-metrics.
- Lägg till 3 punkts estimat och byt ut distribution  
** Fördelning av cykeltid kan modelleras med weibull dist med olika shape (ref Troy Magennis). Est för en user story borde ha samma fördelning:
** -- Cykeltid i veckor = Est för en user story / Tid per vecka
** -- Det finns flera sätt att modellera tid för en aktivitet, bla PERT https://en.wikipedia.org/wiki/PERT_distribution - modified PERT med lambda = 3 används SUCCA och SEER 
** -- Antal user stories per vecka = Tid per vecka / Est för en user story
- Lägg till en instruktion för att hur appen ska användas.








