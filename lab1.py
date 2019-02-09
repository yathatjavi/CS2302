# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:34:45 2019

@author: Javier Soto
CS2302
lab 01
"""

import numpy as np
import matplotlib.pyplot as plt
import math 

#method for problem 4
def six_circles(ax,n,center,radius):
    if n>0:
        x,y= circle(center,radius)
        delta_radius = radius*.33333
        #create child circle
        x1,y1=circle(center,delta_radius)
        x2,y2=circle([center[0]-(delta_radius*2),center[1]],delta_radius)
        x3,y3=circle([center[0]+(delta_radius*2),center[1]],delta_radius)
        x4,y4=circle([center[0],center[1]+(delta_radius*2)],delta_radius)
        x5,y5=circle([center[0],center[1]-(delta_radius*2)],delta_radius)
        #plot child circles
        ax.plot(x,y)
        ax.plot(x1,y1)
        ax.plot(x2,y2)
        ax.plot(x3,y3)
        ax.plot(x4,y4)
        ax.plot(x5,y5)
       #recusivley fill all circles
        six_circles(ax,n-1,center,delta_radius)
        six_circles(ax,n-1,[center[0]-(delta_radius*2),center[1]],delta_radius)
        six_circles(ax,n-1,[center[0]+(delta_radius*2),center[1]],delta_radius)
        six_circles(ax,n-1,[center[0],center[1]-(delta_radius*2)],delta_radius)
        six_circles(ax,n-1,[center[0],center[1]+(delta_radius*2)],delta_radius)
        
#method for problem 1
def draw_squares(ax,n,center,w,size):
    if n>0:
        #helper method to retrun the points of the square based of origin
        center = square(center,size/2)
        #draw square with provide points
        ax.plot(center[:,0],center[:,1],color='k')
        #next four recursive call draw children squares
        draw_squares(ax,n-1,center[0],w,size/4)
        draw_squares(ax,n-1,center[1],w,size/4)
        draw_squares(ax,n-1,center[2],w,size/4)
        draw_squares(ax,n-1,center[3],w,size/4)
       
#method for problem 2
def turning_circles(ax,n,origin,radius):
    if n>0:
        #creates np.array of x points and array of y coordinates
        center=[origin[0]+radius,0]
        x,y = circle(center,radius)
        ax.plot(x,y)
        turning_circles(ax,n-1,origin,radius*.50)
         
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)#creates equal spaced lines, n lines, between 0 and 6.3
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def square(center,half_len):
    #4 arrays to hold x,y of each point of the square
    #indiviual lines for easier readability
    #lt= left top ect... will move neg half length and up half length ect...
    lt = np.array([center[0]-half_len,center[1]+half_len])
    rt= np.array([center[0] + half_len,center[1] + half_len])
    rb = np.array([center[0] + half_len,center[1] - half_len])
    lb = np.array([center[0]-half_len,center[1]-half_len])
    points =np.array([lt,rt,rb,lb,lt])
    return points
    

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
        
#method for problem 3
def draw_btree(ax,n,x,y,delta_x,delta_y):
    if n>0:
        #for ease of ploting create 2 lists of corrisponding x,y values
        x_values = [x-delta_x,x,x+delta_x]
        y_values = [y-delta_y,y,y-delta_y]
        ax.plot(x_values,y_values)
        #draw center then left child then right child 
        draw_btree(ax,n-1,x_values[0],y_values[0],delta_x*.5,delta_y*.5)
        draw_btree(ax,n-1,x_values[2],y_values[2],delta_x*.5,delta_y*.5)
    

plt.close("all") 
fig, ax = plt.subplots() 
#six_circles(ax, 4, [0,0], 100)
turning_circles(ax, 10, [0,0], 100)
#draw_circles(ax, 5, [0,0], 100,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
#fig.savefig('circles.png')
'''
plt.close("all") 
orig_size = 1000
#p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
#draw_squares(ax,4,[0,0],(1/4),orig_size)
draw_btree(ax,8,100,100,10,10)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')'''