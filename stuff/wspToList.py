from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options=ChromeOptions()
#CREAR carpeta data para guarda la sesion
options.add_argument(r"user-data-dir=C:\Users\Setxh\Desktop\learning-python-v1\drivers\data")
driver=Chrome(executable_path=r'C:\Users\Setxh\Desktop\learning-python-v1\drivers\chromedriver.exe',options=options)

contactos=[]
aux=[]
file=open('contactos.txt', 'r') 
contactos=file.readlines()
file.close()

for ele in range(len(contactos)):
    contactos[ele]=contactos[ele].replace("+",'').replace("\n","")

for numeroElementos in range(len(contactos)):
    i=0
    j=11
    x=len(contactos[numeroElementos])//11
    for enu in range(x):
        aux.append(contactos[numeroElementos][i:j])
        i+=11
        j+=11


def mandarMensaje():
  
    for elemento in range(len(aux)):
            
            if(elemento==0):
                numero=aux[elemento]
                texto=str(input('Ingresa un mensaje: '))
                url=f"https://web.whatsapp.com/send?phone=+{numero}&text={texto}"
                driver.get(url)
                WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button"))).click()

    
            else:
                numero=aux[elemento]
                driver.execute_script("window.open('');")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                url=f"https://web.whatsapp.com/send?phone=+{numero}&text={texto}"
                driver.get(url)
                WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button"))).click()
                
                
           
    driver.close()
            
            


mandarMensaje()