import wx
import wx.lib.mixins.listctrl as listmix
import datetime
import operate_database as operate

header = ("SQL", u"実行時間", u"実行日時")
db = operate.OperateDatabase()
cnx = db.connect()


# ウィンドウの設定
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 600))
        self.InNotebook()

    def InNotebook(self):
        nb = wx.Notebook(self)
        import_sql = ImportSQL(nb)
        show_result = Show_Result(nb, import_sql.list_result)
        nb.AddPage(import_sql, "入力")
        nb.AddPage(show_result, "出力")
        nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, lambda event: show_result.Show())
        self.Centre()
        self.Show(True)

    def change_statusbar(self, msg):
        self.SetStatusBar(msg)


# タブごとにクラス分け
# 入力タブ
class ImportSQL(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.list_result = []
        text_box = self.text_box = wx.TextCtrl(self, wx.ID_ANY)
        button = wx.Button(self, -1, "実行")
        button.Bind(wx.EVT_BUTTON, self.OnExecButton)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(text_box, flag=wx.GROW)
        layout.Add(button, flag=wx.GROW)

        self.SetSizer(layout)

    # 実行ボタン
    def OnExecButton(self, event):
        cur = cnx.cursor()
        cur.execute("use test;")
        text_sql = self.text_box.GetValue()
        if text_sql == "":
            text_sql = "None"
            exec_time = "0"
        else:
            exec_time = db.cal_exec_time(text_sql, cnx)
        dt_now = datetime.datetime.now()
        self.list_result.append(
            [text_sql, exec_time, dt_now.strftime('%Y/%m/%d %H:%M:%S')])


# 　出力タブ
class Show_Result(wx.Panel, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, list_result):
        super().__init__(parent)
        self.list_result = list_result
        self.listctrl = wx.ListCtrl(
            self, wx.ID_ANY, style=wx.LC_REPORT)
        for col, v in enumerate(header):
            self.listctrl.InsertColumn(col, v)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.listctrl, flag=wx.EXPAND |
                   wx.ALL, border=10, proportion=1)
        self.SetSizer(layout)
        self.Show

    # 実行結果
    def Show(self):
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self.listctrl.DeleteAllItems()
        for line in range(len(self.list_result)):
            self.listctrl.InsertItem(line, self.list_result[line][0])
            for col in range(1, 3):
                self.listctrl.SetItem(
                    line, col, self.list_result[line][col])
                self.listctrl.SetColumnWidth(col, wx.LIST_AUTOSIZE)
