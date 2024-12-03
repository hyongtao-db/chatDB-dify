import urllib.request
import json

def main(sql_query: str) -> dict:
    # Flask 服务端点
    api_url = "http://192.168.10.219:5003/execute_query"

    # 请求体
    payload = {
        "sql_query": sql_query
    }

    # 将查询参数进行 URL 编码
    encoded_params = urllib.parse.urlencode(payload)

    # 创造请求对象， 拼接完整的 URL
    req = f"{api_url}?{encoded_params}"

    try:
        # 发送请求并获取响应
        with urllib.request.urlopen(req) as response:
            # 读取并解码响应
            result_data = json.loads(response.read().decode('utf-8'))
            # 将结果转换为字符串格式
            result_str = json.dumps(result_data, ensure_ascii=False) # 确保中文字符正常显示
            print(result_str)
            return {
                'result': result_str # 返回字符串类型结果
            }
    except Exception as e:
        raise Exception(f"Error:{str(e)}")
