import self as self

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contats_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("Enter")) > 0):
             wd.find_element_by_link_text("add new").click()
             wd.get("http://localhost/addressbook/edit.php")

    def back_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        wd.get("http://localhost/addressbook/index.php")

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        edit_button = wd.find_elements_by_xpath('//img[@alt="Edit"]')
        edit_button[index].click()

    def delete_contact_by_index(self, index):
       # wd = self.app.wd
       # self.open_home_page()
        # select contact by index
        #self.select_contact_by_index(index)
        # submit deletion
        #wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert OK
        #Alert(wd).accept()
        #wd.find_element_by_css_selector("div.msgbox")
        #self.return_homepage()
        #self.contact_cache = None

       wd = self.app.wd
       self.select_contact_by_index()
       wd.find_element_by_xpath('//input[@value="Delete"]').click()
       wd.switch_to.alert.accept()
       wd.find_element_by_css_selector("div.msgbox")
       self.open_home_page()
       self.contact_cache = None

    def edit(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # fill group form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.back_homepage()
        self.contaсt_cache = None
    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_fieled_value_for_selects("bday", contact.bday)
        self.change_fieled_value_for_selects("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_fieled_value_for_selects("aday", contact.aday)
        self.change_fieled_value_for_selects("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           wd.find_element_by_name(field_name).clear()
           wd.find_element_by_name(field_name).send_keys(text)

    def change_fieled_value_for_selects(self, field_name, text):
        wd = self.app.wd
        if text is not None:
           wd.find_element_by_name(field_name).click()
           Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def select_first_contact(self):
        wd = self.app.wd
        # submit modification
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text('home').click()

    def create(self, new_contact_data):
        wd = self.app.wd
        self.open_contats_page()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # Submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.back_homepage()
        self.contaсt_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.back_homepage()
        self.contaсt_cache = None


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def get_contact_list(self, contaсt_cache = None):
        if contaсt_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contaсt_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contaсt_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contaсt_cache)





