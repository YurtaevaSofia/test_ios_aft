class SummaryPage:
    _button_backup_1min = ['id', 'Backup (~1 min)']
    _button_i_will_take_risk = ['id', 'io.zerion.android:id/skipButton']
    _popup_button_update_later = ['id', 'android:id/button2']
    _button_got_it = ['id', 'Got it.']
    _button_show_seed_phrase = ['id', 'Show seed phrase']
    _button_confirm_phrase = ['id', 'Confirm']
    _number = ['id', '']
    _nicely_done = ['id', 'Nicely done!']
    _finish_button = ['id', 'Finish']
    _warning_notification = ['id', 'Don\'t try to guess the word']

    @classmethod
    def get_button_backup_1min(cls):
        return cls._button_backup_1min

    @classmethod
    def get_popup_button_update_later(cls):
        return cls._popup_button_update_later

    @classmethod
    def get_button_got_it(cls):
        return cls._button_got_it

    @classmethod
    def get_button_show_seed_phrase(cls):
        return cls._button_show_seed_phrase

    @classmethod
    def get_button_confirm_phrase(cls):
        return cls._button_confirm_phrase

    @classmethod
    def get_number(cls):
        return cls._number

    @classmethod
    def get_nicely_done(cls):
        return cls._nicely_done

    @classmethod
    def get_finish_button(cls):
        return cls._finish_button

    @classmethod
    def get_warning_notification(cls):
        return cls._warning_notification