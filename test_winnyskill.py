
import requests
import random
import string 
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time
import json
from pytest import mark,fixture


@fixture(scope="function")
def verify_clean_updating(login_logout):
    headers = {'Authorization': login_logout }
    r = requests.get(f'http://localhost:8000/users/2', headers=headers)
    json = r.json()
    username = json['username']
    print(username)
    yield
    data= {
        "username":username
    }
    r = requests.post(f'http://localhost:8000/users/2', data=data, headers=headers)
    time.sleep(2)
    response = requests.get(f'http://localhost:8000/users/2', headers=headers)
    json = response.json()
    username = json['username']
    print(username)
    







def test_recaptcha_verification():
    driver=webdriver.Firefox()
    driver.get("http://localhost:3000/authentication/sign-up")
    iframe=driver.find_element(By.CSS_SELECTOR,"iframe")
    driver.switch_to.frame(iframe)
    recaptcha=driver.find_element(By.XPATH,'//span[@id="recaptcha-anchor"]')
    recaptcha.click()
    driver.implicitly_wait(40)
    success=driver.find_element(By.XPATH,'//div[@id="recaptcha-accessible-status"]')
    if success.get_attribute("textContent")=="You are verified":
        assert success.get_attribute("textContent")=="You are verified"
        driver.switch_to.default_content()
    time.sleep(15)
    driver.quit()
    

    
@mark.parametrize("payloads",json.load(open('test_data.json')))
def test_post_courses(payloads,login_logout):
    headers = {'Authorization': login_logout }
    r = requests.post(f'http://localhost:8000/courses/',payloads, headers=headers)
    assert r.status_code == 200



def test_update_profile(self,login_logout,verify_clean_updating):
    
    data= {
        "username":"brahim Etouti"
    }
    headers = {'Authorization':login_logout }
    r = requests.post(f'http://localhost:8000/users/2', data=data, headers=headers)
    assert r.status_code == 201
    response = requests.get(f'http://localhost:8000/users/2', headers=headers)
    json = response.json()
    username = json['username']
    assert username=="brahim Etouti"