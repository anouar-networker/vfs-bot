from playwright.sync_api import sync_playwright
import time
import random
import sys

URL = "https://visa.vfsglobal.com/mar/fr/che/application-detail"

print("BOT STARTED", flush=True)

while True:

    try:

        print("Opening browser...", flush=True)

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox"]
            )

            page = browser.new_page()

            print("Opening VFS...", flush=True)

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
                print("🚨 SLOT DISPONIBILE!", flush=True)

            else:
                print("Nessuno slot.", flush=True)

            browser.close()

    except Exception as e:

        print("Errore:", str(e), flush=True)

    sleep_time = random.randint(240, 420)

    print(f"Sleep {sleep_time}s", flush=True)

    time.sleep(sleep_time)
