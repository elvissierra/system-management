from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1650x700+0+0")
        self.root.title("")
        self.root.config(bg="white")
        self.root.focus_force()

        # ====
        # all vaiables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_employ_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # search bar
        SearchFrame = LabelFrame(
            self.root,
            text="search employee",
            font=("goudy old style", 12, "bold"),
            bg="white",
        )
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # options
        cmb_search = ttk.Combobox(
            SearchFrame,
            textvariable=self.var_searchby,
            values=("select", "email", "name", "contact"),
            state="readonly",
            justify=CENTER,
            font=("goudy old style", 15),
        )
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(
            SearchFrame,
            textvariable=self.var_searchtxt,
            font=("goudy old style", 15),
            bg="light yellow",
        ).place(x=200, y=10)
        btn_search = Button(
            SearchFrame,
            text="search",
            font=("goudy old style", 15),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
        ).place(x=410, y=10, width=150, height=30)

        # title
        title = Label(
            self.root,
            text="emplyee details",
            font=("goudy old style", 15),
            bg="#0f4d7d",
            fg="white",
        ).place(x=50, y=100, width=1000)

        # content
        # row 1
        lbl_empid = Label(
            self.root,
            text="emplyee ID",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=350, y=150)

        lbl_gender = Label(
            self.root,
            text="gender",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=50, y=150)

        lbl_contact = Label(
            self.root,
            text="contact",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=750, y=150)

        # entries
        txt_empid = Entry(
            self.root,
            textvariable=self.var_employ_id,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=150, y=150, width=180)

        """txt_gender = Entry(
            self.root,
            textvariable=self.var_gender,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=500, y=150, width=150)"""

        cmb_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("select", "male", "female", "other"),
            state="readonly",
            justify=CENTER,
            font=("goudy old style", 15),
        )
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)

        txt_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=850, y=150, width=180)

        # row 2
        lbl_name = Label(
            self.root,
            text="Name",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=50, y=190)

        lbl_dob = Label(
            self.root,
            text="DOb",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=350, y=190)

        lbl_doj = Label(
            self.root,
            text="DOJ",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=750, y=190)

        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=150, y=190, width=180)

        txt_dob = Entry(
            self.root,
            textvariable=self.var_dob,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=500, y=190, width=180)

        txt_doj = Entry(
            self.root,
            textvariable=self.var_doj,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=850, y=190, width=180)

        # row 3
        lbl_email = Label(
            self.root,
            text="email",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=50, y=230)

        lbl_pass = Label(
            self.root,
            text="password",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=350, y=230)

        lbl_utype = Label(
            self.root,
            text="user type",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=750, y=230)

        txt_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=150, y=230, width=180)

        txt_pass = Entry(
            self.root,
            textvariable=self.var_pass,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=500, y=230, width=180)

        cmb_utype = ttk.Combobox(
            self.root,
            textvariable=self.var_utype,
            values=("select", "admin", "employ"),
            state="readonly",
            justify=CENTER,
            font=("goudy old style", 15),
        )
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # row 4
        lbl_address = Label(
            self.root,
            text="address",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=50, y=270)

        lbl_salary = Label(
            self.root,
            text="salary",
            font=("goudy old style", 15),
            bg="white",
        ).place(x=500, y=270)

        self.txt_address = Text(
            self.root,
            font=("goudy old style", 15),
            bg="white",
        )
        self.txt_address.place(x=150, y=270, width=180, height=60)

        txt_salary = Entry(
            self.root,
            textvariable=self.var_salary,
            font=("goudy old style", 15),
            bg="white",
        ).place(x=600, y=270, width=180)

        # buttons
        btn_add = Button(
            self.root,
            text="save",
            font=("goudy old style", 15),
            bg="lightblue",
            fg="black",
            cursor="hand2",
        ).place(x=500, y=305, width=110, height=28)

        btn_update = Button(
            self.root,
            text="update",
            font=("goudy old style", 15),
            bg="light green",
            fg="black",
            cursor="hand2",
        ).place(x=620, y=305, width=110, height=28)

        btn_delete = Button(
            self.root,
            text="delete",
            font=("goudy old style", 15),
            bg="pink",
            fg="black",
            cursor="hand2",
        ).place(x=740, y=305, width=110, height=28)

        btn_clear = Button(
            self.root,
            text="clear",
            font=("goudy old style", 15),
            bg="light yellow",
            fg="black",
            cursor="hand2",
        ).place(x=860, y=305, width=110, height=28)

        # employ details result
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient=VERTICAL)

        self.EmployTable = ttk.Treeview(
            emp_frame,
            columns=(
                "eid",
                "name",
                "email",
                "gender",
                "contact",
                "dob",
                "doj",
                "password",
                "utype",
                "address",
                "salary",
            ),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
        )
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.EmployTable.xview)
        scrolly.config(command=self.EmployTable.yview)

        self.EmployTable.heading("eid", text="EMP ID")
        self.EmployTable.heading("name", text="Name")
        self.EmployTable.heading("email", text="Email")
        self.EmployTable.heading("gender", text="Gender")
        self.EmployTable.heading("contact", text="Contact")
        self.EmployTable.heading("dob", text="dob")
        self.EmployTable.heading("doj", text="doj")
        self.EmployTable.heading("password", text="password")
        self.EmployTable.heading("utype", text="utype")
        self.EmployTable.heading("address", text="address")
        self.EmployTable.heading("salary", text="salary")

        self.EmployTable["show"] = "headings"

        self.EmployTable.column("eid", width=90)
        self.EmployTable.column("name", width=100)
        self.EmployTable.column("email", width=100)
        self.EmployTable.column("gender", width=100)
        self.EmployTable.column("contact", width=100)
        self.EmployTable.column("dob", width=100)
        self.EmployTable.column("doj", width=100)
        self.EmployTable.column("password", width=100)
        self.EmployTable.column("utype", width=100)
        self.EmployTable.column("address", width=100)
        self.EmployTable.column("salary", width=100)

        self.EmployTable.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
