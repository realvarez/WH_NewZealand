import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

time_wait = 20

def log_in(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(by=By.NAME, value="username").send_keys(os.getenv("USERNAME_NZ_PAGE"))
        driver.find_element(by=By.NAME, value="password").send_keys(os.getenv("PASSWORD_NZ_PAGE"))
        driver.find_element(by=By.XPATH, value="//input[@value='LOGIN']").click()
    except TimeoutException:
        driver.refresh()
        log_in(driver)
    

def wh_schemes_selection(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
                (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Working Holiday Schemes'])[1]/following::a[1]")
        ))
        driver.find_element(
            by=By.XPATH, value="(.//*[normalize-space(text()) and normalize-space(.)='Working Holiday Schemes'])[1]/following::a[1]"
        ).click()
    except TimeoutException:
        driver.refresh()
        wh_schemes_selection(driver)

    

def select_country_visa(driver):
    id_button = "ContentPlaceHolder1_countryRepeater_countryDivFooter_5"
    try:
        WebDriverWait(driver, time_wait).until(
            EC.presence_of_element_located(
                (By.ID, id_button)
            )
        )
        while (
            driver.find_element(
                by=By.ID, value=id_button
            ).get_attribute("class") != 'category-item-footer-open'
        ):
            print("waiting...")
            time.sleep(5)
            driver.refresh()
            try:
                WebDriverWait(driver, time_wait).until(
                    EC.presence_of_element_located(
                        (By.ID, id_button)
                    )
                )
            except TimeoutException:
                driver.refresh()

        driver.find_element(by=By.ID, value=id_button).click()
    except TimeoutException:
        driver.refresh()
        select_country_visa(driver)

    

def apply_selected_country(driver):
    try:
        WebDriverWait(driver, time_wait).until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_applyNowButton")
            )
        )
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_applyNowButton").click()
    except TimeoutException:
        driver.refresh()
        apply_selected_country(driver)
    

def personal_details(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
            (By.ID, "ContentPlaceHolder1_personDetails_dateOfBirthDatePicker_DatePicker")
        ))
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_personDetails_dateOfBirthDatePicker_DatePicker").send_keys(os.getenv("VALUE_DATE_BIRTH"))
        driver.execute_script(f"document.getElementById('ContentPlaceHolder1_personDetails_genderDropDownList').value = '{os.getenv('VALUE_GENDER')}';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_personDetails_CountryDropDownList').value = '45';")
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_addressContactDetails_address_address1TextBox").send_keys(os.getenv('VALUE_ADDRESS'))
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_addressContactDetails_address_suburbTextBox").send_keys(os.getenv('VALUE_SUBURB'))
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_addressContactDetails_address_cityTextBox").send_keys(os.getenv('VALUE_CITY'))
        driver.execute_script("document.getElementById('ContentPlaceHolder1_addressContactDetails_address_countryDropDownList').value = '45';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_hasAgent_representedByAgentDropdownlist').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_hasCreditCard_hasCreditCardDropDownlist').value = 'Yes';")

        driver.find_element(by=By.ID, value="ContentPlaceHolder1_wizardPageHeader_nav_pageTabs_TabHeaders_tabButton_1").click()
    except TimeoutException:
        driver.refresh()
        personal_details(driver)
        
    

def personal_identification(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_identification_passportNumberTextBox")
        ))
        driver.find_element(
            by=By.ID, value="ContentPlaceHolder1_identification_passportNumberTextBox"
            ).send_keys(os.getenv('VALUE_PASSPORT'))
        driver.find_element(
            by=By.ID, value="ContentPlaceHolder1_identification_confirmPassportNumberTextBox"
            ).send_keys(os.getenv('VALUE_PASSPORT'))
        driver.find_element(
            by=By.ID, value="ContentPlaceHolder1_identification_passportExpiryDateDatePicker_DatePicker"
            ).send_keys(os.getenv('VALUE_DATE_EXPIRY_PASS'))
        driver.find_element(
            by=By.ID, value="ContentPlaceHolder1_identification_otherIssueDateDatePicker_DatePicker"
            ).send_keys(os.getenv('VALUE_DATE_EMISION_CI'))
        driver.find_element(
            by=By.ID, value="ContentPlaceHolder1_identification_otherExpiryDateDatePicker_DatePicker"
            ).send_keys(os.getenv('VALUE_DATE_EXPIRY_CI'))
        driver.execute_script(
            "document.getElementById('ContentPlaceHolder1_identification_otherIdentificationDropdownlist').value = '3';"
            )
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_wizardPageHeader_nav_sectionTabs_TabHeaders_tabButton_1").click()
    except TimeoutException:
        driver.refresh()
        personal_identification(driver)


def health(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_medicalConditions_renalDialysisDropDownList")
        ))
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_renalDialysisDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_tuberculosisDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_cancerDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_heartDiseaseDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_disabilityDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_hospitalisationDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_residentailCareDropDownList').value = 'No';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_tbRiskDropDownList').value = 'No';")
        if os.getenv('VALUE_GENDER') == 'F':
            driver.execute_script("document.getElementById('ContentPlaceHolder1_medicalConditions_pregnancy_pregnancyStatusDropDownList').value = 'No';")
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_wizardPageHeader_nav_sectionTabs_TabHeaders_tabButton_2").click()
    except TimeoutException:
        driver.refresh()
        health(driver)
        

def character(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_character_imprisonment5YearsDropDownList")
        ))
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_imprisonment5YearsDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_imprisonment12MonthsDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_deportedDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_chargedDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_convictedDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_underInvestigationDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_excludedDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_character_removedDropDownList').value = 'No';")
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_wizardPageHeader_nav_sectionTabs_TabHeaders_tabButton_3").click()
    except TimeoutException:
        driver.refresh()
        character(driver)
    


def wh_specifics(driver):
    try:
        WebDriverWait(driver, time_wait).until(EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_previousWhsPermitVisaDropDownList")
        ))
        driver.execute_script("document.getElementById('ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_previousWhsPermitVisaDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_sufficientFundsHolidayDropDownList').value = 'Yes';") 
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_offshoreDetails_intendedTravelDateDatePicker_DatePicker").send_keys("15/10/2025")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_offshoreDetails_beenToNzDropDownList').value = 'No';")    
        driver.execute_script("document.getElementById('ContentPlaceHolder1_offshoreDetails_requirementsQuestions_sufficientFundsOnwardTicketDropDownList').value = 'Yes';")
        driver.execute_script("document.getElementById('ContentPlaceHolder1_offshoreDetails_requirementsQuestions_readRequirementsDropDownList').value = 'Yes';")
        driver.find_element(by=By.ID, value="ContentPlaceHolder1_wizardPageFooter_wizardPageNavigator_validateButton").click()
    except TimeoutException:
        driver.refresh()
        wh_specifics(driver)
    

if __name__ == "__main__":
    load_dotenv()

    fxdriver = webdriver.Firefox(executable_path="./geckodriver.exe")
    fxdriver.get('https://onlineservices.immigration.govt.nz/')
    log_in(fxdriver)
    wh_schemes_selection(fxdriver)
    select_country_visa(fxdriver)
    apply_selected_country(fxdriver)
    personal_details(fxdriver)
    personal_identification(fxdriver)
    health(fxdriver)
    character(fxdriver)
    wh_specifics(fxdriver)
