#Python Marvel Cinematic Universe Quiz

print("-----------------------🦸‍♂️🛡️The Ultimate Marvel Cinematic Universe Quiz---------------------------------")

questions= ("Most of the series had our heroes preoccupied with retrieving which items?: ",
            "The MCU heroes treat this guy as their boss. What's his name?: ",
            "This rare element took center stage in the \"Black Panther\" film. Can you name the chemical?: ",
            "When not in hero duty, Hawkeye goes by which name?: ",
            "So, who is Groot?: ",
            "He's Thor's hateful brother whom everybody loves anyway. What's his name?: ",
            "In which MCU film did Valkyrie fly for the first time?: ",
            "Which Chris played Star-Lord?: ",
            "Who is Gamora's sister?: ",
            "What is Black Widow's given name?: ")

options= (("A. Pym Particles", "B. Midi-chlorians", "C. Deathly Hallows", "D. Infinity Stones"),
          ("A. Nick Fury ", "B. Phil Coulson", "C. Chester Phillips", "D. Howard Stark"),
          ("A. Vibranium", "B. Plutonium", "C. Adamantium", "D. Uranium"),
          ("A. Johann Schmidt ", "B. Erik Selvig", "C. Clint Barton", "D. Peter Parker"),
          ("A. William Hurt", "B. Vin Diesel", "C. Josh Brolin ", "D. Sam Rockwell "),
          ("A. T'Chaka", "B. Loki", "C. Drax ", "D. Dormammu"),
          ("A. Iron Man 2", "B. Thor: Ragnarok", "C. Avengers: Age of Ultron ", "D. Doctor Strange"),
          ("A. Chris Pratt ", "B. Chris Evans ", "C. Chris Hemsworth", "D. Chris Pine"),
          ("A. Aurora", "B. Nebula", "C. Asteroid", "D. Meteor"),
          ("A. Natasha Romanoff", "B. Wanda Maximoff", "C. Irani Rael ", "D. Ava Starr"))

answers=("D", "A", "A", "C", "B", "B", "B", "A", "B", "A")
guesses=[]
score=0
questionNum=0
for question in questions:
    print("--------------------------------------------------")
    print(question)
    for option in options [questionNum]:
        print(option)

    guess= input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess== answers[questionNum]:
        score += 2
        print("✅Correct!!")

    else:
        print("❌Incorrect!!")
        print(f"The correct answer is {answers[questionNum]}")

    questionNum += 1
print("--------------------------------------------------------------------------------------------------------")
print(f"Your score is {score}/20")
if score == 20:
    print("👑 MCU GOD! Infinity Gauntlet worthy!")
elif score >= 15:
    print("🦸‍♂️ Avenger Level!")
else:
    print("📚 Keep watching! You'll get there!")