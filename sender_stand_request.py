import configuration
import requests
import data


# def post_products_kits(products_ids):
#     return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
#                          headers=data.headers)
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=user_body)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USER_MODEL_PATH)
# response = post_products_kits(data.product_ids);
# print(response.status_code)
# print(response.json())