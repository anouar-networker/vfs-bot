from playwright.sync_api import sync_playwright
import time
import random

EMAIL = "anouar.1985@hotmail.it"
PASSWORD = "Juvenet1@"

LOGIN_URL = "https://visa.vfsglobal.com/mar/fr/login"

while True:

    try:

        print("BOT STARTED", flush=True)

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
                args=["--no-sandbox"]
            )

            page = browser.new_page()

            print("Opening login...", flush=True)

            page.goto(LOGIN_URL, timeout=120000)

            time.sleep(5)

            # LOGIN
            page.fill('input[type="email"]', EMAIL)
            page.fill('input[type="password"]', PASSWORD)

            print("Waiting Cloudflare...", flush=True)

            time.sleep(10)

            page.click('button[type="submit"]')

            time.sleep(10)

            print("Clicking reservation...", flush=True)

            page.click("text=Démarrer une nouvelle réservation")

            time.sleep(5)

            # CENTRE
            page.select_option(
                'select',
                label='Centre de demande de visa pour la Suisse, Rabat'
            )

            time.sleep(2)

            # CATEGORY
            selects = page.locator('select')

            selects.nth(1).select_option(label='Visa Schengen type C')

            time.sleep(2)

            # SUBCATEGORY
            selects.nth(2).select_option(label='Touriste')

            time.sleep(10)

            content = page.content()

            unavailable = (
                "aucune place de rendez-vous n'est actuellement disponible"
            )

            if unavailable.lower() in content.lower():

                print("❌ Nessuno slot", flush=True)

            else:

                print("🚨 SLOT DISPONIBILE!", flush=True)

            browser.close()

    except Exception as e:

        print("ERRORE:", str(e), flush=True)

    sleep_time = random.randint(240, 420)

    print(f"Sleep {sleep_time}s", flush=True)

    time.sleep(sleep_time)
