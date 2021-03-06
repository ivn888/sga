# Autogenerated with SMOP 
from smop.core import *
# TransformStress.m

    
@function
def TransformStress(stress=None,tX1=None,pX1=None,tX3=None,ntX1=None,npX1=None,ntX3=None,*args,**kwargs):
    varargin = TransformStress.varargin
    nargin = TransformStress.nargin

    #TransformStress transforms a stress tensor from old X1,X2,X3 to new X1'
#,X2',X3' coordinates
    
    #   USE: nstress = TransformStress(stress,tX1,pX1,tX3,ntX1,npX1,ntX3)
    
    #   stress = 3 x 3 stress tensor
#   tX1 = trend of X1 
#   pX1 = plunge of X1 
#   tX3 = trend of X3
#   ntX1 = trend of X1'
#   npX1 = plunge of X1'
#   ntX3 = trend of X3'
#	nstress = 3 x 3 stress tensor in new coordinate system
    
    #   NOTE: All input angles should be in radians
    
    #   TransformStress uses function DirCosAxes
    
    #MATLAB script written by Nestor Cardozo for the book Structural 
#Geology Algorithms by Allmendinger, Cardozo, & Fisher, 2011. If you use
#this script, please cite this as "Cardozo in Allmendinger et al. (2011)"
    
    #Direction cosines of axes of old coordinate system
    odC=DirCosAxes(tX1,pX1,tX3)
# TransformStress.m:25
    #Direction cosines of axes of new coordinate system
    ndC=DirCosAxes(ntX1,npX1,ntX3)
# TransformStress.m:28
    #Transformation matrix between old and new coordinate system
    a=zeros(3,3)
# TransformStress.m:31
    for i in arange(1,3).reshape(-1):
        for j in arange(1,3).reshape(-1):
            #Use dot product
            a[i,j]=dot(ndC[i,1],odC[j,1]) + dot(ndC[i,2],odC[j,2]) + dot(ndC[i,3],odC[j,3])
# TransformStress.m:35
    
    #Transform stress tensor from old to new coordinate system (Eq. 5.12)
    nstress=zeros(3,3)
# TransformStress.m:40
    for i in arange(1,3).reshape(-1):
        for j in arange(1,3).reshape(-1):
            for k in arange(1,3).reshape(-1):
                for L in arange(1,3).reshape(-1):
                    nstress[i,j]=dot(dot(a[i,k],a[j,L]),stress[k,L]) + nstress[i,j]
# TransformStress.m:45
    
    return nstress
    
if __name__ == '__main__':
    pass
    