# Autogenerated with SMOP 
from smop.core import *
# FixedAxisFPFGrowth.m

    
@function
def FixedAxisFPFGrowth(yp=None,psect=None,pramp=None,pslip=None,G=None,*args,**kwargs):
    varargin = FixedAxisFPFGrowth.varargin
    nargin = FixedAxisFPFGrowth.nargin

    #FixedAxisFPFGrowth plots the evolution of a simple step, fixed axis
#fault propagation fold and adds growth strata for a given subsidence 
#versus uplift rate
    
    #   USE: frames = FixedAxisFPFGrowth(yp,psect,pramp,pslip,G)
    
    #   yp = Datums or vertical coordinates of undeformed, horizontal beds
#   psect = A 1 x 2 vector containing the extent of the section, and the 
#           number of points in each bed
#   pramp = A 1 x 2 vector containing the x coordinate of the lower bend in
#           the decollement, and the ramp angle 
#   pslip = A 1 x 2 vector containing the total and incremental slip
#   G = Subsidence versus uplift rate
#   frames = An array structure containing the frames of the fold evolution
#            You can play the movie again just by typing movie(frames)
#   
#   NOTE: Input ramp angle should be in radians
    
    #MATLAB script written by Nestor Cardozo for the book Structural 
#Geology Algorithms by Allmendinger, Cardozo, & Fisher, 2011. If you use
#this script, please cite this as "Cardozo in Allmendinger et al. (2011)"
    
    # Base of layers
    base=yp[1]
# FixedAxisFPFGrowth.m:25
    #Top of layers
    top=yp[max(size(yp))]
# FixedAxisFPFGrowth.m:27
    #Extent of section and number of points in each bed
    extent=psect[1]
# FixedAxisFPFGrowth.m:30
    npoint=psect[2]
# FixedAxisFPFGrowth.m:30
    #Make undeformed beds geometry: This is a grid of points along the beds
    xp=arange(0.0,extent,extent / npoint)
# FixedAxisFPFGrowth.m:32
    XP,YP=meshgrid(xp,yp,nargout=2)
# FixedAxisFPFGrowth.m:33
    #Fault geometry and slip
    xramp=pramp[1]
# FixedAxisFPFGrowth.m:36
    ramp=pramp[2]
# FixedAxisFPFGrowth.m:36
    slip=pslip[1]
# FixedAxisFPFGrowth.m:37
    sinc=pslip[2]
# FixedAxisFPFGrowth.m:37
    #Number of slip increments
    ninc=round(slip / sinc)
# FixedAxisFPFGrowth.m:39
    # Make ten growth strata
    nincG=round(ninc / 10)
# FixedAxisFPFGrowth.m:42
    # Initialize count of growth strata to 1
    countG=1
# FixedAxisFPFGrowth.m:44
    #Solve model parameters
#First equation of Eq. 11.16
    gam1=(pi - ramp) / 2.0
# FixedAxisFPFGrowth.m:48
    #Second equation of Eq. 11.16
    gamestar=acot((3.0 - dot(2.0,cos(ramp))) / (dot(2.0,sin(ramp))))
# FixedAxisFPFGrowth.m:50
    #Third equation of Eq. 11.16
    gamistar=gam1 - gamestar
# FixedAxisFPFGrowth.m:52
    #Fourth equation of Eq. 11.16
    game=acot(cot(gamestar) - dot(2.0,cot(gam1)))
# FixedAxisFPFGrowth.m:54
    #Fifth equation of Eq. 11.16
    gami=asin((dot(sin(gamistar),sin(game))) / sin(gamestar))
# FixedAxisFPFGrowth.m:56
    #Ratio of backlimb length to total slip (P/S) (Eq. 11.17)
    a1=cot(gamestar) - cot(gam1)
# FixedAxisFPFGrowth.m:58
    a2=1.0 / sin(ramp) - (sin(gami) / sin(game)) / sin(game + gami - ramp)
# FixedAxisFPFGrowth.m:59
    a3=sin(gam1 + ramp) / sin(gam1)
# FixedAxisFPFGrowth.m:60
    lbrat=a1 / a2 + a3
# FixedAxisFPFGrowth.m:61
    #Change in slip across boundary between backlimb and forelimb (Eq. 11.19)
    R=sin(gam1 + ramp) / sin(gam1 + game)
# FixedAxisFPFGrowth.m:63
    # Incremental Crestal uplift. Eq. 15 of Hardy and Poblet (2005)
    inccrupl=dot((sin(gam1) / sin(gam1 + game)),sin(game))
# FixedAxisFPFGrowth.m:65
    #From the origin of each bed compute the number of points that are in the
#hanging wall. These points are the ones that will move. Notice that this
#has to bee done for each slip increment, since the fault propagates
    hwid=zeros(ninc,size(yp,2))
# FixedAxisFPFGrowth.m:70
    for i in arange(1,ninc).reshape(-1):
        uplift=dot(dot(dot(lbrat,i),sinc),sin(ramp))
# FixedAxisFPFGrowth.m:72
        for j in arange(1,size(yp,2)).reshape(-1):
            if yp[j] - base <= uplift:
                hwid[i,j]=0
# FixedAxisFPFGrowth.m:75
                for k in arange(1,size(xp,2)).reshape(-1):
                    if xp[k] <= xramp + (yp[j] - base) / tan(ramp):
                        hwid[i,j]=hwid[i,j] + 1
# FixedAxisFPFGrowth.m:78
            else:
                hwid[i,j]=size(xp,2)
# FixedAxisFPFGrowth.m:82
    
    #Deform beds. Apply velocity fields of Eq. 11.18
#Loop over slip increments
    for i in arange(1,ninc).reshape(-1):
        # Compute uplift
        lb=dot(dot(lbrat,i),sinc)
# FixedAxisFPFGrowth.m:91
        uplift=dot(lb,sin(ramp))
# FixedAxisFPFGrowth.m:92
        lbh=dot(lb,cos(ramp))
# FixedAxisFPFGrowth.m:93
        xt=xramp + lbh
# FixedAxisFPFGrowth.m:95
        yt=base + uplift
# FixedAxisFPFGrowth.m:96
        for j in arange(1,size(XP,1)).reshape(-1):
            #number of hanging wall points in bed
        #If pregrowth bed
            if j <= size(yp,2):
                points=hwid[i,j]
# FixedAxisFPFGrowth.m:102
            else:
                points=size(XP,2)
# FixedAxisFPFGrowth.m:105
            #Loop over number of hanging wall points in each bed
            for k in arange(1,points).reshape(-1):
                #If point is in domain 1
                if XP[j,k] < xramp - (YP[j,k] - base) / tan(gam1):
                    XP[j,k]=XP[j,k] + sinc
# FixedAxisFPFGrowth.m:111
                else:
                    #If point is in domain 2
                    if XP[j,k] < xt - (YP[j,k] - yt) / tan(gam1):
                        XP[j,k]=XP[j,k] + dot(sinc,cos(ramp))
# FixedAxisFPFGrowth.m:115
                        YP[j,k]=YP[j,k] + dot(sinc,sin(ramp))
# FixedAxisFPFGrowth.m:116
                    else:
                        #If point is in domain 3
                        if XP[j,k] < xt + (YP[j,k] - yt) / tan(game):
                            XP[j,k]=XP[j,k] + dot(dot(sinc,R),cos(game))
# FixedAxisFPFGrowth.m:120
                            YP[j,k]=YP[j,k] + dot(dot(sinc,R),sin(game))
# FixedAxisFPFGrowth.m:121
        #Plot increment
    #Fault
        xf=matlabarray(cat(0,xramp,xramp + lbh))
# FixedAxisFPFGrowth.m:129
        yf=matlabarray(cat(base,base,uplift + base))
# FixedAxisFPFGrowth.m:130
        plot(xf,yf,'r-','LineWidth',2)
        hold('on')
        for j in arange(1,size(yp,2)).reshape(-1):
            #If beds cut by the fault
            if yp[j] - base <= uplift:
                plot(XP[j,1:1:hwid[i,j]],YP[j,1:1:hwid[i,j]],'k-')
                plot(XP[j,hwid[i,j] + 1:1:size(xp,2)],YP[j,hwid[i,j] + 1:1:size(xp,2)],'k-')
            else:
                plot(XP[j,:],YP[j,:],'k-')
        # Growth beds
        for j in arange(size(yp,2) + 1,size(XP,1)).reshape(-1):
            plot(XP[j,:],YP[j,:],'g-')
        #Plot settings
        text(dot(0.8,extent),dot(2.75,max(yp)),strcat('Slip = ',num2str(dot(i,sinc))))
        axis('equal')
        axis(cat(0,extent,0,dot(3.0,max(yp))))
        hold('off')
        frames[i]=getframe
# FixedAxisFPFGrowth.m:155
        #are not calculated. Growth strata will not look right for subsidence
    #rate lower than uplift rate G < 1.0
        if (i == dot(countG,nincG)):
            # Make growth strata
        # Update top
            top=top + dot(dot(dot(nincG,sinc),inccrupl),G)
# FixedAxisFPFGrowth.m:162
            xp=arange(dot(i,sinc),extent + dot(i,sinc),extent / npoint)
# FixedAxisFPFGrowth.m:164
            GXP,GYP=meshgrid(xp,top,nargout=2)
# FixedAxisFPFGrowth.m:165
            XP=matlabarray(cat([XP],[GXP]))
# FixedAxisFPFGrowth.m:167
            YP=matlabarray(cat([YP],[GYP]))
# FixedAxisFPFGrowth.m:168
            countG=countG + 1
# FixedAxisFPFGrowth.m:170
    
    return frames
    
if __name__ == '__main__':
    pass
    