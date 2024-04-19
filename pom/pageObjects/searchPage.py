class searchPage:
    
    def __init__(self, page):
        self.page = page
        self.full_name_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/input')
        self.email_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/input')
        self.number_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/input')
        self.subject_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/input')
        self.message_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[5]/textarea')
        self.send_button = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/input')

    def navigate(self):
        self.page.goto("http://192.168.1.115:5173")
        self.page.click('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[6]/a')
        
    def search(self, fullname, email, number, subject, message):
        self.full_name_input.fill(fullname)
        self.email_input.fill(email)
        self.number_input.fill(number)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        self.send_button.click()