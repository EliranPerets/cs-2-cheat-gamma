import sys
import time
import zipfile
import os
import subprocess
import threading
import sqlite3
import ctypes
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QBitmap, QPainter, QRegion, QMouseEvent
from ip_update import updated_ip


ip_change = updated_ip
process_name = "main.exe"

# Globals
launch_menu = 0
name = ""
password = ""
time_yes = ""
downloadperc = ""
ui = None
pid = None


def hide_window():
    ###Hide the app window NightMatch
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    GWL_HWNDPARENT = -8
    WS_POPUP = 0x80000000
    WS_VISIBLE = 0x10000000
    SW_HIDE = 0

    handle = ctypes.windll.user32.FindWindowW(None, "NightMatch")
    if not handle:
        return

    style = ctypes.windll.user32.GetWindowLongW(handle, GWL_EXSTYLE)
    style = style | WS_EX_APPWINDOW
    ctypes.windll.user32.SetWindowLongW(handle, GWL_EXSTYLE, style)
    ctypes.windll.user32.SetWindowLongW(handle, GWL_HWNDPARENT, 0)
    style = style & ~WS_POPUP & ~WS_VISIBLE
    ctypes.windll.user32.SetWindowLongW(handle, GWL_EXSTYLE, style)
    ctypes.windll.user32.ShowWindow(handle, SW_HIDE)


# AppData path
appdata = os.getenv('LOCALAPPDATA')


# SQLite helpers
conn = None
cur = None

def connect_to_db():
    #Open (and create if needed) the local login database under LOCALAPPDATA/Imguistudio
    global conn, cur
    db_dir = os.path.join(appdata, 'Imguistudio')
    os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(os.path.join(db_dir, 'login.db'))
    cur = conn.cursor()


def is_database_exists():
    #Return True if the login DB exists and has the 'profile' table.
    try:
        db_path = os.path.join(appdata, 'Imguistudio', 'login.db')
        if not os.path.exists(db_path):
            return False
        with sqlite3.connect(db_path) as c:
            cur = c.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='profile';")
            return cur.fetchone() is not None
    except Exception:
        return False


class Ui_NightMatch(object):
    def __init__(self):
        #Set up fields for the dialog and dynamic labels/buttons.
        self.window = None
        self.timelabel = None
        self.namelabel = None
        self.downloadpercent = None
        self.dragging = False
        self.offset = QPoint()
        self.name = None
        self.password = None
        self.pushButton = None
        self.loginb = None
        self.unlog = None
        self.load = None

    # Refresh the Remaining Time label text from global time_yes.
    def update_text(self):
        if self.timelabel:
            self.timelabel.setText(time_yes)

    # Refresh the download percent label text from global downloadperc.
    def update_percentage(self):
        if self.downloadpercent:
            self.downloadpercent.setText(downloadperc)

    def setupUi(self, NightMatch):
        self.window = NightMatch
        NightMatch.setObjectName("NightMatch")
        NightMatch.resize(298, 160)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        NightMatch.setSizePolicy(sizePolicy)
        NightMatch.setMinimumSize(QtCore.QSize(298, 160))
        NightMatch.setMaximumSize(QtCore.QSize(298, 160))
        NightMatch.setWindowOpacity(1.0)
        NightMatch.setAutoFillBackground(False)
        NightMatch.setSizeGripEnabled(False)
        NightMatch.setModal(False)

        # Remove the "?" help button and frame
        NightMatch.setWindowFlags(NightMatch.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        NightMatch.setWindowFlags(NightMatch.windowFlags() | Qt.FramelessWindowHint)
        NightMatch.setMask(self.createRoundMask(NightMatch.size()))

        self.pushButton = QtWidgets.QPushButton(NightMatch)
        self.pushButton.setGeometry(QtCore.QRect(100, 105, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.load = QtWidgets.QPushButton(NightMatch)
        self.load.setGeometry(QtCore.QRect(50, 95, 200, 50))
        self.load.setObjectName("load")

        self.loginb = QtWidgets.QPushButton(NightMatch)
        self.loginb.setGeometry(QtCore.QRect(100, 105, 100, 30))
        self.loginb.setObjectName("loginb")

        self.unlog = QtWidgets.QPushButton(NightMatch)
        self.unlog.setGeometry(QtCore.QRect(205, 10, 50, 30))
        self.unlog.setObjectName("unlog")

        self.exit = QtWidgets.QPushButton(NightMatch)
        self.exit.setGeometry(QtCore.QRect(260, 10, 30, 30))
        self.exit.setObjectName("exit")

        self.retranslateUi(NightMatch)
        QtCore.QMetaObject.connectSlotsByName(NightMatch)

        self.pushButton.clicked.connect(self.button1)
        self.loginb.clicked.connect(self.login_push)
        self.load.clicked.connect(self.loadcon)
        self.unlog.clicked.connect(self.logout)
        self.exit.clicked.connect(self.exit_application)

        self.name = QtWidgets.QLineEdit(NightMatch)
        self.name.setGeometry(QtCore.QRect(75, 35, 150, 21))
        self.name.setObjectName("name")
        self.password = QtWidgets.QLineEdit(NightMatch)
        self.password.setGeometry(QtCore.QRect(75, 75, 150, 21))
        self.password.setObjectName("password")

        # Initial visibility
        self.name.hide()
        self.password.hide()
        self.pushButton.show()
        self.loginb.hide()
        self.unlog.hide()
        self.load.hide()

        # Make window draggable
        NightMatch.mousePressEvent = self.mousePressEvent
        NightMatch.mouseMoveEvent = self.mouseMoveEvent
        NightMatch.mouseReleaseEvent = self.mouseReleaseEvent

    def exit_application(self):
        #Close the app when the X button is clicked.
        QtWidgets.QApplication.quit()

    def mousePressEvent(self, event: QMouseEvent):
        #Begin dragging the frameless window.
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        #Move the window when mouse is pressed
        if self.dragging and self.window:
            self.window.move(self.window.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        #Stop dragging on mouse release.
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def createRoundMask(self, size, radius=10):
        #Create a rounded-rectangle window mask for the frameless dialog.
        mask = QBitmap(size)
        mask.clear()
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawRoundedRect(0, 0, size.width(), size.height(), radius, radius)
        painter.end()
        return QRegion(mask)

    def retranslateUi(self, NightMatch):
        _translate = QtCore.QCoreApplication.translate
        NightMatch.setWindowTitle(_translate("NightMatch", "NightMatch"))
        self.pushButton.setText(_translate("NightMatch", "Login"))
        self.loginb.setText(_translate("NightMatch", "Connect"))
        self.load.setText(_translate("NightMatch", "start"))
        self.unlog.setText(_translate("NightMatch", "logout"))
        self.exit.setText(_translate("NightMatch", "X"))

    def button1(self):
        #Handle the initial Login button: autologin if DB exists, else show fields.
        global yes_or_no_db
        if not yes_or_no_db:
            self.name.show()
            self.password.show()
            self.loginb.show()
        self.needlogin()
        self.pushButton.hide()

    def show_popup(self):
        #Show a simple info popup with the server response text.
        popup = QMessageBox()
        popup.setWindowTitle('Popup Title')
        popup.setText(for_popup)
        popup.setIcon(QMessageBox.Information)
        popup.setStandardButtons(QMessageBox.Ok)
        popup.setDefaultButton(QMessageBox.Ok)
        popup.exec_()

    def login_push(self):
        #Send credentials to the server and, on success, switch UI to logged-in state.
        global name, password
        name = self.name.text()
        password = self.password.text()
        account(name, password)
        if launch_menu == 1:
            self.rednedrtext()
            self.loginb.hide()
            self.name.hide()
            self.password.hide()
            self.load.show()
            self.unlog.show()
        else:
            try:
                self.show_popup()
            except Exception as e:
                print(f"An error occurred: {e}")

    def rednedrtext(self):
        #Render static labels (username and remaining time) after successful login.
        global name
        if not self.namelabel:
            self.namelabel = QLabel(f"Logged as : {name}", self.window)
            self.namelabel.setGeometry(QtCore.QRect(20, 15, 150, 21))
            self.namelabel.setObjectName("label")
            self.namelabel.show()
        else:
            self.namelabel.setText(f"Logged as : {name}")

        # Download percent label (only shown during download)
        if not self.downloadpercent:
            self.downloadpercent = QLabel(downloadperc, self.window)
            self.downloadpercent.setGeometry(QtCore.QRect(0, 80, 300, 21))
            self.downloadpercent.setAlignment(Qt.AlignCenter)
            self.downloadpercent.setObjectName("label")
            self.downloadpercent.hide()

        # Move Remaining Time label a bit up so it doesn't overlap the Start button
        if not self.timelabel:
            self.timelabel = QLabel(time_yes, self.window)
            self.timelabel.setGeometry(QtCore.QRect(0, 60, 300, 21))  # y changed from 95 -> 60
            self.timelabel.setAlignment(Qt.AlignCenter)
            self.timelabel.setObjectName("label")
            self.timelabel.show()
        else:
            self.timelabel.setText(time_yes)

    def needlogin(self):
        #If credentials exist in DB, attempt autologin and update UI accordingly.
        global name, password, yes_or_no_db
        if yes_or_no_db:
            logindata = read_db()
            if logindata:
                name, password = logindata[0], logindata[1]
                account(name, password)
                if launch_menu == 1:
                    self.rednedrtext()
                    self.loginb.hide()
                    self.name.hide()
                    self.password.hide()
                    self.load.show()
                    self.unlog.show()
                else:
                    try:
                        self.show_popup()
                    except Exception as e:
                        print(f"An error occurred: {e}")
                    self.loginb.show()
                    self.name.show()
                    self.password.show()

    def loadcon(self):
        #Start the background download/unpack/run flow and show progress label.
        self.load.hide()
        if self.downloadpercent:
            self.downloadpercent.show()
        thread = threading.Thread(target=threadnew, daemon=True)
        thread.start()

    def logout(self):
        #Clear the DB and return to the pre-login UI.
        global yes_or_no_db
        clear_database(os.path.join(appdata, 'Imguistudio', 'login.db'))
        yes_or_no_db = is_database_exists()
        self.load.hide()
        self.unlog.hide()
        self.pushButton.show()
        if self.timelabel:
            self.timelabel.hide()
        if self.namelabel:
            self.namelabel.hide()


# Networking and process helpers
import requests


def terminate_process(target_pid):
    #Terminate a process by PID if possible
    try:
        if not target_pid:
            return
        process = psutil.Process(target_pid)
        process.terminate()
        process.wait(timeout=5)
        print(f"Process {target_pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"No process with PID {target_pid} found.")
    except psutil.AccessDenied:
        print(f"Access denied to terminate process {target_pid}.")


def check():
    #Periodically verify login/remaining time with the server and update the UI.
    global time_yes, ui
    while True:
        try:
            server_url = f"https://{ip_change}/check_login"
            data_to_send = {"name": name, "password": password}
            response = requests.post(server_url, json=data_to_send)
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    remaining = response_data.get('remaining time', None)
                    time_yes = f'Remaining Time:{remaining}' if remaining is not None else 'Error: "remaining time" not found in the response'
                    if ui:
                        ui.update_text()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                terminate_process(pid)
                sys.exit()
        except Exception as e:
            print(f"Check error: {e}")
        time.sleep(60)


def get_pid_by_name(pname):
    """Return the first PID of a process by executable name, else None."""
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == pname:
            print(process.info['pid'])
            return process.info['pid']
    return None


def threadnew():
    #Download, unzip, run main.exe, then delete it when finished.
    global pid, downloadperc

    def run_and_delete_file(exe_path, file_to_delete, pname):
        #Run the EXE, capture PID by name, wait, then delete the EXE file.
        global pid
        try:
            process = subprocess.Popen([exe_path])
            hide_window()
            time.sleep(5)
            _pid = get_pid_by_name(pname)
            if _pid:
                pid = _pid
            process.wait()
            try:
                os.remove(file_to_delete)
                print(f"Deletion of {file_to_delete} successful!")
            except Exception as e:
                print(f"Delete error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def download_and_unpack_zip(url, target_directory):
        #Stream-download a ZIP from url, show progress, unzip into target_directory.
        global downloadperc
        try:
            os.makedirs(target_directory, exist_ok=True)
            base = os.path.basename(url)
            file_name = os.path.join(target_directory, base if base.lower().endswith('.zip') else base + '.zip')

            with requests.get(url, stream=True) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0)) or None
                downloaded_size = 0
                with open(file_name, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1_000_000):
                        if chunk:
                            file.write(chunk)
                            if total_size:
                                downloaded_size += len(chunk)
                                downloadperc = f"Downloading... {downloaded_size / total_size:.1%}"
                                if ui:
                                    ui.update_percentage()
            # Unzip
            if file_name.lower().endswith('.zip'):
                with zipfile.ZipFile(file_name, 'r') as zip_ref:
                    zip_ref.extractall(target_directory)
                try:
                    os.remove(file_name)
                except Exception:
                    pass
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    # Get download path from server
    try:
        server_url = f"https://{ip_change}/download"
        data_to_send = {"name": name, "password": password}
        response = requests.post(server_url, json=data_to_send)
        d_path = response.text
        if response.status_code == 200:
            webpage_url = f'https://{ip_change}{d_path}'
            download_folder = os.path.join(appdata, 'Imguistudio')
            download_and_unpack_zip(webpage_url, download_folder)
            exe_path = os.path.join(download_folder, 'main.exe')
            run_and_delete_file(exe_path, exe_path, process_name)
        else:
            print("Login failed:", response.text)
    except Exception as e:
        print(f"Download thread error: {e}")


def account(nm, pwd):
    #Verify credentials with the server, store them, and start the checker thread.
    global time_yes, launch_menu
    server_url = f"https://{ip_change}/check_login"
    data_to_send = {"name": nm, "password": pwd}
    response = requests.post(server_url, json=data_to_send)
    if response.status_code == 200:
        try:
            response_data = response.json()
            remaining = response_data.get('remaining time', None)
            time_yes = f'Remaining Time:{remaining}' if remaining is not None else 'Error: "remaining time" not found in the response'
        except Exception as e:
            print(f"Error: {e}")
        launch_menu = 1
        create_db(nm, pwd)
        startnew = threading.Thread(target=check, daemon=True)
        startnew.start()
    else:
        global for_popup
        for_popup = response.text or "Login failed"
        for ch in ['{', '}', '"']:
            for_popup = for_popup.replace(ch, "")


def create_db(nm, pwd):
    #Create the credentials table if needed and upsert the latest login.
    global cur, conn
    if cur is None or conn is None:
        connect_to_db()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS profile (
            name TEXT PRIMARY KEY,
            pass TEXT
        );
        """
    )
    cur.execute("REPLACE INTO profile (name, pass) VALUES (?, ?)", (nm, pwd))
    conn.commit()
    return conn


def read_db():
    #Read the first stored (name, pass) from the local DB in the appdata folder.
    db_path = os.path.join(appdata, 'Imguistudio', 'login.db')
    if not os.path.exists(db_path):
        return None
    with sqlite3.connect(db_path) as c:
        cur = c.cursor()
        cur.execute('SELECT name, pass FROM profile LIMIT 1;')
        row = cur.fetchone()
        return row


def clear_database(database_path):
    #Drop all tables from the DB (used for logout/clear state).
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
        connection.commit()
        connection.close()
        print("Database cleared successfully.")
    except Exception as e:
        print(f"Error clearing the database: {str(e)}")


import win32gui
import win32con

def set_window_topmost():
    #Keep the dialog always on top (optional helper, runs in a loop).
    window_title = "NightMatch"
    while True:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd == 0:
            time.sleep(1)
            continue
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        time.sleep(1)


if __name__ == "__main__":
    # Bootstrap app: load DB, build UI, and start the Qt event loop
    file_to_delete = os.path.join(appdata, 'Imguistudio', 'login.db')
    yes_or_no_db = is_database_exists()
    connect_to_db()

    app = QtWidgets.QApplication(sys.argv)
    NightMatch = QtWidgets.QDialog()
    ui = Ui_NightMatch()
    ui.setupUi(NightMatch)
    NightMatch.show()

    # ontop = threading.Thread(target=set_window_topmost, daemon=True)
    # ontop.start()

    sys.exit(app.exec())
