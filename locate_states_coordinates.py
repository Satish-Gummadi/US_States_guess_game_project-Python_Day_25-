# # this code will return the coordinates of the state when clicked on the US map
# # the values of the same have been added to 50_states.csv file corresponding to its state name
# import turtle
#
# screen = turtle.Screen()
# screen.title('Guess the U.S. States name')
# image = 'blank_states_img.gif'
# screen.addshape(image)
# turtle.shape(image)
#
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# # this will keep our screen open even under clicks unlike screen.exitonclick() command
# turtle.mainloop()

import pandas as pd

fd = pd.read_csv('50_states.csv')

for i in fd.state:
    print(i)
#
# print(fd.loc[fd['state'] == 'Ohio'])
#
# x = fd.loc[fd['state'] == 'Ohio'].y
#
#
# print(x.iloc[0])