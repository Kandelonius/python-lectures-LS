# Hello! This is my program!

1  # PRINT_BEEJ
1  # PRINT_BEEJ
1  # PRINT_BEEJ
1  # PRINT_BEEJ

3  # SAVE_REG R1,99
1
99

4  # PRINT_REG R1
1
2  # HALT

1  # PRINT_BEEJ  Address 0
3  # SAVE_REG R1,37
1
37
4  # PRINT_REG R1
1
2  # HALT

3 # SAVE_REG R0,11
0
11
3 # SAVE_REG R1,22
1
22
5 # PUSH R0
0
5 # PUSH R1
1
6 # POP R0
0
6 # POP R1
1
4 # PRINT_REG R0  # 22
0
2 # HALT

3 # SAVE_REG R0,37
0
37
4 # PRINT_REG R0
0

3 # SAVE_REG R1,13
1
13

7 # CALL R1
1
7 # CALL R1
1

2 # HALT

# Subroutine:
1 # PRINT_BEEJ  # address 13
1 # PRINT_BEEJ
1 # PRINT_BEEJ
8 # RET