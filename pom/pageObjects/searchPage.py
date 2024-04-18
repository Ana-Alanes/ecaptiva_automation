class searchPage:
    
    def __init__(self, page):
        self.page = page
        self.full_name_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[1]/input')
        self.email_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/input')
        self.subject_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/input')
        self.cuntry_button = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/div/select')
        self.number_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div')
        self.message_input = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[5]/textarea')
        self.send_button = page.locator('//*[@id="root"]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/form/input')

    def navigate(self):
        self.page.goto("http://192.168.1.52:5173/")
        self.page.click('//*[@id="my-header"]/div[2]/div[2]/nav/ul/li[6]/a')
        
    def search(self, fullname, email, subject, number, message):
        self.full_name_input.fill(fullname)
        self.email_input.fill(email)
        self.cuntry_button.click()
        self.number_input.fill(number)
        self.subject_input.fill(subject)
        self.message_input.fill(message)
        self.send_button.click()