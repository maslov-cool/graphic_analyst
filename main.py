import io
import sys
import sqlite3
import datetime
import pyqtgraph.exporters
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QColorDialog, QFileDialog, QTableWidgetItem
from PyQt6.QtGui import QPixmap, QColor

registration = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Регистрация</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextBrowser" name="back_background">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>800</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="front_background">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>150</y>
      <width>500</width>
      <height>500</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
   </widget>
   <widget class="QLabel" name="reg_text">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>150</y>
      <width>250</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>50</weight>
      <italic>false</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
     </font>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(85, 85, 255);</string>
    </property>
    <property name="text">
     <string>Регистрация</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="text">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>150</y>
      <width>20</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>32</pointsize>
     </font>
    </property>
    <property name="text">
     <string>|</string>
    </property>
   </widget>
   <widget class="QLabel" name="entr_text">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>150</y>
      <width>250</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(75, 75, 75);</string>
    </property>
    <property name="text">
     <string>Вход</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="name_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>230</y>
      <width>201</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите имя:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="name_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>270</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="surname_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>300</y>
      <width>271</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите фамилию:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="surname_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>350</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="login_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>390</y>
      <width>251</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите логин:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>440</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="password_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>470</y>
      <width>211</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите пароль:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="password_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>530</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>570</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: red;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="register_btn">
    <property name="geometry">
     <rect>
      <x>275</x>
      <y>600</y>
      <width>250</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Зарегистрироваться</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(registration)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.back_background.setStyleSheet("""
                    QTextBrowser {
                        background-image: url('images/background.jpg'); /* Укажите путь к вашему изображению */
                        background-repeat: no-repeat;
                        background-position: center;
                        background-size: cover;
                        width: 100%;
                    }
                """)
        self.front_background.setStyleSheet('background-color: rgb(239, 175, 140);')

        self.register_btn.setStyleSheet("""
                            QPushButton {
                                background-color: rgb(85, 85, 255); /* Цвет фона */
                            }""")

        self.register_btn.clicked.connect(self.action)
        self.entr_text.mousePressEvent = self.entrance_action

    def entrance_action(self, event):
        self.hide()
        self.entrance = Entrance()
        self.entrance.show()

    def action(self):
        # Подключение к базе данных
        conn = sqlite3.connect('bd.sqlite')
        cursor = conn.cursor()

        if cursor.execute('''SELECT password FROM users_information 
        WHERE login = ?''', (self.login_input.text(),)).fetchall():
            self.label.setText('Такой логин уже зарегистрирован в системе!')

        elif not self.name_input.text() or not self.surname_input.text() or not self.login_input.text() or \
                not self.password_input.text():
            self.label.setText('Все поля обязательно должны быть заполнены!')

        else:
            # Подготовка SQL-запроса для вставки данных
            query = '''INSERT INTO users_information (name, surname, login, password) VALUES (?, ?, ?, ?)'''
            values = (
                self.name_input.text(), self.surname_input.text(), self.login_input.text(), self.password_input.text())
            cursor.execute(query, values)

            # Сохранение изменений
            conn.commit()

            self.label.setText('Вы успешно зарегистрированы!')


entrance = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Вход</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextBrowser" name="back_background">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>800</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; 
     &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; 
content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; 
font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; 
-qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QTextBrowser" name="front_background">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>150</y>
      <width>500</width>
      <height>400</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
   </widget>
   <widget class="QLabel" name="reg_text">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>150</y>
      <width>250</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>50</weight>
      <italic>false</italic>
      <bold>false</bold>
      <underline>false</underline>
      <strikeout>false</strikeout>
     </font>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(75, 75, 75);</string>
    </property>
    <property name="text">
     <string>Регистрация</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="text">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>150</y>
      <width>20</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>32</pointsize>
     </font>
    </property>
    <property name="text">
     <string>|</string>
    </property>
   </widget>
   <widget class="QLabel" name="entr_text">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>150</y>
      <width>250</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(85, 85, 255);</string>
    </property>
    <property name="text">
     <string>Вход</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="login_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>240</y>
      <width>251</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите логин:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="login_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>290</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="password_label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>330</y>
      <width>211</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите пароль:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="password_input">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>400</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>440</y>
      <width>430</width>
      <height>30</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: red;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="entrance_btn">
    <property name="geometry">
     <rect>
      <x>325</x>
      <y>480</y>
      <width>150</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Entrance(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(entrance)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.back_background.setStyleSheet("""
                            QTextBrowser {
                                background-image: url('images/background.jpg'); /* Укажите путь к вашему изображению */
                                background-repeat: no-repeat;
                                background-position: center;
                                background-size: cover;
                                width: 100%;
                            }
                        """)
        self.front_background.setStyleSheet('background-color: rgb(239, 175, 140);')

        self.entrance_btn.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(85, 85, 255); /* Цвет фона */
                    }""")

        self.entrance_btn.clicked.connect(self.action)
        self.reg_text.mousePressEvent = self.registration_action

    def registration_action(self, event):
        self.hide()
        self.registration = Registration()
        self.registration.show()

    def action(self):
        # Подключение к базе данных
        conn = sqlite3.connect('bd.sqlite')
        cursor = conn.cursor()

        if not self.login_input.text() or not self.password_input.text():
            self.label.setText('Все поля обязательно должны быть заполнены!')

        elif not cursor.execute('''SELECT password FROM users_information 
                WHERE login = ?''', (self.login_input.text(),)).fetchall():

            self.label.setText('Неверный логин')

        elif self.password_input.text() != cursor.execute('''SELECT password FROM users_information
                WHERE login = ?''', (self.login_input.text(),)).fetchall()[0][0]:
            self.label.setText('Неверный пароль')

        else:
            self.label.setText('Вы успешно вошли в приложение!')

            self.hide()
            self.graphic_analyst = GraphicAnalyst(cursor.execute('''SELECT id FROM users_information
                        WHERE login = ?''', (self.login_input.text(),)).fetchall()[0][0])
            self.graphic_analyst.show()


graphic_analyst = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1200</width>
    <height>616</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1200</width>
    <height>616</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1200</width>
    <height>616</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Графический аналитик</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextBrowser" name="background">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>600</width>
      <height>600</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>331</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Введите функцию:</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="function_text">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>500</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>281</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цвет линии:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="color_choose_btn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>160</y>
      <width>191</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>15</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Выберите цвет</string>
    </property>
    <property name="checkable">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>230</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Значения X:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>270</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>min:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>270</y>
      <width>81</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>max:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>370</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Значения Y:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>410</y>
      <width>61</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>min:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>410</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>max:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="draw_btn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>520</y>
      <width>551</width>
      <height>61</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Нарисовать график</string>
    </property>
   </widget>
   <widget class="PlotWidget" name="graphicsView">
    <property name="geometry">
     <rect>
      <x>598</x>
      <y>0</y>
      <width>600</width>
      <height>530</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="save_btn">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>598</x>
      <y>528</y>
      <width>600</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Сохранить график</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="min_x">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>320</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="max_x">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>320</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="min_y">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>456</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="max_y">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>456</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1200</width>
     <height>26</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu">
    <property name="title">
     <string>Информация о программе и история запросов</string>
    </property>
    <addaction name="history_act"/>
    <addaction name="possible_functions_act"/>
    <addaction name="input_format_act"/>
    <addaction name="about_program_act"/>
   </widget>
   <widget class="QMenu" name="menu_2">
    <property name="title">
     <string>Выход</string>
    </property>
    <addaction name="exit_act"/>
   </widget>
   <widget class="QMenu" name="menu_3">
    <property name="title">
     <string>О создателе</string>
    </property>
    <addaction name="about_author_act"/>
   </widget>
   <addaction name="menu"/>
   <addaction name="menu_2"/>
   <addaction name="menu_3"/>
  </widget>
  <action name="history_act">
   <property name="text">
    <string>История Запросов</string>
   </property>
  </action>
  <action name="possible_functions_act">
   <property name="text">
    <string>Возможные функции</string>
   </property>
  </action>
  <action name="input_format_act">
   <property name="text">
    <string>Формат ввода</string>
   </property>
  </action>
  <action name="about_program_act">
   <property name="text">
    <string>О программе</string>
   </property>
  </action>
  <action name="exit_act">
   <property name="text">
    <string>Выйти из приложения</string>
   </property>
  </action>
  <action name="about_author_act">
   <property name="text">
    <string>Об авторе</string>
   </property>
  </action>
 </widget>
 <customwidgets>
  <customwidget>
   <class>PlotWidget</class>
   <extends>QGraphicsView</extends>
   <header>pyqtgraph</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
"""


class GraphicAnalyst(QMainWindow):
    def __init__(self, id):
        super().__init__()
        f = io.StringIO(graphic_analyst)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.id = id

        self.history_act.triggered.connect(self.fun_history)
        self.possible_functions_act.triggered.connect(self.fun_possible_functions)
        self.input_format_act.triggered.connect(self.fun_input_format)
        self.about_program_act.triggered.connect(self.fun_about_program)
        self.exit_act.triggered.connect(self.fun_exit)
        self.about_author_act.triggered.connect(self.fun_about_author)
        self.color_choose_btn.clicked.connect(self.color_choose)
        self.draw_btn.clicked.connect(self.draw)
        self.save_btn.clicked.connect(self.save)

        self.background.setStyleSheet('background-color: rgb(85, 255, 0);')

        self.draw_btn.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(255, 170, 0);; /* Цвет фона */
                    }""")

        self.save_btn.setStyleSheet("""
                            QPushButton {
                                background-color: rgb(255, 170, 0);; /* Цвет фона */
                            }""")

        self.color_choose_btn.setStyleSheet("""
                                    QPushButton {
                                        background-color: rgb(255, 170, 0);; /* Цвет фона */
                                    }""")


        self.color = 'w'

        self.pos_functions = PossibleFunctions()
        self.format_input = InputFormat()
        self.program_about = AboutProgram()
        self.about_author = AboutAuthor()

    def fun_history(self):
        self.history = History(self.id)
        self.history.show()

    def fun_possible_functions(self):
        self.pos_functions.show()

    def fun_input_format(self):
        self.format_input.show()

    def fun_about_program(self):
        self.program_about.show()

    def fun_about_author(self):
        self.about_author.show()

    def fun_exit(self):
        self.hide()
        self.entrance = Entrance()
        self.entrance.show()

    def color_choose(self):
        color = QColorDialog().getColor()
        if color.isValid():
            self.color = color.name()

    def draw(self):
        # Подключение к базе данных
        conn = sqlite3.connect('bd.sqlite')
        cursor = conn.cursor()

        query = '''INSERT INTO history (users_id, function_text, min_x, max_x, min_y, max_y, date, time) VALUES (?, 
        ?, ?, ?, ?, ?, ?, ?)'''
        values = (
            self.id, 'y = ' + self.function_text.text(), self.min_x.text(), self.max_x.text(),
            self.min_y.text(), self.max_y.text(), str(datetime.datetime.now().date()),
            str(datetime.datetime.now().time()))
        cursor.execute(query, values)

        # Сохранение изменений
        conn.commit()

        self.save_btn.setEnabled(True)

        self.graphicsView.clear()

        all_x, all_y = [], []
        x = int(self.min_x.text())
        while x <= int(self.max_x.text()):
            if int(self.min_y.text()) <= eval(self.function_text.text()) <= int(self.max_y.text()):
                all_x.append(x)
                all_y.append(eval(self.function_text.text()))
            else:
                break
            x += 0.01

        self.graphicsView.plot(all_x, all_y, pen=self.color, name='y = ' + self.function_text.text())

    def save(self):
        exporter = pyqtgraph.exporters.ImageExporter(self.graphicsView.plotItem)
        exporter.export(QFileDialog.getExistingDirectory(self, 'Выбрать картинку', '') + '/' + 'График.png')


history = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>widget</class>
 <widget class="QWidget" name="widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>400</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>400</width>
    <height>400</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>400</width>
    <height>400</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>История запросов</string>
  </property>
  <widget class="QTableWidget" name="history">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>400</width>
     <height>400</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class History(QWidget):
    def __init__(self, id):
        super().__init__()
        f = io.StringIO(history)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.id = id

        connection = sqlite3.connect('bd.sqlite')
        cursor = connection.cursor()

        query = '''SELECT function_text, min_x, max_x, min_y, max_y, date, time FROM history WHERE users_id = ?'''
        values = (self.id,)
        result = cursor.execute(query, values).fetchall()[::-1]

        self.history.setRowCount(len(result))
        self.history.setColumnCount(len(result[0]))

        # Закрашиваем шапку таблицы (горизонтальные заголовки)
        self.history.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Закрашиваем боковую шапку таблицы (вертикальные заголовки)
        self.history.verticalHeader().setStyleSheet(
            "QHeaderView::section { background-color: rgb(255, 170, 127);}")

        # Устанавливаем заголовки столбцов
        header_labels = ['Function Text', 'Min X', 'Max X', 'Min Y', 'Max Y', 'Date', 'Time']
        self.history.setHorizontalHeaderLabels(header_labels)

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                item.setBackground(QColor(85, 255, 255))
                self.history.setItem(i, j, item)

        connection.close()


possible_functions = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>580</width>
    <height>250</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>580</width>
    <height>250</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>580</width>
    <height>250</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Возможные функции</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>600</width>
     <height>400</height>
    </rect>
   </property>
   <property name="minimumSize">
    <size>
     <width>600</width>
     <height>400</height>
    </size>
   </property>
   <property name="maximumSize">
    <size>
     <width>600</width>
     <height>400</height>
    </size>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Возможные функции:
1. Линейные функции: y = mx + b
2. Квадратичные функции: y = ax² + bx + c
3. Синусоидальные функции: y = A * sin(ωx + φ)
4. Косинусоидальные функции: y = A * cos(ωx + φ)
5. Экспоненциальные функции: y = a * e^(bx)
6. Логарифмические функции: y = log_a(x)
7. Степенные функции: y = a * x^b
8. Тригонометрические функции: y = sin(x), y = cos(x), y = tan(x)
9. Параметрические уравнения: x(t), y(t)
10. Полиномы: y = a₀ + a₁x + a₂x² + ... + aₙxⁿ</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class PossibleFunctions(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(possible_functions)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.label.setStyleSheet("""
                    QLabel {
                        background-color: rgb(0, 170, 255);
                    }
                """)


input_format = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>200</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>600</width>
    <height>200</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>600</width>
    <height>200</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Формат ввода</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>600</width>
     <height>400</height>
    </rect>
   </property>
   <property name="minimumSize">
    <size>
     <width>600</width>
     <height>400</height>
    </size>
   </property>
   <property name="maximumSize">
    <size>
     <width>600</width>
     <height>400</height>
    </size>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Формат ввода:
Пользователь вводит функцию в одном из следующих форматов:
  - Линейная: 2*x + 3
  - Квадратичная: x**2 - 4*x + 4
  - Тригонометрическая: sin(x)
  - Экспоненциальная: 2**x
  - Логарифмическая: log(x, 10)</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class InputFormat(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(input_format)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.label.setStyleSheet("""
                            QLabel {
                                background-color: rgb(0, 170, 255);
                            }
                        """)


about_program = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>600</width>
    <height>750</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>600</width>
    <height>750</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>600</width>
    <height>750</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>О программе</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>600</width>
     <height>750</height>
    </rect>
   </property>
   <property name="minimumSize">
    <size>
     <width>600</width>
     <height>400</height>
    </size>
   </property>
   <property name="maximumSize">
    <size>
     <width>6000</width>
     <height>4000</height>
    </size>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string>О программе: 
Программа предназначена для визуализации 
математических функций с использованием библиотеки PyQtGraph. 

Она предоставляет пользователю интерфейс для ввода 
математической функции в текстовом формате. После 
ввода функции программа анализирует её, преобразует 
в подходящий формат и строит график 
на основе заданного диапазона значений для 
переменной

 Основные функции программы: - 

Ввод функции: 
Пользователь вводит функцию в текстовое поле. - 

Проверка корректности: 
Программа проверяет, правильно ли введена функция, и предоставляет 
обратную связь. - 

Построение графика: 
После успешной проверки программа строит график функции, 
используя PyQtGraph, и отображает его в 
интерфейсе. - 

Настройки графика: 
Пользователь может выбирать диапазон значений для x, а 
также настраивать внешний вид графика (цвет, 
стиль линии и т.д.). 

Таким образом, 
программа позволяет легко и быстро визуализировать 
различные математические функции, делая процесс интерактивным 
и наглядным.</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AboutProgram(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(about_program)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.label.setStyleSheet("""
                            QLabel {
                                background-color: rgb(0, 170, 255);
                            }
                        """)


about_author = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Об авторе</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextBrowser" name="background">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>800</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="photo">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>40</y>
      <width>431</width>
      <height>531</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>580</y>
      <width>400</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
      <italic>true</italic>
      <strikeout>false</strikeout>
      <kerning>true</kerning>
     </font>
    </property>
    <property name="text">
     <string>Made by Maslov Alexander</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="about_author">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>710</y>
      <width>550</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>22</pointsize>
     </font>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string>Подробнее об авторе</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>630</y>
      <width>781</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>17</pointsize>
      <underline>false</underline>
     </font>
    </property>
    <property name="text">
     <string>Ученик 10 класса, спортсмен, обожает программирование))</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""



class AboutAuthor(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(about_author)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.about_author.setText('<a href="https://maslov-cool.github.io/my_site_2024/homepage.html">'
                                  'Подробнее об авторе</a>')
        self.about_author.setOpenExternalLinks(True)

        # Изображение sbackground
        self.pixmap = QPixmap('images/me.ico')
        self.photo.setPixmap(self.pixmap)

        self.background.setStyleSheet("""
                            QTextBrowser {
                                background-color: rgb(0, 170, 255);
                            }
                        """)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Registration()
    program.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
