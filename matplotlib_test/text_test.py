import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig, ax = plt.subplots()


#title
ax.set_title('Mathematics', fontsize=30, fontweight='bold')


#10x10 grid for positioning text
ax.axis([0, 10, 0, 10])

#remove all ticks and numbers from plot
ax.tick_params(
    axis='both',
    which='both',
    bottom = False,
    top = False,
    labelbottom = False,
    right = False,
    left = False,
    labelleft = False)

#create question text
question_x = 0.1
question_y = 9.5
ax.text(question_x, question_y, "What is 7 + 8", fontsize=30)

#create btn_correct
btn_correct_x = 0.7
btn_correct_y = 0.06
btn_correct_w = 0.1
btn_correct_h = 0.05
btn_correct_axes = fig.add_axes([btn_correct_x, btn_correct_y, btn_correct_w, btn_correct_h])
btn_correct = Button(btn_correct_axes, 'Correct', color="green")
#btn_correct.on_clicked(show_answer)

#create btn wrong
btn_wrong_x = 0.6
btn_wrong_y = 0.06
btn_wrong_w = 0.1
btn_wrong_h = 0.05
btn_wrong_axes = fig.add_axes([btn_wrong_x, btn_wrong_y, btn_wrong_w, btn_wrong_h])
btn_wrong= Button(btn_wrong_axes, 'Wrong', color="red")
#btn_correct.on_clicked(show_answer)

#callback function for showing notes
def show_notes(event):
    print("show notes activated")
    answer_x = 0.1
    answer_y = 9
    answer_spacer = 0.2
    ax.text(answer_x, answer_y, "When adding numbers mentally, try to add the least significant digits first.", fontsize=10, color="blue")
    ax.text(answer_x, answer_y - (answer_spacer * 1), "for example, adding 74 + 39, first start by adding 4 and 9 = 13", fontsize=10, color="blue")
    ax.text(answer_x, answer_y - (answer_spacer * 2), "now add the more significant digits 70 + 30 = 100", fontsize=10, color="blue")
    ax.text(answer_x, answer_y - (answer_spacer * 3), "finally, 100 + 13 = 113", fontsize=10, color="blue")

#create btn notes
btn_notes_x = 0.5
btn_notes_y = 0.06
btn_notes_w = 0.1
btn_notes_h = 0.05
btn_notes_axes = fig.add_axes([btn_notes_x, btn_notes_y, btn_notes_w, btn_notes_h])
btn_notes= Button(btn_notes_axes, 'Notes', color="yellow")
btn_notes.on_clicked(show_notes)

#callback function for showing answer
def show_answer(event):
    answer_x = 0.1
    answer_y = 0.5
    ax.text(answer_x, answer_y, "7 + 8 = 15", fontsize=30, color="green")

#create show answer btn
btn_answer_x = 0.8
btn_answer_y = 0.06
btn_answer_w = 0.1
btn_answer_h = 0.05
btn_answer_axes = fig.add_axes([btn_answer_x, btn_answer_y, btn_answer_w, btn_answer_h])
btn_answer = Button(btn_answer_axes, 'Show Answer')
btn_answer.on_clicked(show_answer)

plt.show()
