#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    # Initialiser le nœud ROS
    rospy.init_node('circle_turtle', anonymous=True)

    # Créer un éditeur pour le sujet /turtle1/cmd_vel
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Définir la fréquence de publication des messages
    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        # Créer un message Twist
        twist = Twist()

        # Définir les composantes du message Twist pour faire un cercle
        twist.linear.x = 2.0 # Avancer avec une certaine vitesse linéaire
        twist.angular.z = 1.0 # Tourner avec une certaine vitesse angulaire

        # Publier le message
        pub.publish(twist)

        # Dormir jusqu'à la prochaine itération
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
