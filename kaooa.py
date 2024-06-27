import turtle
error = 20
import time
screen = turtle.Screen()
new_turtle_for_writing = turtle.Turtle()
# Set the background color
screen.bgcolor("black")
def draw_star(side_length):
    turtle.penup()
    turtle.goto(-side_length/2, 0)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color('white')
    intersection_points = []
    for i in range(0,5):
        turtle.forward(side_length)  
        turtle.speed(10)
        x, y = turtle.pos()   
        intersection_points.append((x, y))
        turtle.right(144)     

    return intersection_points
chance = 0
all_points = [(-4.263256414560601e-14, 145.30850560107217),(200.0, 0.0),   (123.60679774997907, -235.11410091698917),(-123.60679774997891, -235.1141009169893), (-200.0, -8.526512829121202e-14),(-47.0, -1.0),(48.0, -2.0),(76.0, -87.0),(-1.0, -145.0),(-75.0, -89.0)]
turtle_for_points = []
for kkk in all_points:
    k = turtle.Turtle()
    k.shape('circle')
    k.shapesize(2)
    k.color('grey')
    k.speed(10)
    k.penup()

    turtle_for_points.append(k)
    k.setpos(kkk)
all_turtle_vulture = turtle.Turtle()
graph_crow_move ={
    1: [6,7],
    2: [7,8],
    3: [8,9],
    4: [9,10],
    5:  [10,6],
    6: [1,5,7,10],
    7: [1,2,6,8],
    8: [2,3,7,9],
    9: [3,4,8,10],
    10: [4,5,6,9],
}
graph_vulture_move = {
    1: [6,7,10,8],
    2: [7,8,6,9],
    3: [9,8,10,7],
    4: [9,10,8,6],
    5: [10,6,9,7],
    6: [5,1,7,10,2,4],
    7: [1,2,6,8,5,3],
    8: [2,3,7,9,1,4],
    9: [3,4,10,8,5,2],
    10: [4,5,6,9,1,3],
}
def write_message(message):
    global new_turtle_for_writing
    new_turtle_for_writing.clear()
    new_turtle_for_writing.penup()
    new_turtle_for_writing.hideturtle()
    new_turtle_for_writing.setpos(-100,-400)
    new_turtle_for_writing.color('white')
    new_turtle_for_writing.pendown()
    new_turtle_for_writing.write(message, font=("Arial", 16, "normal"))
# def #(message):
#     global new_turtle_for_writing
#     new_turtle_for_writing.clear()
#     new_turtle_for_writing.penup()
#     new_turtle_for_writing.hideturtle()
#     new_turtle_for_writing.setpos(-150,-300)
#     new_turtle_for_writing.color('red')
#     new_turtle_for_writing.pendown()
#     new_turtle_for_writing.write(message, font=("Arial", 16, "normal"))
    # time.sleep(0.5)
flag_crow = [0,0,0,0,0,0,0,0,0]
all_turtle_crow = []
total_crows = 0
vulture_points = 0 
def give_me_exact_coordinates(x,y):
    for point in all_points:
        if x+error>=point[0] and x - error<=point[0] and y + error >=point[1] and y - error<=point[1]:
            return (point[0], point[1])
def return_node(x,y):
    global all_points
    lol = 0 
    for point in all_points:
        lol = lol+1    
        if give_me_exact_coordinates(x,y) != None:
            (lol_x,lol_y) = give_me_exact_coordinates(x,y)
        if lol_x==point[0] and lol_y==point[1]:
            return lol 
def move_possible_crow(curx,cury,x,y):
    list_of_neghbours =  graph_crow_move[return_node(curx,cury)]
    # print(f"all possible neigbours {list_of_neghbours} {return_node(curx,cury)}")
    for neighbour in list_of_neghbours:
        if all_points[neighbour-1][0]+error>=x and all_points[neighbour-1][0]-error<=x and all_points[neighbour-1][1]+error>=y and all_points[neighbour-1][1]-error<=y:

            return True
        # else:
    return False
def if_can_kill():
    global all_turtle_vulture
    global graph_vulture_move
    global occupied_array
    (v_x,v_y) = all_turtle_vulture.pos()
    node1 = return_node(v_x,v_y)
    list = graph_vulture_move[node1]
    if len(list)==6:
        count = 0 
        for i in range(len(list)):
            # if i %2==1:
            #     continue
            if i < 2:
                continue
            if i >=4:
                continue
            
          
            if occupied_array[list[i]-1]==1 and occupied_array[list[i+2]-1]==0:
                return True
                # return True
    if len(list)==4:
        count = 0 
        for i in range(len(list)):
            # if i %2==0:
            #     continue
            # if count>=2:
            if i >=2:
                continue
            if occupied_array[list[i]-1]==1 and occupied_array[list[i+2]-1]==0:
                return True
                    # return True
            count = count+1
    return False
    # for turtle in all_turtl:

def move_possible_vulture(curx,cury,x,y):
    list_of_neighbouts = graph_vulture_move[return_node(curx,cury)]
    # print(return_node(curx,cury))
    
    # print("list of neighbours")
    # print(list_of_neighbouts)
    count = 0
    flag_can_kill = 0  
    if if_can_kill()==True:
        flag_can_kill = 1 
    for neighbour in list_of_neighbouts:
        
        if all_points[neighbour-1][0]+error>=x and all_points[neighbour-1][0]-error<=x and all_points[neighbour-1][1]+error>=y and all_points[neighbour-1][1]-error<=y:
            if len(list_of_neighbouts)==6:
                if flag_can_kill==1:
                    if count<4:
                        continue
                if count>=4:

                    if occupied_array[list_of_neighbouts[count-2]-1]==0:
                        return False
            elif len(list_of_neighbouts)==4:
                if flag_can_kill==1:
                    if count<2:
                        continue
                if count>=2:
                    # print(f"occupied array {occupied_array[list_of_neighbouts[count-2]]}")
                    if occupied_array[list_of_neighbouts[count-2]-1]==0:
                        return False
            return True
        count = count +1 
        # else:
    return False
def get_mouse_click_coor(x, y):
    print(x, y)
def distance(x,y,x1,y1):
    distance = ((x-x1)**2 + (y-y1)**2)**0.5
    return distance
occupied_array=[0,0,0,0,0,0,0,0,0,0,0]
def check_occupied(x,y):
    node_number = return_node(x,y)
    if occupied_array[node_number-1]==1:
        return True
    else:
        return False
def jump_correct(x,y):
    global vulture_points
    global flag_crow; 
    (x1,y1) = give_me_exact_coordinates(x,y)
    # print(f"exact coordinates are {x1,y1}")
    (vulture_pos_x,vulture_pos_y) = all_turtle_vulture.pos()
    # print(f"vulture ppints are {vulture_pos_x,vulture_pos_y}")
    current_slope = (y1 - vulture_pos_y)/(x1-vulture_pos_x)

    # print(f"initial slope {current_slope}")
    for turtle in all_turtle_crow:
        
        (crow_x,crow_y) = turtle.pos()
        if vulture_pos_x<x1:
            if crow_x>x1 or crow_x<vulture_pos_x:
                continue
        elif vulture_pos_x >x1:
            if crow_x>vulture_pos_x or crow_x<x1:
                continue
        elif vulture_pos_y<y1:
            if crow_y>y1 or crow_y<vulture_pos_y:
                continue
        elif vulture_pos_y>y1:
            if crow_y<y1 or crow_y>vulture_pos_y:
                continue
            
        if crow_x == 300 and crow_y == 300 :
            continue
        # print(f"crow points are {crow_x,crow_y}")
        new_slope = (y1 - crow_y)/(x1-crow_x)
        # print(f"slope is {new_slope}")
        
        if  new_slope+0.6 >= current_slope and new_slope-0.6<=current_slope:
            return turtle
    return 0 
def move(x, y, a, b):
    # print("yes")
    for turtle in all_turtle_crow:
        if x+error>=turtle.xcor() and x - error <=turtle.xcor():
            if y+error>=turtle.ycor() and y-error<=turtle.ycor():
                # print("yes")
                turtle.setposition(a,b)
                break

def valid_point(x,y):
    for point in all_points:
        if point[0]+error>=x and point[0]-error<=x:
            if point[1]+error>=y and point[1] - error<=y:
                return True 

    return False 

def drag_handler(x, y):
    turtle.goto(x, y)
def get_coor(x,y,x1,y1):
    # print(x,y,x1,y1)
    for turtle in all_turtle_crow:
        (crow_x,crowy) = turtle.pos()
        if x+error >=crow_x and x-error<=crow_x and y+ error>=crowy and y - crowy<=crowy:
            make_occupied_modified(x1,y1,turtle)
            turtle.setpos(x1,y1)
check_flag_111 = 0 
prev_y_checked = 0 
prev_x_checked = 0 
def check_vulture():
    global all_turtle_vulture
    global graph_vulture_move
    global occupied_array
    (v_x,v_y) = all_turtle_vulture.pos()
    node = return_node(v_x,v_y)
    list1 = graph_vulture_move[node]
    # print(list1)
    for i in list1:
        # print(f"{occupied_array[i-1]}")
        if occupied_array[i-1]==0:
            return True
    return False
def decide_chance(x,y):
    global new_turtle_for_writing
    global chance; 
    global vulture_points 
    global total_crows
    global prev_x_checked
    global prev_y_checked
    global check_flag_111
    if  chance>1 and check_vulture()==False :
        print("crow win")
        exit()
    if vulture_points == 4:
        print("vulture win")
        exit()
    
    if  valid_point(x,y)==False:
            #("invalid move")
            if check_flag_111 == 1:
                check_flag_111 = 0
                # print("came in check flag 111")
                chance = 4
                return 
            chance = chance -1 
    else:
        node = return_node(x,y)
        if check_flag_111 == 1 :
            if occupied_array[return_node(x,y)-1]==0 :
                check_flag_111 = 0 
                # chance = chance
                return
            for turtle1 in all_turtle_crow:
                # (t_x,t_y) = turtle.pos()
                # print("OK!!!")
                (l_x,l_y) = turtle1.pos()
                (x1,y1) = (0,0)
                if  give_me_exact_coordinates(l_x,l_y) != None:
                    (x1,y1) = give_me_exact_coordinates(l_x,l_y)
                    # print(x1,y1,all_points[node-1][0], all_points[node-1][1])
                # if t_x+error>=x and t_x-error<=x and t_y+error>=y and t_y-error<=y :
                if x1 == all_points[node-1][0] and y1==all_points[node-1][1]:
                    if move_possible_crow(all_points[node-1][0],all_points[node-1][1], prev_x_checked,prev_y_checked) == True:
                        make_occupied_modified(prev_x_checked,prev_y_checked,turtle1)
                        turtle1.setpos(prev_x_checked,prev_y_checked)
                        check_flag_111 = 0 
                        chance = chance+1
                        # print(chance)
                        if chance>1:
                            color_all_possible_for_vulture()
                        if  chance>1 and check_vulture()==False :
                            write_message("crow win")
                            print("crow win")
                            time.sleep(3)
                            exit()
                        write_message('vulture turn ')
                        return 
                    else:
                        print("not possible to move crow to that position")
                        # chance = chance
                        check_flag_111= 0 
                        if  chance>1 and check_vulture()==False :
                            write_message("crow win")
                            print("crow win")
                            time.sleep(3)
                            exit()
                        write_message('crow turn')
                        # check_flag_111 = 0  
                        return 
        if check_occupied(x,y)==True:
            #("invalid move due to occupancy")
            # if chance%2 -- 
            chance = chance-1 
        else:
            if chance%2==0 :
                
                if total_crows>=7:
                    if check_flag_111 == 0 :
                        prev_x_checked = x
                        prev_y_checked = y 
                        check_flag_111 = 1 
                        if  chance>1 and check_vulture()==False :
                            write_message("crow win")
                            
                            print("crow win")
                            time.sleep(3)
                            exit()
                        return 
                else:
                    place_crow(node)
                if  chance>1 and check_vulture()==False :
                    print("crow win")
                    exit()
                write_message('vulture turn')
                if chance>1:
                    color_all_possible_for_vulture()
            elif chance%2==1:
                
                (vulture_pos_x,vulture_pos_y) = all_turtle_vulture.pos()
                # print("yes just above func")
                
                if chance>1:
                    # print("yes just above func")
                    if move_possible_vulture(vulture_pos_x,vulture_pos_y,x,y) == False:
                        print("invalid move, vulture can not move to that position ")
                        write_message('vulture turn')
                        return 
                        # return 
                    else:
                        place_vulture(node)
                else:
                    place_vulture(node)
                # if check_crow_ended()
                if vulture_points==4:
                    write_message('vulture win')
                    # screen.clear()
                    # turtle.write("vulture win")
                    print("vulture win")
                    print("game over")
                    time.sleep(3)
                    exit()
                write_message('crow turn')
                color_all_possible_grey()

    
    chance = chance+1
def color_all_possible_grey():
    global turtle_for_points
    global occupied_array
    count = 0 
    for turtle in turtle_for_points:
        if occupied_array[count]==0:
            turtle.color('grey')
        count = count+1
def color_all_possible_for_vulture():
    global all_turtle_vulture
    global all_points
    global turtle_for_points
    global occupied_array
    (v_x,v_y) = all_turtle_vulture.pos()
    lol = 0 
    for turtle in turtle_for_points:
        if occupied_array[lol]==0:
            turtle.color('grey')
        lol = lol +1 
    count = 0 
    for point in all_points:
        if move_possible_vulture(v_x,v_y,point[0],point[1])==True:
            if occupied_array[count]==0:
                turtle_for_points[count].color('green')
        count = count +1 
            
def make_occupied_modified(x,y, turtle1):
    global occupied_array
    (v_x,v_y) = turtle1.pos()
    node_prev = return_node(v_x,v_y)
    node_new = return_node(x,y)
    occupied_array[node_prev-1] = 0 
    occupied_array[node_new-1] = 1
def make_occupied_empty(x,y):
    global occupied_array
    node_new = return_node(x,y)
    occupied_array[node_new -1] = 0 
vulture_count = 0 
def place_vulture(node):
    global vulture_count
    global chance
    global all_turtle_vulture
    global vulture_points
    global occupied_array
    global turtle_for_points
    # print(f"node in place vulture{node}")
    if occupied_array[node-1]==0:
        if chance>1:
            make_occupied_modified(all_points[node-1][0],all_points[node-1][1],all_turtle_vulture)
        crow_jump_turtle = jump_correct(all_points[node-1][0], all_points[node-1][1])
        if crow_jump_turtle != 0 and vulture_count==1 :
            (crow_x,crow_y) = crow_jump_turtle.pos()
            make_occupied_empty(crow_x,crow_y)
            crow_jump_turtle.setposition((300,300 - 50*vulture_points))
            crow_jump_turtle.color('red')
            turtle_for_points[return_node(all_points[node-1][0],all_points[node-1][1])-1].color('grey')
            all_turtle_vulture.setposition(all_points[node-1][0],all_points[node-1][1])
            vulture_points = vulture_points+1
        if vulture_count==1:
            turtle_for_points[return_node(all_points[node-1][0],all_points[node-1][1])-1].color('grey')

            all_turtle_vulture.setposition(all_points[node-1][0],all_points[node-1][1])
        else :
            # print("yes trying to do ")
            all_turtle_vulture.shape('circle')
            all_turtle_vulture.color('yellow')
            all_turtle_vulture.penup()
            all_turtle_vulture.speed(0)
            turtle_for_points[return_node(all_points[node-1][0],all_points[node-1][1])-1].color('grey')

            all_turtle_vulture.setposition(all_points[node-1][0],all_points[node-1][1])
            vulture_count = vulture_count+1
        
        occupied_array[node-1] =1 
        # print("vulture tried to occupy")
    # else:
    #     print("check")
    

def place_crow(node):
    global occupied_array
    global chance
    global all_turtle_crow
    global flag_crow
    global total_crows
    global occupied

    if occupied_array[node-1]==0:
        new_player = turtle.Turtle()
        new_player.shape('circle')
        new_player.color("#00FFFF")
        new_player.penup()
        new_player.speed(0)
        new_player.setposition(all_points[node-1][0],all_points[node-1][1])
        all_turtle_crow.append(new_player)
        total_crows = total_crows+1
        flag = 1 
        occupied_array[node-1] = 1 
    else:
        print("invalid position for placing crow!!!!")
        chance = chance-1 
      
    
star_side_length = 400

star_intersection_points = draw_star(star_side_length)
star_intersection_points.append((-47.0, -1.0))
star_intersection_points.append((-75.0, -89.0))
star_intersection_points.append((-1.0, -145.0))
star_intersection_points.append((76.0, -87.0))
star_intersection_points.append((48.0, -2.0))

# turtle.title("yess")
my_turtle = turtle.Turtle()

# Move the turtle to a starting position (optional)
my_turtle.penup()
my_turtle.goto(-50, -300)
my_turtle.pendown()
my_turtle.color('white')
# Write something on the screen
# my_turtle.write("Hello, Turtle!", font=("Arial", 16, "normal"))
turtle.onscreenclick(decide_chance)
turtle.mainloop()
# while True:
#     turtle.write("gopal")
# Close the turtle graphics window on click
# turtle.exitonclick()