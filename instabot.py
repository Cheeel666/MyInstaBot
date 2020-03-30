from selenium import webdriver
import time

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@name = \"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name = \"password\"]").send_keys(password)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(3)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Не сейчас')]").click()
        time.sleep(3)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format((self.username))).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        followers = self._get_names()
        dif = set(following).difference(set(followers))
        dif = list(dif)
        dif.sort()
        for i in dif:
            print(i)

    def _get_names(self):
        time.sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight;
                        """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name != '']
        names = list(set(names))
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

    def unfollow_me(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format((self.username))).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        followers = self._get_names()
        dif = set(followers).difference(set(following))
        dif = list(dif)




print("1. Показать неподписанных на вас людей")
print("Введите действие:")
check_inp = input()
if check_inp == '1' or check_inp == '2':
    a = InstaBot("login", "pw")
while 1:
    if check_inp == '1':
        a.get_unfollowers()
    #if check_inp == '2':
    #   a.unfollow_me()
    else:
        exit()
    print("Введите действие:")
    check_inp = input()
