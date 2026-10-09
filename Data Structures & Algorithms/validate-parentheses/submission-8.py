class Solution:
    def isValid(self, s: str) -> bool:
        open_para = ["(", "{", "["]
        stack = []

        for para in s:
            if para in open_para:
                stack.append(para)
            else:
                if len(stack) == 0:
                    return False
                if para == ")" and stack.pop() != "(" :
                        return False
                if para == "}" and stack.pop() != "{":
                        return False
                if para == "]" and stack.pop() != "[":
                        return False

        return len(stack) == 0