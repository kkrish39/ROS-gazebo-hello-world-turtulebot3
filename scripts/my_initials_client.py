#!/usr/bin/env python
import rospy
from project_00.srv import MyInitials

#client handler to send data to draw initials
def draw_initials_client():
    rospy.wait_for_service('my_initials_server')
    try:
        draw_initals = rospy.ServiceProxy('my_initials_server', MyInitials)
        #data to trace the letter K
        letter_K_data_points = [[30,90,'rotate',False],[10,3,'move',True],[30,180,'rotate',False],
        [10,6,'move',True],[30,180,'rotate',False],[10,3,'move',True],
        [30,45,'rotate',True],[10,4,'move',True],[30,180,'rotate',True],
        [10,4,'move',True],[30,90,'rotate',False],[10,4,'move',True]]

        for r in letter_K_data_points:
            draw_initals(r[0], r[1], r[2], r[3])
       
    except rospy.ServiceException, e:
        print("Service call failed: %s"%e)


if __name__ == '__main__':
    print("Cleint sending data to draw the letter K...")
    draw_initials_client()
    print("Data sent successfully...")