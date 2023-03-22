
import turtle

screen = turtle.Screen()
screen.title('Guess the U.S. States name')
image = 'blank_states_img.gif'

# turtle shape can be circle, square etc, but it has no specific shape like our image
# so we will first add the image using addshape
screen.addshape(image)

# now we will use this image to define the shape of our turtle
turtle.shape(image)

screen.exitonclick()