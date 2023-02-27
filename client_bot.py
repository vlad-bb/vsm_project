from dotenv import dotenv_values


"""Settings"""
config = dotenv_values(".env")
GPT_TOKEN_PERSONAL = config['CLIENT_TOKEN']