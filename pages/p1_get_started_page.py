
class GetStartedPage:

    _icon = ['xpath', '//XCUIElementTypeApplication[@name="Zerion"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeImage']
    _title1 = ['xpath', '//XCUIElementTypeStaticText[@name="One Wallet To Do It All"]']
    _title2 = ['xpath', '//XCUIElementTypeStaticText[@name="Build a Truly Multichain Portfolio"]']
    _title3 = ['xpath', '//XCUIElementTypeStaticText[@name="Explore Web3 With People You Trust"]']
    _button_get_started = ['id', 'Get started']
    _subtitle1 = ['id', 'Turn your phone into Web3 Mission Control with a wallet built for humans, not degens.']
    _subtitle2 = ['id', 'Track your complete portfolio across and manage all your private keys in one app.']
    _subtitle3 = ['id', 'Follow any wallet and NFT collection. Build your own Web3 community and identity.']


    @classmethod
    def get_icon(cls):
        return cls._icon

    @classmethod
    def get_title1(cls):
        return cls._title1

    @classmethod
    def get_title2(cls):
        return cls._title2

    @classmethod
    def get_title3(cls):
        return cls._title3

    @classmethod
    def get_button_get_started(cls):
        return cls._button_get_started

    @classmethod
    def get_subtitle1(cls):
        return cls._subtitle1

    @classmethod
    def get_subtitle2(cls):
        return cls._subtitle2

    @classmethod
    def get_subtitle3(cls):
        return cls._subtitle3





