import os
import time

import yaml
from selenium.webdriver.common.by import By
from _helpers.webscrapper import WebScraper
from config import CREDENTIALS_PATH


class WealthSimpleLoginAutomation(WebScraper):
    def __init__(self, url):
        super().__init__(url)

    def get_css_selector(self, attribute_value, attribute='type'):
        self.update_soup()
        element = self.soup.find('input', {attribute: attribute_value})
        return f'#{element["id"]}' if element else None

    def enter_text(self, text, attribute_value, attribute='type'):
        selector = self.get_css_selector(attribute_value, attribute)
        if selector:
            field = self.driver.find_element(By.CSS_SELECTOR, selector)
            field.send_keys(text)
        else:
            print(f"Field with {attribute}={attribute_value} not found")

    def enter_email(self, username):
        self.enter_text(username, 'text')

    def enter_password(self, password):
        self.enter_text(password, 'password')

    # def enter_recovery_code(self, yaml_file_path=CREDENTIALS_PATH):
    #     recovery_code = self.read_yaml(yaml_file_path)
    #     self.enter_text(recovery_code, 'text', 'inputmode')

    def enter_recovery_code(self, recov_code):
        self.enter_text(recov_code, 'text', 'inputmode')

    # def click_button(self, button_text):
    #     try:
    #         button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
    #         button.click()
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         print(f"'{button_text}' button not found or click failed")

    def click_button(self, data_testid=None, button_class=None, xpath=None, css_selector=None):
        from selenium.common import NoSuchElementException
        try:
            button = None
            if data_testid:
                button = self.driver.find_element(By.CSS_SELECTOR, f'[data-testid="{data_testid}"]')
            elif button_class:
                button = self.driver.find_element(By.CLASS_NAME, button_class)
            elif xpath:
                button = self.driver.find_element(By.XPATH, xpath)
            elif css_selector:
                button = self.driver.find_element(By.CSS_SELECTOR, css_selector)

            if button:
                button.click()
            else:
                print("Button not found with provided selectors")

        except NoSuchElementException as e:
            print(f"Error: {e}")
            print("Button not found or click failed")

    def save_new_recovery_code(self, yaml_file_path=CREDENTIALS_PATH):
        self.update_soup()
        element = self.soup.find('input', {'disabled': ''})
        if element:
            recov_code = element['value']
            self.write_yaml(yaml_file_path, recov_code)
            print(f'New recovery code saved: {recov_code}')
        else:
            print("New recovery code field not found")

    @staticmethod
    def read_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read().strip()
        print(f"No data in {file_path}")
        return None

    @staticmethod
    def read_yaml(file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config['WEALTH_SIMPLE']['RECOVERY_CODE']

    @staticmethod
    def write_file(data, file_path):
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def write_yaml(file_path, recovery_code):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        config['WEALTH_SIMPLE']['RECOVERY_CODE'] = recovery_code
        with open(file_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)


if __name__ == '__main__':
    credentials_manager = CredentialsManager(CREDENTIALS_PATH)
    link, login, pwd, recovery_code = credentials_manager.get_credentials('WEALTH_SIMPLE')
    login_automation = WealthSimpleLoginAutomation(link)
    login_automation.enter_email(login)
    login_automation.enter_password(pwd)
    # login_automation.click_button('Log in')
    login_automation.click_button(data_testid="login-form-submit")
    login_automation.click_button('Use recovery code instead')
    login_automation.enter_recovery_code(recovery_code)
    login_automation.click_button('Continue')
    time.sleep(3)
    login_automation.save_new_recovery_code()
    login_automation.click_button('Continue')
    time.sleep(600)
    # login_automation.quit()
