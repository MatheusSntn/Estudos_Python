# Abstracao
# Log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log: # Superclasse
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') # Template Method - é o comeco do 
                                                             # Padrao de projetos
    def log_error(self, msg): # Abstracao
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log): #sobreescrevendo o metodo, Leskov Substiton Principal
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada )
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Nao deu certo irmao')
    lp.Log_success('Boa Boa')
    lf = LogFileMixin()
    lf.log_error('Nao deu certo irmao')
    lf.Log_success('Boa Boa')
    