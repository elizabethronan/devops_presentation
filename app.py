import psycopg2
import boto3
import json, subprocess

def get_secret():
    # Extract secret from AWS
    secret = subprocess.check_output(
        ['bash',
        '-lc',
        "aws secretsmanager get-secret-value --secret-id 'arn:aws:secretsmanager:us-east-1:834922934112:secret:rds!db-9e259e04-e679-4537-b0f5-70289dc2fde7-2G57H5' --query SecretString --output text"
        ]
    ).decode(); password = json.loads(secret)['password']

    return secret, password

def get_conn(password):
    conn = None
    try:
        conn = psycopg2.connect(
            host='database-ge.cspks6qqgm4n.us-east-1.rds.amazonaws.com',
            port=5432,
            database='postgres',
            user='postgres',
            password=password,
            sslmode='verify-full',
        sslrootcert='/Users/elizabethronan/global-bundle.pem'
        )
        cur = conn.cursor()
        cur.execute('SELECT version();')
        print(cur.fetchone()[0])
        cur.close()
    except Exception as e:
        print(f"Database error: {e}")
        raise
    finally:
        if conn:
            print('Connection successful!')
            conn.close()

if __name__ == '__main__':
    secret, password = get_secret()
    get_conn(password)
