#Simplify Path
#Input: path = "/home/" -> 마지막 /없애라
#Output: "/home"
#Input: path = "/../" -> root로부터 ..은 root
#Output: "/"
#Input: path = "/home//foo/" 쌍슬래쉬 없애라
#Output: "/home/foo"
#점 3개부터는 디렉토리 이름으로 간주
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = [i for i in path.split('/') if i] #if i 필수
        result = []
        print(dirs)
        for i in dirs:
            if i == '.':
                continue
            if i == '..':
                if len(result) > 0:
                    result.pop()
                continue
            result.append(i)
        return '/'+'/'.join(result)