from seleniumbase import SB

with SB(uc=True, test=True) as lidya:

    if True:
        url = "https://kick.com/brutalles"
        lidya.uc_open_with_reconnect(url, 5)
        lidya.uc_gui_click_captcha()
        lidya.sleep(1)
        lidya.uc_gui_handle_captcha()
        lidya.sleep(1)
        if lidya.is_element_present('button:contains("Accept")'):
            lidya.uc_click('button:contains("Accept")', reconnect_time=4)
        if lidya.is_element_visible('#injected-channel-player'):
            while lidya.is_element_visible('#injected-channel-player'):
                lidya.sleep(10)
