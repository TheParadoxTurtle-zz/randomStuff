import random
q = [
"What is your favorite Apollo mission?",
"Who is your favorite K-On Character?",
"What is your favorite suite moment? (This applies even to people who have only known the suite for approx. 15 minutes)"
"What law do you think is stupid and unnecessary?"
"There is a chess-boxing tournament among the participants. Who wins?"
"What is your favorite Nicolas Cage movie/moment?"
"Who here is the biggest dingus and why?",
"What has been your favorite question so far?",
"Why is Paul a big frik?",
"What has been your biggest ...frik moment in college?",
"What fictional character would be your best friend?",
"What fictional character would you date?",
"Who is your celebrity crush? (People not anime)(Looking at you, Paul)",
"You have the power to make Peter Salovey sing one song for Karaoke in front of the whole school. What song do you pick?",
"What is your favorite variation of Hari?",
"How did Bolotsky die?",
"Did Homura do anything wrong?",
"Where in the world is Carmen Sandiego?",
"How would (the player) die in a horror movie?",
"Which suite member would be the perfect Bond and who would be his bond girl?",
"What is the best emoticon? ",
"How would you annoy Hari?",
"No impossible questions please",
"If the suite went to war, what would be your tactic? <- what does that mean",
"Who would be the best bearer of the One Ring?",
"What really grinds your gears?",
"(The player) stars in a movie. Give a one sentence synopsis.",
"Choose a starter pokemon and explain.",
"Where does Ben buy his next pair of running shoes?",
"Which country embodies (the player)?",
"What piece of furniture embodies (the player)?",
"Nominate a new suite mascot (i.e. not bread).",
"If you were a book, what would be your title?",
"What movie describes your life?",
"What movie title describes your life?",
"What makes Harold tick?",
"What flag is the suite missing?",
"Which Power Ranger are you?",
"What is your favorite late-night snack?",
"If you could teach a Splash class on anything, what would it be?",
"If you could eat/drink only one thing for the rest of your life, what would it be?",
"Who here would be your arch-nemesis?",
"What is the meaning of life?",
"What color would you dye your hair?",
"Why is it so cold in the winter?",
"What is the meaning of life?",
"What country best represents your hair?",
"If you worked in IT, what would you do all day?",
"What kind of ship are you?",
"Which singer are you?",
"What is your favorite Snapple flavor?"
]
while True:
    raw_input();
    index = int(random.random()*len(q))
    print q[index]

