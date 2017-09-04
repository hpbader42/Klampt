import math
from klampt.math import so3,se3,vectorops

def interpolate_linear(a,b,u):
    """Interpolates linearly in cartesian space between a and b."""
    return vectorops.madd(a,vectorops.sub(b,a),u)

def interpolate_euler_angles(ea,eb,u,convention='zyx'):
    """Interpolates between the two euler angles.
    TODO: The default implementation interpolates linearly.  Can you
    do better?
    """
    return interpolate_linear(ea,eb,u)

def euler_angle_to_rotation(ea,convention='zyx'):
    """Converts an euler angle representation to a rotation matrix.
    Can use arbitrary axes specified by the convention
    arguments (default is 'zyx', or roll-pitch-yaw euler angles).  Any
    3-letter combination of 'x', 'y', and 'z' are accepted.
    """
    axis_names_to_vectors = dict([('x',(1,0,0)),('y',(0,1,0)),('z',(0,0,1))])
    axis0,axis1,axis2=convention
    R0 = so3.rotation(axis_names_to_vectors[axis0],ea[0])
    R1 = so3.rotation(axis_names_to_vectors[axis1],ea[1])
    R2 = so3.rotation(axis_names_to_vectors[axis2],ea[2])
    return so3.mul(R0,so3.mul(R1,R2))

#TODO: play around with these euler angles -- they'll determine the start and end of the rotations
ea = [math.pi/4,0,0]
eb = [math.pi*7/4,0,0]



def do_interpolate(u):
    global ea,eb
    #linear interpolation with euler angles
    e = interpolate_euler_angles(ea,eb,u)
    return euler_angle_to_rotation(e)
    #TODO: at the end of Problem 4.2, comment out the 3 prior lines and
    #uncomment this one.
    #return so3.interpolate(euler_angle_to_rotation(ea),euler_angle_to_rotation(eb),u)


# Use the space below to answer the written questions posed in Problem 4.2.
#
#
#
#
#
#
#

