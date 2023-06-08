#import self as self
import re
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

 #   def open_contats_page(self):
 #       wd = self.app.wd
 #       if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("Enter")) > 0):
 #            wd.find_element_by_link_text("add new").click()
 #            #wd.get("http://localhost/addressbook/edit.php")
 #           self.app.open_home_page()

    def back_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
#        wd.get("http://localhost/addressbook/index.php")
        self.open_home_page()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        #self.open_home_page()
        self.app.open_home_page()
        edit_button = wd.find_elements_by_xpath('//img[@alt="Edit"]')
        edit_button[index].click()


    def select_contact_by_id(self, id):
        wd = self.app.wd
#        self.open_home_page()
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()





    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        #self.open_home_page()
        self.app.open_home_page()
        view_button = wd.find_elements_by_xpath('//img[@alt="Details"]')
        view_button[index].click()

    def delete_contact_by_index(self, index):
       wd = self.app.wd
       #self.select_contact_by_index(index)
       #self.open_home_page()
       self.app.open_home_page()
       wd.find_elements_by_name("selected[]")[index].click()
       wd.find_element_by_xpath('//input[@value="Delete"]').click()
       wd.switch_to.alert.accept()
       #wd.implicitly_wait(5)
       self.contact_cache = None


    def delete_contact_by_id(self, id):
       wd = self.app.wd
       #self.open_home_page()
       self.app.open_home_page()
       self.select_contact_by_id(id)
       wd.find_element_by_xpath('//input[@value="Delete"]').click()
       wd.switch_to.alert.accept()
       #wd.implicitly_wait(5)
       self.contact_cache = None


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
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
        self.change_field_value("phone2", contact.secondaryphone)
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
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
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
        #self.open_home_page()
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.back_homepage()
        self.contaсt_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        #self.open_home_page()
        self.app.open_home_page()
        wd.find_elements_by_css_selector(f"a[href*='{id}']")[1].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.back_homepage()
        self.contaсt_cache = None


    def count(self):
        wd = self.app.wd
        #self.open_home_page()
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
    contaсt_cache = None

    def get_contact_list(self):
        if self.contaсt_cache is None:
            wd = self.app.wd
            #self.open_home_page()
            self.app.open_home_page()
            self.contaсt_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_css_selector("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails_from_home_page = cells[4].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contaсt_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails_from_home_page))
        return list(self.contaсt_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_by_index(self, index):
        wd = self.app.wd
        #self.open_home_page()
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        for element in wd.find_elements_by_name("entry"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            cells = element.find_elements_by_css_selector("td")
            lastname = cells[1].text
            firstname = cells[2].text
            address = cells[3].text
            all_emails_from_home_page = cells[4].text
            all_phones = cells[5].text
            return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails_from_home_page)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)












