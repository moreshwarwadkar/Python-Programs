class BankAccount:

    bank_name = 'UNiK Bank'
    _branch_code = 'UNK007'

    def __init__(self):
        self.account_holder_name = 'Mr Unik'
        self.account_type = 'Current'

        self._minimum_balance = 500
        self._daily_limit = 2000

        self.__account_number = 988776655443
        self.__ifsc_code = 'UNK11MH'
        self.__balance = 0
        self.__upi_pin = 0
        self.__pan_number = 'MMHHA1107M'
        self.__adhar_number = 987654325432

    def get_upi(self):
        print('UPI Pin:',self.__upi_pin)

    def get_balance(self):
        print('Balance:',self.__balance)

    def set_upi(self,upi):

        if len(str(upi)) == 4:
            self.__upi_pin = upi
            print(f'{upi} Pin Set Successfull')
        else:
            print('UPI Pin Must be 4 Digits Only..!!')
            
    def set_balance(self,amt):

        if amt >= 0:
            self.__balance += amt
            print(f'{amt} Added Successfull')
        else:
            print('Invalid Amount..!!')

    @property
    def pan_number(self):
        return self.__pan_number

    @property
    def adhar_number(self):
        return self.__adhar_number
        
obj = BankAccount()

print('Account Number:',obj._BankAccount__account_number)
print('IFSC Code:',obj._BankAccount__ifsc_code)

print('Pan Number:',obj.pan_number)
print('Adhar Number:',obj.adhar_number)

print('Bank Name:',BankAccount.bank_name)
print('Branch Code:',BankAccount._branch_code)

obj.set_upi(1122)
obj.get_upi()

obj.set_balance(5000)
obj.get_balance()

print('Account Holder:',obj.account_holder_name)
print('Account Type:',obj.account_type)
print('Minimum Balance:',obj._minimum_balance)
print('Daily Limit:',obj._daily_limit)


'''
OUTPUT: 

Account Number: 988776655443
IFSC Code: UNK11MH
Pan Number: MMHHA1107M
Adhar Number: 987654325432
Bank Name: UNiK Bank
Branch Code: UNK007
1122 Pin Set Successfull
UPI Pin: 1122
5000 Added Successfull
Balance: 5000
Account Holder: Mr Unik
Account Type: Current
Minimum Balance: 500
Daily Limit: 2000
'''
