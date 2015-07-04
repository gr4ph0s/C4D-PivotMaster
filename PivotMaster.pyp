import  c4d,os
from c4d import gui, plugins, Vector, Matrix


class mesh():
    def __init__(self,doc):
        self._MESH                = doc.GetActiveObject()
    
    
        self._RADIUS              = self._MESH.GetRad()
        self._ALL_POINTS          = self._MESH.GetAllPoints()
        self._NOMBRE_POINT        = self._MESH.GetPointCount()
        self._CURRENT_AXIS        = self._MESH.GetMg()
        self._BOUDING_BOX_CENTER  = self._MESH.GetMp() + self._MESH.GetAbsPos()

    def getCenterObj(self):
        self._BOUDING_BOX_CENTER = self._MESH.GetMp() + self._MESH.GetAbsPos()  
    
    def getCurrentAxis(self):
        self._CURRENT_AXIS = self._MESH.GetMg()
        
    def newMatrix(self):
        return Matrix(self._BOUDING_BOX_CENTER, Vector(1, 0, 0), Vector(0, 1, 0), Vector(0, 0, 1))
    

class pivotTool(mesh):

    def __init__(self,doc):
        mesh.__init__(self,doc)

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




class MyUA(c4d.gui.GeUserArea):

    xValue = 0          
    yValue = 0

    def __init__(self,doc):
        
        dir, file = os.path.split(__file__)
        path = os.path.join(dir, "res")      
        image = path + "\image1.jpg"

        self.document = doc
        self.__hover = False

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

        self.bmp = c4d.bitmaps.BaseBitmap()   #Create an instance of the BaseBitmap class
        self.bmp.InitWith(image)              #Initialize it with the image

        self.xValue = 5
        self.yValue = 5

    def DrawMsg(self, x1, y1, x2, y2, msg):

        self.DrawSetPen(c4d.COLOR_BG)         #COLOR_BG is the image we load with DrawBitmap
        self.DrawRectangle(x1, y1, x2, y2)    #Draws a rectangle and fills it with the image bitmap
        self.SetClippingRegion(x1, y1, x2, y2)
        w, h = self.bmp.GetSize()
        self.DrawBitmap(self.bmp, x1 + self.xValue, y1 + self.yValue, w, h, 0, 0, w, h, c4d.BMP_NORMAL | c4d.BMP_ALLOWALPHA)



        self.DrawBorder(c4d.BORDER_ROUND, x1+5, y1+5, x2-5, y2-5)


    def Message(self, msg, result): 
        if msg.GetId() == c4d.BFM_GETCURSORINFO: 
            if not self.__hover: 
                print "over" 
                self.__hover = True 
                self.Redraw() 
                self.SetTimer(100) 
        return super(MyUA, self).Message(msg, result) 

    def Timer(self, msg):
        base = self.Local2Global() 
        bc = c4d.BaseContainer() 
        res = self.GetInputState(c4d.BFM_INPUT_MOUSE, c4d.BFM_INPUT_MOUSELEFT, bc) 
        x = bc.GetLong(c4d.BFM_INPUT_X) - base['x'] 
        y = bc.GetLong(c4d.BFM_INPUT_Y) - base['y'] 
        if x > self.GetWidth() or x < 0 or y > self.GetHeight() or y < 0: 
            print "out" 
            self.__hover = False 
            self.SetTimer(0) 
            self.Redraw() 

    def getButton(self,x,y):
        for i in self.position:
            if x > i[0] and x < i[2] and y > i[1] and y < i[3]:
                print i[4]
                self.document.StartUndo()
                self.document.AddUndo(c4d.UNDOTYPE_CHANGE, op)

                blaaa = pivotTool(self.document)
                blaaa.updateAxis(i[4])

                op.Message(c4d.MSG_UPDATE)
                doc.EndUndo()
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

class MyDialog(c4d.gui.GeDialog):
    def setData(self,document):
        self.doc = document
        self.ua = MyUA(self.doc) 


    def CreateLayout(self):
        self.AddUserArea(2000, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT) 
        self.AttachUserArea(self.ua, 2000)
        self.AddButton(1000, c4d.BFH_CENTER, 80, 15, "Click Me")
        self.AddButton(1001, c4d.BFH_CENTER, 80, 15, "Close")
        return True

    def InitValues(self):
        doc = None
        ua = None
        return True

    def Command(self, id, msg):
        if id==1000:
            self.ua.xValue = 100
            self.ua.yValue = 100
            self.ua.Redraw()

        elif id==1001:
            self.Close()
        return True



class LunchUI(c4d.plugins.CommandData):
    PLUGIN_ID   = 10000090 # TEST ID
    op          = None
    dlg         = None
    ua          = None
    document    = None
    ICON        = None

    def Init(self, op) :
        print op
        return True

    def Execute(self, doc):
        if not self.dlg: self.dlg = MyDialog()
        self.dlg.setData(doc)
        self.dlg.Open(c4d.DLG_TYPE_ASYNC, self.PLUGIN_ID, -1, -1, 220, 310)
        return True

    def RestoreLayout(self, subid):
        if not self.dlg:
            self.dlg  = MyDialog()
        return self.dlg.Restore(self.PLUGIN_ID, subid)


    @classmethod
    def Register(PivotMaster):
        data = {
            "id":     PivotMaster.PLUGIN_ID,
            "icon":   PivotMaster.ICON,
            "str":    "PivotMaster",
            "help":   "Click on the circle",
            "info":   c4d.PLUGINFLAG_COMMAND_HOTKEY,
            "dat":    PivotMaster(),
        }
        c4d.plugins.RegisterCommandPlugin(**data)

if __name__ == "__main__":
    LunchUI.Register()