import os
from prisma import Prisma
from dotenv import load_dotenv



env_file_path = os.path.abspath(os.path.join(os.path.abspath(__file__),"..","..","..",".env"))
load_dotenv(env_file_path)

db = Prisma()



