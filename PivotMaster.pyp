import  c4d,os,types
from c4d import gui, plugins, Vector, Matrix, bitmaps

MODULE_ID                   =   1035532

PIVOT_MASTER_PLUGIN_NAME    =   1000
PIVOT_MASTER_ABOUT          =   1001
PIVOT_MASTER_ALERT_OBJ      =   1002
PIVOT_MASTER_ALERT_NULL     =   1003
PIVOT_MASTER_ALERT_MULTI    =   1004

class mesh():
    
    def __init__(self,obj):
        self._MESH                = obj
    
        self._RADIUS              = self._MESH.GetRad()
        self._ALL_POINTS          = self._MESH.GetAllPoints()
        self._NOMBRE_POINT        = self._MESH.GetPointCount()
        self._CURRENT_AXIS        = self._MESH.GetMg()
        self._BOUDING_BOX_CENTER  = self._MESH.GetMp() + self._MESH.GetAbsPos()
        
    def newMatrix(self):
        return Matrix(self._BOUDING_BOX_CENTER, Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1))
    

class pivotTool(mesh):

    def __init__(self,obj):
        mesh.__init__(self,obj)
        self._Matrix = self.newMatrix()
       
        
        self.__FRONT_TOP_LEFT       = 1
        self.__FRONT_TOP_CENTER     = 2
        self.__FRONT_TOP_RIGHT      = 3
        self.__FRONT_CENTER_LEFT    = 4
        self.__FRONT_CENTER_CENTER  = 5
        self.__FRONT_CENTER_RIGHT   = 6
        self.__FRONT_BOT_LEFT       = 7
        self.__FRONT_BOT_CENTER     = 8
        self.__FRONT_BOT_RIGHT      = 9


        self.__MID_TOP_LEFT         = 10
        self.__MID_TOP_CENTER       = 11
        self.__MID_TOP_RIGHT        = 12
        self.__MID_CENTER_LEFT      = 13
        self.__MID_CENTER_CENTER    = 14
        self.__MID_CENTER_RIGHT     = 15
        self.__MID_BOT_LEFT         = 16
        self.__MID_BOT_CENTER       = 17
        self.__MID_BOT_RIGHT        = 18


        self.__BACK_TOP_LEFT        = 19
        self.__BACK_TOP_CENTER      = 20
        self.__BACK_TOP_RIGHT       = 21
        self.__BACK_CENTER_LEFT     = 22
        self.__BACK_CENTER_CENTER   = 23
        self.__BACK_CENTER_RIGHT    = 24
        self.__BACK_BOT_LEFT        = 25
        self.__BACK_BOT_CENTER      = 26
        self.__BACK_BOT_RIGHT       = 27
        
    
    def updateAxis(self, where):
        
        vbuffer   = Vector(0, 0, 0)
        nbpts     = self._MESH.GetPointCount()
        points    = self._MESH.GetAllPoints()

        #FRONT_TOP_LEFT
        if where == self.__FRONT_TOP_LEFT :
            vbuffer = Vector (-self._RADIUS.x, self._RADIUS.y , -self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #FRONT_TOP_CENTER
        elif where == self.__FRONT_TOP_CENTER :
            vbuffer = Vector ( 0, self._RADIUS.y , -self._RADIUS.z )
            self._Matrix.off += vbuffer 
                    
         #FRONT_TOP_RIGHT
        elif where == self.__FRONT_TOP_RIGHT :
            vbuffer = Vector (self._RADIUS.x, self._RADIUS.y , -self._RADIUS.z)
            self._Matrix.off += vbuffer        
               
        #FRONT_CENTER_LEFT
        elif where == self.__FRONT_CENTER_LEFT :
            vbuffer = Vector (-self._RADIUS.x, 0 , -self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #FRONT_CENTER_CENTER
        elif where == self.__FRONT_CENTER_CENTER :
            vbuffer = Vector ( 0, 0 , -self._RADIUS.z )
            self._Matrix.off += vbuffer
                    
         #FRONT_CENTER_RIGHT
        elif where == self.__FRONT_CENTER_RIGHT :
            vbuffer = Vector (self._RADIUS.x, 0 , -self._RADIUS.z)
            self._Matrix.off += vbuffer      
            
        #FRONT_BOT_LEFT
        elif where == self.__FRONT_BOT_LEFT :
            vbuffer = Vector (-self._RADIUS.x, -self._RADIUS.y , -self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #FRONT_BOT_CENTER
        elif where == self.__FRONT_BOT_CENTER :
            vbuffer = Vector ( 0, -self._RADIUS.y , -self._RADIUS.z )
            self._Matrix.off += vbuffer 
                    
        #FRONT_BOT_RIGHT
        elif where == self.__FRONT_BOT_RIGHT :
            vbuffer = Vector (self._RADIUS.x, -self._RADIUS.y , -self._RADIUS.z)
            self._Matrix.off += vbuffer     
       
        #MID_TOP_LEFT
        elif where == self.__MID_TOP_LEFT :
            vbuffer = Vector (-self._RADIUS.x, self._RADIUS.y , 0)
            self._Matrix.off += vbuffer
        
        #MID_TOP_CENTER
        elif where == self.__MID_TOP_CENTER :
            vbuffer = Vector ( 0, self._RADIUS.y , 0 )
            self._Matrix.off += vbuffer 
                    
         #MID_TOP_RIGHT
        elif where == self.__MID_TOP_RIGHT :
            vbuffer = Vector (self._RADIUS.x, self._RADIUS.y , 0)
            self._Matrix.off += vbuffer        
               
        #MID_CENTER_LEFT
        elif where == self.__MID_CENTER_LEFT :
            vbuffer = Vector (-self._RADIUS.x, 0 , 0)
            self._Matrix.off += vbuffer
        
        #MID_CENTER_CENTER
        elif where == self.__MID_CENTER_CENTER :
            vbuffer = Vector ( 0, 0 , 0 )
            self._Matrix.off += vbuffer
                    
         #MID_CENTER_RIGHT
        elif where == self.__MID_CENTER_RIGHT :
            vbuffer = Vector (self._RADIUS.x, 0 , 0)
            self._Matrix.off += vbuffer      
            
        #MID_BOT_LEFT
        elif where == self.__MID_BOT_LEFT :
            vbuffer = Vector (-self._RADIUS.x, -self._RADIUS.y , 0)
            self._Matrix.off += vbuffer
        
        #MID_BOT_CENTER
        elif where == self.__MID_BOT_CENTER :
            vbuffer = Vector ( 0, -self._RADIUS.y , 0 )
            self._Matrix.off += vbuffer 
                    
        #MID_BOT_RIGHT
        elif where == self.__MID_BOT_RIGHT :
            vbuffer = Vector (self._RADIUS.x, -self._RADIUS.y , 0)
            self._Matrix.off += vbuffer 
        
        #BACK_TOP_LEFT
        elif where == self.__BACK_TOP_LEFT :
            vbuffer = Vector (-self._RADIUS.x, self._RADIUS.y , self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #BACK_TOP_CENTER
        elif where == self.__BACK_TOP_CENTER :
            vbuffer = Vector ( 0, self._RADIUS.y , self._RADIUS.z )
            self._Matrix.off += vbuffer 
                    
         #BACK_TOP_RIGHT
        elif where == self.__BACK_TOP_RIGHT :
            vbuffer = Vector (self._RADIUS.x, self._RADIUS.y , self._RADIUS.z)
            self._Matrix.off += vbuffer        
               
        #BACK_CENTER_LEFT
        elif where == self.__BACK_CENTER_LEFT :
            vbuffer = Vector (-self._RADIUS.x, 0 , self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #BACK_CENTER_CENTER
        elif where == self.__BACK_CENTER_CENTER :
            vbuffer = Vector ( 0, 0 , self._RADIUS.z )
            self._Matrix.off += vbuffer
                    
         #BACK_CENTER_RIGHT
        elif where == self.__BACK_CENTER_RIGHT :
            vbuffer = Vector (self._RADIUS.x, 0 , self._RADIUS.z)
            self._Matrix.off += vbuffer      
            
        #BACK_BOT_LEFT
        elif where == self.__BACK_BOT_LEFT :
            vbuffer = Vector (-self._RADIUS.x, -self._RADIUS.y , self._RADIUS.z)
            self._Matrix.off += vbuffer
        
        #BACK_BOT_CENTER
        elif where == self.__BACK_BOT_CENTER :
            vbuffer = Vector ( 0, -self._RADIUS.y , self._RADIUS.z )
            self._Matrix.off += vbuffer 
                    
        #BACK_BOT_RIGHT
        elif where == self.__BACK_BOT_RIGHT :
            vbuffer = Vector (self._RADIUS.x, -self._RADIUS.y , self._RADIUS.z)
            self._Matrix.off += vbuffer 
         
        
        newMatrix = ~self._Matrix * self._CURRENT_AXIS
        for i in range(nbpts) :
            points[i] = newMatrix.Mul(points[i])             
        
        self._MESH.SetAllPoints(points)
        self._MESH.SetMl(self._Matrix)





class pictureManagment(c4d.gui.GeUserArea):

    def __init__(self,doc):
        self.doc        = doc
        self.obj        = None

        self._DOING     = False
        self.__hover    = False
        self._COUNT     = 0
  
        dir, file = os.path.split(__file__)
        self.path = os.path.join(dir, "res")

        self.bmp = c4d.bitmaps.BaseBitmap()
        self.bmp.InitWith(self.path + "\PivotMaster.jpg")  
        
        self.position = ([  [8   ,32  ,28  ,48  ,1],
                            [61  ,43  ,78  ,58  ,2],
                            [116 ,52  ,132 ,68  ,3],
                            [8   ,94  ,25  ,109 ,4],
                            [61  ,105 ,77  ,129 ,5],
                            [116 ,118 ,130 ,130 ,6],
                            [10  ,157 ,25  ,171 ,7],
                            [62  ,167 ,78  ,180 ,8],
                            [115 ,179 ,132 ,194 ,9],

                            [46  ,20  ,61  ,32  ,10],
                            [98  ,27  ,112 ,42  ,11],
                            [153 ,39  ,167 ,53  ,12],
                            [46  ,79  ,62  ,93  ,13],
                            [90  ,80  ,120 ,113 ,14],
                            [152 ,100 ,166 ,115 ,15],
                            [47  ,139 ,62  ,152 ,16],
                            [97  ,150 ,114 ,164 ,17],
                            [150 ,162 ,166 ,178 ,18],

                            [80  ,6   ,96  ,17  ,19],
                            [133 ,14  ,148 ,28  ,20],
                            [186 ,23  ,201 ,36  ,21],
                            [82  ,64  ,96  ,77  ,22],
                            [133 ,75  ,146 ,87  ,23],
                            [185 ,84  ,200 ,99  ,24],
                            [83  ,122 ,97  ,134 ,25],
                            [132 ,133 ,147 ,147 ,26],
                            [184 ,142 ,202 ,159 ,27]
                            ])

    def DrawMsg(self, x1, y1, x2, y2, msg):
        self.DrawSetPen(c4d.COLOR_BG)
        self.DrawRectangle(0, 0, 208, 200)
        self.SetClippingRegion(0, 0, 208, 200)
        self.DrawBitmap(self.bmp, 5, 5, 200, 190, 0, 0, 200, 190, c4d.BMP_NORMAL | c4d.BMP_ALLOWALPHA)

        self.DrawBorder(c4d.BORDER_ROUND, 5, 5, 203, 195)


    def Message(self, msg, result): 
        if msg.GetId() == c4d.BFM_GETCURSORINFO: 
            if not self.__hover: #hover the total image
                self.__hover = True 
                self.Redraw() 
                self.SetTimer(100) 
        return super(pictureManagment, self).Message(msg, result) 

    def Timer(self, msg):
        if self._COUNT == 10:
            self._DOING = True
            self._COUNT = 0

        self._COUNT += 1
        base = self.Local2Global() 
        bc = c4d.BaseContainer() 
        res = self.GetInputState(c4d.BFM_INPUT_MOUSE, c4d.BFM_INPUT_MOUSELEFT, bc)

        x = bc.GetLong(c4d.BFM_INPUT_X) - base['x'] 
        y = bc.GetLong(c4d.BFM_INPUT_Y) - base['y'] 
        if x > self.GetWidth() or x < 0 or y > self.GetHeight() or y < 0:
            self.__hover = False 
            self.SetTimer(0) 
            self.Redraw() 

    def getButton(self,x,y):
        if self._DOING == True:
            for i in self.position:
                if x > i[0] and x < i[2] and y > i[1] and y < i[3]:
                    self._DOING = False
                    self.obj = self.doc.GetActiveObjects(0)
                    #We check if we got much more one item select
                    if len(self.obj) >= 2 :
                        gui.MessageDialog(c4d.plugins.GeLoadString(PIVOT_MASTER_ALERT_MULTI))
                    else :
                        self.obj = self.obj[0]
                        #We check if we got a slection
                        if self.obj == None:
                            gui.MessageDialog(c4d.plugins.GeLoadString(PIVOT_MASTER_ALERT_OBJ))
                        else :
                            #We check if is not a null
                            if self.obj.GetTypeName() != "Polygon":
                                gui.MessageDialog(c4d.plugins.GeLoadString(PIVOT_MASTER_ALERT_NULL))
                            else :
                                    self.doc.StartUndo()
                                    self.doc.AddUndo(c4d.UNDOTYPE_CHANGE, self.obj)

                                    objet = pivotTool(self.obj)
                                    objet.updateAxis(i[4])

                                    self.obj.Message(c4d.MSG_UPDATE)
                                    self.doc.EndUndo()
                                    c4d.EventAdd()
                            
        
    def InputEvent(self, msg):

        action = c4d.BaseContainer(c4d.BFM_ACTION)
        action.SetLong(c4d.BFM_ACTION_ID, self.GetId())

        while self.GetInputState(c4d.BFM_INPUT_MOUSE, c4d.BFM_INPUT_MOUSELEFT, msg):
            if msg.GetLong(c4d.BFM_INPUT_VALUE)==0: break

            if msg[c4d.BFM_INPUT_DEVICE] == c4d.BFM_INPUT_MOUSE:
                x, y = msg[c4d.BFM_INPUT_X], msg[c4d.BFM_INPUT_Y]
                g2l  = self.Global2Local()
                x += g2l['x']
                y += g2l['y']

            if msg[c4d.BFM_INPUT_CHANNEL] == c4d.BFM_INPUT_MOUSELEFT:
                self.getButton(x,y)

                action.SetLong(c4d.BFM_ACTION_INDRAG, True)
                self.SendParentMessage(action)
                self.Redraw()

        action.SetLong(c4d.BFM_ACTION_INDRAG, False)
        self.SendParentMessage(action)

        return True

class myUI(c4d.gui.GeDialog):
    def __init__(self,doc) :        
        self.doc = doc
        self.pictureManagment = pictureManagment(self.doc)  

    def CreateLayout(self):
        self.AddUserArea(2000, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT) 
        self.AttachUserArea(self.pictureManagment, 2000)
        self.AddStaticText(1101, c4d.BFH_CENTER, 0, 20, c4d.plugins.GeLoadString(PIVOT_MASTER_ABOUT))
        return True


class lunchUI(c4d.plugins.CommandData):
    dialog = None
    
    def Execute(self, doc):
        if self.dialog is None:
           self.dialog = myUI(doc)
        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=MODULE_ID, defaulth=280, defaultw=220)

    def RestoreLayout(self, sec_ref):
        if self.dialog is None:
           self.dialog = myUI(doc)
        return self.dialog.Restore(pluginid=MODULE_ID, secret=sec_ref)

if __name__ == "__main__":
     bmp = bitmaps.BaseBitmap()
     dir, f = os.path.split(__file__)
     fn = os.path.join(dir, "res", "PivotMaster.tif")
     bmp.InitWith(fn)
     c4d.plugins.RegisterCommandPlugin(id=MODULE_ID, str=c4d.plugins.GeLoadString(PIVOT_MASTER_PLUGIN_NAME),
                                      help="Click on the circle",info=0,
                                        dat=lunchUI(), icon=bmp)