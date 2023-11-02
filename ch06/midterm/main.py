import turtle

branch_length = int(input("Please enter the length of the branch (reccomended is larger than 80): "))
leaf_color = input("Please enter the color you would like your leaves to be (make sure to spell correctly!): ")
screen = turtle.Screen()
screen.bgcolor("lightblue")

def draw_tree(branch_length = 0, leaf_color = ""):
    
    """
    Draws the tree that the user provides parameters for.
    
    Args:
        branch_length (int): is used in the algorith for the length of the branches on the tree
        leaf_color (string): is used to decide the color that the leaves will be on the tree
    Returns:
        branch_length (int): confirms with the user their input in the main function
        leaf_color (string): confirms with the user their input in the main function
    """
    
    branch_length = branch_length
    tree_bark_color = "brown"
    tree_turtle = turtle.Turtle()
    tree_turtle.speed(0)

    def draw_branch(branch_length):
        if branch_length > 5:
            tree_turtle.forward(branch_length)
            tree_turtle.color(tree_bark_color)
            tree_turtle.pensize(branch_length / 10)

            tree_turtle.right(20)
            draw_branch(branch_length - 15)

            tree_turtle.left(40)
            draw_branch(branch_length - 15)

            tree_turtle.color(leaf_color)
            tree_turtle.pensize(100/branch_length * 8)
            tree_turtle.right(20)
            tree_turtle.backward(branch_length)

    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(220)
    tree_turtle.down()
    
    draw_branch(branch_length)
    
    tree_turtle.color(tree_bark_color)
    tree_turtle.pensize(branch_length / 5)
    tree_turtle.forward(branch_length)
    tree_turtle.up()
    tree_turtle.backward(branch_length)
    tree_turtle.down()
    
    screen.exitonclick()
    return branch_length, leaf_color

def draw_ground():
    
    """
    Draws the ground that the tree is drawn on creating depth.
    
    No Args
    
    No Return
    """
 
    ground_turtle = turtle.Turtle()
    ground_turtle.speed(0)
    ground_color = "green"

    y_ground = -screen.window_height() / 3

    ground_turtle.penup()
    ground_turtle.goto(-screen.window_width() / 2, y_ground)
    ground_turtle.pendown()

    ground_turtle.fillcolor(ground_color)

    ground_turtle.begin_fill()

    ground_turtle.forward(screen.window_width())
    ground_turtle.right(90)
    ground_turtle.forward(screen.window_height() / 3)
    ground_turtle.right(90)
    ground_turtle.forward(screen.window_width())
    ground_turtle.right(90)
    ground_turtle.forward(screen.window_height() / 3)

    ground_turtle.end_fill()
    ground_turtle.hideturtle()
    

def main():
    draw_ground()
    tree_values = draw_tree(branch_length, leaf_color)
    print(tree_values[0], "is the length of the branches that was chosen and", tree_values[1], "is the color of the leaves!" )

main()