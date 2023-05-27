class Solution:
    def intToRoman(self, num: int) -> str:

        # during each iteration we will get a single digit of the int
        # calculate length of the int
        num_digits = len(str(num))

        res = ""
        j = num_digits-1 # start from rightmost digit

        for i in range(num_digits):
            curr_digit = (num // (10**j)) % 10 # get a single digit from the int
            place = int(str("1" + j * "0")) # calculate the place eg. one's, ten's

            # accounting for the exceptions
            if curr_digit == 4:
                if place == 1: res += "IV"
                elif place == 10: res += "XL"
                elif place == 100: res += "CD"
            elif curr_digit == 9:
                if place == 1: res += "IX"
                elif place == 10: res += "XC"
                elif place == 100: res += "CM"

            # non-exceptions
            else:
                if place == 1:
                    if 5 <= curr_digit < 9:
                        res += "V" + (curr_digit-5)*"I"
                    else:
                        res += curr_digit * "I"
                elif place == 10:
                    if 5 <= curr_digit < 9:
                        res += "L" + (curr_digit-5)*"X"
                    else:
                        res += curr_digit * "X"
                elif place == 100:
                    if 5 <= curr_digit < 9:
                        res += "D" + (curr_digit-5)*"C"
                    else:
                        res += curr_digit * "C"
                elif place == 1000:
                        res += curr_digit * "M"

            j -= 1 # move pointer to the left

        return res
