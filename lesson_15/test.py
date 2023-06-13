import copy


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        "PAYPALISHIRING"
        """
        [
            y = 0 x = 0[1][ ][ ][7][ ][  ][13]
            y = 1 x = 0[2][ ][6][8][ ][12][14]
            y = 2 x = 0[3][5][ ][9][11][ ][  ]
            y = 3 x = 0[4][ ][ ][10][ ][ ][  ]
        ]
        """
        diagonal_len = len(s) % numRows
        column_count = diagonal_len ^ diagonal_len + 3
        matrix = [['' for _ in range(numRows + 1)] for x in range(column_count)]
        y = 0
        x = 0
        next_vertical = 0 + diagonal_len + 1
        print(matrix)
        for idx in range(len(s)):
            print(matrix)
            if next_vertical >= x:
                # vertical increase only y + 1
                matrix[y][x] = s[idx]
                x += 1
            else:
                x -= 2
                y += 1
                matrix[y][x] = s[idx]
            if x == numRows:
                next_vertical = x + diagonal_len + 1
                x = 0

        return matrix


print(Solution().convert('PAYPALISHIRING', 3))

