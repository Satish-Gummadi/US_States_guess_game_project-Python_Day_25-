
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('Guess the U.S. States name')
image = 'blank_states_img.gif'
# turtle shape can be circle, square etc, but it has no specific shape like our image
# so we will first add the image using addshape
screen.addshape(image)
# now we will use this image to define the shape of our turtle
turtle.shape(image)

df = pd.read_csv('50_states.csv')
guessed_set = []
t = turtle.Turtle()
t.penup()

game_is_on = True
score = 0
while score < 50:
    answer_state = screen.textinput(title=f'{score}/50 Guess the state',prompt="What's the name of the other state?")
    answer_state = answer_state.title()
    # print(answer_state)
    if answer_state == 'Exit':              #to exit the screen when we are done
        break

    for state in df.state:
        if answer_state in guessed_set:
            break
        elif answer_state == state:
            score += 1
            guessed_set.append(answer_state)
            t.hideturtle()
            x = df[df.state == answer_state].x
            y = df[df.state == answer_state].y
            t.goto(x.item(),y.item())
            t.write(answer_state,align='center')
    # print(score)

# now to print all the states which we have not guessed
for state in df.state:
    t.speed(7)
    if state not in guessed_set:
        x = df[df.state == state].x
        y = df[df.state == state].y
        t.goto(x.item(),y.item())
        t.color('red')
        t.write(state,align='center')

print(f'Your score is {score}/50')

turtle.mainloop()
# turtle.exitonclick()