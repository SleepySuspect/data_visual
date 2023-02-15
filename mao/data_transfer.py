from mao.food import Food


if __name__ == '__main__':
    with open("data.txt", 'r', encoding='utf-8') as infile:
        all_data = []
        temp_data = []
        count = 0
        for line in infile:
            data_line = line.strip("\n")  # 去除首尾换行符
            if count != 8:
                count += 1
                temp_data.append(data_line)
            else:
                food = Food(temp_data)
                all_data.append(food)
                temp_data = []
                count = 0
