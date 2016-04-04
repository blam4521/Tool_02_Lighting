from PySide import QtGui as qg 
from PySide import QtCore as qc

import maya.cmds  as mc
import pymel.core as pm

import maya.OpenMayaUI as mui
import shiboken

class InterpolateIt(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setObjectName('Lighting Tools')
        self.setWindowTitle('Lighting Tools v1.04')
        self.setFixedWidth(314)

        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)

        main_widget = qg.QWidget()
        main_layout = qg.QVBoxLayout()
        main_layout.setContentsMargins(5,5,5,5)
        main_layout.setAlignment(qc.Qt.AlignTop)
        main_widget.setLayout(main_layout)
        #scroll_area.setWidget(main_widget)

        self.interp_layout = qg.QVBoxLayout()
        self.interp_layout.setContentsMargins(0,0,0,0)
        self.interp_layout.setSpacing(0)
        self.interp_layout.setAlignment(qc.Qt.AlignTop)
        main_layout.addLayout(self.interp_layout)

        button_layout = qg.QHBoxLayout()
        button_layout.setContentsMargins(0,0,0,0)
        button_layout.setAlignment(qc.Qt.AlignRight)
        main_layout.addLayout(button_layout)

        add_button = qg.QPushButton('New...')
        button_layout.addWidget(add_button)

        new_widget = InterpolateWidget()
        #new_widget.hideCloseButton()
        self.interp_layout.addWidget(new_widget)

        self._interp_widget = []
        self._interp_widget.append(new_widget)

        self._dock_widget = self._dock_name = None

        

    #------------------------------------------------------------------------------------------#

class InterpolateWidget(qg.QFrame):
    def __init__(self, *args, **kwargs):
        qg.QFrame.__init__(self, *args, **kwargs)
        
        self.setLayout(qg.QVBoxLayout())
        self.layout().setContentsMargins(5,5,5,5)
        self.layout().setSpacing(5)
        self.setFrameStyle(qg.QFrame.Panel | qg.QFrame.Raised)
        self.setFixedHeight(150)

        
        self.main_widget = qg.QWidget()
        self.main_widget.setObjectName('mainWidget')
        self.main_widget.setLayout(qg.QVBoxLayout())
        self.main_widget.layout().setContentsMargins(2,2,2,2)
        self.main_widget.layout().setSpacing(5)
        self.layout().addWidget(self.main_widget)
        

        title_layout = qg.QHBoxLayout()
        select_layout = qg.QHBoxLayout()
        button_layout = qg.QHBoxLayout()
        slider_layout = qg.QHBoxLayout()
        check_layout  = qg.QHBoxLayout()
        self.main_widget.layout().addLayout( title_layout )
        self.main_widget.layout().addLayout( select_layout )
        self.main_widget.layout().addLayout( button_layout )
        self.main_widget.layout().addLayout( slider_layout )
        self.main_widget.layout().addLayout(                      check_layout )

        title_line =qg.QLineEdit('Untitled')
        #adds widget to layout
        title_layout.addWidget(title_line)

        self.close_bttn = qg.QPushButton('X')
        #set the height and width of the button
        self.close_bttn.setFixedHeight( 30 )
        self.close_bttn.setFixedWidth( 30 )

        select_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))
        
        select_layout.addSpacerItem(qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding))

        button_layout.addWidget(self.store_start_bttn)
        button_layout.addWidget(self.reset_item_bttn)
        button_layout.addWidget(self.store_end_bttn)

        self.slider = qg.QSlider()
        self.slider.setRange(0, 49)
        self.slider.setOrientation(qc.Qt.Horizontal)
        
        slider_layout.addWidget(self.start_lb)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.end_lb)

        self.transforms_chbx = qg.QCheckBox('Transform')
        self.attributes_chbx = qg.QCheckBox('UD Attributes')
        self.transforms_chbx.setCheckState(qc.Qt.Checked)
        check_layout.addWidget(self.transforms_chbx)
        check_layout.addWidget(self.attributes_chbx)

        self.items = {}
        self.slider_down = False

        

#--------------------------------------------------------------------------------------------------#

dialog = None

def create(docked=True):
    global dialog

    if dialog is None:
        dialog = InterpolateIt()

    # docking window if statment    
    if docked is True:
        ptr = mui.MQtUtil.mainWindow()
        main_window = shiboken.wrapInstance(long(ptr), qg.QWidget)

        dialog.setParent(main_window)
        size = dialog.size()

        name = mui.MQtUtil.fullName(long(shiboken.getCppPointer(dialog)[0]))
        dock = mc.dockControl(
            allowedArea =['right', 'left'],
            area        = 'right',
            floating    = False,
            content     = name,
            width       = size.width(),
            height      = size.height(),
            label       = 'Interpolate It')

        widget      = mui.MQtUtil.findControl(dock)
        dock_widget = shiboken.wrapInstance(long(widget), qc.QObject)
        #dialog.connectDockWidget(dock, dock_widget)

    else:
        dialog.show()


def delete():
    global dialog
    if dialog:
        dialog.close()
        dialog = None


from digital_tutors import interpolate_it_01;
reload(interpolate_it_01)
interpolate_it_01.create()
