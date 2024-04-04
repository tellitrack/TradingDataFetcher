import pandas as pd

from enum import Enum

from rest_service_manager import ClientApp, ServiceManager
from credentials_manager import CredentialsManager, CredentialKey

_URL_COINGECKO = 'https://api.coingecko.com/api/v3/'
_URL_GECKOTERMINAL = 'https://api.geckoterminal.com/api/v2/'


class CoinGecko(Enum):
    PING = 'ping'
    TRENDING = 'search/trending'
    DEX_RECENTLY_UPDATED = 'tokens/info_recently_updated'
    TRENDING_POOLS = 'networks/avax/trending_pools?page=1'


class CoinGeckoServiceManager:

    def __init__(self):
        self.client_app = ClientApp(client_id='CG-w1DuSVNN74UFgzE8xZpTNgtt')

        self.service_manager = ServiceManager(client_app=self.client_app,
                                              api_name="CoinGecko")

    def get_trending(self):
        uri = f'{_URL_COINGECKO}'
        uri_endpoint = f'{CoinGecko.TRENDING.value}'

        uri_request = f'{uri}{uri_endpoint}'
        result = self.service_manager.get(uri_request=uri_request)['coins']
        result = {coin['item']['symbol']: {'price': coin['item']['data']['price'],
                                           'market_cap': coin['item']['data']['market_cap'],
                                           'total_volume': coin['item']['data']['market_cap']} for coin in result}
        df = pd.DataFrame(result).T
        return df

    def get_dex_recently_updated(self):
        uri = f'{_URL_GECKOTERMINAL}'
        uri_endpoint = f'{CoinGecko.DEX_RECENTLY_UPDATED.value}'

        uri_request = f'{uri}{uri_endpoint}'
        result = self.service_manager.get(uri_request=uri_request)
        result = {coin['attributes']['name']: {'symbol': coin['attributes']['symbol'],
                                               'address': coin['attributes']['address'],
                                               'network': coin['relationships']['network']['data']['id'],
                                               'website': coin['attributes']['websites'][0]}
                  for coin in result['data']}
        result = pd.DataFrame(result).T
        result = result[~result['network'].isin(['eth', 'bsc'])]
        return result

    def get_trending_pools(self):
        uri = f'{_URL_GECKOTERMINAL}'
        uri_endpoint = f'{CoinGecko.TRENDING_POOLS.value}'

        uri_request = f'{uri}{uri_endpoint}'
        result = self.service_manager.get(uri_request=uri_request)['data']

        result = {coin['attributes']['name']: {'creation': coin['attributes']['pool_created_at'],
                                               'address': coin['attributes']['address'],
                                               'market_cap': f"$ {coin['attributes']['market_cap_usd']}",
                                               'volume h1': f"$ {round(float(coin['attributes']['volume_usd']['h1']), 1)}",
                                               'volume h24': f"$ {round(float(coin['attributes']['volume_usd']['h24']), 1)}"}
                  for coin in result}
        result = pd.DataFrame(result).T
        return result


# def format_dataframe(df):
#     formatted_text = ""
#     for index, row in df.iterrows():
#         formatted_text += f"*** {index} ***\n"
#         for col in df.columns:
#             formatted_text += f"- {col}: {row[col]}\n"
#         formatted_text += "\n"
#     return formatted_text


def format_dataframe(df, max_chars=4000):
    messages = []
    current_message = ""
    for index, row in df.iterrows():
        crypto_info = f"*** {index} ***\n" + "".join(f"- {col}: {row[col]}\n" for col in df.columns) + "\n"

        # Vérifier si l'ajout de cette info dépasse la limite de caractères
        if len(current_message) + len(crypto_info) > max_chars:
            messages.append(current_message)
            current_message = crypto_info
        else:
            current_message += crypto_info

    # Ajouter le dernier message s'il contient du texte
    if current_message:
        messages.append(current_message)

    return messages


if __name__ == '__main__':
    cg = CoinGeckoServiceManager()

    """
    TRENDING TOKENS ON COINGECKO
    """
    # trending_df = cg.get_trending()
    # message = format_dataframe(trending_df)
    # telegram_token, telegram_chat_ids = credentials_manager.get_credentials(CredentialKey.TELEGRAM)
    # group_chat_id = telegram_chat_ids.get('FABRICE_TRADING')
    # response = TelegramSender(token=telegram_token)
    # response.send_sync_message(chat_id=-1002084350699, message=message, parsing_mode='Markdown')

    """
    RECENTLY UPDATED ON DEX
    """
    # recently_updated = cg.get_dex_recently_updated()
    # messages = format_dataframe(recently_updated)
    # telegram_token, telegram_chat_ids = credentials_manager.get_credentials(CredentialKey.TELEGRAM)
    # group_chat_id = telegram_chat_ids.get('FABRICE_TRADING')
    # response = TelegramSender(token=telegram_token)
    # for message in messages:
    #     response.send_sync_message(chat_id=-1002084350699, message=message, parsing_mode='Markdown')

    """
    TRENDING POOLS ON AVALANCHE
    """
    trending_pools = cg.get_trending_pools()
    messages = format_dataframe(trending_pools)
    telegram_token, telegram_chat_ids = credentials_manager.get_credentials(CredentialKey.TELEGRAM)
    group_chat_id = telegram_chat_ids.get('FABRICE_TRADING')
    response = TelegramSender(token=telegram_token)
    for message in messages:
        response.send_sync_message(chat_id=-1002084350699, message=message, parsing_mode='Markdown')
    print()
