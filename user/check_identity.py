import re
def is_valid_id_or_rc_number(identity: str) -> bool:
    if identity is None or identity == "":
        return False

    pid_char_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    pid_id_int = [1, 10, 19, 28, 37, 46, 55, 64, 39, 73, 82, 2, 11, 20, 48, 29, 38, 47, 56, 65, 74, 83, 21, 3, 12, 30]

    pid_resident_first_int = [1, 10, 9, 8, 7, 6, 5, 4, 9, 3, 2, 2, 11, 10, 8, 9, 8, 7, 6, 5, 4, 3, 11, 3, 12, 10]

    pid_resident_second_int = [0, 8, 6, 4, 2, 0, 8, 6, 2, 4, 2, 0, 8, 6, 0, 4, 2, 0, 8, 6, 4, 2, 6, 0, 8, 4]

    identity = identity.upper()  # 轉換為大寫
    identity_arr = list(identity)  # 字串轉換為列表

    verify_num = 0

    # 檢查身分證字號
    if re.match("[A-Z]{1}[1-2]{1}[0-9]{8}",identity) and len(identity) == 10:
        # 第一碼
        verify_num += pid_id_int[pid_char_array.index(identity_arr[0])]
        # 第二~九碼
        for i in range(1, 9):
            verify_num += int(identity_arr[i]) * (9 - i)
        # 檢查碼
        verify_num = (10 - (verify_num % 10)) % 10
        return verify_num == int(identity_arr[9])

    # 檢查統一證(居留證)編號 (2031/1/1停用)
    verify_num = 0
    if re.match("[A-Z]{1}[A-D]{1}[0-9]{8}",identity) and len(identity) == 10:
        # 第一碼
        verify_num += pid_resident_first_int[pid_char_array.index(identity_arr[0])]
        # 第二碼
        verify_num += pid_resident_second_int[pid_char_array.index(identity_arr[1])]
        # 第三~八碼
        for i in range(2, 9):
            verify_num += int(identity_arr[i]) * (9 - i)
        # 檢查碼
        verify_num = (10 - (verify_num % 10)) % 10
        return verify_num == int(identity_arr[9])

    # 檢查統一證(居留證)編號 (2021/1/2實施)
    verify_num = 0
    if re.match("[A-Z]{1}[89]{1}[0-9]{8}",identity) and len(identity) == 10:
        # 第一碼
        verify_num += pid_resident_first_int[pid_char_array.index(identity_arr[0])]
        # 第二~八碼
        for i in range(1, 9):
            verify_num += int(identity_arr[i]) * (9 - i)
        # 檢查碼
        verify_num = (10 - (verify_num % 10)) % 10
        return verify_num == int(identity_arr[9])

    return False