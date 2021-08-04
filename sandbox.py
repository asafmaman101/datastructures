import datastructures as ds



def solution(str1, str2):
    if '.' not in str1:
        str1 += '.'
    if '.' not in str2:
        str2 += '.'

    str1 = ''.join(list(reversed(str1)))
    str2 = ''.join(list(reversed(str2)))


    if str1.index('.') > str2.index('.'):
        str2 = '0' * (str1.index('.') - str2.index('.')) + str2
    else:
        str1 = '0' * (str2.index('.') - str1.index('.')) + str1

    i = 0
    carry = 0
    ans = ''

    while i < len(str1) and i < len(str2):
        if str1[i] == '.':
            ans += '.'

        else:
            digits_sum = int(str1[i]) + int(str2[i]) + carry
            digit = digits_sum % 10
            carry = digits_sum // 10
            ans += str(digit)
        i += 1

    ans += str1[i:]
    ans += str2[i:]

    print(''.join(list(reversed(ans))))



if __name__ == '__main__':
    # g = ds.UndirectedGraph({'A': {'B', 'F', 'H'}, 'B': {'G', 'C'}, 'C': {'D'}, 'E': {'F'}, 'D': {'J', 'E', 'K'}, 'I': {'H', 'J'}})
    # print(g.bfs('A'))
    # print(g)

    t = ds.BinaryTree()
    a = ds.BinaryTreeNode(1)
    b = ds.BinaryTreeNode(2)
    c= ds.BinaryTreeNode(3)
    d = ds.BinaryTreeNode(4)
    t.root = a
    a.right = b
    a.left = c
    c.right = d

    print(t)