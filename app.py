from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

# 初始化 Flask 应用
app = Flask(__name__)

# PostgreSQL 数据库连接设置
DB_HOST = 'localhost'
DB_PORT = '5432'  # 默认端口，按需修改
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = '123456'

# 连接到 PostgreSQL 数据库的函数
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# 处理 /execute_query 路由
@app.route('/execute_query', methods=['GET'])
def execute_query():
    # 获取用户传入的 SQL 查询
    query = request.args.get('sql_query')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # 连接到数据库并执行查询
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()  # 获取查询结果
        cur.close()
        conn.close()
        
        # 返回查询结果
        return jsonify({'result': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 启动 Flask 服务
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
