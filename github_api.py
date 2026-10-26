import requests

def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(url, timeout=10)

    except requests.exceptions.Timeout:
        print("请求超时，请检查网络后重试。")
        return None

    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络后重试。")
        return None

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return None

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 404:
        print("仓库不存在，请检查用户名和仓库名。")
        return None

    elif response.status_code == 403:
        print("请求被拒绝，可能是权限不足或触发 API 限流。")
        return None

    elif response.status_code == 429:
        print("请求过于频繁，请稍后重试。")
        return None

    else:
        print(f"请求失败，HTTP状态码：{response.status_code}")
        return None