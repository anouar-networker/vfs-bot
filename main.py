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
                channel="chrome",
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-dev-shm-usage"
                ]
            )

            context = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                ),
                viewport={
                    "width": 1366,
                    "height": 768
                },
                locale="fr-FR"
            )

            page = context.new_page()

            print("Opening login...", flush=True)

            page.goto(LOGIN_URL, timeout=120000)

            time.sleep(15)

            html = page.content()

            print(html[:2000], flush=True)

            if "cf-browser-verification" in html.lower():
                print("⚠️ Cloudflare detected", flush=True)

            print("Filling login...", flush=True)

            page.fill('input[type="email"]', EMAIL)

            page.fill('input[type="password"]', PASSWORD)

            time.sleep(5)

            page.click('button[type="submit"]')

            time.sleep(15)

            print("Click reservation...", flush=True)

            page.click("text=Démarrer une nouvelle réservation")

            time.sleep(5)

            selects = page.locator('select')

            selects.nth(0).select_option(
                label='Centre de demande de visa pour la Suisse, Rabat'
            )

            time.sleep(2)

            selects.nth(1).select_option(
                label='Visa Schengen type C'
            )

            time.sleep(2)

            selects.nth(2).select_option(
                label='Touriste'
            )

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
