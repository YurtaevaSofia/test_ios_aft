class SetPasscodePage:

    _button_numeral = ['id', '']

    @classmethod
    def get_button_numeral(cls, number):
        temp_list = [cls._button_numeral[0], cls._button_numeral[1] + number]
        return temp_list



