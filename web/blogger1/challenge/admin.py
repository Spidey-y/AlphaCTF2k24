import asyncio
from pyppeteer import launch
from sys import argv


async def main(url='https://blogger.challenge.alphabit.club/'):
    browser = await launch(headless=True,    handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False, executablePath="/usr/bin/chromium", args=['--no-sandbox'])
    page = await browser.newPage()

    await page.goto('https://blogger.challenge.alphabit.club/login')

    await page.type('input[name="username"]', 'admin')
    await page.type('input[name="password"]', 'su3r5ecr3tp4ssw0rd852461337')

    await page.click('#login')
    await page.goto(url)
    await asyncio.sleep(1)
    await browser.close()


def run_pupp(url):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(url))
    loop.close()
