class Solution:
    def interpret(self, command: str) -> str:
        a=command.replace("()","o").replace("(al)","al")
        return a  
        