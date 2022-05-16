from datetime import datetime,timedelta
from Datas_br import Datasbr

hoje = Datasbr()
print(f'{hoje.dia_semana()} - {hoje.format_data()}')
