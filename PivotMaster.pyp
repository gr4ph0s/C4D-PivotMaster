#   ENGLISH VERSION :
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# Adam Maxime Aka Gr4ph0s wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp
# ----------------------------------------------------------------------------
# BIG THANKS TO :
#       - CÃ©sar Vonc    for all is open source python plugin for c4d    => http://cesar.vonc.fr
#       - oli_d         for his help                                    => http://frenchcinema4d.fr/member.php?55058-oli_d
#       - xs_yann       for his help                                    => http://www.xsyann.com
#       - valkaari      for his help                                    => http://www.valkaari.com
#       - Mipoll        for the main idea                               => http://mipollstudio.blogspot.fr
#       - Aurety        for nothing but I like to thanks him !          => http://www.lev-communication.fr
#
#   FRENCH VERSION :
# ----------------------------------------------------------------------------
# "LICENCE BEERWARE" (RÃ©vision 42):
# Adam Maxime Aka Gr4ph0s a crÃ©Ã© ce fichier. Tant que vous conservez cet avertissement,
# vous pouvez faire ce que vous voulez de ce truc. Si on se rencontre un jour et
# que vous pensez que ce truc vaut le coup, vous pouvez me payer une biÃ¨re en
# retour. Poul-Henning Kamp
# ----------------------------------------------------------------------------
# Un grand merci Ã  :
#       - CÃ©sar Vonc    pour son aide et tout ces plugins c4d open source   => http://cesar.vonc.fr
#       - xs_yann       pour son aide                                       => http://www.xsyann.com
#       - valkaari      pour son aide                                       => http://www.valkaari.com
#       - oli_d         pour son aide                                       => http://frenchcinema4d.fr/member.php?55058-oli_d
#       - Mipoll        pour l'idÃ©e principale                              => http://mipollstudio.blogspot.fr
#       - Aurety        pour rien mais j'aime le remercier !                => http://www.lev-communication.fr

import  c4d,os,types

import urllib
import urllib2
from c4d import gui, plugins, Vector, Matrix, bitmaps


MODULE_ID                   =   1035532
VERSION                     =   1.6

PIVOT_MASTER_PLUGIN_NAME    =   1000
PIVOT_MASTER_ABOUT          =   1001
PIVOT_MASTER_ALERT_OBJ      =   1002
PIVOT_MASTER_ALERT_NULL     =   1003
PIVOT_MASTER_GROUP_PROGRESS =   1004
PIVOT_MASTER_TEXT_PROGRESS  =   1005
PIVOT_MASTER_PROGRESS       =   1006



class mesh():
    def __init__(self,obj):
        self._MESH                = obj

        self._RADIUS              = self._MESH.GetRad()
        self._ALL_POINTS          = self._MESH.GetAllPoints()
        self._NOMBRE_POINT        = self._MESH.GetPointCount()
        self._CURRENT_AXIS        = self._MESH.GetRelMl()
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


        newMatrix =~ self._Matrix * self._CURRENT_AXIS


        for i in range(nbpts) :
            points[i] = newMatrix.Mul(points[i])

        self._MESH.SetAllPoints(points)
        self._MESH.SetMl(self._Matrix)



class pictureManagment(c4d.gui.GeUserArea):
    def __init__(self,UI):
        self.UI         = UI
        self.progress   = 0
        self.doc        = None
        self.obj        = None

        self._DOING     = False
        self.__hover    = False
        self._COUNT     = 0

        dir, file = os.path.split(__file__)
        self.path = os.path.join(dir, "res")


        self.bmp = c4d.bitmaps.BaseBitmap()
        self.bmp.InitWith(os.path.join(self.path,"PivotMaster.jpg"))


        self.position = ([  [0   ,32  ,28  ,48  ,1],
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

    def GetMinSize(self):
        return self.bmp.GetSize()

    def DrawMsg(self, x1, y1, x2, y2, msg):
        self.DrawSetPen(c4d.COLOR_BG)
        self.DrawRectangle(0, 0, 200, 190)
        self.SetClippingRegion(0, 0, 200, 190)
        self.DrawBitmap(self.bmp, 0, 0, 200, 190, 0, 0, 200, 190, c4d.BMP_NORMAL | c4d.BMP_ALLOWALPHA)

    def Message(self, msg, result):
        if msg.GetId() == c4d.BFM_GETCURSORINFO:
            if not self.__hover: #hover the total image
                self.__hover = True
                self.Redraw()
                self.SetTimer(100)
        return super(pictureManagment, self).Message(msg, result)

    def Timer(self, msg):
        if self._COUNT == 2:
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
    	self.doc = c4d.documents.GetActiveDocument()
        if self._DOING == True :
            for i in self.position:
                if x > i[0] and x < i[2] and y > i[1] and y < i[3]:
                    self._DOING = False
                    self.obj = self.doc.GetActiveObjects(0)
                    if len(self.obj) == 0 :
                        gui.MessageDialog(c4d.plugins.GeLoadString(PIVOT_MASTER_ALERT_OBJ))
                    else :
                        self.UI.initProgressBar()
                        compteur = 0
                        for obj in self.obj:
                            compteur += 1
                            if not obj.CheckType(c4d.Opolygon):
                                gui.MessageDialog(c4d.plugins.GeLoadString(PIVOT_MASTER_ALERT_NULL))
                                return False
                            else :
                                self.UI.setProgressBar(compteur,len(self.obj))
                                self.doc.StartUndo()
                                self.doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

                                objet = pivotTool(obj)
                                objet.updateAxis(i[4])

                                obj.Message(c4d.MSG_UPDATE)
                                self.doc.EndUndo()
                                c4d.EventAdd()

                        self.UI.closeProgressBar()


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

    def __init__(self) :
        self.pictureManagment = pictureManagment(self)
        self.progress = 0

    def initProgressBar(self, Message = c4d.plugins.GeLoadString(PIVOT_MASTER_TEXT_PROGRESS)):
        self.progress = 0
        progressMsg = c4d.BaseContainer(c4d.BFM_SETSTATUSBAR)
        progressMsg.SetBool(c4d.BFM_STATUSBAR_PROGRESSON, True)
        progressMsg[c4d.BFM_STATUSBAR_NETTXT] = Message
        progressMsg[c4d.BFM_STATUSBAR_PROGRESS] = 0.0
        self.SendMessage(PIVOT_MASTER_PROGRESS, progressMsg)
        self.LayoutChanged(PIVOT_MASTER_GROUP_PROGRESS)
        return True

    def setProgressBar(self,currentValue,MaxValue):
        if MaxValue < currentValue : return False
        self.progress = float(currentValue) / float(MaxValue)
        progressMsg = c4d.BaseContainer(c4d.BFM_SETSTATUSBAR)
        progressMsg[c4d.BFM_STATUSBAR_PROGRESS] = self.progress
        self.SendMessage(PIVOT_MASTER_PROGRESS, progressMsg)
        self.LayoutChanged(PIVOT_MASTER_GROUP_PROGRESS)
        return True

    def closeProgressBar(self):
        progressMsg = c4d.BaseContainer(c4d.BFM_SETSTATUSBAR)
        progressMsg.SetBool(c4d.BFM_STATUSBAR_PROGRESSON, False)
        self.SendMessage(PIVOT_MASTER_PROGRESS, progressMsg)
        self.LayoutChanged(PIVOT_MASTER_GROUP_PROGRESS)
        return True

    def CreateLayout(self):
        self.SetTitle(c4d.plugins.GeLoadString(PIVOT_MASTER_PLUGIN_NAME) + " V" + str(VERSION))
        self.AddUserArea(2000, c4d.BFH_CENTER)
        self.AttachUserArea(self.pictureManagment, 2000)

        self.GroupBegin(PIVOT_MASTER_GROUP_PROGRESS, c4d.BFH_SCALEFIT|c4d.BFV_TOP, 1, 1)
        self.GroupBorderNoTitle(c4d.BORDER_ACTIVE_1)
        self.AddCustomGui(PIVOT_MASTER_PROGRESS, c4d.CUSTOMGUI_PROGRESSBAR, "", c4d.BFH_SCALEFIT|c4d.BFV_TOP, 0, 0)
        self.GroupEnd()

        self.AddStaticText(1101, c4d.BFH_CENTER, 0, 20, c4d.plugins.GeLoadString(PIVOT_MASTER_ABOUT))

        return True


class lunchUI(c4d.plugins.CommandData):
    dialog = None

    def Message(self, type, data):
        return True
       #self.dialog.initProgressBar()

    def Execute(self, doc):
        if self.dialog is None:
           self.dialog = myUI()
        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=MODULE_ID, defaulth=280, defaultw=190)

    def RestoreLayout(self, sec_ref):
        if self.dialog is None:
           self.dialog = myUI()
        return self.dialog.Restore(pluginid=MODULE_ID, secret=sec_ref)

if __name__ == "__main__":
     bmp = bitmaps.BaseBitmap()
     dir, f = os.path.split(__file__)
     fn = os.path.join(dir, "res", "PivotMaster.tif")
     bmp.InitWith(fn)
     c4d.plugins.RegisterCommandPlugin(id=MODULE_ID, str=c4d.plugins.GeLoadString(PIVOT_MASTER_PLUGIN_NAME),
                                       help="Click on the circle",info=0,
                                       dat=lunchUI(), icon=bmp)