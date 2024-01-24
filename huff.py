class StringEdit:
    def template(self):
        data = self.inputData()
        converted_data = self.convert(data)
        self.outputData(converted_data)

    def inputData(self):
        input_string = input("Masukkan angka pisah spasi: ")
        return list(map(int, input_string.split()))

    def convert(self, data):
        char_list = [chr(num + 64) for num in data]
        return char_list

    def outputData(self, converted_data):
        print("step-1(input) :", ' '.join(str(num) for num in converted_data))
        print("step-2(convert) :", converted_data)
        print("step-3(output) :")
        max_length = len(converted_data)
        for i, char in enumerate(converted_data):
            spaces = "_" * (max_length - i)
            print("|" + spaces + "_" * (len(char)-1) + char)

StringEdit().template()