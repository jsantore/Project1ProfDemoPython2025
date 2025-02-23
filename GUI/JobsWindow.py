from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox, QLineEdit, \
    QTextEdit
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel

from PySide6.QtGui import QTextCharFormat, QFont


class JobsWindow(QWidget):
    def __init__(self, jobs_data):
        super().__init__()
        self.jobs_data = jobs_data
        self.list_control = None
        self.setup_window()
        self.job_title =None
        self.job_description =None
        self.company = None
        self.job_location = None
        self.full_time = None
        self.salary = None
        self.link = None

    def setup_window(self):
        self.setWindowTitle('Select a Job')
        top_layout = QHBoxLayout()
        self.list_control = QListWidget()
        # setup the list control
        top_layout.addWidget(self.list_control)
        self.fill_job_list(self.jobs_data)
        self.setLayout(top_layout)
        # put together the more data section
        more_data_panel = QVBoxLayout()
        self.fill_more_data_panel(more_data_panel)
        top_layout.addLayout(more_data_panel)
        self.show()

    def fill_more_data_panel(self, panel: QVBoxLayout):
        label_font = QFont('Arial', 12, QFont.Weight.Bold)
        company_label = QLabel('Company:')
        company_label.setFont(label_font)
        panel.addWidget(company_label)
        self.company = QLineEdit()
        panel.addWidget(self.company)
        panel.addWidget(QLabel('Job Title:'))
        self.job_title = QLineEdit()
        panel.addWidget(self.job_title)
        panel.addWidget(QLabel('Job Description:'))
        self.job_description = QTextEdit()
        panel.addWidget(self.job_description)
        panel.addWidget(QLabel('Job Location:'))
        self.job_location = QLineEdit()
        panel.addWidget(self.job_location)
        panel.addWidget(QLabel('Full Time:'))
        self.full_time = QLineEdit()
        panel.addWidget(self.full_time)
        full_time_label = QLabel('Full Time/Part Time:')
        panel.addWidget(full_time_label)
        self.full_time = QLineEdit()
        panel.addWidget(self.full_time)
        salary_label = QLabel('Salary:')
        panel.addWidget(salary_label)
        self.salary = QLineEdit()
        panel.addWidget(self.salary)
        link_label = QLabel('Job HyperLink:')
        panel.addWidget(link_label)
        self.link = QLineEdit()
        panel.addWidget(self.link)

        # company_row = QHBoxLayout()
        # company_row.addWidget(QLabel('Company:'))
        # self.company = QLineEdit()
        # company_row.addWidget(self.company)
        # panel.addLayout(company_row)
        # title_row = QHBoxLayout()
        # title_row.addWidget(QLabel('Job Title:'))
        # self.job_title = QLineEdit()
        # title_row.addWidget(self.job_title)
        # panel.addLayout(title_row)
        # description_row = QHBoxLayout()
        # description_row.addWidget(QLabel('Job Description:'))
        # self.job_description = QTextEdit()
        # description_row.addWidget(self.job_description)
        # panel.addLayout(description_row)


    def fill_job_list(self, data_to_show:list):  # allow list to be filtered in sprint4
        for job in data_to_show:
            job_text_for_list = f"{job['company_name']} : {job['job_title']}"
            item = QListWidgetItem(job_text_for_list, listview = self.list_control)
