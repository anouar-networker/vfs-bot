from playwright.sync_api import sync_playwright
import time
import random

URL = "https://visa.vfsglobal.com/mar/fr/che/application-detail"

while True:

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            print("Opening VFS...")

            page.goto(URL, timeout=120000)

            time.sleep(10)

            content = page.content()

            unavailable = [
                "No appointment slots available",
                "No slots available",
                "Aucun créneau disponible"
            ]

            found = True

            for txt in unavailable:
                if txt.lower() in content.lower():
                    found = False

            if found:
                print("🚨 SLOT DISPONIBILE!")

            else:
                print("Nessuno slot.")

            browser.close()

    except Exception as e:

        print("Errore:", e)

    sleep_time = random.randint(240, 420)

    print(f"Sleep {sleep_time}s")

    time.sleep(sleep_time)
