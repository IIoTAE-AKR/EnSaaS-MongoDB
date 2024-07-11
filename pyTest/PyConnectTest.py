import json
import psycopg2

def testPostgreSQL():
    # secret.json 파일 읽기
    with open('../secret.json', 'r') as f:
        secret = json.load(f)

    # 데이터베이스 연결 정보 추출
    postgres_database = secret["credentials"]["database"]
    postgres_user = secret["credentials"]["username"]
    postgres_password = secret["credentials"]["password"]
    postgres_host = secret["credentials"]["externalHosts"].split(':')[0]
    postgres_port = secret["credentials"]["port"]
    postgres_uri = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}"

    try:
        conn = psycopg2.connect(postgres_uri)
        cur = conn.cursor()

        cur.execute("SELECT * FROM test.TempHumi")
        rows = cur.fetchmany(2)
        colnames = [desc[0] for desc in cur.description]

        cur.close()
        conn.close()

        result = [dict(zip(colnames, row)) for row in rows]
        return result
    except psycopg2.Error as e:
        print(f"Unable to connect to PostgreSQL instance: {str(e)}")
        return {"Err": f"Unable to connect to PostgreSQL instance: {str(e)}"}
    except Exception as e:
        print(f"An error occurred while connecting to PostgreSQL: {str(e)}")
        return {"Err": f"An error occurred while connecting to PostgreSQL: {str(e)}"}

if __name__ == "__main__":
    result = testPostgreSQL()
    print(result)
