class GeneratingWalletPage:
    _button_generating = ['id', 'Finish']
    _subtitle_owner_of = ['id', 'You are now the proud owner of']

    @classmethod
    def get_button_generating(cls):
        return cls._button_generating

    @classmethod
    def get_subtitle_owner_of(cls):
        return cls._subtitle_owner_of


