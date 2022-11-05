# Maths Game
# By theadventureofe(John Gormley)
# A game to test your skills
# the_adventure_of_e λ

import random

class Question:
    def __init__(self, category, english, answer, notes =  ""):
        self.category = category
        self.english = english
        self.answer = answer
        self.notes = notes

# questions to ask
polish_level = [1,2]
russian_level =[1,2]
irish_level = [2]

# create list of questions
questions = []

#LEVEL 1. YES/NO
if 1 in polish_level:
    questions.append( Question("Polish", "yes", "tak", "tak"))
    questions.append( Question("Polish", "no", "nie", "nyeh"))

if 1 in russian_level:
    questions.append( Question("Russian", "no", "нет", "nyet"))
    questions.append( Question("Russian", "yes", "да", "da"))

#LEVEL 2. GREETINGS AND BYES
if 2 in polish_level:
    questions.append( Question("Polish", "hi", "cześć", "cheisch"))
    questions.append( Question("Polish", "goodbye", "do widzenia", "oh veeDENya"))

if 2 in russian_level:
    questions.append( Question("Russian", "hi", "привет", "PRI-vi-et"))
    questions.append( Question("Russian", "goodbye", "до свидания", "daw svi-DAN-ya"))

if 2 in irish_level:
    questions.append( Question("Irish", "hi", "dia duit", "jee-ah ditch"))
    questions.append( Question("Irish", "goodbye", "slán", "slaun"))

#LEVEL 3. MAN WOMAN CHILD
if 3 in polish_level:
    questions.append( Question("Polish", "man", "mężczyzna", "mess-CHEZ-nah"))
    questions.append( Question("Polish", "woman", "kobieta", "co-biet-ah"))
    questions.append( Question("Polish", "child", "dziecko", "jiets-co"))

if 3 in russian_level:
    questions.append( Question("Russian", "man", "мужчина", "moo-SHEEN-ah"))
    questions.append( Question("Russian", "woman", "женщина", "ZJANE-shin-ah"))
    questions.append( Question("Russian", "child", "ребёнок", "Ree-bion-ok"))

if 3 in irish_level:
    questions.append( Question("Irish", "man", "fear", "far"))
    questions.append( Question("Irish", "woman", "bean", "ban"))
    questions.append( Question("Irish", "child", "páiste", "posh-cha"))

#level 4: COMMON FOOD
if 4 in polish_level:
    questions.append( Question("Polish", "bread", "chleb", "Hhhleb"))
    questions.append( Question("Polish", "apple", "jabłko", "YAB-ko"))
    questions.append( Question("Polish", "cabbage", "kapusta", "kah-POOST-ah"))

if 4 in russian_level:
    questions.append( Question("Russian", "bread", "хлеб", "Hhhleb"))
    questions.append( Question("Russian", "apple", "яблоко", "YAB-lah-kah"))
    questions.append( Question("Russian", "cabbage", "капуста", "kah-POOST-ah"))

if 4 in irish_level:
    questions.append( Question("Irish", "bread", "arán", "arawn"))
    questions.append( Question("Irish", "apple", "úll", "ool"))
    questions.append( Question("Irish", "cabbage", "cabáiste", "ca-bauw-styah"))



def print_q(q_number, question):
    if question.category == "Russian" or question.category == "Polish" or question.category == "Irish":
       print(str(q_number) + ". (" + question.category + ") How do you say " + question.english + " in " + question.category + "?")

already_asked = []
got_correct = []
got_wrong = []

def ask_q():
        q_num = random.randrange(0, len(questions))

        # check question is not already asked
        # if not, ask question
        #add to questions already asked
        if q_num not in already_asked:
            already_asked.append(q_num)
            print_q(ask_q.counter, questions[q_num])
            answer_given = input(": ")

            if answer_given == questions[q_num].answer:
                print("correct")
                got_correct.append(q_num)
            else:
                print("WRONG! The correct answer is", questions[q_num].answer)
                got_wrong.append(q_num)

            ask_q.counter += 1

            print("Pronounced like: " + questions[q_num].notes)
            print()
        else:
            ask_q() #RECURSION!!!! to always ask a valid question

ask_q.counter = 1 #static variable to count questions

def main():
    print(len(questions))
    for i in range(len(questions)):
        ask_q()

    print("you got " + str(len(got_correct)) + " correct")
    print("you got " + str(len(got_wrong)) + " wrong")


if __name__ == "__main__":
    main()
