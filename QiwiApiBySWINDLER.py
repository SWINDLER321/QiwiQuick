import time
import requests

# You can read about params here https://developer.qiwi.com/ru/qiwi-wallet-personal/?python#payments 

class QiwiApi(object):
    def __init__(self, token, phone):
        """
        :type token: str
        :type phone: str
        :type delay: int

        :param token: QIWI API token
        :param phone: Your phone [required for pay() function]
        :param delay: Loop sleep time
        """
        self.r = requests.Session()
        self.r.headers['Accept'] = 'application/json'
        self.r.headers['authorization'] = 'Bearer ' + token
        self.phone = phone

    def get_all_profile_info(self):
        response = self.r.get('https://edge.qiwi.com/person-profile/v1/profile/current').json()
        return response

    def get_identifiaction_info(self):
        response = self.r.get(f'https://edge.qiwi.com/identification/v1/persons/{self.phone}/identification').json()
        return response


    def get_balance_info(self):
        response = self.r.get(f'https://edge.qiwi.com/funding-sources/v2/persons/{self.phone}/accounts').json()
        return response

    @property
    def _transaction_id(self):
        """
        Generates transaction id for pay() function.
        :return: UNIX time * 1000
        """

        return str(int(time.time() * 1000))

    def withdraw_money(self, account, amount, currency='643', comment=None, tp='Account', acc_id='643'):

        post_args = {
            "id": self._transaction_id,
            "sum": {
                "amount": amount,
                "currency": currency
            },
            "paymentMethod": {
                "type": tp,
                "accountId": acc_id
            },
            "fields": {
                "account": account
            }
        }
        if comment is not None:
            post_args['comment'] = comment

        response = self.r.post(
            url='https://edge.qiwi.com/sinap/api/v2/terms/99/payments',
            json=post_args
        )
        return response.json()
