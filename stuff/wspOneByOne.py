from _typeshed import OpenTextMode
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options=ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\Setxh\Desktop\learning-python-v1\drivers\data")
driver=Chrome(executable_path=r'C:\Users\Setxh\Desktop\learning-python-v1\drivers\chromedriver.exe',options=options)

contactos=[]
with open('contactos.txt',"r") as file:
    contactos.append(file.readline)

print(contactos)

def mandarMensaje():
    cantidad=0
    otro=False
    while(otro!=True):
        if(cantidad==0):
            numero=str(input('Ingresa un numero: '))
            texto=str(input('Ingresa un mensaje: '))
            
            url=f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
            driver.get(url)
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button"))).click()
            cantidad+=1
        else:
            otroMensaje=str(input('Otro mensaje y/Y o N/n: '))
            if(otroMensaje in ['y','Y']):
    
                numero=str(input('Ingresa un numero: '))
                #texto=str(input('Ingresa un mensaje: '))
                driver.execute_script("window.open('');")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                url=f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
                driver.get(url)
                WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button"))).click()
                
                
            else:
                otro=True
                driver.close()
            
            


mandarMensaje()