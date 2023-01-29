import app_settings as app
import operate_database as operate
import wx

if __name__ == '__main__':
    # データベース接続
    db = operate.OperateDatabase()
    cnx = db.connect()
    db.create(cnx)
    # アプリケーションオブジェクトの生成
    aplication = wx.App()
    frame = app.MainFrame(None, "DB_Benchmark")
    frame.Show()
    aplication.MainLoop()
