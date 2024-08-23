import gettext
import os
import utils.config as config

def setup_localization(lang=None):
    if lang is None:
        lang = config.CURRENT_LANGUAGE
    localedir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources', 'locales')
    translate = gettext.translation('messages', localedir, languages=[lang], fallback=True)
    translate.install()
    return translate.gettext

_ = setup_localization()

def change_language(lang):
    global _
    config.CURRENT_LANGUAGE = lang
    _ = setup_localization(lang)