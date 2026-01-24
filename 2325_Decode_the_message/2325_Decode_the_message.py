class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        final_list = ''
        for i in key:
            if i in final_list or i==' ':
                continue
            else:
                final_list += i
        output = ''
        for i in message:
            if i==' ':
                output += ' '
            else:
                index = final_list.index(i)
                output += alphabets[index]
        return output
        