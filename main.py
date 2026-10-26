from github_api import get_repo_info

owner=input("用户名:").strip()
repo=input("仓库:").strip()

if not owner or not repo:
    print("请正确输入用户名和仓库")

else:
    data = get_repo_info(owner, repo)

    if data:
        print(data["name"])
        print(data["stargazers_count"])
        print(data["forks_count"])