from dotenv import dotenv_values


"""Settings"""
config = dotenv_values(".env")
CLIENT_TOKEN = config['CLIENT_TOKEN']