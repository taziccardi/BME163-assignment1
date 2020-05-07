import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import math

plt.style.use('BME163.mplstyle') #sets standard settings

figureHeight = 2
figureWidth = 3.42

plt.figure(figsize = (figureWidth,figureHeight))

panelWidth = 1
panelHeight = 1

relativePanelWidth = panelWidth/figureWidth
relativePanelHeight = panelHeight/figureHeight

# left,bottom,width,height
panel1 = plt.axes([0.1,0.2,relativePanelWidth,relativePanelHeight])
panel2 = plt.axes([0.55,0.2,relativePanelWidth,relativePanelHeight])

#defines colors as RGB values
blue = (0,0,1)
red = (1,0,0)
green = (0,1,0)
yellow = (1,1,0)
black = (0,0,0)
white = (1,1,1)

#dots in panel1
xList = np.arange(0,(math.pi/2),0.06)

f = 0 #counter for fade effect in panel1
for value in xList:
    xvalue = np.cos(value)
    yvalue = np.sin(value)
    panel1.plot(xvalue-0.025,yvalue-0.04,
                marker = 'o',
                markerfacecolor = (1-f,1-f,1-f),
                markeredgecolor = 'black',
                markersize = 2,
                markeredgewidth = 0,
                linewidth = 0)
    if f < 1:
        f += 1/27
    else:
        f = 1

R = np.linspace(red[1],red[0],11)
G = np.linspace(green[0],green[1],11)
B = np.linspace(blue[2],blue[2],11)

#rectangles in panel2
r = -1 #counter for rows, fading from blue to pink
for x in np.arange(0,1,0.1):
    c = 0 #counter for collumns, fading from blue/pink to light blue/white
    r += 1
    for i in np.arange(0,1,0.1):
        rectangle = mplpatches.Rectangle([i,x],0.1,0.1,
                            facecolor = (R[c],G[r],B[c]),
                            edgecolor = 'black',
                            linewidth = 1)
        c += 1
        panel2.add_patch(rectangle)

panel1.set_xlim(0,1)
panel1.set_ylim(0,1)

#removes all labels and axis
panel1.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False,
                   right=False, labelright=False,
                   top=False, labeltop=False)
panel2.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False,
                   right=False, labelright=False,
                   top=False, labeltop=False)

plt.savefig('HW1.png',dpi = 600)
