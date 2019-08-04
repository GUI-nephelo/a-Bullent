from setting.settings import *
class Block():
    def __init__(self,pos,type,size=(20,20)):
        self.pos=pos
        self.type=type
        self.size=size
    def draw(self):
        if 0<self.type<255:
            self.color=(self.type*16,0,256-self.type*16)
        else:
            self.color=(127,127,127)
        draw.rect(screen,self.color,self.pos+self.size,0)
        f1.render_to(screen,(self.pos[0]+3,self.pos[1]),str(self.type))
        #print("draw")
    def __repr__(self):
        return "pos:%s,color:%s,size:%s,type:%s"%(self.pos,self.color,self.size,self.type)