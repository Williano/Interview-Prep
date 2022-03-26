"""
    Title: Generate String from palindrome
    Description:
    Given the a string, return a palindrome made from all its characters. If no
    such palindrome exists, return None

    Example 1:

    Input: AAAACACBA
    Output: AAACBCAAA


    Example 2:

    Input: RARARA
    Output: None
    Reason: Because A and R appear  3 times which odd number of times

"""


class Solution:
    def generate_palindrome(self, string_in: str):
        # Count occurrences of each character

        char_count = {}

        for char in string_in:

            if char in char_count:
                char_count[char] += 1

            else:
                char_count[char] = 1

        # Find characters that repeat odd number of times
        odd_chars = ""
        even_chars = ""
        odd_chars_count = 0

        for char in char_count:

            if char_count[char] % 2 != 0:
                odd_chars_count += 1
                odd_chars += char

            else:
                half_of_even_char = char_count[char] // 2
                even_chars += char * half_of_even_char

        # If there are multiple characters that appear only once, then the string
        # can't be a palindrome so return None
        if odd_chars_count > 1:
            return None

        # Generate palindrome using start of even_characters + odd_characters
        # + reverse_of_even_characters

        return even_chars + odd_chars + even_chars[::-1]


# def main():

#     print(generate_palindrome("RARARA"))

#     print(generate_palindrome("AAAACACBA"))


# if __name__ == "__main__":
#     main()
