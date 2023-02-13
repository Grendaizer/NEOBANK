from source.bin.homepage import Home_Page


def test_neobank(initdriver):
    page = Home_Page(initdriver)
    page.opentab()
    page.check_titlename('NEOBANK для бізнесу')
    page.enter_number('+380636901699')
    page.click_button_continue()
    page.on_fullscreen_mode()
    page.check_text_on_page('Відкриття бізнес-рахунку можливе тільки через додаток NEOBANK для бізнесу')
