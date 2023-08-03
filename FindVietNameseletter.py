def find_vietnamese_letters(input_str):
    vietnamese_letters = {
        'aw': 'ă',
        'aa': 'â',
        'dd': 'đ',
        'ee': 'ê',
        'oo': 'ô',
        'ow': 'ơ',
        'w': 'ư'
    }

    count = 0
    vietnamese_chars = []

    i = 0
    while i < len(input_str):
        found = False
        for key in vietnamese_letters:
            if input_str[i:i+len(key)] == key:
                count += 1
                vietnamese_chars.append(vietnamese_letters[key])
                i += len(key)
                found = True
                break
        if not found:
            i += 1

    return count, vietnamese_chars

# Lấy dữ liệu nhập từ bàn phím
input_str = input("Nhập chuỗi chữ cái Latin: ")

# Gọi hàm count_vietnamese_letters và lưu kết quả vào biến result
result_count, result_chars = find_vietnamese_letters(input_str)

# In kết quả
print("Chuỗi đã nhập:", input_str)
print("Số lượng chữ cái Tiếng Việt có thể được tạo thành:", result_count)
print("Các chữ cái Tiếng Việt có thể được tạo thành:", ", ".join(result_chars))
