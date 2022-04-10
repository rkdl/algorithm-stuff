'''
candy = "aaabbccc"

crush(candy) = "bbccc" -> "bb"

example 2

candy = "abbbaa"
         ^

crush(candy) = "aaa" -> ""

input is english lowercase


* apply crush recursively
* Time O(N ^ 2)
* Space O(N ^ 2)


Iterative brute force:
Time: O(N^2)
Mem: O(N)

"bbcb" => "bbcb"

count = {b:3, c:1}



abbbaa
   ^
aaa
^^^
'''


# def crush(candy: str) -> str:
#     if not candy:
#         return candy

#     result = []  # a  # O(N Mem)

#     cur_letter_count = 0  # 3
#     prev_letter = candy[0]  # a

#     for letter in candy:
#         if letter == prev_letter:
#             cur_letter_count += 1
#         else:
#             if cur_letter_count < 3:
#                 for _ in range(cur_letter_count):
#                     result.append(prev_letter)
#             cur_letter_count = 1

#         prev_letter = letter
    
#     if cur_letter_count < 3 and (len(candy)bbcb< 3 or candy[-3] != prev_letter):
#         for _ in range(cur_letter_count):
#             result.append(prev_letter)
    
#     processed_candy = ''.join(result)  # ""

#     if candy != processed_candy:
#         return crush(processed_candy)
#     return processed_candy


"abbabbabbabbabbabbabbcccb"

def crush(candy: str) -> str:
    stack = []

    for letter in candy:
        stack.append(letter)

        if len(stack) >= 3 and stack[-3] == stack[-2] == stack[-1]:
            for _ in range(3):
                stack.pop()

    return ''.join(stack)


print('exp empty:', crush(''))
print('exp bb:', crush('bb'))
print('exp empty:', crush('abbbaa'))
print('exp bbcb:', crush('bbcb'))
print('exp empty:', crush('aaa'))