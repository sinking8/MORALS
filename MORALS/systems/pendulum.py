import numpy as np 
from MORALS.systems.system import BaseSystem

class Pendulum(BaseSystem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "pendulum"

        self.l = 0.5
        self.state_bounds = np.array([[-self.l, self.l], [-self.l, self.l], [-2*self.l*np.pi, 2*self.l*np.pi], [-2*self.l*np.pi, 2*self.l*np.pi]])
        
    def transform(self,s):
        x = self.l * np.sin(s[:,0])
        y = self.l * np.cos(s[:,0])
        xdot = self.l * np.cos(s[:,0]) * s[:,1]
        ydot = -self.l * np.sin(s[:,0]) * s[:,1]
        return np.array([x,y,xdot,ydot]).T

    import numpy as np

    def reverse_transform(self,x, y, xdot, ydot,):
        # Recover theta (angle)
        theta = np.arctan2(x, y)

        # Recover theta_dot (angular velocity)
        theta_dot_x = xdot / (self.l * np.cos(theta))
        theta_dot_y = -ydot / (self.l * np.sin(theta))

        # Average theta_dot for numerical stability
        theta_dot = (theta_dot_x + theta_dot_y) / 2.0

        # Combine theta and theta_dot to form the state vector s
        s = np.vstack((theta, theta_dot)).T
        return s

    
    # def transform(self,s):
    #     x = self.l * np.sin(s[0])
    #     y = self.l * np.cos(s[0])
    #     xdot = self.l * np.cos(s[0]) * s[1]
    #     ydot = -self.l * np.sin(s[0]) * s[1]
    #     return np.array([x,y,xdot,ydot])
    
    # def inverse_transform(self,s):
    #     theta = np.arctan2(s[0],s[1])
    #     thetadot = -(-s[1] * s[2] + s[0] * s[3]) / (s[0]*s[0] + s[1]*s[1])
    #     return np.array([theta,thetadot])
     
    def inverse_transform(self,s):
        theta = np.arctan2(s[:,0],s[:,1])
        thetadot = -(-s[:,1] * s[:,2] + s[:,0] * s[:,3]) / (s[:,0]*s[:,0] + s[:,1]*s[:,1])
        return np.array([theta,thetadot])
    
    def get_true_bounds(self):
        return np.array([[-np.pi, np.pi], [-2*np.pi, 2*np.pi]])