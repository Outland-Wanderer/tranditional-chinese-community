translate traditional_chinese python:
    gui.language = "japanese-normal"

    gui.system_font = "Source_Han_Sans_CN-Regular.otf"

    gui.text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = FontGroup().add("AR_PL_KaitiM_Big5.TTF", 0x2014, 0x201f).add("AR_PL_KaitiM_Big5.TTF", 0x2E80, 0xffff).add("garamond.ttf", 0x0000, 0xffff)

    gui.name_text_font = "LXGWWenKaiLite-Bold.ttf"

    gui.text_size = 32

    gui.name_text_size = 48

    gui.headline_text_font = FontGroup().add("Source_Han_Serif_CN-Bold.otf", 0x2E80, 0xffff).add("kingthing.ttf", 0x0000, 0xffff)

    @gui.variant
    def small():
        gui.text_size = 48
        gui.name_text_size = 42

translate traditional_chinese style book_style:
    font "nzgrKangxi.ttf"

translate traditional_chinese style pling_button_text:
    font gui.text_font

translate traditional_chinese style screen_title_text:
    font gui.headline_text_font

translate traditional_chinese style screen_content_button_text:
    font gui.headline_text_font

translate traditional_chinese style screen_content_text:
    font gui.headline_text_font

translate traditional_chinese style page_button_text:
    font gui.headline_text_font

translate traditional_chinese style click_button_text:
    font gui.headline_text_font

translate traditional_chinese style footstep_button_text:
    font gui.headline_text_font

translate traditional_chinese style stash_button_text:
    font gui.headline_text_font

translate traditional_chinese style screen_title_text:
    font gui.headline_text_font

translate traditional_chinese style screen_content_text:
    font gui.headline_text_font

translate traditional_chinese style screen_content_white_text:
    font gui.text_font

translate traditional_chinese style screen_content_yellow_text:
    font gui.text_font

translate traditional_chinese style quest_title_text:
    font gui.text_font

translate traditional_chinese style quest_line_breaker_text:
    font gui.text_font

translate traditional_chinese style stats_label_text:
    font gui.text_font

translate traditional_chinese style vitals_label_text:
    font gui.text_font

translate traditional_chinese style ruby_style is default:
    size 24
    yoffset -32

translate traditional_chinese style say_dialogue:
    ruby_style style.ruby_style
    ruby_line_leading 12

translate traditional_chinese style history_text:
    ruby_style style.ruby_style
