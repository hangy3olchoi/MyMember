# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from sqlite_member import sqliteCRUD

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MyMember CRUD System", pos = wx.DefaultPosition, size = wx.Size( 500,320 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"회원아이디", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txt_id = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txt_id, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"회원이름", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txt_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.txt_name, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"패스워드", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txt_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txt_password, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"회원특징", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer9.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txt_remark = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
        bSizer9.Add( self.txt_remark, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"Find", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"SelectAll", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button7, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        self.resultArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.HSCROLL|wx.TE_MULTILINE )
        bSizer1.Add( self.resultArea, 0, wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnFind )
        self.m_button7.Bind( wx.EVT_BUTTON, self.OnSelectAll )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        id = self.txt_id.GetValue()
        name = self.txt_name.GetValue()
        password = self.txt_password.GetValue()
        remark = self.txt_remark.GetValue()
        
        try:
            sqliteCRUD.insertData(id, name, password, remark)
            
        except:
            print('예외발생!')
        
        finally:
            print('입력작업 종료')
        
        
        event.Skip()
    
    def OnDelete( self, event ):
        id = self.txt_id.GetValue()
        res = sqliteCRUD.delete(id)
        
        print(id + ' 자료삭제 성공')
        
        # if res > 0:
        #     print('자료삭제 성공, 삭제 자료수: %d'%res)
        #
        # else:
        #     print('삭제할 자료가 없습니다')    
               
        event.Skip()
    
    def OnUpdate( self, event ):
        id = self.txt_id.GetValue()
        name = self.txt_name.GetValue()
        password = self.txt_password.GetValue()
        remark = self.txt_remark.GetValue()
        
        try:
            sqliteCRUD.update(((name, password, remark, id)))
            
        except:
            print('예외발생!')
        
        finally:
            print('입력작업 종료')
            
        event.Skip()
    
    def OnFind( self, event ):
        key = self.txt_id.GetValue()
        row = sqliteCRUD.select(key)
        
        self.txt_id.SetValue(row[0])
        self.txt_name.SetValue(row[1])
        self.txt_password.SetValue(row[2])
        self.txt_remark.SetValue(row[3])
        
        event.Skip()
    
    def OnSelectAll( self, event ):
        rows = sqliteCRUD.selectAll()
        
        for row in rows:
            self.resultArea.AppendText("{},{},{},{}\n".format(row[0],row[1],row[2],row[3]))
        
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(parent = None)
    frame.Show()
    
    app.MainLoop()    
    
    pass