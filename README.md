# gazebo-hello-world-turtulebot3
This project is a hello world gazebo project at which we will introduce a turtlebot in a gazebo environment and make it draw my inital 'K' autonomously.

# Package name - project_00. 
I’ve included catkin, rospy, geometry_msgs, message_generation, std_msgs as the dependencies.

# About the Node:
	I’ve constructed a “my_initials” node. Here, I have a server and a client and constructed the project in a way that the client is requesting the server to draw my Initial.
	My server will be listening to the requests from the client. Upon receiving the corresponding data to trace the letter ‘K’, it will make the turtle rotate or move forward by publishing it to the turtle node’s  velocity topic “/turtle1/cmd_vel”.

# rqt_graph :
![rosgraph](https://user-images.githubusercontent.com/55424824/82131820-30e9cb80-978e-11ea-8741-a565288598cb.png)


# My_initials output:
![my_initials](https://user-images.githubusercontent.com/55424824/82131825-3f37e780-978e-11ea-9e4e-ca81b16dd2bd.png)
