import redis
import MySQLdb as mysql

def setup_redis():
    pool = redis.ConnectionPool(host='localhost', port=3000, db=0)
    rd = redis.Redis(connection_pool=pool)
    return rd

def setup_mysql():
    database = "sys"
    my = mysql.connect(host = "127.0.0.1", user = "root", passwd = "senhasegura",db = database)

    return my

def setup_bd():
    setup_redis()
    setup_mysql()

def busca_bd(valor, chave):
    ms = setup_mysql()
    cursor = ms.cursor()
    cursor.execute("select " + valor + " from " + chave)
    resultado = cursor.fetchall()
    ms.close()
    return resultado

def busca_cache(valor,chave):
    rd = setup_redis()
    if (rd.exists(chave)):
        if (rd.exists(valor)):
            return rd.get(chave)
        else:
            return False
    else:
        return False


def main():
    chave = "alunos"
    valor = "*"
    retorno = busca_cache(valor,chave)
    if not retorno:
        print busca_bd(valor,chave)
    else:
        print busca_cache(valor,chave)

main()