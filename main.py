import sys
import requests
import ctypes
import platform
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QLineEdit, \
    QPushButton, QSplitter, QMessageBox, QGroupBox,QAction, QMainWindow, QDialog,QPlainTextEdit
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices,QPixmap,QIcon,QImage
from tiqu import tiquff

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('微信编辑器VIP收费模板提取助手V2.1 by @imwzh')
        self.setGeometry(300, 300, 400, 280)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 移除最大化按钮
        self.createMenu()

        # 加载远程图标
        icon_url = 'https://res.wx.qq.com/a/fed_upload/9300e7ac-cec5-4454-b75c-f92260dd5b47/logo-mp.ico'
        icon_data = requests.get(icon_url).content
        icon = QIcon()
        icon.addPixmap(QPixmap.fromImage(QImage.fromData(icon_data)), QIcon.Normal)
        self.setWindowIcon(icon)
        # 主窗口布局
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        splitter = QSplitter(Qt.Vertical)
        main_layout.addWidget(splitter)

        # 创建固定的选项栏
        self.options_widget = QWidget(splitter)
        vbox_options = QVBoxLayout(self.options_widget)

        group_box = QGroupBox("请选择编辑器平台")  # 添加选项栏标题
        vbox_options.addWidget(group_box)
        hbox_radio = QHBoxLayout(group_box)

        self.radio1 = QRadioButton('135编辑器')
        self.radio1.setChecked(True)  # 设置默认选中状态
        self.radio1.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio1)

        self.radio2 = QRadioButton('96编辑器')
        self.radio2.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio2)

        self.radio3 = QRadioButton('365编辑器')
        self.radio3.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio3)

        self.radio4 = QRadioButton('小墨鹰编辑器')
        self.radio4.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio4)

        self.radio5 = QRadioButton('主编编辑器')
        self.radio5.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio5)

        self.radio6 = QRadioButton('壹伴编辑器')
        self.radio6.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio6)

        self.radio7 = QRadioButton('易点编辑器')
        self.radio7.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio7)

        self.radio8 = QRadioButton('秀米编辑器')
        self.radio8.toggled.connect(self.on_radio_button_toggled)
        hbox_radio.addWidget(self.radio8)
        # 不需要重复添加group_box到vbox_options
        #vbox_options.addLayout(hbox_radio)

        # 创建内容区域
        self.content_widget = QWidget(splitter)
        self.content_area = QVBoxLayout(self.content_widget)
        self.content_area.setAlignment(Qt.AlignTop)  # 设置内容区域顶部对齐

        # 默认显示选项1对应的内容
        self.show_option1_content()

        splitter.addWidget(self.options_widget)
        splitter.addWidget(self.content_widget)

        self.show()

    def show_option1_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建一个水平布局来放置文本标签、编辑框和按钮
        hbox = QHBoxLayout()
        wenben = QHBoxLayout()
        tips = QHBoxLayout()

        self.label = QLabel('【135编辑器】输入样式/模板ID:')
        self.edit = QLineEdit('145180')
        self.button = QPushButton('提取样式/模板')
        self.button.clicked.connect(self.button_click135)
        self.button.setFixedSize(200, 36)
        self.edit.setFixedSize(300, 36)

        self.label_tips = QLabel(
            '说明：135编辑器的样式和模板都支持')
        self.label_tips.setStyleSheet('margin-top:20px;')
        self.link_label = QLabel('<a href="https://www.135editor.com/beautify_editor.html">打开135微信编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)  # 居中添加超链接标签
        self.link_label.setStyleSheet('margin-top: 20px;')

        self.link_label = QLabel('<a href="https://www.135editor.com/style-center">打开135微信编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)  # 居中添加超链接标签
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox.addWidget(self.label)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.button)
        tips.addWidget(self.label_tips)

        self.content_area.addLayout(hbox)
        self.content_area.addLayout(tips)
        self.content_area.addLayout(wenben)

    def show_option2_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.label1 = QLabel('【96编辑器】输入素材ID：')
        self.edit1 = QLineEdit('56371')
        self.button1 = QPushButton('提取素材')
        self.button1.setFixedSize(200, 36)
        self.edit1.setFixedSize(330, 36)
        self.button1.clicked.connect(self.button_click96ys)

        self.label2 = QLabel('【96编辑器】输入模板ID：')
        self.edit2 = QLineEdit('19940')
        self.button2 = QPushButton('提取模板')
        self.button2.setFixedSize(200, 36)
        self.edit2.setFixedSize(330, 36)
        self.button2.clicked.connect(self.button_click96mb)

        self.link_label = QLabel('<a href="https://bj.96weixin.com">打开96微信编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://bj.96weixin.com/material/style">打开96微信编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.edit1)
        hbox1.addWidget(self.button1)

        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.edit2)
        hbox2.addWidget(self.button2)

        self.content_area.addLayout(hbox1)
        self.content_area.addLayout(hbox2)
        self.content_area.addLayout(wenben)

    def show_option3_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.label365_1 = QLabel('【365编辑器】输入素材ID：')
        self.edit365_1 = QLineEdit('61968')
        self.button365_1 = QPushButton('提取素材')
        self.button365_1.setFixedSize(200, 36)
        self.edit365_1.setFixedSize(330, 36)
        self.button365_1.clicked.connect(self.button_click365ys)

        self.label365_2 = QLabel('【365编辑器】输入模板ID：')
        self.edit365_2 = QLineEdit('NOFODhhNGG')
        self.button365_2 = QPushButton('提取模板')
        self.button365_2.setFixedSize(200, 36)
        self.edit365_2.setFixedSize(330, 36)
        self.button365_2.clicked.connect(self.button_click365mb)

        self.link_label = QLabel('<a href="https://www.365editor.com">打开365微信编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://www.365editor.com/material">打开365微信编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox3.addWidget(self.label365_1)
        hbox3.addWidget(self.edit365_1)
        hbox3.addWidget(self.button365_1)

        hbox4.addWidget(self.label365_2)
        hbox4.addWidget(self.edit365_2)
        hbox4.addWidget(self.button365_2)

        self.content_area.addLayout(hbox3)
        self.content_area.addLayout(hbox4)
        self.content_area.addLayout(wenben)

    def show_option4_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.labelmy_1 = QLabel('【小墨鹰编辑器】输入样式ID：')
        self.editmy_1 = QLineEdit('195274')
        self.buttonmy_1 = QPushButton('提取样式')
        self.buttonmy_1.setFixedSize(200, 36)
        self.editmy_1.setFixedSize(330, 36)
        self.buttonmy_1.clicked.connect(self.button_clickmyys)

        self.labelmy_2 = QLabel('【小墨鹰编辑器】输入模板ID：')
        self.editmy_2 = QLineEdit('7843')
        self.buttonmy_2 = QPushButton('提取模板')
        self.buttonmy_2.setFixedSize(200, 36)
        self.editmy_2.setFixedSize(330, 36)
        self.buttonmy_2.clicked.connect(self.button_clickmyqw)

        self.link_label = QLabel('<a href="https://www.xmyeditor.com/">打开小墨鹰编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://www.xmyeditor.com/styles.html">打开小墨鹰编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox5.addWidget(self.labelmy_1)
        hbox5.addWidget(self.editmy_1)
        hbox5.addWidget(self.buttonmy_1)

        hbox6.addWidget(self.labelmy_2)
        hbox6.addWidget(self.editmy_2)
        hbox6.addWidget(self.buttonmy_2)

        self.content_area.addLayout(hbox5)
        self.content_area.addLayout(hbox6)
        self.content_area.addLayout(wenben)

    def show_option5_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox7 = QHBoxLayout()
        hbox8 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.labelzb_1 = QLabel('【主编编辑器】输入样式ID：')
        self.editzb_1 = QLineEdit('64569')
        self.buttonzb_1 = QPushButton('提取样式')
        self.buttonzb_1.setFixedSize(200, 36)
        self.editzb_1.setFixedSize(330, 36)
        self.buttonzb_1.clicked.connect(self.button_clickzbys)

        self.labelzb_2 = QLabel('【主编编辑器】输入模板ID：')
        self.editzb_2 = QLineEdit('20827')
        self.buttonzb_2 = QPushButton('提取模板')
        self.buttonzb_2.setFixedSize(200, 36)
        self.editzb_2.setFixedSize(330, 36)
        self.buttonzb_2.clicked.connect(self.button_clickzbmb)

        self.link_label = QLabel('<a href="https://www.zhubian.com/">打开主编编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://www.zhubian.com/material/style">打开主编编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox7.addWidget(self.labelzb_1)
        hbox7.addWidget(self.editzb_1)
        hbox7.addWidget(self.buttonzb_1)

        hbox8.addWidget(self.labelzb_2)
        hbox8.addWidget(self.editzb_2)
        hbox8.addWidget(self.buttonzb_2)

        self.content_area.addLayout(hbox7)
        self.content_area.addLayout(hbox8)
        self.content_area.addLayout(wenben)


    def show_option6_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox9 = QHBoxLayout()
        hbox10 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.labelyb_1 = QLabel('【壹伴编辑器】输入样式ID：')
        self.edityb_1 = QLineEdit('20365')
        self.buttonyb_1 = QPushButton('提取样式')
        self.buttonyb_1.setFixedSize(200, 36)
        self.edityb_1.setFixedSize(330, 36)
        self.buttonyb_1.clicked.connect(self.button_clickybys)

        self.labelyb_2 = QLabel('【壹伴编辑器】输入模板ID：')
        self.edityb_2 = QLineEdit('909')
        self.buttonyb_2 = QPushButton('提取模板')
        self.buttonyb_2.setFixedSize(200, 36)
        self.edityb_2.setFixedSize(330, 36)
        self.buttonyb_2.clicked.connect(self.button_clickybmb)

        self.link_label = QLabel('<a href="https://www.yibanbianji.com/">打开壹伴编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://yiban.io/style_center/0_1_0">打开壹伴编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox9.addWidget(self.labelyb_1)
        hbox9.addWidget(self.edityb_1)
        hbox9.addWidget(self.buttonyb_1)

        hbox10.addWidget(self.labelyb_2)
        hbox10.addWidget(self.edityb_2)
        hbox10.addWidget(self.buttonyb_2)

        self.content_area.addLayout(hbox9)
        self.content_area.addLayout(hbox10)
        self.content_area.addLayout(wenben)

    def show_option7_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox11 = QHBoxLayout()
        hbox12 = QHBoxLayout()
        wenben = QHBoxLayout()

        self.labelyd_1 = QLabel('【易点编辑器】输入样式ID：')
        self.edityd_1 = QLineEdit('6680')
        self.buttonyd_1 = QPushButton('提取样式')
        self.buttonyd_1.setFixedSize(200, 36)
        self.edityd_1.setFixedSize(330, 36)
        self.buttonyd_1.clicked.connect(self.button_clickydys)

        self.labelyd_2 = QLabel('【易点编辑器】输入模板ID：')
        self.edityd_2 = QLineEdit('7')
        self.buttonyd_2 = QPushButton('提取模板')
        self.buttonyd_2.setFixedSize(200, 36)
        self.edityd_2.setFixedSize(330, 36)
        self.buttonyd_2.clicked.connect(self.button_clickydmb)

        self.link_label = QLabel('<a href="https://www.wxeditor.com/">打开易点编辑器</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')
        self.link_label = QLabel('<a href="https://www.wxeditor.com/material">打开易点编辑器样式中心</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox11.addWidget(self.labelyd_1)
        hbox11.addWidget(self.edityd_1)
        hbox11.addWidget(self.buttonyd_1)

        hbox12.addWidget(self.labelyd_2)
        hbox12.addWidget(self.edityd_2)
        hbox12.addWidget(self.buttonyd_2)

        self.content_area.addLayout(hbox11)
        self.content_area.addLayout(hbox12)
        self.content_area.addLayout(wenben)

    def show_option8_content(self):
        # 清空内容区域
        self.clear_content_area()

        # 创建两个水平布局来放置文本标签、编辑框和按钮
        hbox13 = QHBoxLayout()
        wenben = QHBoxLayout()
        tipsxm = QHBoxLayout()

        self.labelxm_1 = QLabel('【秀米编辑器】输入风格排版ID：')
        self.editxm_1 = QLineEdit('130561')
        self.buttonxm_1 = QPushButton('提取内容')
        self.buttonxm_1.setFixedSize(200, 36)
        self.editxm_1.setFixedSize(330, 36)
        self.buttonxm_1.clicked.connect(self.button_clickxmys)

        self.label_tipsxm = QLabel('说明：此平台提取较慢，约5-10秒，请耐心等待。')
        self.label_tipsxm.setStyleSheet('margin-top:20px;')
        self.link_label = QLabel('<a href="https://xiumi.us/#/studio/shop/paper?page=0&freefilter=all&by_nearest=1">打开秀米风格排版</a>')
        self.link_label.setOpenExternalLinks(True)  # 设置使链接可以在浏览器中打开
        wenben.addWidget(self.link_label, alignment=Qt.AlignLeft)
        self.link_label.setStyleSheet('margin-top: 20px;')

        hbox13.addWidget(self.labelxm_1)
        hbox13.addWidget(self.editxm_1)
        hbox13.addWidget(self.buttonxm_1)
        tipsxm.addWidget(self.label_tipsxm)

        self.content_area.addLayout(hbox13)
        self.content_area.addLayout(wenben)
        self.content_area.addLayout(tipsxm)
    def clear_content_area(self):
        # 清空内容区域
        while self.content_area.count() > 0:
            item = self.content_area.takeAt(0)
            if item.layout():
                # 清空布局内的小部件
                while item.layout().count() > 0:
                    sub_item = item.layout().takeAt(0)
                    widget = sub_item.widget()
                    if widget:
                        widget.setParent(None)
                # 删除布局本身
                item.layout().setParent(None)
            elif item.widget():
                # 清空单个小部件
                widget = item.widget()
                widget.setParent(None)

    def on_radio_button_toggled(self):
        if self.radio1.isChecked():
            self.show_option1_content()
        elif self.radio2.isChecked():
            self.show_option2_content()
        elif self.radio3.isChecked():
            self.show_option3_content()
        elif self.radio4.isChecked():
            self.show_option4_content()
        elif self.radio5.isChecked():
            self.show_option5_content()
        elif self.radio6.isChecked():
            self.show_option6_content()
        elif self.radio7.isChecked():
            self.show_option7_content()
        elif self.radio8.isChecked():
            self.show_option8_content()

    def createMenu(self):
        menu_bar = self.menuBar()

        sm_action = QAction('免责声明', self)
        sm_action.triggered.connect(self.showsmDialog)
        menu_bar.addAction(sm_action)

        help_action = QAction('使用帮助', self)
        help_action.triggered.connect(self.OpenHelpPage)
        menu_bar.addAction(help_action)

        other_action = QAction('其他方案', self)
        other_action.triggered.connect(self.showOtherDialog)
        menu_bar.addAction(other_action)

        about_action = QAction('常见问题', self)
        about_action.triggered.connect(self.showQueDialog)
        menu_bar.addAction(about_action)

        about_action = QAction('关于软件', self)
        about_action.triggered.connect(self.showAboutDialog)
        menu_bar.addAction(about_action)

        exit_action = QAction('退出软件', self)
        exit_action.triggered.connect(self.close)
        menu_bar.addAction(exit_action)


    def showsmDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('免责声明')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        text = "本工具适用于快速提取微信编辑器模板(代码)，仅供学习交流，勿用于其他用途。\n\n支持各平台的样式+模板提取，复制的模板内容（不限于版式、图片等）可能存在版权风险。\n\n一切风险责任请自行承担，本工具不承担任何责任，如不同意请自行关闭软件。\n\n"
        label = QLabel(text, dialog)
        label.setWordWrap(True)  # 设置为True以启用自动换行
        layout = QVBoxLayout(dialog)
        layout.addWidget(label)
        dialog.setFixedWidth(300)

        # 创建按钮布局和按钮
        btn_layout = QHBoxLayout()
        btn1 = QPushButton('我同意', dialog)
        btn1.clicked.connect(dialog.accept)  # 关闭对话框并接受用户同意
        btn1.setFixedSize(140, 34)
        btn2 = QPushButton('不同意', dialog)
        btn2.clicked.connect(QApplication.instance().quit)  # 关闭对话框并退出软件
        btn2.setFixedSize(140, 34)

        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        layout.addLayout(btn_layout)

        dialog.exec_()

    def showOtherDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('其他方案')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        dialog.setFixedWidth(300)

        # 创建标签和布局
        text = '【万能前端大法】浏览器审查元素(一般为F12)，找到类似于<section> ···</section>, 直接复制使用，此方法技术要求相对较高 \n\n【浏览器插件】通过油猴+插件的形式直接点击使用，但一般只能提取素材，模板是提取不了的。部分油猴插件由于更新年代久远，部分有失效的情况\n\n'
        label = QLabel(text, dialog)
        label.setWordWrap(True)  # 设置为True以启用自动换行
        layout = QVBoxLayout(dialog)
        layout.addWidget(label)
        dialog.setFixedWidth(300)

        btn_layout = QHBoxLayout()
        btn1 = QPushButton('万能前端大法', dialog)
        btn1.clicked.connect(self.wanneng)
        btn1.setFixedSize(140, 34)
        btn2 = QPushButton('浏览器油猴插件', dialog)
        btn2.clicked.connect(self.youhou)
        btn2.setFixedSize(140, 34)

        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        layout.addLayout(btn_layout)

        dialog.exec_()

    def wanneng(self):
        url = QUrl('https://www.imwzh.com/archives/45.html')
        QDesktopServices.openUrl(url)

    def youhou(self):
        url = QUrl('https://greasyfork.org/zh-CN/scripts/by-site/135editor.com')
        QDesktopServices.openUrl(url)

    def showQueDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('常见问题')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        dialog.setFixedWidth(300)

        # 创建主布局
        main_layout = QVBoxLayout(dialog)

        # 标题和内容
        text = """【1】支持获取什么？\n支持各大编辑器的样式和模板的提取\n\n【2】如何知道ID？\n有三个地方可以获取\n第一种，在各编辑器平台一般左侧会存在样式或模板列表中，鼠标悬停即有提示ID;\n第二种，在编辑器平台的样式或模板中心，列表页或某个样式的详情页都会有ID（部分平台是预览时就会显示ID）;\n第三种，从样式中心点击进入的模板详情，浏览器窗口中的链接，最后的一串数字即为ID\n\n
【3】SVG的怎么提取？\n本工具不支持SVG提取，提取SVG模板是分分钟的事，但是提取出来是源码，而各大SVG编辑器中无法导入外部源码(仅支持插入他们自己的组件)，故即使提取出模板源码但如果不懂前端知识也无法使用。\n如果懂前端知识的也就不需要用本工具提取源码了。\n\n
【4】提取源码成功后怎么办？\n1.随意找一个编辑器平台(不需要遵循135提取的必须135用，粘到96等等其他平台也能用，素材/模板在各个平台之间都是互通的。)\n2.在编辑器工具栏找到[html]或源码图标工具，点击进入\n3.粘贴提取的源码\n4.重新点击[html]或源码图标工具，退出源码模式\n5.自由发挥\n\n
【5】点击按钮出现无响应假死状态？\n因部分解析调用的官方接口获取模板，极少数情况下会有卡顿情况，可等待5-10秒完成提取。超过10秒就重启工具吧。
        """

        # 创建 QPlainTextEdit，并设置文本内容
        plain_text_edit = QPlainTextEdit()
        plain_text_edit.setPlainText(text)
        plain_text_edit.setReadOnly(True)  # 设置为只读

        # 添加到布局
        main_layout.addWidget(plain_text_edit)

        dialog.exec_()

    def OpenHelpPage(self):
        url = QUrl('https://docs.qq.com/doc/DZHVpektYYkZhdnBr')
        QDesktopServices.openUrl(url)

    def showAboutDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('关于软件')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        dialog.setFixedWidth(300)

        layout = QVBoxLayout(dialog)

        labels_info = [
            ('软件版本：V2.1', Qt.AlignCenter),
            ('发布日期：2025-04-04', Qt.AlignCenter),
            ('软件作者：<a href="https://www.imwzh.com">imwzh[个人主页]</a>', Qt.AlignCenter),
            ('联系邮箱：<a href="mailto:admin@imwzh.com">admin@imwzh.com</a>', Qt.AlignCenter),
            ('', Qt.AlignCenter)
        ]

        for info, alignment in labels_info:
            label = QLabel(dialog)
            label.setTextFormat(Qt.RichText)  # 设置为富文本格式
            label.setTextInteractionFlags(Qt.TextBrowserInteraction)  # 允许超链接点击
            label.setOpenExternalLinks(True)  # 打开外部链接
            label.setText(info)
            label.setAlignment(alignment)
            layout.addWidget(label)

        image_url = 'https://www.imwzh.com/wxgzh.jpg'
        req = requests.get(image_url)
        if req.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(req.content)
            if not pixmap.isNull():
                image_label = QLabel(dialog)
                image_label.setPixmap(pixmap.scaledToWidth(200))
                image_label.setAlignment(Qt.AlignCenter)
                layout.addWidget(image_label)

        label4 = QLabel('微信公众号：武志红的杂货铺', dialog)
        label4.setAlignment(Qt.AlignCenter)
        layout.addWidget(label4)
        label4.setStyleSheet('margin-top:10px;margin-bottom:20px;')

        dialog.setFixedSize(dialog.sizeHint())
        dialog.exec_()

    def button_click135(self):
        # 初始化
        worker = tiquff
        # 获取编辑框内容
        id = self.edit.text().strip()
        if id.isdigit():
            worker.tiqu135sc(self, id)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_click96ys(self):
        # 初始化
        worker = tiquff
        content = self.edit1.text().strip()
        if content.isdigit():
            worker.tiqu96ys(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_click96mb(self):
        # 初始化
        worker = tiquff
        content = self.edit2.text().strip()
        if content.isdigit():
            worker.tiqu96mb(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    # 365-元素
    def button_click365ys(self):
        # 初始化
        worker = tiquff()
        content = self.edit365_1.text().strip()
        if content.isdigit():
            worker.tiqu365sc1(int(content))
        elif content.isalpha():
            worker.tiqu365sc2(content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID信息！')

    # 365-模板
    def button_click365mb(self):
        # 初始化
        worker = tiquff()
        content = self.edit365_2.text().strip()
        if content.isdigit():
            worker.tiqu365mb1(int(content))
        elif content.isalpha():
            worker.tiqu365mb2(content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID信息！')

    # 小墨鹰-元素
    def button_clickmyys(self):
        # 初始化
        worker = tiquff
        content = self.editmy_1.text().strip()
        if content.isdigit():
            worker.tiqumyys(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    # 小墨鹰-模板
    def button_clickmyqw(self):
        # 初始化
        worker = tiquff
        content = self.editmy_2.text().strip()
        if content.isdigit():
            worker.tiqumyqw(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_clickzbys(self):
        # 初始化
        worker = tiquff
        content = self.editzb_1.text().strip()
        if content.isdigit():
            worker.tiquzbys(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_clickzbmb(self):
        # 初始化
        worker = tiquff
        content = self.editzb_2.text().strip()
        if content.isdigit():
            worker.tiquzbmb(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_clickybys(self):
        # 初始化
        worker = tiquff
        content = self.edityb_1.text().strip()
        if content.isdigit():
            worker.tiquybys(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    # 壹伴模板
    def button_clickybmb(self):
        # 初始化
        worker = tiquff
        content = self.edityb_2.text().strip()
        if content.isdigit():
            worker.tiquybmb(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    # 易点-元素
    def button_clickydys(self):
        # 初始化
        worker = tiquff
        content = self.edityd_1.text().strip()
        if content.isdigit():
            # worker.tiquxmys(self, content)
            QMessageBox.information(self, '提示', '因平台验证拦截，暂不支持样式提取！')
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')
    def button_clickydmb(self):
        # 初始化
        worker = tiquff
        content = self.edityd_2.text().strip()
        if content.isdigit():
            worker.tiquydmb(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

    def button_clickxmys(self):
        # 初始化
        worker = tiquff
        content = self.editxm_1.text().strip()
        if content.isdigit():
            worker.xiumiyulan(self, content)
        else:
            QMessageBox.information(self, '提示', '请输入有效模板/素材ID数字！')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    # On Windows, hide the console window   用于打包多文件时隐藏CMD窗口
    if platform.system() == "Windows":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    # On macOS, hide the console window (for completeness, though generally not shown by default)
    elif platform.system() == "Darwin":
        app_info = Qt.ApplicationAttribute(Qt.AA_DisableWindowContextHelpButton)
        app.setAttribute(app_info)
    ex = Example()
    sys.exit(app.exec_())

