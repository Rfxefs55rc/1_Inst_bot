import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def run_bot():
    # إعدادات المتصفح لـ Replit
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless') 

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 20)

    try:
        # 1. الدخول لصفحة تسجيل الدخول أولاً
        print("جاري الدخول لصفحة تسجيل الدخول...")
        driver.get("https://fastfollow.in/login") # تأكد من رابط تسجيل الدخول الصحيح للموقع
        time.sleep(3)

        # 2. إدخال بيانات الحساب
        print("إدخال بيانات الاعتماد...")
        user_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        pass_field = driver.find_element(By.NAME, "password")
        
        user_field.send_keys("withgaza2026")
        pass_field.send_keys("ASAS_666")
        
        # الضغط على زر الدخول (غالباً ما يكون زر submit)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10) # انتظار تسجيل الدخول بالكامل

        # 3. الانتقال للرابط المطلوب لتنفيذ المهمة
        print("الانتقال لرابط الأداة...")
        driver.get("https://fastfollow.in/tools/send-follower/70279583446")
        
        # 4. الضغط على خانة 175
        btn_175 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '175')]")))
        btn_175.click()

        # 5. وضع الاسم bila.lzaqout
        name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
        name_input.clear()
        name_input.send_keys("bila.lzaqout")

        # 6. الضغط على الزر الأخضر الأول
        green_btn = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-success')]")
        green_btn.click()
        time.sleep(5)

        # 7. حذف الرقم وكتابة 175 في الواجهة الجديدة
        qty_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='number']")))
        qty_input.clear()
        qty_input.send_keys("175")

        # 8. الضغط على الزر الأخضر النهائي
        final_btn = driver.find_element(By.XPATH, "(//button[contains(@class, 'btn-success')])[last()]")
        final_btn.click()

        print("تمت العملية بنجاح. انتظار 200 ثانية...")
        time.sleep(200)

    except Exception as e:
        print(f"حدث خطأ: {e}")
    finally:
        driver.quit()

# نظام التكرار العشوائي (ما بين ساعة وساعتين)
while True:
    run_bot()
    
    # حساب وقت انتظار عشوائي بين 3600 (ساعة) و 7200 (ساعتين) ثانية
    wait_time = random.randint(3600, 7200)
    minutes = wait_time // 60
    
    print(f"انتهت الدورة. سأنتظر لمدة {minutes} دقيقة قبل المحاولة القادمة...")
    time.sleep(wait_time)
